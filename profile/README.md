# Katzenpost

A post-quantum mix network providing strong metadata privacy
against global passive adversaries.

📄 [Paper](https://arxiv.org/abs/2501.02933) ·
🌐 [Website](https://katzenpost.network) ·
📚 [Docs](https://katzenpost.network/docs/) ·
💬 [Community](https://katzenpost.network/pages/community/)

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

### Thin clients

Language bindings for building applications that talk to `kpclientd`:

- **Go** — in the monorepo at
  [`client2/thin`](https://github.com/katzenpost/katzenpost/tree/main/client2/thin)
- **Rust and Python** — [thin_client](https://github.com/katzenpost/thin_client)

### Project

- **[website](https://github.com/katzenpost/website)** —
  source for katzenpost.network

---

## New here?

- **Use it**: build [katzenqt](https://github.com/katzenpost/katzenqt)
  and `kpclientd` (see Clients above) — pre-built packages coming
- **Run a node**: [Admin Guide](https://katzenpost.network/docs/admin_guide/)
- **Build on it**: [Thin Client API](https://katzenpost.network/docs/thin_client_api_reference/)
- **Contribute**: [katzenpost/katzenpost](https://github.com/katzenpost/katzenpost) — issues and PRs
- **Research**: [Echomix paper](https://arxiv.org/abs/2501.02933) and [Threat Model](https://katzenpost.network/docs/threat_model/)

---

## License

GNU AGPL-3.0 across the org. A small number of submodules use
different licenses; see the LICENSE file inside each repository.
