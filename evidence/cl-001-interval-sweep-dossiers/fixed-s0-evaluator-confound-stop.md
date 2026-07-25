---
artifact_type: construction_audit_stop
status: draft
experiment: CL-001
frame_ref: experiments/CL-001-phi-frame.md
source_id: cl001-fixed-s0-evaluator-confound-stop-20260724
source_type: construction/provenance audit
applies_to_packets: active-cl001-dollar-arm-pending; active-cl001-bitcoin-arm-pending
evidence_lanes: Frame adherence and declared-field guard; Evaluator sweep and population boundary; Constraint class and exit-cost interval; Falsifiers, open fields, and routing
provenance: governance/CHARTER.md; experiments/CL-001-phi-frame.md; experiments/CL-001-interval-sweep.md; evidence/cl-001-interval-sweep-dossiers/dollar-evaluator-sweep-us-argentina-retail.md; evidence/cl-001-interval-sweep-dossiers/bitcoin-evaluator-sweep-us-salvador-retail.md; inspected 2026-07-24
extracted_by: Codex child run RUN-20260724-230909-continuity-ledger-progress-fixed-s0-evaluator-audit
extracted_on: 2026-07-24
updated_by: Codex child run RUN-20260725-031112-continuity-ledger-progress
updated_on: 2026-07-25
claim_status: none
verdict: none
---

# Fixed-S0 Evaluator-Confound Stop

## Source Boundary

The current evaluator pairs do not yet support the experiment's required
fixed-`S0` attribution. Changing from US to Argentine retail, or from US to
Salvadoran retail, changes more than the evaluator index: the active dossiers
explicitly import different jurisdictional rules, policy states, financial
infrastructure, access paths, subsidies, wallets, and exchange conditions.

The bounded construction-space screen in
`fixed-s0-construction-space-screen.md` found no current-contract witness that
keeps the named population pairs while holding `S0`, `T`, `B`, and the relevant
institutional imports fixed as only evaluator `i` changes. CL-001 therefore
stops before packet population. This is a design-identification stop, not a
CL-001 gate score, claim result, or verdict.

Repo-local surfaces used:

- `governance/CHARTER.md`, especially the Nearer Guiding Hypothesis, Frame
  Discipline, and CL-001 outcome contract.
- `experiments/CL-001-phi-frame.md`.
- `experiments/CL-001-interval-sweep.md`.
- `evidence/cl-001-interval-sweep-dossiers/dollar-evaluator-sweep-us-argentina-retail.md`.
- `evidence/cl-001-interval-sweep-dossiers/bitcoin-evaluator-sweep-us-salvador-retail.md`.
- `evidence/cl-001-interval-sweep-dossiers/fixed-s0-construction-space-screen.md`.

This construction audit uses current repo-local evidence and does not score any
gate and does not populate any active CL-001 packet field. It did not read the
founding corpus, private T-03 capsule, or unblinding key.

### Audit Question

Can the named evaluator sweep instantiate this charter requirement?

> the class of constraints the ledger finds binding varies with `S0` at fixed
> evaluator, and does not vary with the evaluator at fixed `S0`

The frame declaration makes the required intervention stricter: evaluator
populations may not redeclare `R0`, `M1`, `Omega`, or any frame field, and `T`
is the only free field across the target arms.

### Construction Test

For each arm, a valid evaluator comparison needs a witness of the form:

```text
(R0, K0, S0, M0, T, B, M1, Omega, institutional imports) fixed
i changes
```

The current evidence instead has this form:

```text
i changes
jurisdiction, policy, access, and institutional imports also change
```

Those additional changes need not be called part of `S0` to create the defect.
If they affect which constraints bind or the cost of exit, the experiment
cannot attribute the observed movement to evaluator preference. If they are
promoted into `S0`, `T`, or `B`, then the comparison is no longer fixed-`S0`.
If they are discarded, the packet erases load-bearing differences already
named by its own evidence.

### Scoped Extraction

| Arm | Current evaluator contrast | Co-varying construction burden already recorded | Why fixed-`S0` is not witnessed |
|---|---|---|---|
| Dollar | US retail / Argentine retail | US payment and banking surveys are paired with Argentine banking infrastructure, foreign-currency accounts, exchange rules, and an April 2025 policy change. The dossier says exchange-market access is not identical to retail settlement access and that peso-denominated payment access must be separated from dollar-denominated settlement. | The evidence does not hold institutional enforcement and access conditions fixed. A difference in binding constraint or exit cost could follow jurisdiction, exchange regime, banking rails, denomination use, or policy timing rather than evaluator preference. |
| Bitcoin | US retail / Salvadoran retail | US cryptocurrency survey and tax treatment are paired with Salvadoran Bitcoin law, 2025 reform, public-policy implementation, remittance/inclusion evidence, wallet/subsidy context, and changing acceptance obligations. The dossier itself asks whether the reform creates frame pressure. | Protocol validity may remain fixed while the settlement-facing enforcement boundary and imported institutional surfaces vary. A difference could follow law, subsidy, wallet design, exchange access, or policy time rather than evaluator preference. |

The evidence is sufficient for the stop because the burden is not to prove
that every co-varying surface changes the result. The burden is to supply a
construction that holds the experiment's causal fields fixed before using the
result to choose between its two lethal branches. No such construction is
present.

### Typed Quantities

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
| Evaluator index `i` | Declared sweep coordinate over named retail populations | Frame declaration and active scaffold. | Jurisdiction, law, policy time, banking rails, wallet design, subsidy, exchange access. |
| `S0` | Declared retail-settlement enforcement-substrate role | Frame declaration. | A population label, preference, exit cost, or legitimacy. |
| `T` | Arm-specific enforcement mechanism/posture and the only free frame field | Frame declaration. | Evaluator index, institutional import, merit ordering. |
| `B` | Shared settlement-recognition boundary role | Frame declaration. | Concrete jurisdiction-specific legal or operational boundary. |
| Exit-cost interval | Still-unconstructed typed burden | Active evaluator dossiers. | Account ownership, payment share, legal status, price, legitimacy. |

### Two-Outcome Boundary

CL-001 has no "instrument could not discriminate" result after it begins.
That rule prevents a failed instrument from becoming a survival branch.

It does not authorize running a known non-identifying comparison. Under Frame
Discipline rules 1 and 2, a wrong frame stops before outcome visibility and a
replacement is preregistered separately. Treating within-arm movement as
"preferences do" when jurisdictional and institutional mechanisms also move
would manufacture the experiment's first lethal branch rather than test it.

### Losses And Imports

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
| The dollar evaluator change imports a different jurisdiction, exchange regime, banking infrastructure, and policy date. | `S0`, `T`, `B`, `I`, `L`, `N`, `V` | Active dollar evaluator dossier and construction-space screen. | No current-contract construction isolates evaluator variation from those mechanisms. |
| The Bitcoin evaluator change imports different legal status, tax treatment, policy implementation, wallet/subsidy context, and access conditions. | `B`, `I`, `L`, `N`, `P`, `V` | Active Bitcoin evaluator dossier and construction-space screen. | No current-contract construction isolates evaluator variation from those mechanisms. |
| Calling the imported differences "context" does not make them inert if they affect the binding constraint or exit cost. | `I`, `N`, `V` | Charter causal attribution plus both dossier burden tables. | A positive fixed-field witness or new preregistration is required. |

Until a separately governed run supplies one of the admissible wakes below:

- do not populate active dollar or Bitcoin packet fields;
- do not execute the evaluator sweep;
- do not interpret evaluator differences as preference effects;
- do not treat T-03 blind-return readiness as sufficient to open packet
  population; and
- do not repair the committed frame or substitute populations inside this
  Run.

The private T-03 capsule and key were not read. This stop is independent of
their integrity, inferability, and material sufficiency.

### Agency And Feedback Burden

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
| Fixed-`S0` evaluator comparison as the experiment's causal surface. | Charter, frame declaration, and active scaffold require it. | No construction witness fixes enforcement and institutional surfaces while only `i` changes. | Ordinary cross-jurisdiction observational comparison absorbs the present design. |
| Routing a recognized frame defect to the frame holder. | Charter Frame Discipline rule 7. | Parent Runtime delivery is still required for the stable Attention pointer. | A record that is not delivered remains a routing failure. |
| T-03 blind return as independent process progress. | Existing public T-03 preparation and validator receipt. | It cannot repair evaluator identification. | Blinding integrity does not absorb a causal-design defect. |

### What This Source Does Not Establish

This audit does not establish that a particular jurisdictional or institutional
surface actually causes a measured constraint difference. It does not establish
the correct replacement populations or frame, a binding constraint class, an
exit-cost interval, an active packet field, a gate result, a claim result, or a
CL-001 verdict.

It establishes only that the current evidence does not identify the
fixed-`S0` intervention the preregistered causal interpretation requires.

### Falsifiers And Reopen Conditions

This stop can be superseded only by one of:

1. new evidence that overturns the construction-space screen by showing, for
   both named evaluator pairs, common jurisdictional and operational
   enforcement surfaces with `S0`, `T`, `B`, policy time, access, and all
   outcome-relevant institutional imports fixed while only `i` changes;
2. a new preregistered CL-001 design that changes the evaluator pairs while
   preserving the charter's causal question; or
3. a new preregistered frame that explicitly types the jurisdictional and
   institutional surfaces rather than hiding or discarding them.

A new source alone does not clear the stop unless it supplies the missing
identification. A T-03 return alone does not clear it because blinding and
fixed-`S0` identification are independent method burdens.

### Routing

Stable awareness pointer:
`system-attention#continuity-ledger-cl001-fixed-s0-evaluator-stop`.

Decision needed from the frame holder:

- **A — Recommended:** keep CL-001 stopped and preregister a replacement
  evaluator design using within-context matched retail strata so evaluator
  characteristics can vary without changing the institutional enforcement
  surface.
- **B:** preregister a typed frame that makes jurisdictional and institutional
  variation explicit, accepting that this changes the present experiment.
- **C:** preregister an analytic-panel evaluator design, explicitly retyping
  `i` and treating it as a measurement-bias test rather than a retail binding-
  constraint comparison.
- **D:** defer; the current CL-001 scaffold remains stopped.

This route is decision-ready evidence, not authority to choose or implement a
replacement.

## No Claim Promotion

This audit cannot promote a CL-001 packet, populate a packet field, score a
gate, change claim status, choose `SHARED_STRUCTURE`, `NARROWER_STRUCTURE`, or
`KILL`, or issue a legitimacy verdict. It records that the current experiment
lacks the fixed-`S0` identification needed to run its preregistered
discriminator.
