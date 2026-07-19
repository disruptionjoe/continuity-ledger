---
artifact_type: experiment_scaffold
status: active_scaffold
experiment: CL-001
claim_status: none
verdict: none
---

# CL-001: Interval Sweep

Status: active scaffold. This is not a preregistration, packet, gate receipt, or
verdict.

## Charter Source

The active CL-001 experiment is the Interval Sweep defined in
`governance/CHARTER.md`. It replaces the retired Bitcoin proof-of-work /
oxygenic photosynthesis pair, which is preserved at
`experiments/CL-001-bitcoin-photosynthesis-pair-and-null.md` and
`hypotheses/HORIZON.md`.

## Objective

Test whether, at one declared frame, the binding constraint class follows the
enforcement substrate rather than the evaluator population.

## Declared Frame

Frame `Phi` is declared in `experiments/CL-001-phi-frame.md`. It fixes the
shared comparison frame for the active dollar/Bitcoin Interval Sweep and leaves
`T` as the only free field before any current arm packet is populated.

## Required Frame Discipline

- Declare and commit frame `Phi` before any arm is populated.
- Hold `R0`, `M1`, and `Omega` fixed across arms.
- Leave `T` as the only free field across the dollar and Bitcoin arms.
- If the frame is wrong, stop and preregister a new run rather than repairing
  the frame after an outcome is visible.
- Populate at least one material field blind when field population begins.

## Arms And Sweep

| Arm | Substrate posture | Evaluator populations |
|---|---|---|
| Dollar | discretionary exclusion, appealable | US retail and Argentine retail |
| Bitcoin | rule-constant exclusion, unappealable | US retail and Salvadoran retail |

No field in this scaffold establishes those postures as source-supported packet
claims. Packet population requires later source dossiers and gate receipts.

## Preregistered Outcomes

The charter permits no third branch:

- `KILL`: the binding constraint class varies with evaluator population at
  fixed `S0`.
- `SHARED_STRUCTURE` or `NARROWER_STRUCTURE`: the binding constraint class is
  invariant across evaluator populations and varies with `S0` at fixed
  evaluator index.

Any non-preregistered result is `KILL` on instrument failure.

## Current Missing Work

- Current packet files for the dollar and Bitcoin arms.
- Packet-field selection from the active draft dossier set under
  `evidence/cl-001-interval-sweep-dossier-manifest.md`.
- Exact field-level source completion wherever the draft dossiers leave a
  material field open.
- A valid blinded material-field package and receipt before any unblinded
  population of that field.
- Final near-miss/control admission at the same declared `R0` and `M1` before
  absorber scoring.
- Arm-symmetry receipts before any verdict.

## No Claim Promotion

This scaffold cannot populate a CL-001 packet, score any gate, accept a
repo-owned claim, or issue a CL-001 verdict.
