---
source_id: active-cl001-blinded-material-field-package-t-01-20260719
source_type: process package
applies_to_packets: active-cl001-dollar-arm-pending; active-cl001-bitcoin-arm-pending
evidence_lanes: Frame adherence and declared-field guard; Mechanism and transition boundary; Settlement regime and class definition; Constraint class and exit-cost interval; Absorber, near-miss null, and arm-symmetry pressure; Falsifiers, open fields, and routing
provenance: governance/CHARTER.md; experiments/CL-001-phi-frame.md; experiments/CL-001-interval-sweep.md; evidence/cl-001-interval-sweep-source-intake.md; evidence/cl-001-interval-sweep-dossier-manifest.md; evidence/cl-001-interval-sweep-dossiers/arm-symmetry-blinding-receipt.md; active mechanism and evaluator dossiers inspected 2026-07-19
extracted_by: Codex child run RUN-20260719-545
extracted_on: 2026-07-19
status: draft
claim_status: none
verdict: none
---

# Blinded Material-Field Package T-01

## Source Boundary

This draft process package selects `T` as the first active CL-001 material field
eligible for blind handling. `T` is selected because the declared frame in
`experiments/CL-001-phi-frame.md` makes it the only free field across the dollar
and Bitcoin arms, and the active experiment scaffold identifies the first packet
population burden as a field-level selection through a valid blinded package.

Package id: `CL001-BLIND-T-01`.

This file is the public package contract and receipt checklist. It is not the
blind author's source bundle, because putting the unblinding key or unreduced
arm-specific source names in the repository would make the package non-blind.
It does not populate any active CL-001 packet field, does not score any gate,
does not issue a verdict, and does not establish that blind population can
succeed.

Repo-local surfaces used:

- `governance/CHARTER.md`, especially Frame Discipline rule 6, Frame Discipline
  rule 7, and Neutrality gate arm-symmetry exposure.
- `experiments/CL-001-phi-frame.md`.
- `experiments/CL-001-interval-sweep.md`.
- `evidence/cl-001-interval-sweep-source-intake.md`.
- `evidence/cl-001-interval-sweep-dossier-manifest.md`.
- `evidence/cl-001-interval-sweep-dossiers/arm-symmetry-blinding-receipt.md`.
- Current active dollar and Bitcoin mechanism and evaluator dossiers.

### Scoped Extraction

| Process-supported point | Packet field candidates | Evidence lane | Scope limit |
|---|---|---|---|
| `T` is the first selected material field for blind handling. | `T`, `V` | Mechanism and transition boundary; Falsifiers, open fields, and routing | Selection only; no field value is populated. |
| The blind task must ask for an enforcement-mechanism or enforcement-posture description while preserving the declared frame. | `T`, `B`, `V` | Frame adherence and declared-field guard; Mechanism and transition boundary | If the blind author needs `R0`, `M1`, `Omega`, or boundary role to vary, the result is a stop record. |
| The blind source bundle must expose two coded bundles without dollar/Bitcoin arm labels, source names, unique institution names, or source URLs. | `V` | Absorber, near-miss null, and arm-symmetry pressure; Falsifiers, open fields, and routing | This public file does not contain that bundle or the unblinding key. |
| The blind author must return `blind_failed_inferable` if the arm can be identified before extraction. | `V`, `Z` | Absorber, near-miss null, and arm-symmetry pressure | A failed blind is a valid process result, not permission for unblinded packet population. |
| Any blind output must keep all unsupported field-level claims as `Pending exact source selection.` | `T`, `V` | Falsifiers, open fields, and routing | The package cannot silently fill gaps left open by the source dossiers. |

### Typed Quantities

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
| `T` field selection | Process selection of the transduction/enforcement-mechanism field | Charter frame discipline and active scaffold. | Field value, source fact, gate score, verdict. |
| Blind bundle id | Opaque package identifier for the blind author | This process package. | Arm identity, source authority, evidence grade. |
| Inferability status | Process-control result: `blind_ok`, `blind_failed_inferable`, or `blind_failed_insufficient_material` | Required by this package. | Mechanism truth, substrate merit, legitimacy. |
| Unblinding key | Mapping from coded bundle id to arm identity, held outside the blind author's read scope until after return | Required by this package. | Public evidence, packet field, source support. |
| Checksum or commit reference | Integrity pointer for the exact prompt and source bundle supplied | Required by this package. | Gate score, claim status, source grade. |

### Losses And Imports

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
| This run is not blind and therefore imports arm labels, repository context, and known source identities. | `V` | This run's source order and the active dossier set. | A later blind author must work from a redacted bundle and must not read these open-label dossiers in the same run. |
| A valid blind package imports a non-blind packager, a redacted prompt, a coded source bundle, an unblinding key, and a return receipt. | `V` | Charter rule 6 and active source-intake contract. | The later receipt must name the blind author/run, source-bundle checksum, inferred-arm status, and unblinding event. |
| Selecting `T` imports high inferability risk because the current source sets contain unique legal, institutional, protocol, and implementation vocabulary. | `T`, `V`, `Z` | Active mechanism and evaluator dossiers. | The blind bundle must either reduce arm-inferable terms or return `blind_failed_inferable`. |
| A redacted source bundle may lose domain detail needed for a real field value. | `T`, `V` | This package contract. | If redaction removes the material basis for extraction, the blind result is `blind_failed_insufficient_material`, not a populated packet. |
| The package cannot store the unblinding key in this public artifact before blind return. | `V` | Public-repository blinding boundary. | Parent orchestration or a later non-blind packager must preserve the key outside the blind author's read context and commit it only after blind return. |

### Agency And Feedback Burden

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
| Blind `T`-field extraction as a process surface. | Charter and source-intake contract require at least one material field to be populated blind. | No blind author has received a redacted bundle or returned a result. | Ordinary review hygiene can absorb this unless the blind attempt catches arm-name or frame presumption. |
| Inferability failure as a method finding. | The active arm sources are distinctive enough that inferability is a live risk. | No blind run has tested inferability. | If the author can identify the arm, the package fails as a blind without moving packet fields. |
| Routing of frame pressure. | Charter rule 7 requires recognized defects to route out. | No frame defect is found by this package; the route is defined for the later blind result. | A later run that records inferability or frame pressure without routing it fails the method claim. |

### Blind Author Prompt Template

The later blind author should receive only this task capsule plus a coded source
bundle prepared outside the blind author's read context:

```text
You are populating field T for CL001-BLIND-T-01 from two coded source bundles,
Bundle X and Bundle Y. Do not read the continuity-ledger repository, founding
corpus, manifest, or open-label dossiers in this run. If you can identify an
arm before extraction, return blind_failed_inferable and stop.

For each bundle, answer:
1. What enforcement mechanism or posture is supported by the supplied material?
2. Which parts of that answer are directly supported by the material?
3. Which parts remain Pending exact source selection?
4. Did you need R0, M1, Omega, or the settlement-boundary role to vary?
5. What ordinary absorber could explain the same material without CLTP?

Do not compare bundles, score gates, rank mechanisms, issue a verdict, or infer
legitimacy. Return only field-T candidate language, open burdens, and the
inferability status.
```

### Receipt Requirements

A later receipt can satisfy this package only if it records:

- package id `CL001-BLIND-T-01`;
- selected field `T`;
- blind author or run id;
- redacted prompt/source-bundle checksum or commit reference;
- statement that the blind author did not read the founding corpus or open-label
  active dossiers in the same run;
- inferability status before extraction;
- returned field-T candidate language or a stop code;
- unblinding key and unblinding time, committed only after blind return; and
- explicit statement that no gate, claim status, or CL-001 verdict moved.

### What This Source Does Not Establish

This package does not populate any active CL-001 packet field. It does not score
any gate, issue a CL-001 verdict, accept a repo-owned claim, satisfy the
charter's blinded-field requirement, or prove that `T` can be populated blind.

It does not establish:

- a dollar or Bitcoin `T` value;
- that a blind source bundle has been created;
- that a blind author has completed extraction;
- that the arm identity can be hidden from a blind author;
- that the current source dossiers are sufficient for packet population;
- label-swap invariance, no merit ordering, or no same-run founding-corpus
  contamination for a later verdict; or
- a legitimacy verdict about either arm.

### Falsifiers And Reopen Conditions

Reopen or supersede this package if:

- a later packet population run uses any field other than `T` as the first blind
  material field without recording why `T` became invalid;
- the blind author can infer dollar or Bitcoin identity from the coded bundle
  before extraction;
- the source bundle includes arm labels, source names, unique institution names,
  URLs, or repo-local open-label dossier context;
- the redaction removes enough material that `T` cannot be extracted;
- the blind result requires `R0`, `M1`, `Omega`, or the settlement-boundary role
  to vary;
- a later run treats this package as a completed blind receipt; or
- this package is used as evidence that gate 10 has passed.

## No Claim Promotion

This source dossier cannot promote a CL-001 packet, gate, experiment verdict, or
repo-owned claim. It only selects the first material field for blind handling
and records the package and receipt conditions that must be met before `T` can
move into an active packet.
