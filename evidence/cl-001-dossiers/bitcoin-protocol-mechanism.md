---
source_id: btc-protocol-mechanism-whitepaper-devref-core-v31-1
source_type: protocol
applies_to_packets: cl001-bitcoin-proof-of-work
evidence_lanes: mechanism and transition boundary; regime and class definition; typed measurement family; absorber and null pressure
provenance: Bitcoin whitepaper; Bitcoin.org developer block-chain guide and reference; Bitcoin Core v31.1 pow.cpp and chain.h
extracted_by: Codex child run RUN-20260715-440
extracted_on: 2026-07-15
status: draft
claim_status: none
verdict: none
---

# Bitcoin Protocol Mechanism Dossier

## Source Boundary

This draft dossier covers the Bitcoin protocol mechanism queue item for
`cl001-bitcoin-proof-of-work`. It is scoped to proof-of-work, block-header
hashing, target thresholds, cumulative work representation, and difficulty
behavior.

Sources used:

- Satoshi Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System",
  `https://bitcoin.org/bitcoin.pdf`.
- Bitcoin.org Developer Guide, "Block Chain",
  `https://developer.bitcoin.org/devguide/block_chain.html`.
- Bitcoin.org Developer Reference, "Block Chain",
  `https://developer.bitcoin.org/reference/block_chain.html`.
- Bitcoin Core source, tag `v31.1`, peeled commit
  `9be056a8a72b624dae9623b2f7bded92c2a21c91`, `src/pow.cpp` and `src/chain.h`,
  `https://github.com/bitcoin/bitcoin/tree/v31.1`.

The whitepaper is design-level protocol evidence. The Bitcoin.org developer
pages are protocol documentation. Bitcoin Core is implementation evidence for a
widely used node implementation at a pinned tag. None of these sources alone
establish current market behavior, settlement finality, energy expenditure,
participant policy, agency generation, or any CL-001 gate result.

### Scoped Extraction

| Source-supported point | Packet field candidates | Evidence lane | Scope limit |
|---|---|---|---|
| The design links transactions into a hash-based proof-of-work chain and treats cumulative proof-of-work as the basis for accepting a history when nodes rejoin. | `T`, `B`, `C`, `R1`, `K1`, `Z` | Mechanism and transition boundary; regime and class definition; absorber and null pressure | Design-level source; does not prove current network conditions, economic settlement, or participant agency. |
| Proof-of-work is produced by varying block data such as a nonce until the block hash satisfies the required difficulty condition, and later blocks add redo burden for historical modification. | `T`, `B`, `C`, `L`, `Z` | Mechanism and transition boundary; absorber and null pressure | Supports protocol mechanism only; does not quantify electricity, hardware, or environmental loss. |
| Bitcoin.org documentation identifies the serialized block header, previous-header hash, Merkle root, time, `nBits`, and nonce as part of the proof-of-work and block-validity surface. | `S0`, `M0`, `T`, `B`, `S1`, `M1` | Mechanism and transition boundary; typed measurement family | Documentation source; packet population still needs later field-by-field review. |
| The target threshold is represented by `nBits`; a block-header hash must be less than or equal to that target to satisfy proof-of-work. | `M0`, `T`, `B`, `M1`, `C` | Mechanism and transition boundary; typed measurement family | Describes validation criterion, not monetary value, legitimacy, or agency. |
| Difficulty behavior is retargeted over 2,016-block intervals against a two-week target timespan in the developer guide, and Bitcoin Core `pow.cpp` implements interval checks, target calculation, transition limits, target derivation, and proof-of-work comparison. | `T`, `B`, `C`, `F` | Mechanism and transition boundary; feedback and recurrence | Mechanistic feedback only; does not establish a broader agency feedback loop. |
| Bitcoin Core `chain.h` records `nChainWork` as expected hashes up to and including a block and exposes proof calculation from `nBits`. | `C`, `M1`, `V` | Typed measurement family; continuity witness | Implementation-level work accounting; not a universal scalar for security, value, settlement confidence, or agency. |

### Typed Quantities

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
| Block header | Serialized byte structure | Bitcoin.org reference describes an 80-byte header used for proof-of-work hashing. | Electricity, money, settlement confidence, agency. |
| Header hash | 256-bit hash output / ordered integer for target comparison | Bitcoin.org reference and Bitcoin Core proof-of-work check. | Energy consumed, market price, legitimacy, finality. |
| `nBits` | 32-bit compact target encoding | Bitcoin.org reference and Bitcoin Core target derivation. | Hash attempts, joules, fees, exchange value. |
| Target threshold | 256-bit unsigned integer threshold | Bitcoin.org reference and Bitcoin Core `DeriveTarget`. | Difficulty as social burden, market value, agency surface. |
| Nonce | 32-bit header field changed by miners | Bitcoin.org reference and whitepaper mechanism. | Proof-of-work amount, electricity, policy recognition. |
| Difficulty adjustment interval | Block count and elapsed seconds | Bitcoin.org developer guide and Bitcoin Core retarget code. | Ecological feedback, market feedback, agency generation. |
| Chain work | Expected number of hashes represented in implementation state | Bitcoin Core `nChainWork` and `GetBlockProof`. | Economic value, settlement finality, legitimacy, participant action space. |

### Losses And Imports

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
| Hash attempts are computational work, but the cited protocol sources do not by themselves quantify electricity, heat, embodied hardware, mining equipment, or grid effects. | `L`, `I`, `V` | Whitepaper and protocol docs support proof-of-work mechanics; they do not provide a physical loss ledger. | Later evidence must separate hashwork, electricity, hardware depreciation, heat, and externalities. |
| The whitepaper's security story imports an assumption about majority CPU power not cooperating to attack the network. | `I`, `N`, `X`, `V` | Whitepaper design argument. | Later packet work must name the constrained class and avoid treating the assumption as a proved current-world fact. |
| Bitcoin Core implementation evidence imports a specific software version and implementation context. | `V`, `C`, `M1` | Pinned `v31.1` source. | Later review must decide how implementation evidence relates to protocol-level packet claims. |
| Chainwork accounting imports an implementation representation for expected hashes. | `C`, `M1`, `V` | Bitcoin Core `chain.h`. | Later packet work must not convert chainwork into value, finality, legitimacy, or agency without separate evidence. |

### Agency And Feedback Burden

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
| Difficulty retargeting as protocol feedback. | Developer guide and Bitcoin Core `pow.cpp` support a mechanistic retarget process. | Does not establish participant adaptation, agency generation, or settlement behavior. | A non-agency hash benchmark can also adjust difficulty unless persistent recognition and action surfaces are separately shown. |
| Chain extension and cumulative work as a recognition surface. | Whitepaper and Bitcoin Core chain-work representation support protocol recognition of accumulated work. | Does not establish users, miners, markets, developers, or institutions as generated or recruited agent classes. | Ordinary security-protocol and accounting-ledger absorbers remain live. |

### What This Source Does Not Establish

This dossier does not populate the Bitcoin packet fields. It does not score any gate,
issue a CL-001 verdict, accept a repo-owned claim, or establish a
participant-surface dossier.

It does not establish:

- electricity, hardware, environmental, or market-loss quantities;
- settlement finality, monetary value, legitimacy, or fee-market behavior;
- miner, node, wallet, developer, user, or market participant agency;
- a class-relative no-go or constructive escape witness;
- that Bitcoin should pass any CL-001 gate; or
- that the Bitcoin target differs from the hash-without-surface null for a
  non-definitional reason.

### Falsifiers And Reopen Conditions

Reopen or supersede this dossier if:

- a cited URL changes in a way that breaks the extracted point;
- a better pinned protocol source replaces the Bitcoin.org documentation or
  Bitcoin Core tag used here;
- later review finds that the dossier imports participant-surface or economic
  conclusions from a mechanism-only source;
- the packet starts treating chainwork, energy, security, value, finality, or
  agency as interchangeable quantities; or
- null-packet construction shows the same mechanism evidence can satisfy the
  target burden without a persistent recognition or action surface.

## No Claim Promotion

This source dossier cannot promote a CL-001 packet, gate, experiment verdict,
or repo-owned claim. It only records source extraction work for later review.
