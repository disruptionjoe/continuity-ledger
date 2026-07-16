# Steward Memory Log

## 2026-07-14

- Created the provisional local skeleton under Joe's direct instruction.
- Charter, North Star, guiding hypothesis, `AGENTS.md`, GitHub remote, claim
  system, artifact transfer, and automation activation remain intentionally
  pending.
- The setup decision treats Possibility to Capability and WI-069 as distinct
  sibling surfaces. Possibility to Capability owns its possibility-to-capability
  hierarchy and frozen joint-seam packet layer. WI-069 remains the JoeOps
  coordination source for the pre-repo continuity-ledger and agency-transduction
  artifacts until Joe explicitly transfers or links them under this repo's
  future governance.
- Joe authorized activation. The Continuity Ledger name, public posture,
  charter, and `AGENTS.md` were ratified; the 29-file WI-069 corpus transferred
  as checksum-verified exploration history; CL-001 became the first
  falsification run; and routine GitHub versioning plus the standard repository
  steward package were approved. No source-repository claim or verdict moved.

## 2026-07-15

- Added the CL-001 packet workspace with scaffolded Bitcoin proof-of-work,
  oxygenic photosynthesis, and matched-null packet files, plus a deterministic
  validator for packet field/gate shape. No packet gate was scored, no verdict
  was issued, and the frozen WI-069 corpus remained origin history rather than
  evidence.
- Added a CL-001 source-intake contract and validator coverage so later packet
  population must preserve primary-source burden, null symmetry, open-field
  status, and no-claim-promotion boundaries before scoring.
- Added a CL-001 source-dossier template and validator coverage so future
  source passes have an auditable extraction record between source reading and
  packet-field population.
- Added a CL-001 source-dossier manifest and validator coverage so the four
  packet-specific exact-source passes are queued without moving source
  evidence, packet fields, gates, verdicts, or claim status.
- Added a CL-001 draft source dossier for the oxygenic photosynthesis mechanism
  lane, scoped to PSII water oxidation and typed biochemical quantities while
  leaving carbon fixation, biomass, ecological agency, packet fields, gates,
  verdicts, and claim status open.
- Added a CL-001 draft construction dossier for the matched
  hash-without-agency-surface null, scoped to the repo-owned null burden while
  leaving exact hash-computation sources, energy/loss evidence, no-surface
  demonstration, packet fields, gates, verdicts, and claim status open.
- Added a CL-001 draft construction dossier for the matched solar-heating
  inert-matter null, scoped to the repo-owned null burden while leaving exact
  heat-transfer sources, passive-material loss evidence, no-surface
  demonstration, packet fields, gates, verdicts, and claim status open.
- Added a CL-001 draft source dossier for the Bitcoin participant-surface lane,
  scoped to design-level node, client, relay, incentive, and resource-burden
  documentation while leaving current economics, actual participant motivation,
  packet fields, gates, verdicts, and claim status open.
- Added a CL-001 draft source dossier for the oxygenic photosynthesis
  agency-surface lane, scoped to primary production, standing biomass, trophic
  support, and biogeochemical-feedback evidence while leaving biochemical
  carbon-fixation source selection, organism-specific agency, packet fields,
  gates, verdicts, and claim status open.
- Hardened the CL-001 validator so the source-dossier manifest and draft
  dossier queue cannot silently drift: manifest paths must resolve, all draft
  dossiers must remain listed, `source_id` values must stay unique, evidence
  lanes must match the intake contract, and dossier status, claim status, and
  verdict fields must remain non-promotional.

## 2026-07-16

- Merged `agent/link-wi-069-origin` into `main` after measuring the merge clean:
  zero overlapping files against the merge base and `merge-tree` exit 0. Before
  this, `main` presented a four-lane governance manifest over `packets/`,
  `evidence/`, and `results/` directories holding only READMEs, with no
  validator, while all twelve commits of CL-001 substance sat on the branch.
  Every statement on `main` was true and the composite impression was false.
- Installed `LANES.yaml` as the repository's lane declaration, then corrected it
  in the same day. The first revision was rendered from a CapacityOS planning
  manifest rather than authored from this charter, and it carried three defects
  of one kind: the portfolio's view of this repository overwrote the
  repository's view of itself.
- Defect one: the manifest marked "continuity through transduction" as the North
  Star. The charter's Audacious North Star is a theory of evolutionary agency
  escape, which the charter calls the highest-ceiling target and explicitly not
  a premise. It sits above the lane structure and no lane is identical to it.
  The manifest now declares it in `owner.charter_north_star` and forbids marking
  any lane as it.
- Defect two: Lane 1's purpose was written in vocabulary this repository does
  not use. "Coarse-graining" and "reduction" appear zero times in `CHARTER.md`,
  `AGENTS.md`, `README.md`, `steward/README.md`, and
  `hypotheses/FOUNDING-HYPOTHESES.md`. Lane 1 now carries the charter's Nearer
  Guiding Hypothesis in the charter's own terms.
- Defect three: a `special_rules` entry exported CL-H6 Agentic Discovery
  Advantage to ai-epistemology. The charter owns that claim in three places:
  "Agentic Research Claim", "What This Repository Owns", and "Success Standard".
  CL-H6 is now declared as this repository's agent-capability evaluation lens in
  `owner.agent_capability_lens`. Generic agent-method learning still routes to
  ai-epistemology; CL-H6 does not.
- Reshaped the lanes to stop cutting the founding experiment in half. The Nearer
  Guiding Hypothesis explicitly bundles continuity witnesses, generated agency,
  class-relative no-goes, escape moves, and recursive feedback into one
  hypothesis tested by one ten-gate experiment. The earlier Lane 1 / Lane 2
  split ran a boundary through the middle of CL-001, which is why three of its
  ten gates appeared to be blocked in a different lane from the experiment.
  Lane 1 is now `LEDGER-FORCE-OR-FALSIFY` carrying the hypothesis whole; Lane 2
  is `LEDGER-HARDENING`, typed `supporting_progress` with a required lease so
  that retreat from a hard North Star into tractable hardening byproducts hits a
  brake.
- Lane 3 remains admission-gated on the CL-001 verdict. Unchanged by this pass.
- Fixed a real defect in `tests/validate_cltp_packets.py`. `validate_packet()`
  checked `"verdict: unscored" not in text`, a whole-file substring scan, so a
  packet carrying `verdict: SHARED_STRUCTURE` in its front matter validated
  cleanly as long as the literal appeared anywhere in the body. This is the
  guard on a source verdict. It is now scoped to parsed front matter, matching
  the pattern `validate_source_dossiers()` already used twelve lines away.
  Verified adversarially: the old logic passes a smuggled verdict, the new logic
  catches it.
- `LANES.yaml` remains canon-by-derivation, not canon-by-validation. The
  CapacityOS lane schema does not exist yet, so nothing validates this file's
  shape. When the schema lands, this manifest must be validated against it and
  reconciled if the shapes differ.
- Open and not resolved by this pass: the CL-001 matched nulls are specified in
  the charter by stipulated absence of what the agency gate tests, so they
  cannot fail for a non-definitional reason. This makes the preregistered
  `SHARED_STRUCTURE` branch unreachable, and it also disables the charter's own
  Nearer-Guiding-Hypothesis falsifier "matched null controls satisfy the same
  gates as the target examples". Repairing it is a charter amendment and is
  queued as the next decision.
- Amended the charter's Matched Nulls (Joe direct chat, 2026-07-16). Both
  ratified nulls were specified by stipulated absence of what the agency gate
  tests, so neither could fail for a non-definitional reason. This made the
  preregistered `SHARED_STRUCTURE` branch unreachable and disabled the charter's
  own Nearer-Guiding-Hypothesis falsifier "matched null controls satisfy the
  same gates as the target examples", since a null that cannot pass can never
  fire it. CL-001 could neither confirm nor be falsified on that axis. The
  repository had already recorded the definitional-exclusion risk in six places
  across both null packets, the intake contract, and both null dossiers; no run
  ever escalated it. The amendment is additive: both original nulls are retained
  and reclassified as zero-weight floor nulls, and positively specified
  near-miss nulls are added to carry the load. Bitcoin testnet or regtest is the
  near-miss for the Bitcoin target; Rayleigh-Benard convection or a solar pond
  for photosynthesis. A near-miss null may never be selected for lacking an
  agency surface, which would relocate the stipulation from specification time
  to selection time. If no admissible near-miss null exists for a target, the
  verdict is `KILL` on uncontrollability, which is a successful result. No
  target, gate, verdict, or hypothesis changed. Amended before any packet field
  was populated or any gate scored, so nothing is retrofitted; the window for a
  clean amendment was open precisely because the lane had produced nothing.
- Recorded in `experiments/CL-001-...md` that the near-miss null packets,
  manifest entries, and source dossiers do not yet exist. The dossier manifest
  still queues only the two floor nulls. Constructing the near-miss nulls is now
  the load-bearing remaining work in CL-001; until it exists the run can reject
  the trivial case and nothing more.
- Admitted `explorations/candidate-transduction-atlas-seeds.md` as Lane 3
  pre-release exploration material, flagged `provenance_status: broken` and
  `evidence_grade: lead_only`. Joe added it from an external research agent. It
  is gate-compliant: `claim_status: none`, Bitcoin and photosynthesis excluded,
  and every cross-case statement it makes is disconfirming (non-composition,
  fragmentation, witness heterogeneity) rather than a shared-structure claim.
  Its strongest content is the case against the atlas: continuity witnesses are
  heterogeneous across its thirteen cases (provenance in CRISPR, constraint in
  SI and Hamming, entitlement in Torrens and Fedwire, causal dependence in lac,
  quorum sensing, TCP, and LTEE citrate), and imports may carry the explanatory
  load, making "transduction" possibly just a name for cases where someone else
  already paid the setup cost.
- The document's provenance is unusable as delivered. Its 151 citation anchors
  are Unicode Private Use Area tokens (U+E200-U+E202) from the research agent's
  internal citation system, never resolved into references; the file contains
  zero URLs, zero DOIs, and zero links. The charter's Provenance gate requires
  material claims to trace to primary domain evidence, so nothing here may
  populate a packet field or support a gate verdict. The named sources are real
  and hand-checkable, so the work is recoverable by resolving each to a citable
  reference and re-grading the claim it supports.
- Recorded a contamination warning in the document itself. Rayleigh-Benard
  convection is CL-001's near-miss Null B under today's Matched Nulls amendment,
  and this document argues Rayleigh-Benard fails. A Lane 1 run scoring that
  control with this file in view would score it against a standard derived from
  the intuition CL-001 exists to check. The Lane 3 discovery pass predicted this
  closed-loop channel; it arrived within hours, and by our own hand: the charter
  named Rayleigh-Benard before this document existed. Score it from sources.
- Noted that the document's nulls are self-described as "deliberate failures",
  i.e. selected as failures, which is the selection-time stipulation the charter
  now forbids for near-miss nulls. Two are exceptions: the Belgian cadastral map
  (law explicitly denies the maintained record boundary force, a sourced fact)
  and quorum sensing under strong flow (the same system, positive under
  quiescent conditions and null under flow via autoinducer washout, which is a
  controlled intervention on one variable). Quorum-sensing-under-flow is the
  best-shaped near-miss null surfaced so far and is a candidate to replace
  Rayleigh-Benard as Null B.
- Ran CL-001 C-field kind probe (`explorations/2026-07-16-c-field-kind-probe.md`).
  Two agents derived `C` independently, each reading only its own target's
  dossiers, blinded to the other target, to each other, and to the probe author's
  preregistered prediction. Blinding was deliberate: the author had publicly
  predicted an outcome and would otherwise have scored it.
- The prediction failed. It held that `C` would come back kind-heterogeneous
  (Bitcoin a threshold certificate over a counterfactual, photosynthesis physical
  transport) and that CL-001 would die at the continuity gate. Both parts were
  wrong. The candidate kinds converge rather than diverge: Bitcoin as provenance
  with secondary constraint, photosynthesis as constraint with causal dependence
  as runner-up. And the comparison could not run at all, because `C` is OPEN on
  both targets. The prediction presumed a determinable field on both sides; that
  presumption is what the evidence refuses.
- Both derivations converged on two blockers neither was prompted toward. First,
  no witness spans the transduction: Bitcoin's protocol sources do not quantify
  energy, so only one endpoint is typed; photosynthesis's mechanism dossier
  disclaims carbon fixation and biomass while the agency dossier supplies no
  positive `C` candidate, so the two sides do not touch. Second, covariance is
  unstated for both, which the charter makes mandatory and which is independently
  sufficient to hold the field OPEN.
- The probe's real finding is about `R0`, not `C`. `C`'s determinability depends
  on an analyst-chosen regime boundary, and the choice that makes `C`
  determinable is the choice that makes the case trivial. Narrow `R0` to the
  computational regime and Bitcoin's `C` is determinable as provenance in hash
  units, but the transduction becomes hashing to record-of-hashing, which is the
  hash-without-surface null. Narrow photosynthesis to the water-oxidation
  boundary and the Kok constraint spans it, but the packet becomes much narrower
  and owes an account of why that boundary is the interesting one. Nothing in the
  packet, interface, or charter individuates `R0`. The analyst picks and the pick
  decides the answer.
- `C` remains "Open pending primary-source pass" on both packets. No field was
  populated, no gate scored, no verdict implied. Recorded as leads only, carrying
  no weight: the unprovenanced Lane 2 audit's report that `X` collapses because
  `K0` is analyst-chosen, and the unprovenanced Lane 3 material's report that
  many cases are regime-plus-boundary-dependent judgments rather than
  object-level transductions. If those were ever established, three independent
  derivations over disjoint corpora would agree the boundary choice does the
  work. That is a hypothesis about the CLTP, not a result.
- Ran R0 individuation probe (bar preregistered at `c05676f`; result in
  `explorations/2026-07-16-r0-individuation-RESULT.md`). The bar was written and
  committed before any candidate was generated, because the author's C-PROBE-01
  prediction had just been refuted for presuming its own frame. Three agents
  worked independently, none shown the bar, so candidates were built to be strong
  rather than to pass.
- Result: NO ADMISSIBLE RULE. Both constructors killed their own rules unprompted,
  failing conditions they were never shown. The type-fault rule fails scope
  circularity: its inputs are dossier-given, and each dossier's Source Boundary is
  itself an R0 choice, so the rule relocates the analyst's choice upstream and
  returns it as a domain-derived discovery. The mechanism rule passes
  non-circularity on the named fields, and that is what kills it: its output is
  computed entirely from the typed register, so R0 carries no information not
  already in M0/M1. It also fails neutrality, favouring literatures that type by
  ontology over literatures that type by data format, and would report
  "photosynthesis crosses regimes, Bitcoin does not" as a fact about the world
  rather than about two house styles.
- The scoped claim: no AUTONOMOUS R0 rule is charter-admissible, by relocation
  rather than elimination. Every candidate has a non-empty presupposition set, so
  every candidate is a function on packets rather than cases; it constrains the
  packet and cannot ground it. Two charter-internal amplifiers: the transduction
  definition is teleological ("through which downstream action becomes possible"),
  so R0 <- T <- Omega and the source regime is fixed by the agency already
  credited; and the invariance test is K0-indexed while K0 is indexed to R0, so
  the repository contains no apparatus capable of validating an R0 rule.
- The author's second prediction of the day was refuted. Preregistered outcome 3
  read: no admissible rule means the regime boundary is free and the instrument
  cannot discriminate, a KILL on the instrument. The first clause holds; the
  second does not follow. R0 is a gauge choice. Verdicts are gauge-dependent, but
  discrimination is a difference between two packets, and a difference can be
  computed in a fixed gauge without the gauge being canonical. A declared-boundary
  packet can discriminate a target from its matched null if and only if the null
  is evaluated at the same declared boundary. Absolute individuation is dead;
  relative individuation survives and is stronger than what the repo had.
- Live defect: the charter's null-matching criterion, including today's own
  Matched Nulls amendment, never mentions R0 matching. "Matched" currently means
  matched-in-subject-matter, not matched-in-frame. Neither current branch
  discriminates: at the computational R0 the Bitcoin target and its null nearly
  coincide; at the participant R0 the hash null has no counterpart R0 and the
  packets are incommensurable rather than comparable.
- The amendment's near-miss nulls are right for a reason the amendment failed to
  state: testnet/regtest shares mainnet's R0, K0, S0, M0, T, and B and differs
  only in economic R1. R0's arbitrariness is neutralized by pairing, not by
  individuation; the free parameter becomes a shared parameter and the gate
  difference becomes evidence. This is an independent reason floor nulls carry
  zero weight: they cannot be populated at their target's frame at all. Technical
  correction on the record: testnet3's difficulty rules differ from mainnet's, so
  regtest is the cleaner frame-match; the amendment named both without
  distinguishing them.
- Proposed and NOT enacted, each requiring Joe's authorization: R0-matching as a
  null-admissibility condition; regtest over testnet3 as near-miss Null A; and a
  frame sweep, a test the repo does not have, in which a discriminator must be
  shown robust across the R0 dial rather than merely to exist at one setting. If
  the pass/fail pattern inverts anywhere in the sweep, the discriminator is a
  frame artifact. What would be fatal: no frame at which a target passes and its
  frame-matched near-miss null fails. Untested, because CL-001 has never held a
  frame fixed across a target/null pair.
- PROVENANCE DEFECT in the evidence layer, verified, independent of any rule. The
  dossiers' "Non-comparable with" column is repo-authored, not source-derived, and
  sits inside a section whose surrounding discipline signals extraction. Proof:
  `photosynthesis-agency-surface.md:64` sources Net primary production to Field et
  al. (Science 1998) and declares it non-comparable with "Bitcoin chainwork";
  `photosynthesis-mechanism.md:63` does the same for photon absorption. Bitcoin's
  whitepaper is 2008; a 1998 paper did not name Bitcoin chainwork. The cause is
  structural: the template's table is Quantity / Type or unit / Source context /
  Non-comparable with, where "Source context" carries provenance for the quantity
  and the non-comparability column has no attribution column or requirement. The
  graph therefore encodes CL-001's comparison rather than photosynthesis's type
  structure, written by an agent that already knew which cases the charter paired.
  Proposed, not enacted: require source attribution per declaration, or rename the
  column to mark it repo-authored analysis. Both are contract changes affecting six
  dossiers.
