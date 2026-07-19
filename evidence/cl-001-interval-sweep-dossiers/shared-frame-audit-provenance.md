---
source_id: active-cl001-shared-frame-audit-20260719
source_type: construction/provenance
applies_to_packets: active-cl001-dollar-arm-pending; active-cl001-bitcoin-arm-pending
evidence_lanes: Frame adherence and declared-field guard; Falsifiers, open fields, and routing
provenance: governance/CHARTER.md; experiments/CL-001-phi-frame.md; experiments/CL-001-interval-sweep.md; evidence/cl-001-interval-sweep-source-intake.md; evidence/cl-001-interval-sweep-dossier-manifest.md; evidence/cl-001-interval-sweep-dossiers/dollar-enforcement-mechanism-legal-operational.md; evidence/cl-001-interval-sweep-dossiers/bitcoin-enforcement-mechanism-protocol.md; inspected 2026-07-19
extracted_by: Codex child run RUN-20260719-536
extracted_on: 2026-07-19
status: draft
claim_status: none
verdict: none
---

# Shared Frame Audit Provenance Dossier

## Source Boundary

This draft dossier covers the active CL-001 shared-frame audit queue item. It is
a construction and provenance audit over the repo-local frame declaration,
active Interval Sweep scaffold, active source-intake contract, active dossier
manifest, and current dollar/Bitcoin enforcement-mechanism draft dossiers.

Declared frame reference: `experiments/CL-001-phi-frame.md`.

Repo-local surfaces used:

- `governance/CHARTER.md`, especially `Frame Discipline` and `CL-001: The
  Interval Sweep`.
- `experiments/CL-001-phi-frame.md`.
- `experiments/CL-001-interval-sweep.md`.
- `evidence/cl-001-interval-sweep-source-intake.md`.
- `evidence/cl-001-interval-sweep-dossier-manifest.md`.
- `evidence/cl-001-interval-sweep-dossiers/dollar-enforcement-mechanism-legal-operational.md`.
- `evidence/cl-001-interval-sweep-dossiers/bitcoin-enforcement-mechanism-protocol.md`.

These are repo-local authority and construction surfaces, not external domain
sources. This dossier does not populate any packet field, does not select exact
domain sources, does not score any gate, and does not establish that either arm
can be populated later.

### Scoped Extraction

| Construction-supported point | Packet field candidates | Evidence lane | Scope limit |
|---|---|---|---|
| `experiments/CL-001-phi-frame.md` declares `Phi = (R0, K0, S0, M0, T, B)` before any active dollar/Bitcoin packet exists. | `R0`, `K0`, `S0`, `M0`, `T`, `B`, `V` | Frame adherence and declared-field guard | This confirms a declared frame surface exists; it does not prove the frame is adequate. |
| The frame declaration fixes `R0` as a population's transactional expectations over a bounded retail settlement domain, fixes the settlement-boundary role, and leaves `T` as the only free field. | `R0`, `T`, `B`, `V` | Frame adherence and declared-field guard | The declaration is construction authority, not source extraction from dollar or Bitcoin domain evidence. |
| The frame declaration fixes downstream `M1` as unit-of-account capable settlement record and `Omega` as price, save, and contract. | `M1`, `Omega`, `V` | Frame adherence and declared-field guard | This does not claim equal denominations, equal access, equal cost, equal preference, or legitimacy. |
| The active source-intake contract repeats that `R0`, `M1`, and `Omega` are shared declared fields and that evaluator index `i` may not re-declare them. | `R0`, `M1`, `Omega`, `V` | Frame adherence and declared-field guard; Falsifiers, open fields, and routing | The contract can preserve the burden only if later dossiers honor it. |
| The active dollar and Bitcoin enforcement-mechanism dossiers both cite `experiments/CL-001-phi-frame.md` as their declared frame reference. | `T`, `B`, `V` | Frame adherence and declared-field guard | Citation of the frame is not enough to populate the arms; later review must test whether each source pass actually preserves it. |
| The active dossier manifest still blocks packet population until all relevant dossier lanes exist, name provenance, preserve the declared frame, and state open packet fields. | `V` | Falsifiers, open fields, and routing | This preserves the stop condition; it is not a gate receipt or verdict. |

### Typed Quantities

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
| `R0` declaration | Declared regime-boundary class | Frame declaration and intake contract. | Legal-tender status, UTXO state, chainwork, legitimacy, current retail adoption. |
| `T` | Free-field enforcement mechanism or posture | Frame declaration. | `R0`, evaluator index, measured exit cost, legitimacy. |
| `B` | Settlement-recognition boundary role | Frame declaration. | Concrete dollar procedure, concrete Bitcoin validation rule, market preference. |
| `M1` | Shared measurement/accounting family | Frame declaration and intake contract. | Dollars as denomination, satoshis, chainwork, energy, legal right. |
| `Omega` | Declared action-space family | Frame declaration. | Actual ability, cost, preference, legitimacy, success rate. |
| Evaluator index `i` | Sweep coordinate over named retail populations | Frame declaration and active scaffold. | Substrate posture, mechanism `T`, gate verdict, claim status. |

### Losses And Imports

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
| The active frame imports a declared `R0`; it is not autonomously individuated from domain sources. | `R0`, `V` | Charter frame-discipline rule and frame declaration. | Later packet work must preserve this as construction provenance rather than presenting `R0` as extracted. |
| The active frame imports a shared boundary role and action-space family before source population. | `B`, `Omega`, `V` | Frame declaration. | Later source dossiers must show whether arm-specific evidence can live inside the role without re-declaring it. |
| Current enforcement-mechanism dossiers leave evaluator-population exit-cost intervals open. | `L`, `N`, `V` | Existing dollar and Bitcoin enforcement-mechanism draft dossiers. | Dollar US/Argentine and Bitcoin US/Salvadoran evaluator dossiers remain required. |
| Current enforcement-mechanism dossiers do not satisfy control, arm-symmetry, or blinding burdens. | `Z`, `V` | Active dossier manifest and source-intake contract. | Near-miss/control admission and arm-symmetry/blinding receipt dossiers remain required. |
| This construction pass did not inspect the frozen founding corpus and issues no verdict. | `V` | Run scope and this dossier boundary. | A later verdict still needs its own no same-run corpus-contamination receipt. |

### Agency And Feedback Burden

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
| Frame-preserving packet population as a process surface. | Repo-local frame declaration, intake contract, and manifest. | Does not show any generated or recruited agent class; it only records a process guard. | Ordinary preregistration discipline can absorb this without CLTP agency generation. |
| Recognition of frame pressure as a routing burden. | Charter frame-discipline rule 7 and active intake falsifier lane. | No frame defect is found here, and no escalation is triggered. | A later run can still fail by recording a defect without routing it. |
| Common-frame audit over current dollar and Bitcoin mechanism dossiers. | Both active draft dossiers cite the declared frame and preserve non-promotion language. | Does not prove that either arm's material evidence preserves the frame when packet fields are populated. | The audit can be absorbed as document hygiene unless later packet work uses it to stop or preserve a real frame defect. |

### What This Source Does Not Establish

This dossier does not populate any active CL-001 packet field. It does not score
any gate, issue a CL-001 verdict, accept a repo-owned claim, or establish that
the active dollar/Bitcoin frame will survive later source population.

It does not establish:

- that the declared `Phi` frame is adequate or non-artifactual;
- that dollar and Bitcoin enforcement-mechanism evidence can be scored inside
  the same frame;
- evaluator-population exit-cost intervals for US, Argentine, or Salvadoran
  retail contexts;
- near-miss or control admissibility;
- arm-symmetry, label-swap, no-merit-ordering, or blinding completion;
- a legitimacy verdict about any substrate; or
- a class-relative no-go, agency-generation result, or constructive escape
  witness.

### Falsifiers And Reopen Conditions

Reopen or supersede this dossier if:

- later packet population needs any field other than `T` to vary between the
  dollar and Bitcoin arms;
- a later source dossier treats `R0`, `M1`, `Omega`, or the boundary role as
  source-extracted rather than declared;
- evaluator evidence requires a population-specific frame rather than an index
  sweep at fixed substrate posture;
- a control cannot be specified at the same declared `R0` and `M1`;
- a later run reads the founding corpus before issuing a verdict without
  recording that contamination burden; or
- this dossier is used as evidence that the frame passes a CL-001 gate.

## No Claim Promotion

This source dossier cannot promote a CL-001 packet, gate, experiment verdict, or
repo-owned claim. It only records construction/provenance work for later review.
