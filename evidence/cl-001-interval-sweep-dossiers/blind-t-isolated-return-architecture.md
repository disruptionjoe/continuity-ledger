---
source_id: active-cl001-blind-t-isolated-return-architecture-20260719
source_type: process-control architecture
applies_to_packets: active-cl001-dollar-arm-pending; active-cl001-bitcoin-arm-pending
evidence_lanes: Frame adherence and declared-field guard; Mechanism and transition boundary; Absorber, near-miss null, and arm-symmetry pressure; Falsifiers, open fields, and routing
provenance: governance/CHARTER.md; experiments/CL-001-phi-frame.md; evidence/cl-001-interval-sweep-source-intake.md; evidence/cl-001-interval-sweep-dossier-manifest.md; evidence/cl-001-interval-sweep-dossiers/blind-t-public-packaging-method-stop.md
extracted_by: Codex child run RUN-20260719-557-repository-work-cycle-cai-hourly
extracted_on: 2026-07-19
status: draft
claim_status: none
verdict: none
---

# Blind T Isolated Return Architecture

## Source Boundary

This draft process-control architecture covers the next admissible CL-001 field
`T` blinding path after the public non-blind packaging method stop.

Declared frame reference: `experiments/CL-001-phi-frame.md`.

This architecture supersedes the stopped public-package path only at the method
level. It does not create a new public redacted bundle, does not populate any
active CL-001 packet field, does not score any gate, does not complete a blind
author receipt, and does not issue a verdict. It exists to make the next
blind-return attempt separable from the public repository exposure that made
T-01 and T-02 likely inferable.

The public record may contain the protocol, stop codes, and required receipt
shape. The blind read capsule, any unblinding key, and any arm mapping stay out
of committed public files until after the blind author returns. A later run may
use a local ignored handoff surface such as `_local/blind-handoffs/<handoff_id>/`
or an equivalent private handoff, but the public repository may not expose that
read surface before return.

### Scoped Extraction

| Process-supported point | Packet field candidates | Evidence lane | Scope limit |
|---|---|---|---|
| The current public non-blind path is stopped because field-`T` mechanism cues also function as arm-class cues. | `V`, `Z` | Mechanism and transition boundary; Falsifiers, open fields, and routing | Restates the process stop; it does not establish a universal impossibility of blind `T` population. |
| A changed architecture must separate the public committed protocol from the blind author's read surface. | `V` | Frame adherence and declared-field guard; Absorber, near-miss null, and arm-symmetry pressure | The read capsule itself is not created here. |
| The blind author must receive only the task capsule, coded source excerpts, stop-code definitions, and field-`T` extraction target. | `T`, `V` | Mechanism and transition boundary; Falsifiers, open fields, and routing | No repository-wide read, open-label manifest read, founding-corpus read, source URL read, or unblinding key is licensed. |
| The first return condition is inferability before extraction. | `V`, `Z` | Absorber, near-miss null, and arm-symmetry pressure; Falsifiers, open fields, and routing | `blind_failed_inferable` is a valid method result and does not authorize unblinded packet population. |
| The second return condition is material insufficiency. | `T`, `V`, `Z` | Mechanism and transition boundary | `blind_failed_insufficient_material` is a valid method result and preserves the packet field as unpopulated. |
| Only if neither stop condition fires may the blind author return candidate field-`T` language. | `T`, `V` | Mechanism and transition boundary; Frame adherence and declared-field guard | Candidate language remains pre-unblinding material; later open-label review must still check provenance, typed fit, and symmetry before packet population. |

### Typed Quantities

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
| Handoff architecture | Process boundary separating public protocol from private or ignored read capsule. | This architecture and the public packaging method stop. | Blind author receipt, packet field, gate score, verdict. |
| Blind read capsule | Bounded source-excerpt set given to a blind author outside the committed public record before return. | Charter rule 6 and prior T-01/T-02 inferability stops. | Public dossier, unblinding key, source authority. |
| Stop code | Process return classification: `blind_failed_inferable`, `blind_failed_insufficient_material`, or `candidate_t_returned`. | This architecture. | CL-001 outcome, claim status, field value. |
| Unblinding key | Mapping between coded inputs and arm identity, held outside the blind author's read scope until after return. | Prior field-`T` package records. | Evidence grade, source truth, legitimacy verdict. |
| Candidate `T` language | Blind-authored pre-review mechanism description. | A later blind return only. | Accepted packet value, gate pass, source claim. |

### Losses And Imports

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
| This architecture imports the finding that public redaction failed twice before blind return. | `V`, `Z` | T-01/T-02 inferability preflights and the public packaging method stop. | A later handoff must avoid committing the read capsule before return. |
| A private or ignored read capsule loses public review before return. | `V` | Public-path method stop. | The post-return receipt must preserve checksum, source capsule identity, author/run identity, and unblinding time. |
| A blind author imports limited source support only from the capsule. | `T`, `V` | Charter Frame Discipline rule 6. | If the capsule lacks enough mechanism support, the author must return `blind_failed_insufficient_material`. |
| A blind author who can infer the arm imports arm-class knowledge before extraction. | `V`, `Z` | T-01/T-02 cue findings. | The author must return `blind_failed_inferable` before extracting candidate `T` language. |
| Post-return open-label review imports repository context again. | `T`, `V`, `Z` | Active dossier queue and source-intake contract. | Review may reject, narrow, or leave pending the candidate language; it may not retroactively make the blind return stronger than it was. |

### Agency And Feedback Burden

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
| Isolated blind return as a process surface for field `T`. | Charter rule 6 and the method stop's reopen conditions. | No blind author has received an isolated capsule or returned a receipt. | Ordinary open-label review absorbs the surface unless inferability is tested first. |
| Stop-code-first return as routing feedback. | Charter rule 7 and the repeated public packaging defect. | No return exists yet. | A run that records inferability or insufficiency without preserving it as the result repeats the routing failure. |
| Public protocol/private capsule split as a changed blinding architecture. | The public packaging path failed because the committed bundle exposed too much. | No capsule has been constructed under this split. | If a later run commits the capsule before return, this architecture is void for that attempt. |

### What This Source Does Not Establish

This source does not populate any active CL-001 packet field. It does not score
any gate, issue a CL-001 verdict, accept a repo-owned claim, satisfy the
charter's blinded-field requirement, or complete a blind receipt.

It does not establish:

- a dollar or Bitcoin field-`T` value;
- that any blind author exists or has accepted a task;
- that any local or private handoff has been created;
- that a private capsule would be materially sufficient;
- that a private capsule would be non-inferable;
- that a later returned candidate `T` value is source-supported;
- label-swap invariance, no merit ordering, or no same-run founding-corpus
  contamination for a later verdict; or
- a legitimacy verdict about either arm.

### Falsifiers And Reopen Conditions

Reopen or supersede this architecture if:

- a later run commits the blind read capsule publicly before blind return;
- the blind author reads the repository, open-label dossiers, source URLs,
  founding corpus, unblinding key, or arm mapping before returning;
- the blind author cannot decide inferability before extraction;
- the blind author returns candidate `T` language despite recognizing an arm
  before extraction;
- the capsule lacks enough material to describe field `T`;
- post-return review treats candidate language as an accepted packet field
  without open-label provenance and symmetry checks; or
- this architecture is used as evidence that gate 10 has passed or that a
  CL-001 outcome has been reached.

## No Claim Promotion

This source dossier cannot promote a CL-001 packet, gate, experiment verdict, or
repo-owned claim. It only records a changed blind-return method boundary that a
later run may use before active field-`T` packet population.
