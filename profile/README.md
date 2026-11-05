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
💬 [Zulip chat](https://katzenpost.zulipchat.com/)

## Chat

- **[hushphone](https://github.com/katzenpost/hushphone)**: group chat with push-to-talk voice over the Katzenpost mixnet (Linux and Android) or a Reticulum mesh (Linux)
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

New here? Read [Understanding Pigeonhole](https://katzenpost.network/docs/pigeonhole_explained/),
[run a node](https://katzenpost.network/docs/admin_guide/), or browse
[all repositories](https://github.com/orgs/katzenpost/repositories).

## License

GNU AGPL-3.0 across the org, with a few exceptions; see each repository's LICENSE.
