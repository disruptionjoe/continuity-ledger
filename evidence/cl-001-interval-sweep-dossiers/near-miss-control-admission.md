---
source_id: active-cl001-near-miss-control-admission-20260719
source_type: absorber/control construction
applies_to_packets: active-cl001-dollar-arm-pending; active-cl001-bitcoin-arm-pending; active-cl001-control-pending
evidence_lanes: Frame adherence and declared-field guard; Settlement regime and class definition; Evaluator sweep and population boundary; Absorber, near-miss null, and arm-symmetry pressure; Agency surface and action-space burden; Falsifiers, open fields, and routing
provenance: governance/CHARTER.md; experiments/CL-001-phi-frame.md; evidence/cl-001-interval-sweep-source-intake.md; Bitcoin developer testing documentation; active dollar and Bitcoin mechanism/evaluator dossiers; inspected 2026-07-19
extracted_by: Codex child run RUN-20260719-543
extracted_on: 2026-07-19
status: draft
claim_status: none
verdict: none
---

# Near-Miss Control Admission Dossier

## Source Boundary

This draft dossier covers the active CL-001 near-miss/control admission queue
item. It is a construction and admission screen for later control source work:
it names what a control must preserve, which candidate pressures are visible,
and which candidates are not yet admitted.

Declared frame reference: `experiments/CL-001-phi-frame.md`.

Sources used:

- `governance/CHARTER.md`, especially `Matched Nulls`, `R0`-matching condition,
  and `CL-001: The Interval Sweep`.
- `experiments/CL-001-phi-frame.md`.
- `evidence/cl-001-interval-sweep-source-intake.md`.
- `evidence/cl-001-interval-sweep-dossier-manifest.md`.
- `evidence/cl-001-interval-sweep-dossiers/dollar-enforcement-mechanism-legal-operational.md`.
- `evidence/cl-001-interval-sweep-dossiers/bitcoin-enforcement-mechanism-protocol.md`.
- `evidence/cl-001-interval-sweep-dossiers/dollar-evaluator-sweep-us-argentina-retail.md`.
- `evidence/cl-001-interval-sweep-dossiers/bitcoin-evaluator-sweep-us-salvador-retail.md`.
- Bitcoin.org Developer Guide, "Testing Applications",
  `https://developer.bitcoin.org/examples/testing.html`.

This dossier does not admit a control for packet population. It does not
populate any packet field, does not score any gate, and does not establish that
any candidate control shares the declared frame.

### Scoped Extraction

| Construction-supported point | Packet field candidates | Evidence lane | Scope limit |
|---|---|---|---|
| The charter requires a near-miss control to be positively specified rather than selected by stipulated absence of the target agency surface. | `Z`, `V` | Absorber, near-miss null, and arm-symmetry pressure | This is an admission rule, not an admitted control. |
| The charter's `R0`-matching condition requires any near-miss null to be describable at the same declared frame, sharing `R0` and `M1`. | `R0`, `M1`, `Z`, `V` | Frame adherence and declared-field guard; Settlement regime and class definition | A candidate that needs a different frame is a second target, not a control. |
| The Bitcoin developer testing source supports regtest as a reduced-risk application-testing environment. | `T`, `B`, `Z`, `V` | Absorber, near-miss null, and arm-symmetry pressure | Regtest is only a candidate pressure on Bitcoin protocol validity; it does not automatically share retail `R0` or `M1`. |
| The active dollar and Bitcoin mechanism dossiers expose protocol-validity, legal-procedure, appeal, custody, tax, and institutional absorbers. | `Z`, `L`, `I`, `V` | Absorber, near-miss null, and arm-symmetry pressure; Falsifiers, open fields, and routing | The absorbers are live pressure points, not control verdicts. |
| Current evaluator dossiers create population boundaries that any control must preserve rather than replace. | `R0`, `K0`, `S0`, `V` | Evaluator sweep and population boundary | A population-specific control cannot vary the declared substrate role to become easier to score. |

### Typed Quantities

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
| Control admission | Construction status | Charter and source-intake contract. | Packet verdict, gate score, source fact. |
| Near-miss null | Positively specified same-frame control candidate | Charter matched-null rule. | Floor null, target arm, legitimacy verdict. |
| Regtest chain | Local testing environment and private chain state | Bitcoin developer testing documentation. | Bitcoin mainnet settlement, dollar legal tender, retail expectation, market value. |
| Legal-procedure absorber | Institutional remedy or administrative process | Dollar mechanism dossier. | Protocol validation, exit-cost interval, agency generation. |
| Protocol-validity absorber | Rule-validity explanation | Bitcoin mechanism dossier. | Retail access, legal/tax status, user preference. |
| Population boundary | U.S., Argentine, or Salvadoran retail evaluator role | Evaluator dossiers and frame declaration. | Substrate posture, mechanism `T`, gate verdict. |

### Losses And Imports

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
| A control imports its own construction choices and can become a second target if it does not share `R0` and `M1`. | `R0`, `M1`, `Z`, `V` | Charter `R0`-matching condition and frame declaration. | Later control work must state the shared frame before packet population. |
| Regtest imports operator control over chain state and reduced-risk testing conditions. | `T`, `B`, `I`, `Z`, `V` | Bitcoin developer testing source. | This may be too unlike public retail settlement to count as a same-frame near miss. |
| A dollar procedural sandbox, chargeback/dispute subset, or account-access subset would import institutional procedure and may only test appealability. | `I`, `P`, `Z`, `V` | Existing dollar mechanism dossier. | No exact dollar near-miss source is admitted here. |
| An exchange/custody or wallet-mediated Bitcoin control imports an intermediary and may move `T` away from protocol exclusion. | `I`, `B`, `Z`, `V` | Existing Bitcoin mechanism and evaluator dossiers. | Later source work must decide whether the control still tests the Bitcoin substrate or only an intermediary. |

### Agency And Feedback Burden

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
| Regtest or local test chain as a Bitcoin near miss. | Bitcoin developer testing source supports application testing under reduced risk. | Must be shown to share the declared retail `R0` and `M1`; otherwise it is a protocol sandbox, not a near-miss retail control. | It pressures protocol-validity and no-market-value absorbers. |
| Dollar procedural subset as a legal/institutional near miss. | Existing dollar mechanism dossier names consumer error and sanctions review surfaces. | Needs a positively specified same-frame control source, not merely absence of exclusion or absence of appeal. | It pressures ordinary regulated-dispute-resolution absorbers. |
| Custodial or exchange-mediated Bitcoin settlement as a control pressure. | Existing Bitcoin evaluator dossier makes custody and institutional recourse open burdens. | Needs exact source selection and a clear boundary between protocol `T` and intermediary `T`. | It pressures external-institution and custody absorbers. |

### What This Source Does Not Establish

This dossier does not populate any active CL-001 packet field. It does not score
any gate, issue a CL-001 verdict, accept a repo-owned claim, or admit a
near-miss control for active packet population.

It does not establish:

- that regtest, testnet, a sandbox, custody, exchange settlement, or a dollar
  procedural subset is a valid same-frame control;
- that any control passes or fails an agency gate;
- that any control shares `R0`, `M1`, `Omega`, or the settlement-boundary role;
- that a control can be selected by stipulating absence of the target surface;
- that the dollar or Bitcoin arms have a binding constraint class; or
- that the active Interval Sweep is ready to score any absorber gate.

### Falsifiers And Reopen Conditions

Reopen or supersede this dossier if:

- a candidate control needs a different `R0`, `M1`, `Omega`, or settlement
  boundary than `experiments/CL-001-phi-frame.md`;
- a later control is selected because it lacks the agency surface being tested;
- regtest or a similar sandbox is treated as public retail settlement without an
  explicit bridge;
- a dollar control becomes a legal-remedy example rather than a same-frame
  retail settlement near miss;
- a Bitcoin control becomes an exchange/custody example rather than a protocol
  substrate near miss; or
- this dossier is used as evidence that any CL-001 control has been admitted.

## No Claim Promotion

This source dossier cannot promote a CL-001 packet, gate, experiment verdict, or
repo-owned claim. It only records control-admission constraints and candidate
pressure for later review.
