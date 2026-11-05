# Welcome to Katzenpost!

**Katzenpost** is a free software mix network: an anonymous communication network that hides
not only *what* you say but *who you talk to, when, and how much*. End-to-end encryption protects
the content of a message, but the rest still leaks: IP addresses, message sizes and timing, and
from them your social graph. A mix network is built to resist that kind of traffic analysis, even
by a *global passive adversary* who can watch the whole internet at once. Messages are wrapped in
layers of encryption, sent through several mix nodes, and at each hop they are mixed with other
traffic, transformed and delayed, so an observer cannot match what goes in with what comes out.

Katzenpost is also **post-quantum**: its packet format, its PQ Noise links and its storage layer
use hybrid cryptography from our own [hpqc](https://github.com/katzenpost/hpqc) library,
combining time-tested classical primitives with post-quantum ones, so that traffic recorded today
stays private after quantum computers arrive.

On top of the mix network sits **Pigeonhole**, a storage layer that applications talk through. In
plain words: each person writes to their own encrypted, append-only stream of small fixed-size
*boxes*, kept for about two weeks on storage replicas. Whoever holds a stream's read capability
can read it; nobody else can, and the replicas cannot even tell which boxes belong to the same
stream. Clients never reach the replicas directly: every read and write travels through the
mixnet to a *courier*, which forwards it.

**Group chat** is built from those streams. A group is just its members: each writes to a stream
of their own and reads everyone else's. There are no accounts and no chat servers; you join a
group by giving a member a *voucher code* over a channel you trust. Several apps already speak
the same group chat protocol (*katzenqt1*), so one group can mix people on different apps, on
Linux and Android, and even on a [Reticulum](https://reticulum.network) mesh.

You can try all this today on **namenlos**, the public Katzenpost mixnet we run. Its *bridge
replica* is also reachable from Reticulum meshes, at `162.220.11.225:4242`, so mesh users and
mixnet users can share groups.

📄 [Echomix paper](https://arxiv.org/abs/2501.02933) ·
🌐 [Website](https://katzenpost.network) ·
📚 [Docs](https://katzenpost.network/docs/) ·
💬 [Community](https://katzenpost.network/pages/community/)

## Project Overview

**The network.** Everything the mixnet itself runs on is in one Go monorepo.

- **[katzenpost](https://github.com/katzenpost/katzenpost)** — the mix server, the directory
  authorities, the Pigeonhole couriers and replicas (and the mixnet half of the mesh bridge), and
  **`kpclientd`**, the client daemon that does all the networking and cryptography for apps.
- **[thin_client](https://github.com/katzenpost/thin_client)** — Rust, Python and Lean libraries
  for apps that talk to `kpclientd` (the Go one is in the monorepo, under `client2/thin`), plus
  `pigeonhole-cp` for sending files over Pigeonhole.
- **[pigeonhole_protocols](https://github.com/katzenpost/pigeonhole_protocols)** — the protocols
  built on Pigeonhole, in Go, Rust and Python: the katzenqt1 group chat protocol, and the
  framework for mixnet services such as a Zulip bridge and a message of the day.

**Cryptography.**

- **[hpqc](https://github.com/katzenpost/hpqc)** — hybrid post-quantum cryptography in Go, with a
  Python port: NIKEs (including CTIDH), KEMs (ML-KEM-768, FrodoKEM, Classic McEliece, NTRU Prime,
  HQC), signatures, the combiners that make hybrids of them, and **BACAP**, the
  blinding-and-capability scheme Pigeonhole boxes are made of.
- **[highctidh-rs](https://github.com/katzenpost/highctidh-rs)** — Rust bindings to the highctidh
  C library (CTIDH-1024), used by hpqc's NIKE wrapper.
- **[sqisign](https://github.com/katzenpost/sqisign)** — a pure-Rust port of the SQIsign Round 2
  post-quantum signature, level 1.
- **[falcon](https://github.com/katzenpost/falcon)** — Go bindings for the padded Falcon
  post-quantum signature, with C from PQClean.
- **[circl](https://github.com/katzenpost/circl)**,
  **[sphincsplus](https://github.com/katzenpost/sphincsplus)**,
  **[sntrup4591761](https://github.com/katzenpost/sntrup4591761)**,
  **[chacha20](https://github.com/katzenpost/chacha20)** and
  **[chacha20poly1305](https://github.com/katzenpost/chacha20poly1305)** — forks of Cloudflare's
  CIRCL, the SPHINCS+ reference code, Go Streamlined NTRU Prime and Yawning Angel's ChaCha20
  libraries, carried for the stack.
- **[nyquist](https://github.com/katzenpost/nyquist)** — our fork of Yawning Angel's Noise library
  from its PQ Noise branch, so PQ Noise can use hpqc's schemes.
- **[trunnel](https://github.com/katzenpost/trunnel)** — a Go port of Tor's trunnel code generator
  for binary parsing and encoding.
- **[NoiseFramework](https://github.com/katzenpost/NoiseFramework)** — a fork of a Python Noise
  Protocol Framework.

**Apps.** All of these speak katzenqt1, so their users can be in the same groups.

- **[hushphone](https://github.com/katzenpost/hushphone)** — group chat with push-to-talk voice
  messages, for Linux and Android, in Rust with a Slint interface. It reaches Pigeonhole over the
  mixnet (through `kpclientd`) or over a Reticulum mesh.
- **[katzenqt](https://github.com/katzenpost/katzenqt)** — the original group chat client, a
  PySide6 (Qt) desktop app that can also be driven headlessly.
- **[jam](https://github.com/katzenpost/jam)** — a terminal group chat written in Lean.
- **[frank_chat](https://github.com/katzenpost/frank_chat)** — a desktop group chat written in
  Lean, drawn with Paw.
- **[group_chat_client](https://github.com/katzenpost/group_chat_client)** — the Lean client
  engine jam and frank_chat share.
- **[kpclientd-android](https://github.com/katzenpost/kpclientd-android)** — `kpclientd` as an
  Android app, which lets only the apps you allow use the mixnet.
- **[rustic_audio](https://github.com/katzenpost/rustic_audio)** — Rust voice recording,
  processing and Opus encoding, used for hushphone's voice messages; with Python bindings for
  katzenqt in [Rustic_Audio_PyO3](https://github.com/katzenpost/Rustic_Audio_PyO3) and Lean
  bindings in [rustic_audio_lean](https://github.com/katzenpost/rustic_audio_lean).

**Mesh and embedded.** Pigeonhole also runs on [Reticulum](https://reticulum.network) meshes,
where clients do the BACAP encryption themselves.

- **[katzenrns](https://github.com/katzenpost/katzenrns)** — a Python group chat client for a
  Reticulum mesh, desktop or headless.
- **[pigeonhole_rns](https://github.com/katzenpost/pigeonhole_rns)** — the Pigeonhole storage
  replica for Reticulum meshes, in Python, and the mesh half of the bridge to the mixnet.
- **[pigeonhole_reticulous](https://github.com/katzenpost/pigeonhole_reticulous)** — a Group Chat
  app for [Reticulous](https://github.com/reticulous) devices such as the LilyGO T-Deck Plus.

**High-assurance work in Lean 4.** Protocols and apps written in a language that can also prove
things about them. None of it has been audited by a third party.

- **[cryptlib](https://github.com/katzenpost/cryptlib)** — a Lean cryptography library for
  modelling protocols and proving their properties; jam and frank_chat run its katzenqt1 member
  state machine.
- **[uproar](https://github.com/katzenpost/uproar)** — Noise and PQ Noise, with correctness proofs.
- **[lean_tls](https://github.com/katzenpost/lean_tls)** and
  **[lean_quic](https://github.com/katzenpost/lean_quic)** — TLS 1.3 for QUIC, and QUIC itself,
  with post-quantum key exchange.
- **[huh](https://github.com/katzenpost/huh)** — a small remote shell over PQ Noise, on QUIC or TCP.
- **[paw](https://github.com/katzenpost/paw)** — an Elm-style GUI library with security rules in
  its types; **[tessera](https://github.com/katzenpost/tessera)** — terminal user interfaces.
- **[cborg](https://github.com/katzenpost/cborg)** (CBOR),
  **[Logger](https://github.com/katzenpost/Logger)** (logging),
  **[lean_unix_socket](https://github.com/katzenpost/lean_unix_socket)**,
  **[lean_os](https://github.com/katzenpost/lean_os)** (`fsync`) and
  **[crossterm-lean-ffi](https://github.com/katzenpost/crossterm-lean-ffi)** (terminal control) —
  the building blocks the apps above need.
- **[lean-sys](https://github.com/katzenpost/lean-sys)** — our fork of the Rust bindings to Lean's
  C API, published as `katzenpost-lean-sys`; **[lean-ffi](https://github.com/katzenpost/lean-ffi)**
  — Lean FFI examples to Rust and C.

**Tooling and operations.**

- **[kno](https://github.com/katzenpost/kno)** — builds, installs and checks a Katzenpost network,
  and carries the namenlos configs.
- **[status](https://github.com/katzenpost/status)** — mixnet diagnostics and a status page.
- **[mixnet_perf_probe](https://github.com/katzenpost/mixnet_perf_probe)** — hourly timings of
  Pigeonhole operations on namenlos, as Prometheus metrics.
- **[worldmap](https://github.com/katzenpost/worldmap)** — draws a world map with the mix nodes on it.
- **[katzen-airgapped](https://github.com/katzenpost/katzen-airgapped)** — a client that builds
  Sphinx packets and SURBs on an offline machine and sends them from an untrusted online one.

**Research.**

- **[formal_specifications](https://github.com/katzenpost/formal_specifications)** — ProVerif,
  Verifpal, TLA+ and Promela models of BACAP, the client daemon, MKEM, Sphinx and the Noise handshakes.
- **[cryptoproofs](https://github.com/katzenpost/cryptoproofs)** — machine-checkable ProVerif models
  and measurement data.
- **[napkin-math](https://github.com/katzenpost/napkin-math)** — latency measurements of Noise and
  Sphinx, for back-of-the-envelope sizing.
- **[reunion](https://github.com/katzenpost/reunion)** (the REUNION PAKE protocol),
  **[talek](https://github.com/katzenpost/talek)** (a fork of the Talek private publish/subscribe
  system) and **[echo](https://github.com/katzenpost/echo)** (a small Rust program on the thin
  client).

**Website and outreach.** [website](https://github.com/katzenpost/website) (katzenpost.network),
[diagrams](https://github.com/katzenpost/diagrams), [zine](https://github.com/katzenpost/zine)
and this
[.github](https://github.com/katzenpost/.github) profile.

**Older forks**, no longer central: [quic-go](https://github.com/katzenpost/quic-go) (deprecated),
[fdroiddata](https://github.com/katzenpost/fdroiddata) and
[katzen.chat](https://github.com/katzenpost/katzen.chat), the website of the retired Katzen app.

## Getting started

It is early days. The software works, but it is pre-alpha developer software: expect rough
edges, missing documentation and the odd breaking change, and none of it has had a third-party
audit. The mixnet is also slow and low-bandwidth by design, so messages are not instant.

### Chat on the namenlos mixnet

Every mixnet app talks to `kpclientd`, which needs a configuration that says which mixnet to join.

**On Debian or Ubuntu**, the quickest way to get `kpclientd` running against namenlos is
katzenqt's bootstrap, which builds it, installs the namenlos config and starts it as a systemd user
service, then opens katzenqt:

```sh
git clone https://github.com/katzenpost/katzenqt ~/katzenqt
cd ~/katzenqt
make deps
make run
```

With that daemon running, you can also install **hushphone** from its
[releases](https://github.com/katzenpost/hushphone/releases) (a `.deb` for Debian 13 or Ubuntu
24.04) and it will find `kpclientd` by itself. To run `kpclientd` by hand instead, build it with
`make kpclientd` in the [katzenpost](https://github.com/katzenpost/katzenpost) repo and start it
with the namenlos config that [jam](https://github.com/katzenpost/jam#running) carries.

**On Android**, install the `arm64-v8a` APKs of
[kpclientd-android](https://github.com/katzenpost/kpclientd-android/releases) and
[hushphone](https://github.com/katzenpost/hushphone/releases), start the daemon, and allow
hushphone when it asks. If the daemon's built-in config is out of date, ask us for a fresh one on
the [community](https://katzenpost.network/pages/community/) channels.

To chat, one person starts a group; anyone else asks to join and gets a voucher code, which they
send to a member, who adds them.

### Chat on a Reticulum mesh

No `kpclientd` is needed on a mesh. **katzenrns** can start its own private Reticulum instance with
one link to the namenlos bridge replica:

```sh
pip install git+https://github.com/katzenpost/katzenrns
katzenrns --replica 162.220.11.225:4242
```

If you already run `rnsd`, point it at the replica instead; the
[katzenrns README](https://github.com/katzenpost/katzenrns#run) shows the interface to add.
**hushphone** can do the same with `--transport reticulum --replica 162.220.11.225:4242`, though
with that transport, minting and redeeming voucher codes does not work yet.

Through the bridge, mesh users and mixnet users join each other's groups with the same voucher
codes.

### On a LilyGO T-Deck Plus

[pigeonhole_reticulous](https://github.com/katzenpost/pigeonhole_reticulous) brings the same group
chat to the T-Deck Plus, running on [Reticulous](https://github.com/reticulous) firmware. It is
the newest piece: there is no ready-made image or build guide yet, so for now it is for people
already building Reticulous themselves. Watch the repo.

### Building and developing

- **Build the stack**: `make all` in [katzenpost](https://github.com/katzenpost/katzenpost) builds
  every daemon and tool; [Build from source](https://katzenpost.network/docs/build_from_source/)
  walks through it with pinned versions, and the monorepo's `docker/` directory runs a whole test
  mixnet on your machine.
- **Build an app**: start with [Understanding Pigeonhole](https://katzenpost.network/docs/pigeonhole_explained/),
  the [Thin Client API](https://katzenpost.network/docs/thin_client_api_reference/), and the
  minimal group chats in [pigeonhole_protocols](https://github.com/katzenpost/pigeonhole_protocols)'
  `examples/`.
- **Run a node**: the [Admin Guide](https://katzenpost.network/docs/admin_guide/).
- **Understand the design**: the [Echomix paper](https://arxiv.org/abs/2501.02933), the
  [specifications](https://katzenpost.network/docs/specs/) and the
  [threat model](https://katzenpost.network/docs/threat_model/).
- **Contribute**: issues and pull requests are welcome on every repository; most of the work
  happens in [katzenpost](https://github.com/katzenpost/katzenpost).

## License

GNU AGPL-3.0 across the org. A small number of repositories and submodules use different
licenses; see the LICENSE file inside each repository.
