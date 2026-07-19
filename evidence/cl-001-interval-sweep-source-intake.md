---
artifact_type: evidence_intake_contract
status: active_interval_sweep_contract
experiment: CL-001
frame_ref: experiments/CL-001-phi-frame.md
claim_status: none
verdict: none
---

# CL-001 Interval Sweep Source Intake Contract

## Purpose

This file defines the current evidence burden for the active CL-001 Interval
Sweep after the declared Phi frame. It is not evidence, does not select exact
sources, does not populate packet fields, does not score any gate, and does not
issue a verdict.

The contract exists so the dollar and Bitcoin arms can be populated later
without silently changing the frame. Until the burdens below are met by source
dossiers, active packet fields remain closed.

## Boundary Rules

- `experiments/CL-001-phi-frame.md` is the committed frame reference for this
  intake contract.
- `R0`, `M1`, and `Omega` are shared declared fields. They are not extracted
  from sources and may not be redefined by a source pass.
- `T` remains the only free field across the dollar and Bitcoin arms.
- Evaluator index `i` is a sweep coordinate, not a license to re-declare `R0`,
  `M1`, `Omega`, `B`, or the settlement-domain boundary.
- A source dossier that requires another frame field to vary records instrument
  pressure or instrument failure; it does not repair the frame.
- Founding-corpus artifacts and retired CL-001 dossiers may orient reviewers
  only as provenance. They cannot populate active Interval Sweep packet fields.
- This repository may record constraint class and exit-cost structure. It may
  not issue a legitimacy verdict.

## Current Evidence Surfaces

| Evidence surface | Role in CL-001 | Intake standard | Current intake status |
|---|---|---|---|
| Shared frame audit | Guard that later population preserves declared Phi. | Construction/provenance record showing each later dossier keeps `R0`, `M1`, `Omega`, and boundary role fixed. | Pending exact source pass. |
| Dollar enforcement mechanism | Target arm `T` candidate. | Primary, legal-operational, or institutionally authoritative support for discretionary and appealable exclusion in the declared retail settlement domain. | Pending exact source pass. |
| Bitcoin enforcement mechanism | Target arm `T` candidate. | Protocol-level and operational support for rule-constant and unappealable exclusion in the declared retail settlement domain. | Pending exact source pass. |
| Dollar evaluator sweep | Fixed-`S0` evaluator comparison. | Sources sufficient to bound constraint class and exit-cost interval for US retail and Argentine retail without changing the substrate role. | Pending exact source pass. |
| Bitcoin evaluator sweep | Fixed-`S0` evaluator comparison. | Sources sufficient to bound constraint class and exit-cost interval for US retail and Salvadoran retail without changing the substrate role. | Pending exact source pass. |
| Near-miss/control admission | Same-frame pressure against target arms. | Any control must be positively specified at the same declared `R0` and `M1`, and may not be selected by stipulating absence of an agency surface. | Pending exact source pass. |
| Arm-symmetry and blinding receipts | Gate-10 and frame-discipline process burden. | Process evidence that at least one material field was populated blind and that label-swap/no-merit-ordering checks are possible before verdict. | Pending exact source pass. |

## Evidence Lanes

| Evidence lane | Required before active packet population | Applies to |
|---|---|---|
| Frame adherence and declared-field guard | Dossier must state whether it preserves the declared Phi frame and which burden would fail if it does not. | All active surfaces |
| Mechanism and transition boundary | Source must support the operative enforcement process and settlement-recognition boundary claimed for `T` and `B`. | Dollar and Bitcoin arms |
| Settlement regime and class definition | Source must distinguish settlement rules, admissibility, continuation, and exclusion without importing a legitimacy verdict. | Dollar and Bitcoin arms; controls |
| Typed measurement family | Source must keep balances, UTXOs, quoted prices, exit costs, legal rights, energy, fees, and legitimacy unlike unless a typed conversion map is explicitly declared. | All active surfaces |
| Loss, import, and access accounting | Source or construction note must identify access limits, external subsidies, hidden schemas, uncertainty, institutional imports, hardware/network imports, or exchange-rate exposure before any gate is scored. | All active surfaces |
| Constraint class and exit-cost interval | Dossier must name the candidate binding constraint class and the evidence needed to bound its exit-cost interval without ranking arms. | Target arms and evaluator sweep |
| Agency surface and action-space burden | Source must support, weaken, or leave open any claimed participant surface and price/save/contract action space. | Target arms and controls |
| Evaluator sweep and population boundary | Dossier must separate population-specific burdens from substrate-specific claims and preserve fixed-`S0` comparison. | Evaluator sweep |
| Absorber, near-miss null, and arm-symmetry pressure | Source or construction note must name the ordinary explanation, same-frame control pressure, label-swap exposure, and no-merit-ordering burden. | All active surfaces |
| Falsifiers, open fields, and routing | Packet population must keep failure conditions and unresolved source gaps visible, and must route a recognized frame defect out of the local run. | All active surfaces |

## Per-Surface Intake Ledgers

### Shared Frame Audit

| Evidence lane | Minimum source burden | Current intake status |
|---|---|---|
| Frame adherence and declared-field guard | Record that the later dossier uses `experiments/CL-001-phi-frame.md` as the frame source and does not re-declare shared fields. | Pending exact source pass. |
| Falsifiers, open fields, and routing | State the condition under which a source pass stops the run for frame pressure or instrument failure. | Pending exact source pass. |

### Dollar Enforcement Mechanism

| Evidence lane | Minimum source burden | Current intake status |
|---|---|---|
| Mechanism and transition boundary | Source support for how discretionary and appealable exclusion becomes binding in the declared retail settlement domain. | Pending exact source pass. |
| Settlement regime and class definition | Source support for rule recognition, settlement continuation, and ordinary retail actor admissibility without a legitimacy verdict. | Pending exact source pass. |
| Loss, import, and access accounting | Source support for costs, access limits, dispute/appeal imports, institutional boundary conditions, and open burdens. | Pending exact source pass. |
| Constraint class and exit-cost interval | Evidence needed to bound the candidate constraint class and exit-cost interval for the dollar substrate posture. | Pending exact source pass. |

### Bitcoin Enforcement Mechanism

| Evidence lane | Minimum source burden | Current intake status |
|---|---|---|
| Mechanism and transition boundary | Protocol-level source support for how rule-constant and unappealable exclusion becomes binding in the declared retail settlement domain. | Pending exact source pass. |
| Settlement regime and class definition | Source support for recognition, settlement continuation, ordinary retail actor admissibility, and the boundary between protocol validity and external institutions. | Pending exact source pass. |
| Loss, import, and access accounting | Source support for fees, custody/key burdens, network/hardware imports, exchange-rate exposure, and open burdens. | Pending exact source pass. |
| Constraint class and exit-cost interval | Evidence needed to bound the candidate constraint class and exit-cost interval for the Bitcoin substrate posture. | Pending exact source pass. |

### Evaluator Sweep

| Evidence lane | Minimum source burden | Current intake status |
|---|---|---|
| Evaluator sweep and population boundary | Source or construction support for US and Argentine retail under the dollar substrate, and US and Salvadoran retail under the Bitcoin substrate. | Pending exact source pass. |
| Constraint class and exit-cost interval | Evidence sufficient to test whether the binding constraint class moves with evaluator population at fixed `S0`. | Pending exact source pass. |
| Typed measurement family | Explicit separation of quoted prices, legal constraints, market access, volatility, fees, balances, and legitimacy claims. | Pending exact source pass. |

### Near-Miss And Control Admission

| Evidence lane | Minimum source burden | Current intake status |
|---|---|---|
| Absorber, near-miss null, and arm-symmetry pressure | Positively specified controls at the same declared `R0` and `M1`; no control selected by stipulated absence of the tested agency surface. | Pending exact source pass. |
| Settlement regime and class definition | Source or construction support that the control shares the frame rather than becoming a second target. | Pending exact source pass. |

### Arm-Symmetry And Blinding Receipts

| Evidence lane | Minimum source burden | Current intake status |
|---|---|---|
| Absorber, near-miss null, and arm-symmetry pressure | Process receipt for label-swap invariance, no merit ordering, and no same-run founding-corpus contamination before any verdict. | Pending exact source pass. |
| Falsifiers, open fields, and routing | Process receipt showing at least one material field was populated blind, or a stop record explaining why the run cannot satisfy frame discipline. | Pending exact source pass. |

## Control And Symmetry Burdens

- A near-miss control must be admissible at the same declared `R0` and `M1`.
- A control cannot be rejected because it lacks the agency surface being tested.
- A population-specific source cannot change the declared frame to make an arm
  easier to score.
- Arm labels must not carry normative weight. Any source pass that turns
  "appealable" or "unappealable" into a merit ranking fails the neutrality
  burden.
- If the intake contract cannot support a two-outcome sweep, the next output is
  a stop record, not a repaired frame.

## No Claim Promotion

This intake contract cannot promote a CL-001 packet, gate, experiment verdict,
or repo-owned claim. It only defines what must be gathered before later active
Interval Sweep packet population can be audited.
