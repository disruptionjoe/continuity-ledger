---
artifact_type: exploration
probe_id: CL-001-R0-PROBE-02
lane: 1
claim_status: none
verdict: none
status: preregistration
date: 2026-07-16
sequencing_note: This bar was written and committed BEFORE any candidate rule was generated or seen. Its purpose is to prevent the bar being fitted to the candidates.
---

# R0 Individuation: Preregistered Admissibility Bar

`claim_status: none`
`verdict: none`

## The question

`CL-001-C-PROBE-01` found that `C` is OPEN on both founding targets, and that
its determinability turns on an analyst-chosen regime boundary. Narrow `R0` and
`C` resolves but the case collapses toward its own null; widen `R0` and `C` is
OPEN. Nothing in the packet, the CLTP interface, or the charter individuates
`R0`.

So: **is there a rule that fixes `R0` and `R1` for a case, which is not the
analyst's choice?**

This matters more than any single field. If no such rule exists, the CLTP's
regime boundary is a free parameter, every field indexed to it inherits that
freedom, and the instrument cannot discriminate — regardless of how the founding
analogy fares. That would be a `KILL` on the instrument rather than on the
analogy, and it would generalize to every future packet.

## Why this bar is preregistered

The author of this probe predicted the outcome of `C-PROBE-01` and was refuted.
That prediction failed partly because it presumed its own frame. Writing the
admissibility bar *before* generating candidates is the cheapest available guard
against repeating that: a bar written after seeing candidates can be tuned to
admit a favoured one or exclude an inconvenient one.

## The bar

A candidate `R0`-individuation rule is **admissible** only if it satisfies all
five conditions.

### B1. Inter-analyst determinacy

Two competent analysts, applying the rule to the same case with the same pinned
sources, select the same `R0` and `R1`. If the rule requires judgment that the
rule itself does not constrain, it fails.

*Test:* state the rule, hand it plus one dossier set to two independent parties,
compare selections.

### B2. Source-groundedness

Every input the rule consumes is supplied by primary domain sources, not by
analyst preference, research interest, or the desire to make a case work. The
charter already holds that domain laws, empirical facts, and primary literature
are **imported and not owned** here. A rule whose inputs are owned here is a
rule that lets this repository choose its own answer.

### B3. Non-triviality in both directions

The rule must not systematically select:

- the `R0` that makes the case collapse into its own null (the trap `C-PROBE-01`
  found on Bitcoin: hashing to record-of-hashing); nor
- the widest available span, which makes `C` OPEN by construction and renders
  every packet unfillable.

A rule that always returns one of these is not individuating a boundary, it is
expressing a preference with extra steps.

### B4. Non-circularity

The rule may **not** consume `C`, `P`, `A`, `Omega`, `N`, or `X` as inputs.

Those are the fields whose determinacy `R0` is supposed to establish. Fixing the
boundary using them fixes the boundary with the answer. This is the sharpest
condition and the one most candidates are expected to fail.

`M0`/`M1` require care. They are indexed *to* `R0` and `R1`, so a rule that
consumes "the measurement family of `R0`" is circular. A rule that consumes the
unindexed set of typed quantities the sources supply, and derives the boundary
from structural facts about that set, is not obviously circular and must be
judged on its merits.

### B5. Discrimination preservation

Applied to a target and its matched null, the rule must not force an `R0` that
trivially equates them or trivially separates them. The boundary must be
selected by the same procedure on both, and the resulting discrimination (or
failure to discriminate) must be a finding rather than an artifact of selection.

## Possible outcomes, named in advance

- **ADMISSIBLE RULE FOUND.** At least one candidate clears all five. `R0` is
  individuable; `C` and the fields indexed to the boundary become determinable
  in principle; CL-001 proceeds and the instrument survives this attack.
- **NARROWED.** A rule clears the bar only for a restricted class of cases. The
  CLTP is valid on that class and silent elsewhere. States which class.
- **NO ADMISSIBLE RULE.** Every candidate fails at least one condition, and the
  failures are explained rather than merely counted. The regime boundary is a
  free parameter and the instrument cannot discriminate. This is a `KILL` on the
  instrument, and the charter holds that a clean kill is a successful result.

No outcome is preferred. The probe is run to find out.

## Scope limits

This preregistration scores no gate, populates no field, and returns no CL-001
verdict. It fixes a standard. Whether any rule meets it is decided by a later
pass, against this text as written, unamended.
