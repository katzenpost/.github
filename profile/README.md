# Katzenpost

A post-quantum mix network providing strong metadata privacy
against global passive adversaries.

💬 **Come chat with us on Zulip: [katzenpost.zulipchat.com](https://katzenpost.zulipchat.com/)**

Zulip is where the Katzenpost developers talk every day. Drop in to say
hi, ask a question about the code or the research, get help running a
node, or tell us what you're building. No phone number is needed to sign
up, and it works well over Tor.

📄 [Paper](https://arxiv.org/abs/2501.02933) ·
🌐 [Website](https://katzenpost.network) ·
📚 [Docs](https://katzenpost.network/docs/)

---

## Repositories

### Core
- **[katzenpost](https://github.com/katzenpost/katzenpost)** — monorepo:
  - **Mix network**: mix server, directory authority
  - **Pigeonhole protocol**: courier, replica.
    Uses the mixnet as transport for clients to talk to couriers.
  - **Client daemon** (`kpclientd`): mixnet client used by
    applications, including to reach Pigeonhole couriers.
- **[hpqc](https://github.com/katzenpost/hpqc)** —
  hybrid post-quantum cryptography library. Provides KEM, NIKE,
  and signature schemes behind clean interfaces, plus the pieces
  that make them composable:
  - a **KEM combiner** that is provably IND-CCA2 in the QROM,
    based on the [KEM Combiners paper](https://eprint.iacr.org/2018/024)
  - a **NIKE-to-KEM adapter** (an ad-hoc ElGamal construction)
    so any NIKE can be used as a KEM, and combined with other
    KEMs via the combiner
  - a **signature scheme combiner**
  - **BACAP**, a blinding-and-capability scheme used by Pigeonhole

### Clients

- **`kpclientd`** — the Katzenpost client daemon. Lives in the
  [monorepo](https://github.com/katzenpost/katzenpost) at
  [`cmd/kpclientd`](https://github.com/katzenpost/katzenpost/tree/main/cmd/kpclientd);
  build with `make kpclientd` from the repo root. Required by katzenqt.
- **[katzenqt](https://github.com/katzenpost/katzenqt)** —
  Qt group chat client. Talks to `kpclientd`.
- **[jam](https://github.com/katzenpost/jam)** — terminal group chat
  written in Lean that speaks katzenqt's group chat protocol, so jam and
  katzenqt users can share a group. Talks to `kpclientd`.
- **[glint](https://github.com/katzenpost/glint)** — desktop group chat
  in Lean, built on Paw and CryptWalker. Just started.

### Thin clients

Language bindings for building applications that talk to `kpclientd`:

- **Go** — in the monorepo at
  [`client2/thin`](https://github.com/katzenpost/katzenpost/tree/main/client2/thin)
- **Rust and Python** — [thin_client](https://github.com/katzenpost/thin_client),
  which also ships `pigeonhole-cp` for sending files over Pigeonhole
  channels. A Lean thin client is in progress in the same repository.
- **[pigeonhole](https://github.com/katzenpost/pigeonhole)** — a
  high-level Pigeonhole protocol library. Just started.

### Project

- **[website](https://github.com/katzenpost/website)** —
  source for katzenpost.network

---

## New here?

- **Say hi**: [Zulip chat](https://katzenpost.zulipchat.com/) — questions welcome
- **Use it**: build [katzenqt](https://github.com/katzenpost/katzenqt)
  and `kpclientd` (see Clients above) — pre-built packages coming
- **Run a node**: [Admin Guide](https://katzenpost.network/docs/admin_guide/)
- **Build on it**: [Thin Client API](https://katzenpost.network/docs/thin_client_api_reference/)
- **Contribute**: [katzenpost/katzenpost](https://github.com/katzenpost/katzenpost) — issues and PRs
- **Research**: [Echomix paper](https://arxiv.org/abs/2501.02933) and [Threat Model](https://katzenpost.network/docs/threat_model/)

---

## Full repository catalogue

The sections above are the curated front door. Below is every
repository in the organisation, grouped by purpose, so a newcomer can
find the right place quickly and so dead wood is plainly labelled.

### Cryptography libraries and vendored crypto

Live dependencies of `hpqc`:

- **[circl](https://github.com/katzenpost/circl)**: fork of
  Cloudflare's CIRCL, carried for use with `hpqc`.
- **[falcon](https://github.com/katzenpost/falcon)**: Go bindings
  for the Falcon padded post-quantum signature (C vendored from
  PQClean).
- **[sphincsplus](https://github.com/katzenpost/sphincsplus)**:
  fork of the SPHINCS+ reference code.
- **[sntrup4591761](https://github.com/katzenpost/sntrup4591761)**:
  Go Streamlined NTRU Prime 4591^761.

Live dependencies of `katzenpost`:

- **[nyquist](https://github.com/katzenpost/nyquist)**: fork of
  Yawning Angel's Nyquist Noise library, from the `pqnoise` branch;
  supplies the PQ Noise wire protocol.
- **[trunnel](https://github.com/katzenpost/trunnel)**: actively
  maintained Go port of Tor's trunnel binary-serialisation code
  generator; used for Sphinx and Pigeonhole wire types.

Standalone crypto:

- **[sqisign](https://github.com/katzenpost/sqisign)**: pure-Rust
  port of the SQIsign Round 2 (level 1) isogeny-based post-quantum
  signature, checked against the C reference with differential
  vectors and NIST KATs. Alpha.
- **[NoiseFramework](https://github.com/katzenpost/NoiseFramework)**:
  fork of the Python Noise Protocol Framework. Not yet used.

### Research, formal methods and analysis

- **[cryptoproofs](https://github.com/katzenpost/cryptoproofs)**:
  machine-checkable ProVerif models and measurement data.
- **[formal_specifications](https://github.com/katzenpost/formal_specifications)**:
  ProVerif/Noise models for BACAP, client2, MKEM, Sphinx and the
  Noise handshakes.
- **[lean-ffi](https://github.com/katzenpost/lean-ffi)**: Lean FFI
  examples (to Rust and C), supporting the Lean modelling work.
- **[reunion](https://github.com/katzenpost/reunion)**: the REUNION
  PAKE rendezvous protocol.
- **[napkin-math](https://github.com/katzenpost/napkin-math)**:
  back-of-the-envelope latency and sizing calculations.
- **[talek](https://github.com/katzenpost/talek)**: fork of the
  Talek PIR private publish/subscribe system, kept for reference.
- **[echo](https://github.com/katzenpost/echo)**: small Rust example
  service built on the `thin_client` library.

### Lean libraries and tools

Verified protocol code and the libraries Lean applications such as jam
and glint are built from:

- **[CryptWalker](https://github.com/katzenpost/CryptWalker)**: a
  Lean cryptography library for prototyping protocols and proving
  properties about them, including the group chat member state
  machine shared with katzenqt.
- **[uproar](https://github.com/katzenpost/uproar)**: Noise and PQ
  Noise in Lean, with correctness proofs.
- **[huh](https://github.com/katzenpost/huh)**: a secure remote shell
  over PQ Noise, in Lean.
- **[cborg](https://github.com/katzenpost/cborg)**: CBOR
  serialisation for Lean, ported from Haskell's cborg; the CBOR layer
  of the Lean thin client.
- **[Tessera](https://github.com/katzenpost/Tessera)**: terminal user
  interfaces in Lean, Brick-style widgets with the Elm architecture.
- **[paw](https://github.com/katzenpost/paw)**: an Elm-style desktop
  GUI library for Lean, with security rules stated in its types.
- **[Logger](https://github.com/katzenpost/Logger)**: levelled,
  per-module logging for Lean programs.
- **[crossterm-lean-ffi](https://github.com/katzenpost/crossterm-lean-ffi)**:
  terminal control for Lean from the Rust crate crossterm.
- **[lean_unix_socket](https://github.com/katzenpost/lean_unix_socket)**:
  Unix domain sockets for Lean, used to reach `kpclientd`.
- **[lean-sys](https://github.com/katzenpost/lean-sys)**: fork of the
  Rust bindings to Lean's C API, used by the Rust-backed libraries
  above.

### Application support

- **[Rustic_Audio_PyO3](https://github.com/katzenpost/Rustic_Audio_PyO3)**:
  Rust audio recording, DSP and Opus encoding with Python bindings;
  powers push-to-talk voice messages in katzenqt.

### Operations and visualisation

- **[ansible-playbooks](https://github.com/katzenpost/ansible-playbooks)**:
  Ansible playbooks for deploying Katzenpost mix networks.
- **[status](https://github.com/katzenpost/status)**: mixnet
  diagnostics and status page (uses the thin client).
- **[worldmap](https://github.com/katzenpost/worldmap)**: draws a
  world map with mix-network nodes overlaid (uses the thin client).

### Project, documentation and outreach

- **[website](https://github.com/katzenpost/website)**: source for
  katzenpost.network.
- **[.github](https://github.com/katzenpost/.github)**: this
  organisation profile and shared community files.
- **[diagrams](https://github.com/katzenpost/diagrams)**: design
  diagrams and conceptual imagery.
- **[zine](https://github.com/katzenpost/zine)**: LaTeX source for
  the Katzenpost zine.

---

## Housekeeping

These repositories are dormant or superseded or obsolete.
We should think about deleting them.

### Already archived (read-only)

- **[katzen](https://github.com/katzenpost/katzen)**: former Gio
  messaging client, superseded by katzenqt.
- **[client](https://github.com/katzenpost/client)**: old client
  library, superseded by the monorepo `client2`/`kpclientd`.
- **[mixnet_uprising](https://github.com/katzenpost/mixnet_uprising)**:
  historical task tracker.
- **[slides](https://github.com/katzenpost/slides)**: old
  presentation slides.
- **[nixops](https://github.com/katzenpost/nixops)** /
  **[nixpkgs](https://github.com/katzenpost/nixpkgs)**: abandoned
  Nix deployment configuration (last touched 2018).

### Candidates for archival or deletion

- **[quic-go](https://github.com/katzenpost/quic-go)**: fork of
  quic-go.
- **[katzen.chat](https://github.com/katzenpost/katzen.chat)**:
  website for the retired `katzen` app; obsolete with `katzen`.
- **[fdroiddata](https://github.com/katzenpost/fdroiddata)**: stale
  fork of F-Droid metadata for the old `katzen` Android build.
- **[bfg](https://github.com/katzenpost/bfg)**: unlabelled Rust
  experiment, no README, untouched since 2024; purpose unclear.
- **[mceliece](https://github.com/katzenpost/mceliece)**,
  **[chacha20](https://github.com/katzenpost/chacha20)**,
  **[chacha20poly1305](https://github.com/katzenpost/chacha20poly1305)**:
  standalone crypto that `hpqc`/`circl` appear to have superseded;
  verify no remaining dependants before archiving.
- **[qrterminal](https://github.com/katzenpost/qrterminal)**: fork
  with no current consumer.

---

## License

GNU AGPL-3.0 across the org. A small number of submodules use
different licenses; see the LICENSE file inside each repository.
