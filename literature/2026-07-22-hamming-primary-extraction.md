---
artifact_type: primary_source_extraction
status: complete
lane: discovery
recipient_lane: 3
claim_status: none
evidence_grade: primary_source_bounded
candidate_disposition: NARROWER_STRUCTURE_CODING_CONSTRAINT
cl001_isolation: required
---

# Hamming Primary Extraction

## Question and read scope

Does Hamming's 1950 primary paper support the Hamming atlas seed, and does a
Continuity Ledger description add explanatory content beyond ordinary coding
theory?

Source: R. W. Hamming, "Error Detecting and Error Correcting Codes," *Bell
System Technical Journal* 29(2), April 1950, pp. 147-160,
https://doi.org/10.1002/j.1538-7305.1950.tb00463.x. The DOI publisher record
fixes the bibliographic identity. The full-text read used a scan of the same
article carrying its title, author, journal pagination, and 1950 AT&T copyright.

This read is limited to the code construction, its resource/import costs, its
error-class boundary, and the strongest ordinary-theory absorber. It does not
read or score CL-001.

## Source-grounded extraction

| Paper result | Primary location | Continuity Ledger relevance |
|---|---|---|
| A systematic code has `n` binary digits, `m` information digits, and `k = n - m` check digits. Hamming defines redundancy `R = n/m`. | pp. 148-149, section 1 | The reliable regime imports structured redundancy; it does not obtain reliability for free. |
| Redundancy lowers effective channel capacity, and encoding/correcting needs extra equipment. | pp. 148-149 | These are explicit loss/import terms, but they are already native coding-theory costs. |
| An even parity position detects a single error because one changed digit makes parity odd. | pp. 149-150, section 2 | The detection boundary is an exact parity constraint, not a generic agency surface. |
| For single-error correction, ordered parity checks produce a binary checking number that locates the error, with zero meaning no error. | pp. 150-153, section 3 | The source supplies the encoding/decoding mechanism and a worked seven-position example. |
| Adding one overall parity position to a single-error-correcting code distinguishes no error, one error, and two errors under the stated cases. | pp. 153-154, section 4 | The guarantee is class-relative to the declared error cases. |
| In the geometric model, minimum distance at least two detects one error and minimum distance at least three corrects one error by nearest-code-point structure. | pp. 154-156, section 5 | Code distance supplies the exact continuity constraint; no cross-domain invariant is needed. |
| The paper proves minimum-redundancy bounds for its constructed cases under its assumptions and records that general optimal construction beyond distance four was not known. | pp. 157-160, sections 6-9 | The source states both its optimality result and its frontier; later prose must not inflate the bounded claim. |

## Absorber test

Ordinary coding theory absorbs the source-grounded case. The before/after
difference is fully explained by an imported codebook, added check digits,
parity/checking rules, a decoder, and a declared error class. The paper itself
names the cost in reduced effective channel capacity and extra equipment. Its
minimum-distance model explains detection and correction without an additional
transduction primitive.

The original atlas seed's `P / A / Omega` language about a newly recruited
agent class is not established by this paper. Hamming motivates automatic
correction in machines, but does not prove an agency surface or action-space
enlargement in Continuity Ledger's sense. The seed's recursive `F` claim about
larger reliable systems creating more demand for coding is also not a result of
the paper.

## Disposition

`NARROWER_STRUCTURE_CODING_CONSTRAINT` at pre-release exploration grade.

The useful retained structure is typed and domain-local: redundancy plus
distance constraints buy correction capability for a stated error class, with
explicit capacity/equipment costs. This is a strong negative control for any
future atlas because a generic ledger vocabulary adds no demonstrated
explanatory residue here.

No shared cross-case structure, CL-001 field, claim promotion, source-domain
truth beyond the cited paper, or external action follows.

## Handoff and deduplication

Do not repeat the Hamming primary extraction unless a specific reader disputes
a cited page/result. If Lane 3 later opens, use this case as an ordinary-theory
absorber control: any proposed atlas invariant must say more than the exact
redundancy, distance, decoder, error-class, and cost account already supplied
by coding theory.
