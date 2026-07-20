---
artifact_type: evidence_dossier_manifest
status: active_interval_sweep_manifest
experiment: CL-001
frame_ref: experiments/CL-001-phi-frame.md
claim_status: none
verdict: none
---

# CL-001 Interval Sweep Dossier Manifest

## Purpose

This manifest binds the active CL-001 Interval Sweep source-intake contract to
the dossier queue needed before current dollar/Bitcoin packet fields can be
populated. It is not evidence, does not select exact sources, does not score any
gate, and does not issue a verdict.

Active intake contract:
`evidence/cl-001-interval-sweep-source-intake.md`.

Declared frame: `experiments/CL-001-phi-frame.md`.

Current active Interval Sweep dossier files are listed below.

## Current Dossier Queue

Every queued dossier starts as non-promotional. A dossier must preserve source
provenance, scoped extraction, typed quantities, losses/imports, agency and
feedback burden, open fields, falsifiers, and the no-claim-promotion boundary.

| Queue item | Applies to active evidence surface | Source type | Evidence lanes to preserve | Current status |
|---|---|---|---|---|
| Shared-frame audit dossier | Shared frame audit | construction/provenance | Frame adherence and declared-field guard; Falsifiers, open fields, and routing. | Draft dossier: `evidence/cl-001-interval-sweep-dossiers/shared-frame-audit-provenance.md`. |
| Dollar enforcement-mechanism dossier | Dollar enforcement mechanism | primary or institutionally authoritative | Mechanism and transition boundary; Settlement regime and class definition; Loss, import, and access accounting; Constraint class and exit-cost interval; Agency surface and action-space burden. | Draft dossier: `evidence/cl-001-interval-sweep-dossiers/dollar-enforcement-mechanism-legal-operational.md`. |
| Bitcoin enforcement-mechanism dossier | Bitcoin enforcement mechanism | protocol-level and operational | Mechanism and transition boundary; Settlement regime and class definition; Loss, import, and access accounting; Constraint class and exit-cost interval; Agency surface and action-space burden. | Draft dossier: `evidence/cl-001-interval-sweep-dossiers/bitcoin-enforcement-mechanism-protocol.md`. |
| Dollar US retail evaluator dossier | Dollar evaluator sweep | primary, statistical, or construction-supported | Evaluator sweep and population boundary; Constraint class and exit-cost interval; Typed measurement family. | Draft dossier: `evidence/cl-001-interval-sweep-dossiers/dollar-evaluator-sweep-us-argentina-retail.md`. |
| Dollar Argentine retail evaluator dossier | Dollar evaluator sweep | primary, statistical, or construction-supported | Evaluator sweep and population boundary; Constraint class and exit-cost interval; Typed measurement family. | Draft dossier: `evidence/cl-001-interval-sweep-dossiers/dollar-evaluator-sweep-us-argentina-retail.md`. |
| Bitcoin US retail evaluator dossier | Bitcoin evaluator sweep | primary, statistical, protocol-operational, or construction-supported | Evaluator sweep and population boundary; Constraint class and exit-cost interval; Typed measurement family. | Draft dossier: `evidence/cl-001-interval-sweep-dossiers/bitcoin-evaluator-sweep-us-salvador-retail.md`. |
| Bitcoin Salvadoran retail evaluator dossier | Bitcoin evaluator sweep | primary, statistical, protocol-operational, or construction-supported | Evaluator sweep and population boundary; Constraint class and exit-cost interval; Typed measurement family. | Draft dossier: `evidence/cl-001-interval-sweep-dossiers/bitcoin-evaluator-sweep-us-salvador-retail.md`. |
| Near-miss/control admission dossier | Near-miss/control admission | absorber/control or construction | Absorber, near-miss null, and arm-symmetry pressure; Settlement regime and class definition; Frame adherence and declared-field guard. | Draft dossier: `evidence/cl-001-interval-sweep-dossiers/near-miss-control-admission.md`. |
| Arm-symmetry and blinding receipt dossier | Arm-symmetry and blinding receipts | process receipt | Absorber, near-miss null, and arm-symmetry pressure; Falsifiers, open fields, and routing. | Draft dossier: `evidence/cl-001-interval-sweep-dossiers/arm-symmetry-blinding-receipt.md`. |
| Blinded material-field package | First active material-field selection | process package and coded input | Mechanism and transition boundary; Frame adherence and declared-field guard; Falsifiers, open fields, and routing. | Draft package: `evidence/cl-001-interval-sweep-dossiers/blinded-material-field-package-t-01.md`; prepared redacted source bundle: `evidence/cl-001-interval-sweep-dossiers/blind-bundles/cl001-blind-t-01-redacted-source-bundle.md`. |
| Blind bundle inferability preflight | Prepared `CL001-BLIND-T-01` coded input | process-control stop record | Absorber, near-miss null, and arm-symmetry pressure; Falsifiers, open fields, and routing. | Stop record: `evidence/cl-001-interval-sweep-dossiers/blind-bundles/cl001-blind-t-01-inferability-preflight.md`. |
| Revised blinded material-field package | Revised first material-field selection after inferability stop | process package and coded input | Mechanism and transition boundary; Frame adherence and declared-field guard; Falsifiers, open fields, and routing. | Draft package: `evidence/cl-001-interval-sweep-dossiers/blinded-material-field-package-t-02.md`; revised redacted source bundle: `evidence/cl-001-interval-sweep-dossiers/blind-bundles/cl001-blind-t-02-redacted-source-bundle.md`. |

## Symmetry Checks

- Dollar and Bitcoin source burdens must be strong enough to support the same
  declared frame before any active packet field is populated.
- Evaluator dossiers may vary population evidence, but they may not vary `R0`,
  `M1`, `Omega`, or the settlement-boundary role.
- A near-miss/control dossier must be positively specified and frame-matched; it
  cannot be selected by stipulating absence of the target surface.
- Source dossiers must leave fields open when source support is absent,
  secondary-only, or outside this repository's ownership.
- Arm-symmetry receipts must preserve label-swap, no-merit-ordering, blinding,
  and no same-run founding-corpus contamination burdens before any verdict.

## Active Dossier Files

| Dossier | Queue item | Status | Boundary |
|---|---|---|---|
| `evidence/cl-001-interval-sweep-dossiers/shared-frame-audit-provenance.md` | Shared-frame audit dossier | Draft construction/provenance dossier. | Does not populate active packet fields, score frame adherence, or establish that the frame will survive later source population. |
| `evidence/cl-001-interval-sweep-dossiers/dollar-enforcement-mechanism-legal-operational.md` | Dollar enforcement-mechanism dossier | Draft exact source dossier. | Does not populate active dollar packet fields or establish the dollar arm's candidate posture. |
| `evidence/cl-001-interval-sweep-dossiers/bitcoin-enforcement-mechanism-protocol.md` | Bitcoin enforcement-mechanism dossier | Draft exact source dossier. | Does not populate active Bitcoin packet fields or establish the Bitcoin arm's candidate posture. |
| `evidence/cl-001-interval-sweep-dossiers/dollar-evaluator-sweep-us-argentina-retail.md` | Dollar US and Argentine retail evaluator dossiers | Draft evaluator source dossier. | Does not populate active dollar packet fields or establish fixed-`S0` evaluator movement. |
| `evidence/cl-001-interval-sweep-dossiers/bitcoin-evaluator-sweep-us-salvador-retail.md` | Bitcoin US and Salvadoran retail evaluator dossiers | Draft evaluator source dossier. | Does not populate active Bitcoin packet fields or establish fixed-`S0` evaluator movement. |
| `evidence/cl-001-interval-sweep-dossiers/near-miss-control-admission.md` | Near-miss/control admission dossier | Draft control-admission construction dossier. | Does not admit a control, populate active packet fields, score absorber pressure, or establish that any control shares the frame. |
| `evidence/cl-001-interval-sweep-dossiers/arm-symmetry-blinding-receipt.md` | Arm-symmetry and blinding receipt dossier | Draft process receipt dossier. | Records that blinding remains unsatisfied; it does not satisfy the blinded-field requirement, score gate 10, or issue a verdict. |
| `evidence/cl-001-interval-sweep-dossiers/blinded-material-field-package-t-01.md` | Blinded material-field package | Draft process package selecting `T` as the first blind-handled material field. | Does not populate `T`, contain the blind author's read surface, complete a blind receipt, score gate 10, or issue a verdict. |
| `evidence/cl-001-interval-sweep-dossiers/blind-bundles/cl001-blind-t-01-redacted-source-bundle.md` | Blinded material-field package | Prepared redacted coded source bundle for a later blind author. | Contains no unblinding key, does not populate `T`, does not complete a blind receipt, does not score gate 10, and does not issue a verdict. |
| `evidence/cl-001-interval-sweep-dossiers/blind-bundles/cl001-blind-t-01-inferability-preflight.md` | Blind bundle inferability preflight | Stop record for the prepared coded bundle. | Records that the current bundle is likely inferable before extraction; it is not a blind-author receipt and does not populate `T`. |
| `evidence/cl-001-interval-sweep-dossiers/blinded-material-field-package-t-02.md` | Revised blinded material-field package | Draft process package selecting `T` after the T-01 inferability stop and pointing to the revised coded bundle. | Does not populate `T`, complete a blind receipt, score gate 10, or issue a verdict. |
| `evidence/cl-001-interval-sweep-dossiers/blind-bundles/cl001-blind-t-02-redacted-source-bundle.md` | Revised blinded material-field package | Revised redacted coded source bundle for a later blind author. | Contains no unblinding key, does not populate `T`, does not complete a blind receipt, does not score gate 10, and does not issue a verdict. |

## Completion Boundary

This manifest now has a shared-frame audit dossier, first exact source dossiers
for the dollar and Bitcoin enforcement-mechanism surfaces, evaluator-population
source dossiers for the dollar and Bitcoin arms, a near-miss/control admission
dossier, an arm-symmetry/blinding process dossier, a draft package selecting
`T` as the first blind-handled material field, the T-01 prepared redacted coded
source bundle, a non-blind inferability preflight for that bundle, and a T-02
revised redacted coded source bundle with a new checksum. It is not complete
enough to populate a packet field. Packet population remains blocked until a
later packet-population run obtains a valid blind author receipt or records a
blind-author stop on the revised bundle, preserves the declared frame, records
the unblinding event outside the blind author's read scope, and keeps any
remaining field-level source need visible as `Pending exact source selection.`
rather than silently filling it.

## No Claim Promotion

This manifest cannot promote a CL-001 packet, gate, experiment verdict, or
repo-owned claim. It only records the active dossier queue for later exact
source work.
