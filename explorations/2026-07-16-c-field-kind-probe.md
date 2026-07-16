---
artifact_type: exploration
probe_id: CL-001-C-PROBE-01
lane: 1
claim_status: none
verdict: none
evidence_grade: repo_owned_probe_over_pinned_dossiers
scores_no_gate: true
populates_no_field: true
date: 2026-07-16
---

# CL-001 C-Field Kind Probe

`claim_status: none`
`verdict: none`

This probe scores no gate, populates no packet field, and promotes no claim. It
reports what the existing dossier evidence does and does not support for one
CLTP field, `C` (continuity witness), on the two founding targets.

## Why this probe

`C` is the cheapest available attack on the Nearer Guiding Hypothesis. The
hypothesis claims a typed continuity ledger *distinguishes* agency-generating
transduction from ordinary conversion, disclosure, and relabeling. If `C` is
merely "some domain-appropriate witness," the typed witness categories do the
work and the ledger adds nothing. That failure is already named in the charter:
"the continuity relation reduces to vague causal storytelling."

The probe needed no new sourcing. Four dossiers with pinned primary sources
already exist (Bitcoin Core `v31.1` at commit `9be056a8`; Umena 2011, Kok 1970,
Field 1998, Bar-On 2018).

## Method

Two agents derived `C` independently, each reading **only** its own target's
dossiers, the CLTP interface, and the charter's Core Distinctions and
Representation discipline. Neither was told the other target existed. Neither
was told the other agent existed. Neither was told the prediction below.

Blinding was deliberate. The probe's author had publicly predicted an outcome
and would otherwise have been the one scoring it.

## Preregistered prediction, and its failure

The prediction, recorded before the probe ran:

> `C` comes back **kind-heterogeneous** across the pair. Bitcoin's witness is a
> threshold certificate over a counterfactual (`nChainWork` as expected hashes,
> a redo-burden); photosynthesis's is physical transport of electrons and free
> energy. Two different relations wearing the same letter. CL-001 therefore dies
> at the continuity gate.

**This prediction failed.** It was wrong in both of its parts.

1. `C` is not kind-heterogeneous on the evidence. Both derivations landed on
   **constraint** as a live kind: Bitcoin as provenance-with-secondary-constraint,
   photosynthesis as constraint with causal dependence as runner-up. If anything
   the candidates *converge* rather than diverge.
2. The comparison could not be run at all. **`C` is OPEN for both targets.** You
   cannot compare the kinds of two witnesses when neither witness is determined.

The prediction was not merely unconfirmed. It presumed a determinable field on
both sides, and that presumption is what the evidence refuses.

## Result: OPEN on both, for the same two reasons

Both independent derivations returned `C` = **OPEN**, and converged on two
blockers neither was prompted toward.

### 1. No witness spans the transduction

A continuity witness relates a source regime to a target regime. Only one
endpoint is evidenced on each side.

- **Bitcoin.** The dossier states plainly that "the cited protocol sources do
  not by themselves quantify electricity, heat, embodied hardware, mining
  equipment, or grid effects." The energy side has no typed `R0`/`M0`. Relating
  energy to chainwork on this evidence would be exactly the untyped bridge the
  charter bans and the packet names as a falsification condition.
- **Photosynthesis.** The mechanism dossier covers PSII water oxidation and
  disclaims carbon fixation, biomass, and ecological agency. The agency dossier
  covers the far side and supplies no positive `C` candidate at all, only
  prohibitions. The two sides do not touch. No permitted source states any
  relation spanning source regime to target regime.

### 2. Covariance is unstated for both

The charter requires it: "A continuity witness must state its covariance or
transformation behavior." Neither target has source support for it. For Bitcoin
a fragment exists (declared `nBits` ↔ target ↔ proof conversion maps), but
invariance under implementation change is explicitly open. For photosynthesis
there is zero source content on transformation behavior under any admissible
change.

This blocker is independently sufficient and survives every rescoping.

## The finding the probe actually produced

The convergent result is sharper than the prediction it refuted, and it is about
`R0`, not `C`.

**`C`'s determinability depends on an analyst-chosen regime boundary, and the
choice that makes `C` determinable is the choice that makes the case trivial.**

The Bitcoin derivation states it exactly:

> Choose `R0` = the computational regime rather than the physical regime, and
> `C` is determinable today: provenance, in hash units, with the `nBits`
> conversion map as its transformation law. [But] choosing `R0` = hashing regime
> makes the transduction nearly trivial (hashing → record-of-hashing), which is
> precisely the hash-without-surface null. **Picking the `R0` that makes `C`
> determinable is picking the `R0` that makes the case a null.**

The photosynthesis derivation reached the same shape independently:

> Someone could reasonably scope the transduction *at* the water-oxidation
> boundary, in which case the Kok constraint spans it and `C` is arguably
> determinable as a constraint witness. That would be a defensible packet, just a
> much narrower one, and it would owe an account of why the narrow boundary is
> the interesting one. I do not think the sources decide between these scopings.

So on both targets: **narrow the boundary and `C` exists but the case collapses
toward its own null; widen it and `C` is OPEN.** Nothing in the packet, the
interface, or the charter individuates `R0`. The analyst picks, and the pick
decides the answer.

## Open field, honestly stated

`C` remains **"Open pending primary-source pass"** on both packets, unchanged by
this probe. What would close it:

- **Bitcoin:** a pinned primary source giving a typed hash-attempt ↔ energy
  relation with declared units, explicit conversion map, and error bars, stated
  as a typed conversion and not an identity; plus a protocol-level (not
  Core-implementation-level) statement that cumulative work is the chain
  selection quantity.
- **Photosynthesis:** a primary carbon-fixation source linking reducing
  equivalents and ATP to fixed carbon, which both dossiers already name as the
  gating missing piece; primary replacements for the orientation-only sources;
  and a covariance statement.
- **Both:** an account of what fixes `R0` that is not the analyst's choice.

## Related leads, not evidence

Two convergent observations exist outside this probe's evidence base. They are
recorded as leads and carry no weight here.

- An unprovenanced Lane 2 audit reports that `X` (escape witness) collapses into
  relabeling because `K0` is analyst-chosen and nothing individuates it. That is
  the same defect as the one above, in a different field: a CLTP field whose
  value is decided by an unindividuated analyst-chosen class boundary.
- The unprovenanced Lane 3 candidate material
  (`explorations/candidate-transduction-atlas-seeds.md`,
  `provenance_status: broken`) reports across thirteen unrelated cases that
  "many cases are not object-level transductions but regime-plus-boundary-
  dependent judgments."

If those two leads are ever properly established, three independent derivations
over three disjoint corpora would agree that the boundary choice does the work.
That is a hypothesis about the CLTP, not a result. It is not established here and
must not be treated as established.

## What this does not do

- It does not score the continuity gate.
- It does not populate `C`.
- It does not return or imply a CL-001 verdict.
- It does not establish that `C` is undeterminable in principle, only that it is
  undetermined on the pinned evidence currently in this repository.
