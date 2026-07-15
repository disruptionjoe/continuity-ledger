---
artifact_type: evidence_dossier_template
status: active_construction_template
experiment: CL-001
claim_status: none
verdict: none
---

# CL-001 Source Dossier Template

## Purpose

This template defines the extraction record that must sit between a source and
any later CL-001 packet population. A dossier is not itself a packet result,
does not accept a source-domain claim as repo truth, and does not score any gate.

Use one dossier per source or tightly coupled source set. Keep the extraction
scoped enough that a later reviewer can see exactly which packet fields the
source supports, which it does not support, and which imports or losses remain
open.

## Required Dossier Metadata

Each CL-001 source dossier must include:

- `source_id`: stable local identifier for the source.
- `source_type`: primary, protocol, construction, review, or absorber/control.
- `applies_to_packets`: one or more CL-001 packet identifiers.
- `evidence_lanes`: the source-intake lanes this source can bear.
- `provenance`: enough citation or revision detail to audit the source.
- `extracted_by`: agent or human who made the extraction.
- `extracted_on`: date of extraction.
- `status`: draft, checked, superseded, or rejected.

## Required Dossier Sections

Every dossier must preserve these sections in this order.

### Source Boundary

Name the source, its provenance, why it is admissible for CL-001, and whether
it is primary, protocol-level, construction-only, or a secondary orientation
source. Secondary orientation sources cannot populate material packet fields
unless a later run traces the same claim to an admissible source.

### Scoped Extraction

Record only claims the source actually supports. Do not infer CLTP fields from
background knowledge or from the reason the source was selected.

| Source-supported point | Packet field candidates | Evidence lane | Scope limit |
|---|---|---|---|
|  |  |  |  |

### Typed Quantities

List all quantities the source names and keep unlike types unlike.

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
|  |  |  |  |

### Losses And Imports

Record dissipation, uncertainty, hidden schemas, external subsidies, boundary
conditions, missing imports, and observer-side assumptions before any agency or
escape inference is considered.

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
|  |  |  |  |

### Agency And Feedback Burden

Separate source support for a process from support for an agency surface,
action class, action space, and recurrent feedback.

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
|  |  |  |  |

### What This Source Does Not Establish

State which CLTP fields, gates, verdicts, and cross-domain comparisons remain
unestablished after this source is read.

### Falsifiers And Reopen Conditions

Name conditions that would make this dossier unusable, superseded, or too weak
to support packet population.

## No Claim Promotion

A source dossier cannot promote a CL-001 packet, gate, experiment verdict, or
repo-owned claim. It only records source extraction work for later review.
