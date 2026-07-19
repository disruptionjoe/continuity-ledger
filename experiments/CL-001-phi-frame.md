---
artifact_type: experiment_frame_declaration
status: declared_pre_packet
experiment: CL-001
frame_id: CL-001-Phi-2026-07-19
claim_status: none
verdict: none
---

# CL-001 Phi Frame Declaration

Status: declared pre-packet frame. This file fixes the comparison frame for the
active CL-001 Interval Sweep. It is not a packet, source dossier, gate receipt,
preregistration, or verdict.

## Authority

- Charter source: `governance/CHARTER.md`, `Frame Discipline` and `CL-001: The
  Interval Sweep`.
- Active scaffold: `experiments/CL-001-interval-sweep.md`.
- This declaration is committed before any current dollar/Bitcoin CL-001 packet
  file, current source-intake contract, current source-dossier manifest, gate
  receipt, or verdict exists.
- The dollar/Bitcoin arms were selected by the 2026-07-16 charter amendment.
  This frame does not reselect cases; it records the pre-packet frame that later
  population must hold fixed.
- The retired Bitcoin/photosynthesis packet workspace under `packets/cl-001/`
  remains excluded from the active Interval Sweep.

## Frame Tuple

`Phi = (R0, K0, S0, M0, T, B)`.

| Field | Declaration | Guardrail |
|---|---|---|
| `R0` | A population's transactional expectations over a bounded retail settlement domain. | `R0` is declared, not source-extracted. Evaluator populations instantiate the same declared class; they do not redefine it. |
| `K0` | Participant-facing settlement-admissibility class: ordinary retail actors can price, settle, save, and contract only through recognized settlement rules. | This does not issue a legitimacy verdict or claim which rules are better. |
| `S0` | Retail settlement enforcement substrate as a role: the operational substrate through which settlement rules become binding for the selected arm. | No material claim about either arm's actual mechanism is populated here; the arm-specific mechanism is exposed only through `T`. |
| `M0` | Expected transactional entitlement, balance, or spendability representation before enforcement at the boundary. | Legal balances, UTXOs, prices, energy, and legitimacy remain unlike typed quantities. |
| `T` | Free field. Later dollar and Bitcoin packets may differ only in the enforcement mechanism/posture assigned to `T`. | `T` is the only free field. If packet population requires another field to vary, the run stops before scoring and records instrument failure. |
| `B` | Settlement-recognition boundary where non-compliant transfers are excluded from recognized continuation. | The boundary role is shared; concrete exclusion behavior belongs in the later arm-specific `T` population. |

## Fixed Downstream Test Fields

The charter also requires the active arms to share `M1` and `Omega`.

| Field | Declaration | Guardrail |
|---|---|---|
| `M1` | Unit-of-account capable settlement record supporting quoted price, saving, and contracting. | This is a shared measurement/accounting family, not a claim of identical denominations, equal market value, equal access, or legitimacy. |
| `Omega` | Price, save, and contract. | This names the action-space family only; it does not claim the evaluator populations have equal costs, preferences, constraints, or institutional standing. |

## Evaluator Sweep

Evaluator index `i` is swept only after packet population starts:

| Arm | Evaluator populations |
|---|---|
| Dollar | US retail and Argentine retail |
| Bitcoin | US retail and Salvadoran retail |

The evaluator populations are used to test whether the binding constraint class
moves with evaluator population at fixed substrate posture. They may not
redeclare `R0`, `M1`, `Omega`, or any field other than the measured evaluator
index.

## Population Rules

- No active packet field is populated by this frame.
- Later active packets must cite primary domain evidence for material claims.
- At least one material field must be populated blind before any verdict is
  issued.
- If a later packet cannot keep this frame fixed, the active run stops and the
  finding is recorded as instrument failure or routed to a new preregistration.

## No Claim Promotion

This frame declaration cannot populate a CL-001 packet, score a gate, accept a
repo-owned claim, issue a substrate verdict, issue a legitimacy verdict, or
choose between `SHARED_STRUCTURE`, `NARROWER_STRUCTURE`, and `KILL`.
