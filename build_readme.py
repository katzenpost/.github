#!/usr/bin/env python3
"""Rewrite the marked sections of profile/README.md with latest releases and blog posts."""
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

README = Path(__file__).parent / "profile" / "README.md"
FEED = "https://katzenpost.network/blog/index.xml"
REPOS = ["hushphone", "katzenpost", "hpqc", "cryptlib"]
# Some repos only push tags, so fall back to the newest tag when there is no release.
REPO_FIELDS = """name
  releases(first: 5, orderBy: {field: CREATED_AT, direction: DESC}) {
    nodes { tagName publishedAt url isDraft isPrerelease } }
  refs(refPrefix: "refs/tags/", first: 1, orderBy: {field: TAG_COMMIT_DATE, direction: DESC}) {
    nodes { name target { ... on Commit { committedDate }
      ... on Tag { target { ... on Commit { committedDate } } } } } }"""


def latest(repo):
    rels = [r for r in repo["releases"]["nodes"] if r["publishedAt"] and not r["isDraft"]]
    if rels:
        r = rels[0]
        return r["tagName"], r["url"], r["publishedAt"]
    tags = repo["refs"]["nodes"]
    if not tags:
        return None
    t = tags[0]
    date = t["target"].get("committedDate") or t["target"]["target"]["committedDate"]
    url = f"https://github.com/katzenpost/{repo['name']}/releases/tag/{t['name']}"
    return t["name"], url, date


def releases(token):
    query = "{" + "".join(
        f'r{i}: repository(owner: "katzenpost", name: "{n}") {{ {REPO_FIELDS} }}\n'
        for i, n in enumerate(REPOS)
    ) + "}"
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={"Authorization": f"Bearer {token}", "User-Agent": "profile-readme"},
    )
    data = json.load(urllib.request.urlopen(req, timeout=30))
    if "errors" in data:
        sys.exit(f"GraphQL errors: {data['errors']}")
    found = [(repo["name"], latest(repo)) for repo in data["data"].values()]
    found = sorted(((n, *x) for n, x in found if x), key=lambda r: r[3], reverse=True)
    return [f"- [{n} {tag}]({url}) - {date[:10]}" for n, tag, url, date in found]


def posts(n=5):
    with urllib.request.urlopen(FEED, timeout=30) as f:
        root = ET.parse(f).getroot()
    return [
        f"- [{i.findtext('title')}]({i.findtext('link')}) - "
        f"{parsedate_to_datetime(i.findtext('pubDate')).date()}"
        for i in root.iter("item")
    ][:n]


def replace(text, marker, lines):
    pattern = re.compile(rf"(<!-- {marker} starts -->\n).*?(<!-- {marker} ends -->)", re.S)
    if not pattern.search(text):
        sys.exit(f"marker {marker} not found in README.md")
    return pattern.sub(lambda m: m[1] + "\n".join(lines) + "\n" + m[2], text)


if __name__ == "__main__":
    text = README.read_text()
    text = replace(text, "releases", releases(os.environ["GITHUB_TOKEN"]))
    text = replace(text, "blog", posts())
    README.write_text(text)
