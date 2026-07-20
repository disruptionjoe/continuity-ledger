---
source_id: active-cl001-blind-t-isolated-return-protocol-20260720
source_type: process-control protocol
applies_to_packets: active-cl001-dollar-arm-pending; active-cl001-bitcoin-arm-pending
evidence_lanes: Frame adherence and declared-field guard; Mechanism and transition boundary; Absorber, near-miss null, and arm-symmetry pressure; Falsifiers, open fields, and routing
provenance: governance/CHARTER.md; experiments/CL-001-phi-frame.md; evidence/cl-001-interval-sweep-source-intake.md; evidence/cl-001-interval-sweep-dossier-manifest.md; evidence/cl-001-interval-sweep-dossiers/blind-t-public-packaging-method-stop.md; evidence/cl-001-interval-sweep-dossiers/blind-t-isolated-return-architecture.md
extracted_by: Codex child run RUN-20260720-560-repository-work-cycle-cai-hourly
extracted_on: 2026-07-20
status: draft
claim_status: none
verdict: none
---

# Blind T Isolated Return Protocol

## Source Boundary

This draft process-control protocol records the public side of the CL-001
isolated blind-return method for field `T`.

Declared frame reference: `experiments/CL-001-phi-frame.md`.

The protocol implements the already-recorded architecture without creating the
blind read capsule, arm mapping, or unblinding key. It does not populate any
active CL-001 packet field, does not score any gate, does not complete a blind
author receipt, and does not issue a verdict.

The public repository may record the protocol, permitted stop codes, and receipt
shape. The actual read capsule, capsule contents, source ordering, arm mapping,
and unblinding key must remain outside committed public files until after a
blind author returns a receipt or stop result.

### Scoped Extraction

| Process-supported point | Packet field candidates | Evidence lane | Scope limit |
|---|---|---|---|
| A valid isolated return separates the public protocol from the blind author's private read capsule. | `V`, `Z` | Frame adherence and declared-field guard; Absorber, near-miss null, and arm-symmetry pressure | This protocol names the boundary; it does not create the capsule or prove that a capsule can be non-inferable. |
| The blind author must receive only a bounded task capsule, coded source excerpts, the field-`T` extraction target, and the stop-code definitions. | `T`, `V` | Mechanism and transition boundary; Falsifiers, open fields, and routing | Repository-wide reading, open-label dossier reading, source-URL browsing, founding-corpus reading, arm mapping, and unblinding keys are outside the read scope. |
| The return order is stop-code first: inferability before extraction, then material insufficiency, then candidate `T` language only if neither stop fires. | `T`, `V`, `Z` | Mechanism and transition boundary; Falsifiers, open fields, and routing | A stop code is a valid result and does not authorize unblinded packet population. |
| A later receipt must identify the handoff, capsule checksum or digest, blind author or run identity, stop code, and whether any candidate field-`T` language was returned. | `V` | Falsifiers, open fields, and routing | Receipt metadata is process evidence, not a packet field or gate score. |
| Any unblinding event must be recorded after return and outside the blind author's read scope. | `V`, `Z` | Absorber, near-miss null, and arm-symmetry pressure | Unblinding cannot retroactively improve the blind status of the returned text. |

### Typed Quantities

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
| Public protocol | Committed process boundary and receipt shape. | This protocol and the isolated-return architecture. | Blind read capsule, source authority, packet field, gate score. |
| Blind read capsule | Private or ignored bounded text set for the blind author. | Architecture allowed surface; not created here. | Public dossier, unblinding key, accepted evidence grade. |
| Capsule digest | Integrity pointer for the exact private read surface. | Later private handoff and receipt only. | Arm identity, source claim, mechanism verdict. |
| Stop code | One of `blind_failed_inferable`, `blind_failed_insufficient_material`, or `candidate_t_returned`. | This protocol. | CL-001 outcome, claim status, gate pass. |
| Return receipt | Process record for the blind result and later unblinding event. | Later blind run only. | Accepted field value, source truth, legitimacy verdict. |
| Candidate `T` language | Blind-authored pre-review mechanism wording. | Later `candidate_t_returned` result only. | Populated packet field, source-supported extraction, verdict. |

### Losses And Imports

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
| This protocol imports the public-path method stop and the isolated-return architecture. | `V`, `Z` | Prior stop and architecture records. | A later handoff must still avoid public capsule exposure before return. |
| The public protocol author is open-label and cannot serve as the blind author for this handoff. | `V` | Charter Frame Discipline rule 6 and this run's source loading. | A later blind author or bounded run must remain isolated from arm labels and repo context. |
| A private capsule loses pre-return public review. | `V` | Isolated-return architecture. | A later receipt must preserve a digest and enough identity to audit the exact capsule after return. |
| The blind author imports only the capsule text and stop-code definitions. | `T`, `V` | This protocol. | Any outside context read before return voids the blind result for gate-10 purposes. |
| Candidate `T` language imports a later open-label review burden. | `T`, `V`, `Z` | Active dossier queue and source-intake contract. | Open-label review may reject, narrow, or leave pending the candidate language before any packet population. |

### Agency And Feedback Burden

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
| Stop-code-first blind return as a process surface for field `T`. | Charter rule 6, public packaging method stop, and isolated-return architecture. | No private capsule or blind receipt exists yet. | Ordinary open-label review absorbs the surface unless inferability is tested before extraction. |
| Protocol-level routing of recognized inferability or insufficiency. | Charter rule 7 and repeated public-bundle inferability findings. | A later author must actually return the stop instead of continuing to extract. | A run that records a stop but then populates `T` repeats the routing failure. |
| Digest-backed receipt as post-return audit surface. | Architecture's requirement to keep the capsule private before return. | No digest, author, stop code, or unblinding event exists yet. | A receipt without digest or scope identity cannot support the blind-control burden. |

### What This Source Does Not Establish

This source does not populate any active CL-001 packet field. It does not score
any gate, issue a CL-001 verdict, accept a repo-owned claim, satisfy the
charter's blinded-field requirement, or complete a blind author receipt.

It does not establish:

- a dollar or Bitcoin field-`T` value;
- that a materially sufficient private capsule exists;
- that a private capsule would be non-inferable;
- that a blind author has read or returned anything;
- that any candidate `T` language is source-supported;
- label-swap invariance, no merit ordering, or no same-run founding-corpus
  contamination for a later verdict; or
- a legitimacy verdict about either arm.

### Falsifiers And Reopen Conditions

Reopen or supersede this protocol if:

- a later run commits the blind read capsule, arm mapping, or unblinding key
  before blind return;
- the blind author reads the repository, open-label dossiers, source URLs,
  founding corpus, arm mapping, or unblinding key before returning;
- the blind author cannot assess inferability before extraction;
- a returned stop code is ignored and `T` is populated anyway;
- a return receipt lacks a handoff identity, capsule digest, author/run identity,
  stop code, or unblinding timing;
- post-return review treats candidate language as an accepted packet field
  without open-label provenance and symmetry checks; or
- this protocol is used as evidence that gate 10 has passed or that a CL-001
  outcome has been reached.

## No Claim Promotion

This source dossier cannot promote a CL-001 packet, gate, experiment verdict, or
repo-owned claim. It only records the public protocol and receipt shape for a
later isolated blind-return attempt before active field-`T` packet population.
