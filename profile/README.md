# Welcome to Katzenpost!

**Katzenpost** is a free software, post-quantum mix network. End-to-end encryption hides what you
say; a mix network also hides who you talk to, when and how much, even from an adversary who can
watch the whole internet. On top of it, **Pigeonhole** gives apps asynchronous, unlinkable
communication, so people can chat without being online at the same time: messages wait on
replicas for about a week, then are garbage-collected. Our group chat apps are built on it, with
no accounts and no chat servers.

You can try it on **namenlos**, our public mixnet, and on [Reticulum](https://reticulum.network)
meshes, which share groups with the mixnet through a bridge replica. It is early, pre-alpha
software, so expect rough edges.

📄 [Paper](https://arxiv.org/abs/2501.02933) ·
🌐 [Website](https://katzenpost.network) ·
📚 [Docs](https://katzenpost.network/docs/) ·
💬 [Zulip chat](https://katzenpost.zulipchat.com/) ·
📡 [namenlos mixnet status](https://status.namenlos.network/)

## Chat

- **[hushphone](https://github.com/katzenpost/hushphone)**: group chat with push-to-talk voice over the Katzenpost mixnet or a Reticulum mesh, for Linux and Android
- **[katzenqt](https://github.com/katzenpost/katzenqt)**: Qt desktop group chat
- **[jam](https://github.com/katzenpost/jam)** and **[frank_chat](https://github.com/katzenpost/frank_chat)**: terminal and desktop group chat in Lean
- **[katzenrns](https://github.com/katzenpost/katzenrns)**: group chat on a Reticulum mesh
- **[pigeonhole_reticulous](https://github.com/katzenpost/pigeonhole_reticulous)**: group chat for the LilyGO T-Deck Plus
- **[kpclientd-android](https://github.com/katzenpost/kpclientd-android)**: the client daemon on Android

## Build

- **[katzenpost](https://github.com/katzenpost/katzenpost)**: mix server, directory authority, Pigeonhole and the client daemon `kpclientd`
- **[hpqc](https://github.com/katzenpost/hpqc)**: hybrid post-quantum cryptography
- **[thin_client](https://github.com/katzenpost/thin_client)**: Rust, Python and Lean libraries for apps
- **[pigeonhole_protocols](https://github.com/katzenpost/pigeonhole_protocols)**: group chat and service protocols on Pigeonhole
- **[pigeonhole_rns](https://github.com/katzenpost/pigeonhole_rns)**: Pigeonhole replicas for Reticulum meshes
- **[cryptlib](https://github.com/katzenpost/cryptlib)**: Lean cryptography for modelling and proving protocols
- **[kno](https://github.com/katzenpost/kno)**: build, install and check a Katzenpost network

<table><tr><td valign="top" width="50%">

### Latest releases
<!-- releases starts -->
- [hushphone v0.3.7](https://github.com/katzenpost/hushphone/releases/tag/v0.3.7) - 2026-11-20
- [hpqc v0.0.96](https://github.com/katzenpost/hpqc/releases/tag/v0.0.96) - 2026-11-15
- [katzenpost v0.0.111](https://github.com/katzenpost/katzenpost/releases/tag/v0.0.111) - 2026-11-14
- [cryptlib v0.2.0](https://github.com/katzenpost/cryptlib/releases/tag/v0.2.0) - 2026-10-26
<!-- releases ends -->

</td><td valign="top" width="50%">

### Blog posts
<!-- blog starts -->
- [Introduction to Pigeonhole Protocol](https://katzenpost.network/blog/2026/11/05/introduction-to-pigeonhole-protocol/) - 2026-11-05
- [Formalizing Sphinx in Lean](https://katzenpost.network/blog/2026/10/31/formalizing-sphinx-in-lean/) - 2026-10-31
- [Katzenpost threat model document](https://katzenpost.network/blog/2024/04/25/katzenpost-threat-model-document/) - 2024-04-25
- [Mixnet Literature Overview](https://katzenpost.network/blog/2024/04/15/mixnet-literature-overview/) - 2024-04-15
- [hpqc - hybrid post quantum cryptography library](https://katzenpost.network/blog/2024/04/12/hpqc-hybrid-post-quantum-cryptography-library/) - 2024-04-12
<!-- blog ends -->

</td></tr></table>

New here? Read [Understanding Pigeonhole](https://katzenpost.network/docs/pigeonhole_explained/),
[run a node](https://katzenpost.network/docs/admin_guide/), or browse
[all repositories](https://github.com/orgs/katzenpost/repositories).

## License

GNU AGPL-3.0 across the org, with a few exceptions; see each repository's LICENSE.
