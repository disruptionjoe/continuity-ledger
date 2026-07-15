---
artifact_type: evidence_dossier_manifest
status: active_construction_manifest
experiment: CL-001
claim_status: none
verdict: none
---

# CL-001 Source Dossier Manifest

## Purpose

This manifest binds the CL-001 source-dossier template to the four CL-001
packet construction files. It is not evidence, does not select exact sources,
does not fill extraction tables, and does not score any gate.

Use this manifest as the queue for later exact-source passes. A queued dossier
can support packet population only after a later run creates the dossier,
records provenance, extracts source-supported points, and leaves unsupported
fields open.

## Packet Coverage

| Packet id | Packet file | Packet role | Required dossier posture | Current dossier status |
|---|---|---|---|---|
| `cl001-bitcoin-proof-of-work` | `packets/cl-001/bitcoin-proof-of-work.md` | Target case | Protocol-level and participant-surface extraction before packet fields move. | Draft protocol-mechanism dossier exists; draft participant-surface dossier exists. |
| `cl001-oxygenic-photosynthesis` | `packets/cl-001/oxygenic-photosynthesis.md` | Target case | Primary scientific and biochemical/ecological extraction before packet fields move. | Draft mechanism dossier exists; carbon-fixation, biomass, ecological, and agency-surface extraction remain pending exact source selection. |
| `cl001-null-hash-without-agency-surface` | `packets/cl-001/null-hash-without-agency-surface.md` | Matched null | Construction and absorber extraction under the same lane burden as target cases. | Draft construction dossier exists; exact hash-computation source, energy/loss evidence, and no-surface demonstration remain pending source selection. |
| `cl001-null-solar-heating-inert-matter` | `packets/cl-001/null-solar-heating-inert-matter.md` | Matched null | Construction and absorber extraction under the same lane burden as target cases. | Draft construction dossier exists; exact heat-transfer source, passive-material loss evidence, and no-surface demonstration remain pending source selection. |

## Dossier Queue

Every queued dossier starts with `status: draft` and remains non-evidentiary
until it is created from `evidence/cl-001-source-dossier-template.md` with
source provenance and scoped extraction.

| Queue item | Applies to packet | Source type | Evidence lanes to preserve | Status |
|---|---|---|---|---|
| Bitcoin protocol mechanism dossier | `cl001-bitcoin-proof-of-work` | protocol | Mechanism and transition boundary; regime and class definition; typed measurement family; absorber and null pressure. | Draft dossier: `evidence/cl-001-dossiers/bitcoin-protocol-mechanism.md`. |
| Bitcoin participant-surface dossier | `cl001-bitcoin-proof-of-work` | construction or primary | Loss and import accounting; agency surface and action space; class-relative no-go or constraint; feedback and recurrence; falsifiers and open fields. | Draft dossier: `evidence/cl-001-dossiers/bitcoin-participant-surface.md`. |
| Photosynthesis mechanism dossier | `cl001-oxygenic-photosynthesis` | primary | Mechanism and transition boundary; typed measurement family; loss and import accounting; falsifiers and open fields. | Draft dossier: `evidence/cl-001-dossiers/photosynthesis-mechanism.md`. |
| Photosynthesis agency-surface dossier | `cl001-oxygenic-photosynthesis` | primary or review | Agency surface and action space; class-relative no-go or constraint; feedback and recurrence; absorber and null pressure; falsifiers and open fields. | Pending exact source selection. |
| Hash-without-surface construction dossier | `cl001-null-hash-without-agency-surface` | construction | Mechanism and transition boundary; regime and class definition; typed measurement family; loss and import accounting; agency surface and action space; class-relative no-go or constraint; absorber and null pressure; falsifiers and open fields. | Draft dossier: `evidence/cl-001-dossiers/null-hash-without-agency-surface-construction.md`. |
| Solar-heating inert-matter construction dossier | `cl001-null-solar-heating-inert-matter` | construction | Mechanism and transition boundary; regime and class definition; typed measurement family; loss and import accounting; agency surface and action space; class-relative no-go or constraint; absorber and null pressure; falsifiers and open fields. | Draft dossier: `evidence/cl-001-dossiers/null-solar-heating-inert-matter-construction.md`. |

## Symmetry Checks

- Target packets and null packets must use the same source-intake lanes before
  gate scoring.
- Null packets cannot be made to fail by choosing weaker evidence standards
  than the target packets.
- Target packets cannot be made to pass by importing participant, ecological,
  institutional, or observer-side structure without recording that import.
- Source dossiers must leave fields open when source support is absent or only
  secondary orientation is available.

## No Claim Promotion

This manifest cannot promote a CL-001 packet, gate, experiment verdict, or
repo-owned claim. It only records the pending dossier queue for later exact
source work.
