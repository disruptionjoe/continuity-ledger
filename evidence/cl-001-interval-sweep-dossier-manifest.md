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

No current active Interval Sweep dossier file exists yet.

## Current Dossier Queue

Every queued dossier starts as non-promotional. A dossier must preserve source
provenance, scoped extraction, typed quantities, losses/imports, agency and
feedback burden, open fields, falsifiers, and the no-claim-promotion boundary.

| Queue item | Applies to active evidence surface | Source type | Evidence lanes to preserve | Current status |
|---|---|---|---|---|
| Shared-frame audit dossier | Shared frame audit | construction/provenance | Frame adherence and declared-field guard; Falsifiers, open fields, and routing. | Pending exact source selection. |
| Dollar enforcement-mechanism dossier | Dollar enforcement mechanism | primary or institutionally authoritative | Mechanism and transition boundary; Settlement regime and class definition; Loss, import, and access accounting; Constraint class and exit-cost interval; Agency surface and action-space burden. | Pending exact source selection. |
| Bitcoin enforcement-mechanism dossier | Bitcoin enforcement mechanism | protocol-level and operational | Mechanism and transition boundary; Settlement regime and class definition; Loss, import, and access accounting; Constraint class and exit-cost interval; Agency surface and action-space burden. | Pending exact source selection. |
| Dollar US retail evaluator dossier | Dollar evaluator sweep | primary, statistical, or construction-supported | Evaluator sweep and population boundary; Constraint class and exit-cost interval; Typed measurement family. | Pending exact source selection. |
| Dollar Argentine retail evaluator dossier | Dollar evaluator sweep | primary, statistical, or construction-supported | Evaluator sweep and population boundary; Constraint class and exit-cost interval; Typed measurement family. | Pending exact source selection. |
| Bitcoin US retail evaluator dossier | Bitcoin evaluator sweep | primary, statistical, protocol-operational, or construction-supported | Evaluator sweep and population boundary; Constraint class and exit-cost interval; Typed measurement family. | Pending exact source selection. |
| Bitcoin Salvadoran retail evaluator dossier | Bitcoin evaluator sweep | primary, statistical, protocol-operational, or construction-supported | Evaluator sweep and population boundary; Constraint class and exit-cost interval; Typed measurement family. | Pending exact source selection. |
| Near-miss/control admission dossier | Near-miss/control admission | absorber/control or construction | Absorber, near-miss null, and arm-symmetry pressure; Settlement regime and class definition; Frame adherence and declared-field guard. | Pending exact source selection. |
| Arm-symmetry and blinding receipt dossier | Arm-symmetry and blinding receipts | process receipt | Absorber, near-miss null, and arm-symmetry pressure; Falsifiers, open fields, and routing. | Pending exact source selection. |

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

## Completion Boundary

This manifest is complete enough to begin exact source selection when a later
run is assigned to source work. It is not complete enough to populate a packet
field. Packet population remains blocked until the relevant dossier exists,
names its source provenance, and states which packet fields remain open.

## No Claim Promotion

This manifest cannot promote a CL-001 packet, gate, experiment verdict, or
repo-owned claim. It only records the active dossier queue for later exact
source work.
