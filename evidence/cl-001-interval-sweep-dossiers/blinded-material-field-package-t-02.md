---
source_id: active-cl001-blinded-material-field-package-t-02-20260719
source_type: process package
applies_to_packets: active-cl001-dollar-arm-pending; active-cl001-bitcoin-arm-pending
evidence_lanes: Frame adherence and declared-field guard; Mechanism and transition boundary; Settlement regime and class definition; Constraint class and exit-cost interval; Absorber, near-miss null, and arm-symmetry pressure; Falsifiers, open fields, and routing
provenance: governance/CHARTER.md; experiments/CL-001-phi-frame.md; experiments/CL-001-interval-sweep.md; evidence/cl-001-interval-sweep-source-intake.md; evidence/cl-001-interval-sweep-dossier-manifest.md; evidence/cl-001-interval-sweep-dossiers/arm-symmetry-blinding-receipt.md; evidence/cl-001-interval-sweep-dossiers/blind-bundles/cl001-blind-t-01-inferability-preflight.md; evidence/cl-001-interval-sweep-dossiers/blind-bundles/cl001-blind-t-02-redacted-source-bundle.md; active mechanism dossiers inspected 2026-07-19
extracted_by: Codex child run RUN-20260719-549
extracted_on: 2026-07-19
status: draft
claim_status: none
verdict: none
---

# Blinded Material-Field Package T-02

## Source Boundary

This draft process package supersedes `CL001-BLIND-T-01` as the current
blind-facing source-bundle candidate for field `T`. `T` remains the selected
material field because the declared frame in
`experiments/CL-001-phi-frame.md` makes it the only free field across the
dollar and Bitcoin arms.

Package id: `CL001-BLIND-T-02`.

This file is the open-label package contract and receipt checklist, not the
blind author's read surface. The blind-author input is the revised redacted
coded bundle at
`evidence/cl-001-interval-sweep-dossiers/blind-bundles/cl001-blind-t-02-redacted-source-bundle.md`.
The bundle's current SHA-256 is
`FCBE5FAF69704459498A7B6D915479B7AEFE1FB5B705E7055970D2F7BF79F3F6`.

This package responds to the non-blind inferability stop recorded for
`CL001-BLIND-T-01`. It reduces direct arm-class cues while preserving enough
mechanism pressure for a later blind author to attempt extraction. It still
does not establish that the bundle is non-inferable or materially sufficient.

A blind run should receive only the task capsule and coded bundle text from the
revised bundle, not this open-label package. This package does not populate any
active CL-001 packet field, does not score any gate, does not issue a verdict,
and does not establish that blind population can succeed.

### Scoped Extraction

| Process-supported point | Packet field candidates | Evidence lane | Scope limit |
|---|---|---|---|
| `T` remains the first selected material field for blind handling. | `T`, `V` | Mechanism and transition boundary; Falsifiers, open fields, and routing | Selection only; no field value is populated. |
| `CL001-BLIND-T-02` revises the blind-facing source bundle after the T-01 preflight found likely inferability. | `V`, `Z` | Absorber, near-miss null, and arm-symmetry pressure | This is a non-blind packager repair, not a blind-author receipt. |
| The revised bundle removes direct arm labels, source names, URLs, and the unblinding key, and reduces the strongest distinctive phrasing from T-01. | `V` | Frame adherence and declared-field guard; Falsifiers, open fields, and routing | Reduced inferability is not proof of non-inferability. A blind author must still stop if the arm is identifiable. |
| The blind author must return `blind_failed_inferable` if the arm can be identified before extraction. | `V`, `Z` | Absorber, near-miss null, and arm-symmetry pressure | A failed blind is a valid process result, not permission for unblinded packet population. |
| Any blind output must keep all unsupported field-level claims as `Pending exact source selection.` | `T`, `V` | Falsifiers, open fields, and routing | The package cannot silently fill gaps left open by the source dossiers. |

### Typed Quantities

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
| `T` field selection | Process selection of the transduction/enforcement-mechanism field | Charter frame discipline and active scaffold. | Field value, source fact, gate score, verdict. |
| Blind bundle id | Opaque package identifier for the blind author | This process package. | Arm identity, source authority, evidence grade. |
| Source-bundle checksum | Integrity pointer for the exact blind-facing input text | `Get-FileHash` over the revised bundle. | Blind receipt, unblinding key, packet field. |
| Inferability status | Process-control result: `blind_ok`, `blind_failed_inferable`, or `blind_failed_insufficient_material` | Required by this package. | Mechanism truth, substrate merit, legitimacy. |
| Unblinding key | Mapping from coded bundle id to arm identity, held outside the blind author's read scope until after return | Required by this package. | Public evidence, packet field, source support. |

### Losses And Imports

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
| This run is not blind and therefore imports arm labels, repository context, and known source identities. | `V` | This run's source order and the active dossier set. | A later blind author must work from the revised redacted bundle and must not read these open-label dossiers in the same run. |
| Reducing distinctive vocabulary may remove material needed for a strong `T` candidate. | `T`, `V` | The T-01 preflight found the strongest cues were also mechanism-bearing. | If redaction removes the material basis for extraction, the blind result is `blind_failed_insufficient_material`, not a populated packet. |
| The revised bundle still contains generic mechanism cues that may identify an arm to a knowledgeable author. | `V`, `Z` | The revised bundle retains ordering evidence, status-review, threshold, and intermediary/process vocabulary. | The blind author must make inferability the first return condition. |
| The package cannot store the unblinding key in this public artifact before blind return. | `V` | Public-repository blinding boundary. | A later non-blind packager must preserve the key outside the blind author's read context and commit it only after blind return. |

### Agency And Feedback Burden

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
| Revised blind `T`-field extraction as a process surface. | Charter and source-intake contract require at least one material field to be populated blind. | No blind author has received the revised bundle or returned a result. | Ordinary review hygiene can absorb this unless the blind attempt catches arm-name or frame presumption. |
| Inferability failure as a method finding. | The T-01 preflight showed inferability is a live risk for this field. | T-02 has not been independently tested. | If the author can identify the arm, the package fails as a blind without moving packet fields. |
| Routing of process defects. | Charter rule 7 requires recognized defects to route out. | This package routes the T-01 preflight finding into a revised source-bundle candidate. | A later run that records inferability or frame pressure without routing it fails the method claim. |

### Blind Author Prompt Template

The later blind author should receive only the task capsule and coded bundle
text from
`evidence/cl-001-interval-sweep-dossiers/blind-bundles/cl001-blind-t-02-redacted-source-bundle.md`,
not this open-label package:

```text
You are populating field T for CL001-BLIND-T-02 from two coded source bundles,
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

- package id `CL001-BLIND-T-02`;
- selected field `T`;
- blind author or run id;
- redacted prompt/source-bundle checksum or commit reference;
- statement that the blind author did not read the founding corpus or
  open-label active dossiers in the same run;
- inferability status before extraction;
- returned field-`T` candidate language or a stop code;
- unblinding key and unblinding time, committed only after blind return; and
- explicit statement that no gate, claim status, or CL-001 verdict moved.

### What This Source Does Not Establish

This package does not populate any active CL-001 packet field. It does not score
any gate, issue a CL-001 verdict, accept a repo-owned claim, satisfy the
charter's blinded-field requirement, or prove that `T` can be populated blind.

It does not establish:

- a dollar or Bitcoin `T` value;
- that a blind author has completed extraction;
- that the revised source bundle is sufficiently non-inferable or materially
  sufficient for extraction;
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
- the source bundle includes arm labels, source names, unique institution
  names, URLs, or repo-local open-label dossier context;
- the redaction removes enough material that `T` cannot be extracted;
- the blind result requires `R0`, `M1`, `Omega`, or the settlement-boundary role
  to vary;
- a later run treats this package as a completed blind receipt; or
- this package is used as evidence that gate 10 has passed.

## No Claim Promotion

This source dossier cannot promote a CL-001 packet, gate, experiment verdict, or
repo-owned claim. It only selects the first material field for blind handling
after the T-01 inferability stop and records the package and receipt conditions
that must be met before `T` can move into an active packet.
