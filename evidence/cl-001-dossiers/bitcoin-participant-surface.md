---
source_id: btc-participant-surface-whitepaper-devdocs-fullnode-v0
source_type: protocol and construction
applies_to_packets: cl001-bitcoin-proof-of-work
evidence_lanes: loss and import accounting; agency surface and action space; class-relative no-go or constraint; feedback and recurrence; falsifiers and open fields
provenance: Bitcoin whitepaper; Bitcoin.org developer operating-modes guide, P2P network guide and reference, and full-node documentation
extracted_by: Codex child run RUN-20260715-444
extracted_on: 2026-07-15
status: draft
claim_status: none
verdict: none
---

# Bitcoin Participant-Surface Dossier

## Source Boundary

This draft dossier covers the Bitcoin participant-surface queue item for
`cl001-bitcoin-proof-of-work`. It is scoped to design-level and documentation
evidence about nodes, lightweight clients, network relay, mining incentives,
transaction propagation, validation, and resource burdens.

Sources used:

- Satoshi Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System",
  `https://bitcoin.org/bitcoin.pdf`.
- Bitcoin.org Developer Guide, "Operating Modes",
  `https://developer.bitcoin.org/devguide/operating_modes.html`.
- Bitcoin.org Developer Guide, "P2P Network",
  `https://developer.bitcoin.org/devguide/p2p_network.html`.
- Bitcoin.org Developer Reference, "P2P Network",
  `https://developer.bitcoin.org/reference/p2p_networking.html`.
- Bitcoin.org, "Running A Full Node",
  `https://bitcoin.org/en/full-node`.

The whitepaper is design-level protocol evidence. The developer pages are
technical documentation and reference material. The full-node page is
operational guidance about node behavior and resource burdens. These sources
can orient participant-surface packet work, but the dossier does not populate
packet fields, does not score any gate, does not establish current market
behavior, does not establish actual participant motivation, and does not prove agency
generation.

### Scoped Extraction

| Source-supported point | Packet field candidates | Evidence lane | Scope limit |
|---|---|---|---|
| The whitepaper's design uses a peer-to-peer network in which nodes broadcast transactions, gather transactions into blocks, perform proof-of-work, and accept a history by cumulative proof-of-work. | `R1`, `K1`, `P`, `A`, `Omega`, `F`, `Z` | Agency surface and action space; feedback and recurrence; falsifiers and open fields | Design-level support only; does not prove current participants form a generated agency class. |
| The whitepaper's incentive section links block rewards and transaction fees to support for node participation and attack-resistance incentives. | `I`, `L`, `P`, `A`, `Omega`, `N`, `X` | Loss and import accounting; agency surface and action space; class-relative no-go or constraint | Incentive design evidence; does not establish actual profitability, market price, regulatory status, or present-day miner behavior. |
| Bitcoin.org full-node documentation presents full nodes as software that validates transactions and blocks, relays them, and may serve lightweight clients. | `S1`, `P`, `A`, `Omega`, `F`, `V` | Agency surface and action space; feedback and recurrence | Operational documentation; does not by itself show that a new action class is created rather than existing users operating software. |
| Bitcoin.org P2P documentation describes full nodes as peers maintaining a network for block and transaction exchange, while noting that consensus rules do not cover networking. | `B`, `S1`, `P`, `F`, `I`, `V` | Feedback and recurrence; loss and import accounting | Separates peer relay from consensus validity; packet work must not treat networking alone as settlement, finality, or agency. |
| Operating-mode documentation distinguishes full validation from simplified payment verification, including reliance on full nodes, omission risk, privacy exposure, and partition or Sybil pressure. | `I`, `L`, `A`, `Omega`, `Z`, `V` | Loss and import accounting; agency surface and action space; falsifiers and open fields | Supports an import/risk ledger for lightweight clients, not a verdict about Bitcoin's agency surface. |
| The P2P reference describes mempool-related messages as one node's view of unconfirmed transactions and notes miner relevance for transaction-fee gathering. | `M1`, `P`, `A`, `Omega`, `F`, `V` | Agency surface and action space; feedback and recurrence | Implementation/protocol-reference support only; does not establish fee-market equilibrium, miner policy, or settlement outcome. |

### Typed Quantities

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
| Full node | Software role validating and relaying blocks and transactions | Bitcoin.org full-node and P2P documentation. | Money, hashwork, legitimacy, agency generation. |
| Lightweight or SPV client | Client mode using headers and full-node responses | Operating-mode documentation. | Full validation, settlement finality, miner incentives, agency. |
| Transaction | Protocol data object propagated, validated, relayed, or included in blocks | Whitepaper and P2P documentation. | Economic value, legitimacy, action space. |
| Block | Protocol data object containing transactions and proof-of-work linkage | Whitepaper and developer documentation. | Electricity, fees, user trust, agency. |
| Peer connection | Network communication relation over the P2P protocol | P2P guide and reference. | Consensus validity, monetary value, finality. |
| Mempool inventory | Node-local view of unconfirmed transactions | P2P reference. | Complete network truth, settlement, agency surface. |
| Block reward and transaction fee | Protocol/incentive quantities denominated inside Bitcoin accounting | Whitepaper design and fee-related documentation. | Physical energy, legal legitimacy, social coordination, agency. |
| Storage, bandwidth, uptime, and hardware | Operational resource burdens for running a full node | Bitcoin.org full-node documentation. | Chainwork, fees, settlement confidence, agency. |

### Losses And Imports

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
| Full-node operation imports hardware, storage, bandwidth, connectivity, uptime, software maintenance, and operator choice. | `I`, `L`, `S1`, `A`, `V` | Full-node documentation names operating requirements and costs. | Later packet work must decide whether these are source imports, loss burdens, or participant commitments. |
| Lightweight clients import full-node responses and network reachability, with omission, privacy, partition, and Sybil risks. | `I`, `L`, `A`, `Omega`, `V` | Operating-mode documentation. | Later packet work must not treat SPV recognition as full validation without recording trust and privacy burdens. |
| Peer-to-peer relay imports network topology and message propagation separate from consensus validity. | `B`, `I`, `F`, `V` | P2P guide notes networking is separate from consensus rules. | Packet fields must keep network exchange distinct from settlement, finality, legitimacy, and agency. |
| Mining incentives import monetary accounting, transaction fees, subsidy rules, and participant preference assumptions. | `I`, `P`, `A`, `Omega`, `N`, `X` | Whitepaper incentive design and P2P reference fee relevance. | Current economics, exchange rates, regulation, real miner strategy, and environmental externalities remain outside this dossier. |
| Mempool data imports node-local perspective and may be incomplete or policy-dependent. | `M1`, `I`, `F`, `V` | P2P reference frames mempool responses as one node's view. | Later packet work must avoid treating one node's mempool as global Bitcoin state. |

### Agency And Feedback Burden

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
| Full-node validation and relay as a durable recognition surface. | Full-node and P2P documentation support validation, relay, and service to lightweight clients. | Does not prove that this surface creates a new agent class rather than providing tooling to existing actors. | A non-agency relay network can validate and forward records without agency-generating transduction. |
| Miner transaction selection and block construction around rewards or fees. | Whitepaper incentive design and P2P reference support fee relevance for miners. | Needs current-world or explicitly scoped construction evidence before asserting participant strategy or economic agency. | A puzzle contest or benchmark can reward computation without creating settlement or policy agency. |
| SPV or lightweight-client dependence on full nodes. | Operating-mode documentation supports header-based verification and full-node request dependence. | Does not establish that lightweight clients are generated agents; it may show an imported service relation. | Observer-side confidence or thin-client convenience may be an absorber rather than a CLTP agency surface. |
| Peer-to-peer propagation as network feedback. | P2P documentation supports block and transaction exchange among full nodes. | Does not by itself establish recurrence that changes future regimes, interfaces, or action classes. | Ordinary distributed-system propagation can explain message spread without continuity-ledger escape. |

### What This Source Does Not Establish

This dossier does not populate the Bitcoin packet fields. It does not score any
gate, issue a CL-001 verdict, accept a repo-owned claim, or establish that the
Bitcoin target differs from the hash-without-surface null for a
non-definitional reason.

It does not establish:

- current mining economics, fee-market behavior, market price, exchange-rate
  exposure, or regulatory conditions;
- actual user, miner, node-operator, developer, merchant, or institutional
  motivation;
- settlement finality, monetary legitimacy, public adoption, or social value;
- environmental-loss quantities or hardware supply-chain burdens;
- a class-relative no-go or constructive escape witness;
- that Bitcoin should pass any CL-001 gate; or
- that participant surfaces are generated rather than imported from existing
  actors and institutions.

### Falsifiers And Reopen Conditions

Reopen or supersede this dossier if:

- later packet work treats design incentives as observed participant behavior
  without separate evidence;
- a stronger primary or implementation source is selected for node, miner,
  wallet, or fee-policy behavior;
- packet fields collapse full-node validation, SPV trust, settlement
  confidence, monetary value, and agency into one scalar;
- the hash-without-surface null can reproduce the same participant-surface
  support by importing a hidden reward, benchmark, leaderboard, or recognition
  surface; or
- later review determines that the Bitcoin target needs current empirical
  participant evidence before any agency-surface field can be populated.

## No Claim Promotion

This source dossier cannot promote a CL-001 packet, gate, experiment verdict,
or repo-owned claim. It only records source extraction work for later review.
