---
source_id: active-bitcoin-enforcement-whitepaper-devguide-core31-20260719
source_type: protocol and implementation
applies_to_packets: active-cl001-bitcoin-arm-pending
evidence_lanes: Frame adherence and declared-field guard; Mechanism and transition boundary; Settlement regime and class definition; Typed measurement family; Loss, import, and access accounting; Constraint class and exit-cost interval; Agency surface and action-space burden; Falsifiers, open fields, and routing
provenance: Bitcoin whitepaper at bitcoin.org; Bitcoin.org Developer Guide Block Chain; Bitcoin Core repository tag v31.1, including src/pow.cpp and src/chain.h; Bitcoin Core validation feature page; retrieved 2026-07-19
extracted_by: Codex child run RUN-20260719-534
extracted_on: 2026-07-19
status: draft
claim_status: none
verdict: none
---

# Bitcoin Enforcement Mechanism Protocol Dossier

## Source Boundary

This draft dossier covers the active CL-001 Bitcoin enforcement-mechanism queue
item. It is scoped to transaction validity, double-spend exclusion,
proof-of-work ordering, chain-work accounting, difficulty behavior, and
independent validation as protocol-level sources for a rule-constant Bitcoin
settlement boundary.

Declared frame reference: `experiments/CL-001-phi-frame.md`.

Sources used:

- Satoshi Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System",
  `https://bitcoin.org/bitcoin.pdf`.
- Bitcoin.org Developer Guide, "Block Chain",
  `https://developer.bitcoin.org/devguide/block_chain.html`.
- Bitcoin Core repository, tag `v31.1`,
  `https://github.com/bitcoin/bitcoin/tree/v31.1`.
- Bitcoin Core source, tag `v31.1`, `src/pow.cpp`,
  `https://raw.githubusercontent.com/bitcoin/bitcoin/v31.1/src/pow.cpp`.
- Bitcoin Core source, tag `v31.1`, `src/chain.h`,
  `https://raw.githubusercontent.com/bitcoin/bitcoin/v31.1/src/chain.h`.
- Bitcoin.org, "Bitcoin Core Validation",
  `https://bitcoin.org/en/bitcoin-core/features/validation`.

The whitepaper is design-level protocol evidence. The developer guide is
protocol documentation. The Bitcoin Core files are pinned implementation
evidence for a widely used node implementation. The validation page is an
orientation source for independent validation. None of these sources alone
establish current retail adoption, current fees, exchange-rate exposure,
custody behavior, legal status, population-specific exit costs, or any CL-001
gate result.

### Scoped Extraction

| Source-supported point | Packet field candidates | Evidence lane | Scope limit |
|---|---|---|---|
| The whitepaper frames Bitcoin as peer-to-peer electronic cash and uses digital signatures plus a publicly announced transaction history to address double spending without a trusted mint. | `R1`, `K1`, `T`, `B`, `C`, `V` | Mechanism and transition boundary; Settlement regime and class definition | Design-level source; does not prove current retail settlement, exchange infrastructure, custody, or user agency. |
| The whitepaper's proof-of-work construction makes history revision depend on redoing proof-of-work and outpacing later work. | `T`, `B`, `C`, `L`, `N`, `Z` | Mechanism and transition boundary; Constraint class and exit-cost interval | Supports protocol mechanism, not a current-world reversal-cost interval, legal finality, or legitimacy. |
| The Bitcoin.org block-chain guide describes the block chain as an ordered, timestamped public ledger and names full-node independent validation and consensus rules. | `R1`, `K1`, `B`, `M1`, `C`, `V` | Settlement regime and class definition; Typed measurement family | Documentation source; does not establish all wallet, exchange, merchant, or custody behavior. |
| The Bitcoin.org block-chain guide describes unspent transaction outputs and forbidden double spends as part of payment validity. | `T`, `B`, `N`, `M1`, `V` | Mechanism and transition boundary; Constraint class and exit-cost interval | Supports rule-based exclusion of invalid double spends; does not show retail actor exit costs or agency generation. |
| Bitcoin Core v31.1 `pow.cpp` implements difficulty-adjustment behavior, target derivation, proof-of-work range checks, and hash-target comparison. | `T`, `B`, `C`, `F`, `V` | Mechanism and transition boundary; Typed measurement family | Implementation evidence; packet work must distinguish Bitcoin Core behavior from broader network sociology. |
| Bitcoin Core v31.1 `chain.h` records block validity levels and chain-work representation for indexed chain state. | `K1`, `M1`, `C`, `V` | Settlement regime and class definition; Typed measurement family | Implementation accounting; chainwork is not value, legitimacy, agency, or settlement confidence. |
| The Bitcoin Core validation page presents full validation as checking received blocks and transactions for rule validity without trusting the miner who produced them. | `P`, `A`, `Omega`, `Z`, `V` | Agency surface and action-space burden; Falsifiers, open fields, and routing | Orientation source only; does not prove that validation creates a new agent class or that users actually run full nodes. |

### Typed Quantities

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
| Transaction | Protocol data object with signatures, inputs, and outputs | Whitepaper and developer guide. | Legal tender, bank balance, legitimacy, energy. |
| UTXO | Unspent transaction output state | Bitcoin.org block-chain guide. | Dollar account balance, consumer error notice, administrative appeal. |
| Block header | Serialized protocol object containing previous hash, Merkle root, time, target bits, and nonce | Bitcoin Core and developer documentation. | Retail settlement right, legal remedy, market value, agency. |
| Proof-of-work hash | 256-bit hash interpreted against a target threshold | Whitepaper and Bitcoin Core `pow.cpp`. | Electricity, legal tender, transaction value, legitimacy. |
| Target or `nBits` | Compact representation or threshold for proof-of-work validity | Bitcoin Core `pow.cpp` and block-header context. | Chainwork, fees, retail access, legal appealability. |
| Chain work | Expected hash-work accounting in indexed chain state | Bitcoin Core `chain.h`. | Dollar denomination, exchange price, finality, legitimacy. |
| Block validity level | Implementation status flag for validation progress | Bitcoin Core `chain.h`. | Market acceptance, legal right, agency surface. |

### Losses And Imports

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
| Proof-of-work imports computation, hardware, network communication, and electricity, but the selected sources do not quantify those losses. | `L`, `I`, `V` | Whitepaper mechanism and Bitcoin Core proof-of-work implementation. | Later packet work must source physical energy, fees, hardware, and externalities separately. |
| The whitepaper security argument imports assumptions about honest-node or CPU-power distribution. | `I`, `N`, `X`, `V` | Whitepaper design argument. | Later packet work must state the model class and avoid treating the assumption as a proved current-world fact. |
| Bitcoin Core evidence imports a pinned software implementation, tag `v31.1`, not a law of all possible Bitcoin clients. | `I`, `K1`, `V` | GitHub tag `v31.1`, `pow.cpp`, and `chain.h`. | Later review must decide when implementation evidence can support protocol-level packet population. |
| Retail Bitcoin settlement imports wallets, keys, custody choices, exchange paths, price exposure, merchant acceptance, and legal/institutional interfaces outside this source set. | `I`, `L`, `P`, `A`, `Omega`, `V` | The selected sources do not cover these burdens. | Evaluator and participant-surface dossiers remain required before active packet population can score action space or exit-cost intervals. |
| Rule-constant exclusion may be absorbed by ordinary protocol validity unless a later packet shows a CLTP-relevant constraint class and action surface. | `Z`, `N`, `V` | UTXO/double-spend and validation sources support rule exclusion only. | Later work must pressure-test protocol-validity absorber before claiming agency-generating transduction. |

### Agency And Feedback Burden

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
| Full-node validation as a recognition surface. | Developer guide and validation page support independent validation of blocks and transactions. | Does not prove that ordinary retail users operate full nodes or that validation creates a generated agency class. | Ordinary security-protocol validation can absorb the surface without CLTP agency generation. |
| Proof-of-work and difficulty adjustment as recurrent mechanism. | Whitepaper and Bitcoin Core `pow.cpp` support proof-of-work and retarget behavior. | Does not establish participant adaptation, economic incentives, or retail settlement behavior. | A benchmark or puzzle protocol can reproduce difficulty feedback without settlement agency. |
| UTXO and double-spend exclusion as rule-constant settlement boundary. | Developer guide supports output-spend constraints and forbidden double-spend status. | Does not quantify exit cost, fee burden, custody/key loss, or appeal absence. | Ordinary protocol validity may explain exclusion without a broader agency surface. |
| Computational impracticality of reversal as candidate unappealable posture. | Whitepaper supports proof-of-work redo burden as design-level reversal pressure. | Does not establish absolute irreversibility, legal finality, exchange reversals, custody reversals, or social recourse. | External-institution and custodial-service absorbers remain live. |

### What This Source Does Not Establish

This dossier does not populate any active CL-001 packet field. It does not score
any gate, issue a CL-001 verdict, accept a repo-owned claim, or establish the
Bitcoin arm's candidate enforcement posture.

It does not establish:

- current hash rate, current fees, actual confirmation practices, retail use,
  merchant acceptance, exchange access, custody behavior, or legal status;
- US or Salvadoran retail evaluator exit-cost intervals;
- that Bitcoin exclusion is unappealable in every relevant retail settlement
  context;
- that Bitcoin's protocol-validity surface creates or recruits an agency class;
- monetary legitimacy, policy merit, investment value, or user preference;
- a class-relative no-go or constructive escape witness;
- that the Bitcoin arm passes any CL-001 gate; or
- that Bitcoin differs from dollar settlement for a non-frame artifact reason.

### Falsifiers And Reopen Conditions

Reopen or supersede this dossier if:

- active packet population requires changing `R0`, `M1`, `Omega`, or the shared
  settlement-boundary role;
- later work treats Bitcoin Core implementation state as equivalent to all
  Bitcoin settlement behavior without an explicit bridge;
- a stronger pinned protocol or implementation source supersedes tag `v31.1`;
- later evaluator evidence shows that retail Bitcoin settlement depends on
  custodial or legal appeal paths that move the candidate `T` boundary;
- packet work converts chainwork, price, legal status, finality, legitimacy, or
  agency into one scalar; or
- the protocol-validity absorber explains the same evidence without a
  continuity-ledger agency surface.

## No Claim Promotion

This source dossier cannot promote a CL-001 packet, gate, experiment verdict, or
repo-owned claim. It only records source extraction work for later review.
