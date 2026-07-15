# WI-069 Measurement-Transition Example Harvest

Status: exploratory example harvest
Date: 2026-07-12
Work Card: WI-069

## Purpose

This pass looks for examples that fit Joe's reframe:

> Emergence or collapse is not itself the new accounting. It transitions to a different class-relative measurement set.

The goal is to find cases where a system's apparent emergence, collapse, resilience, or failure is best understood as a transition from one measurement regime to another.

## Measurement-Transition Lens

A measurement regime is provisionally:

```text
R = (K, M, A, E, C, F)
```

where:

- `K` = model/system class;
- `M` = observables, metrics, readouts, measurements;
- `A` = admissibility rules;
- `E` = equivalences and quotients;
- `C` = completion/finality rules;
- `F` = absorber/factorization family.

The examples below ask:

```text
R_old -> R_new

What becomes measurable?
What stops being measurable?
What old comparison breaks?
What new admissibility rule appears?
Is the transition emergent, corrective, captured, or collapsing?
```

## Example 1: Recursive AI Model Collapse

Source regime:

`R_old`: model quality measured against an independent real-data distribution.

Target regime:

`R_new`: model quality measured against data increasingly produced by prior models.

Transition:

Independent-source measurement becomes self-output measurement.

What changes:

- Lost measurement: real distribution tails and provenance.
- Gained measurement: apparent internal consistency of model-generated samples.
- Broken comparison: "looks plausible" no longer implies "preserves source distribution."
- Boundary import: independent data source.
- Collapse mode: recursive source collapse.

Why it fits:

The collapse is not merely bad performance. It is a transition to a measurement set that treats generated output as source-equivalent and therefore cannot see the lost tail mass.

Representative sources:

- Nature, "AI models collapse when trained on recursively generated data": https://www.nature.com/articles/s41586-024-07566-y
- arXiv, "The Curse of Recursion": https://arxiv.org/abs/2305.17493

## Example 2: ML Benchmark Saturation To Robustness / OOD Evaluation

Source regime:

`R_old`: leaderboard accuracy on a fixed or saturated benchmark.

Target regime:

`R_new`: robustness, OOD shift, adversarial robustness, temporal shift, subpopulation shift, or failure-detection evaluation.

Transition:

From in-distribution performance measurement to distribution-shift-sensitive measurement.

What changes:

- Lost measurement: discriminative power among top models on saturated tests.
- Gained measurement: robustness under nuisance shifts, semantic shifts, corruption, or adversarial perturbation.
- Broken comparison: two models tied on standard accuracy may differ sharply under shift.
- Boundary import: new test distributions and threat models.
- Emergence/collapse reading: capability may be real but invisible under `R_old`, or apparent capability collapses under `R_new`.

Why it fits:

This is a clean "measurement class transition" example: the object measured as "good model" changes when benchmark saturation or deployment shift invalidates the old measurement set.

Representative sources:

- RobustBench: https://arxiv.org/abs/2010.09670
- WILDS benchmark: https://proceedings.mlr.press/v139/koh21a/koh21a.pdf
- Benchmark saturation study: https://arxiv.org/html/2602.16763v1

## Example 3: Datasheets And Model Cards

Source regime:

`R_old`: model or dataset judged by performance score, size, or benchmark result.

Target regime:

`R_new`: model/dataset judged with provenance, intended use, composition, evaluation details, limitations, and ethical context.

Transition:

From scalar result measurement to contextual accountability measurement.

What changes:

- Lost measurement: simplicity of single-score comparison.
- Gained measurement: source context, intended use, data-generation conditions, limits.
- Broken comparison: two datasets with similar task utility may differ in provenance, representativeness, or permissible use.
- Boundary import: documentation practices and governance norms.
- Emergence/collapse reading: apparent model capability can collapse when its data regime is made visible.

Why it fits:

The system did not just add metadata. It transitioned from "output performance" to "performance under declared data/model conditions."

Representative sources:

- Datasheets for Datasets: https://arxiv.org/abs/1803.09010
- Model Cards for Model Reporting: https://dl.acm.org/doi/10.1145/3287560.3287596

## Example 4: Sepsis-3 Definition Shift

Source regime:

`R_old`: sepsis measured largely through infection plus systemic inflammatory response criteria.

Target regime:

`R_new`: sepsis measured as life-threatening organ dysfunction caused by dysregulated host response to infection, operationalized through SOFA/qSOFA-related tools.

Transition:

From inflammation/sign criteria toward organ-dysfunction and risk/outcome measurement.

What changes:

- Lost measurement: broad sensitivity of older inflammatory criteria.
- Gained measurement: organ dysfunction and mortality-risk emphasis.
- Broken comparison: cases classified under older criteria may not align cleanly with the new definition.
- Boundary import: clinical outcome evidence and consensus process.
- Emergence/collapse reading: a patient state becomes newly legible as dysregulated host-response failure, not merely infection plus inflammation.

Why it fits:

The disease category itself changes measurement regime. The shift is not just a better score; it changes what counts as the thing being measured.

Representative sources:

- JAMA Sepsis-3 consensus definitions: https://jamanetwork.com/journals/jama/fullarticle/2492881
- PubMed record: https://pubmed.ncbi.nlm.nih.gov/26903338/

## Example 5: Homeostasis To Allostasis / Allostatic Load

Source regime:

`R_old`: stability measured by return to a normal set point.

Target regime:

`R_new`: stability measured by adaptive regulation through change, including load, recovery capacity, and chronic stress burden.

Transition:

From current-state correction to history-sensitive adaptive-capacity measurement.

What changes:

- Lost measurement: simple "back to normal" interpretation.
- Gained measurement: adaptive debt, stress load, recovery reserve.
- Broken comparison: two organisms can show similar current readings but different load histories and collapse risk.
- Boundary import: environmental stressors, social support, treatment, rest.
- Collapse mode: overload hidden by local compensation.

Why it fits:

Collapse may occur when the measurement regime treats compensation as health while the target regime would reveal depleted recovery capacity.

Representative sources:

- McEwen, allostasis and allostatic load: https://pubmed.ncbi.nlm.nih.gov/9629234/
- Clarifying homeostasis/allostasis: https://pmc.ncbi.nlm.nih.gov/articles/PMC4166604/

## Example 6: CVSS To EPSS / Exploit-Likelihood Security Triage

Source regime:

`R_old`: vulnerability priority measured by static severity scoring.

Target regime:

`R_new`: vulnerability priority measured by near-term exploit probability, known exploitation, asset context, or decision support.

Transition:

From severity-class measurement to threat-activity and remediation-priority measurement.

What changes:

- Lost measurement: severity as sufficient priority.
- Gained measurement: exploit likelihood over a time window and operational threat context.
- Broken comparison: high severity does not necessarily mean likely exploitation soon.
- Boundary import: observed exploit data, threat intelligence, asset exposure.
- Emergence/collapse reading: security capacity improves when the measurement class changes from "how bad could it be?" to "what is likely to be exploited under current conditions?"

Why it fits:

The operational class changes. The target is not vulnerability severity in the abstract but triage under scarce remediation capacity.

Representative sources:

- FIRST EPSS: https://www.first.org/epss/
- NIST proposed exploit-likelihood metric: https://nvlpubs.nist.gov/nistpubs/cswp/nist.cswp.41.pdf

## Example 7: CALM / Monotonicity In Distributed Systems

Source regime:

`R_old`: consistency assessed as a systems-level coordination or consensus problem.

Target regime:

`R_new`: consistency assessed by the logical monotonicity class of the program.

Transition:

From runtime coordination measurement to program-class measurement.

What changes:

- Lost measurement: implementation-only diagnosis.
- Gained measurement: class frontier separating coordination-free from coordination-required computation.
- Broken comparison: two distributed tasks may look similar operationally but differ by monotonicity.
- Boundary import: logic semantics and consistency specification.
- Emergence/collapse reading: the "impossibility wall" becomes a class-relative measurement boundary.

Why it fits:

The new measurement set changes what is being evaluated: not just whether the distributed system works, but which logical class the program inhabits.

Representative source:

- CALM theorem paper: https://arxiv.org/abs/1901.01930

## Example 8: I-Confluence / Coordination Avoidance

Source regime:

`R_old`: global correctness measured by serializability or universal coordination.

Target regime:

`R_new`: correctness measured by whether independent local transactions preserve application invariants.

Transition:

From one-size consistency measurement to invariant-specific coordination need.

What changes:

- Lost measurement: global coordination as default safety proxy.
- Gained measurement: whether a particular invariant is preserved under merge.
- Broken comparison: all conflicts are not equal; only invariant-breaking conflicts require coordination.
- Boundary import: application-level invariant specification.
- Emergence/collapse reading: unnecessary coordination is a productive-capacity collapse if it serializes work that could safely proceed.

Why it fits:

The measurement transition changes the class of "valid distributed progress."

Representative source:

- Coordination Avoidance in Database Systems: https://arxiv.org/abs/1402.2237

## Example 9: Language Archive To Language Vitality

Source regime:

`R_old`: language preservation measured by records: grammars, dictionaries, recordings, texts.

Target regime:

`R_new`: language vitality measured by intergenerational transmission, use domains, speaker community, attitudes, and institutional support.

Transition:

From record-completion measurement to living-source measurement.

What changes:

- Lost measurement: archive completeness as survival.
- Gained measurement: transmission, community legitimacy, everyday use.
- Broken comparison: a well-documented language may be source-collapsed.
- Boundary import: community practice, teaching, legitimacy, use contexts.
- Collapse mode: finality/readout preservation with source collapse.

Why it fits:

This is one of the cleanest cases where the target measurement set changes from completed record to generative capacity.

Representative source:

- UNESCO Language Vitality and Endangerment: https://ich.unesco.org/doc/src/00120-EN.pdf

## Example 10: Journal Impact Factor To Responsible Research Assessment

Source regime:

`R_old`: research quality inferred from journal-level metrics such as impact factor.

Target regime:

`R_new`: research assessment uses article-level quality, diverse outputs, context, qualitative judgment, openness, reproducibility, contribution type, and field-specific norms.

Transition:

From proxy metric to plural assessment regime.

What changes:

- Lost measurement: single proxy convenience.
- Gained measurement: richer research contribution profile.
- Broken comparison: journal venue cannot validly substitute for article or researcher merit.
- Boundary import: disciplinary judgment and assessment governance.
- Collapse mode: metric capture and Goodharted research behavior.

Why it fits:

The transition is explicitly about changing the measurement set because the old one collapses under institutional targeting.

Representative source:

- DORA declaration: https://sfdora.org/read/

## Example 11: Goodhart / Campbell / Lucas Metric Capture

Source regime:

`R_old`: measure used as an observational proxy.

Target regime:

`R_new`: measure used as control target, incentive, or policy lever.

Transition:

From passive measurement to active intervention measurement.

What changes:

- Lost measurement: statistical regularity under non-targeted conditions.
- Gained measurement: controllable target.
- Broken comparison: pre-policy correlation no longer predicts post-policy behavior.
- Boundary import: agent adaptation and incentives.
- Collapse mode: metric capture.

Why it fits:

This may be the general measurement-transition archetype: the moment a measure becomes a target, it changes class.

Representative sources:

- Goodhart overview with original formulation pointer: https://en.wikipedia.org/wiki/Goodhart%27s_law
- Metric manipulation discussion: https://pmc.ncbi.nlm.nih.gov/articles/PMC7901608/

## Example 12: Financial VaR To Stress Testing / Macroprudential Risk

Source regime:

`R_old`: risk measured by value-at-risk, historical loss distribution, institution-level exposure, or normal-market statistical risk.

Target regime:

`R_new`: risk measured by stress scenarios, macro-financial linkages, systemic contagion, liquidity, and severe-but-plausible adverse conditions.

Transition:

From distributional loss quantile to scenario/system measurement.

What changes:

- Lost measurement: normal-condition precision.
- Gained measurement: system resilience under adverse macro-financial conditions.
- Broken comparison: low VaR does not imply systemic resilience.
- Boundary import: macroeconomic scenarios, interbank linkages, supervisory judgment.
- Collapse mode: local risk measures fail globally.

Why it fits:

The measurement class changes from institution-local statistical risk to system-level stress under coupled scenarios.

Representative sources:

- ECB macro stress testing framework: https://www.ecb.europa.eu/pub/pdf/scpops/ecbocp152.pdf
- IMF stress testing principles/practices: https://www.elibrary.imf.org/display/book/9781484310717/ch002.xml

## Example 13: Lean Supply-Chain Efficiency To Viability

Source regime:

`R_old`: supply-chain health measured by cost, efficiency, utilization, inventory minimization, normal-time service levels.

Target regime:

`R_new`: supply-chain health measured by viability, survivability, resilience, reconfigurability, and long-term provision under disruption.

Transition:

From nominal efficiency measurement to open-system survivability measurement.

What changes:

- Lost measurement: treating slack as waste.
- Gained measurement: adaptive capacity, viable ecosystem, disruption-response balance.
- Broken comparison: the most efficient chain may be least viable.
- Boundary import: alternate suppliers, public infrastructure, geopolitical conditions, reserve capacity.
- Collapse mode: efficiency optimization destroys collapse margin.

Why it fits:

The same network changes class when measured as a viability-preserving ecosystem rather than an optimized flow.

Representative sources:

- Supply chain viability theory: https://www.tandfonline.com/doi/full/10.1080/00207543.2023.2177049
- Viable supply chain model: https://link.springer.com/article/10.1007/s10479-020-03640-6

## Example 14: Species Richness To Functional Diversity / Redundancy

Source regime:

`R_old`: biodiversity measured by species count or taxonomic diversity.

Target regime:

`R_new`: biodiversity measured by functional traits, functional diversity, redundancy, and ecosystem roles.

Transition:

From object-count measurement to function-space measurement.

What changes:

- Lost measurement: simple richness comparison.
- Gained measurement: what species do, whether roles are redundant, and how ecosystem function is preserved.
- Broken comparison: two systems with equal richness may differ in functional resilience.
- Boundary import: trait data and ecosystem-function models.
- Collapse/emergence reading: a community may appear intact by count while functionally collapsed, or functionally resilient despite taxonomic loss.

Why it fits:

The measurement set moves from entities to roles/capabilities.

Representative sources:

- Functional diversity review: https://arxiv.org/html/2506.17839v1
- Functional diversity metrics under aridity gradients: https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2022.923219/full

## Example 15: Ecological State Metrics To Early-Warning Signals

Source regime:

`R_old`: ecosystem stability measured by current state variables and apparent equilibrium.

Target regime:

`R_new`: ecosystem collapse risk measured by recovery rate, autocorrelation, variance, critical slowing down, and basin proximity.

Transition:

From current-state measurement to transition-risk measurement.

What changes:

- Lost measurement: state value as sufficient stability evidence.
- Gained measurement: proximity to bifurcation or regime shift.
- Broken comparison: two ecosystems can have similar current states but different recovery dynamics.
- Boundary import: time-series dynamics and perturbation response.
- Collapse mode: local stability masks global threshold approach.

Why it fits:

Collapse is only visible after moving to a measurement class that tracks dynamical resilience rather than state value.

Representative source:

- Scheffer et al., early warning signals: https://pdodds.w3.uvm.edu/files/papers/others/2009/scheffer2009a.pdf

## Example 16: Planetary Boundaries

Source regime:

`R_old`: environmental issues measured as separate sectoral indicators: carbon, land use, biodiversity, nitrogen, freshwater, etc.

Target regime:

`R_new`: Earth-system stability measured by interacting control variables and safe operating spaces.

Transition:

From issue-specific measurement to coupled boundary measurement.

What changes:

- Lost measurement: isolated policy-silo evaluation.
- Gained measurement: systemic safe-operating-space assessment.
- Broken comparison: staying inside one sector's target may not imply planetary stability.
- Boundary import: Earth-system science and uncertainty thresholds.
- Collapse mode: local compliance with global-boundary transgression.

Why it fits:

This is a direct measurement-regime transition from local environmental metrics to global system-boundary accounting.

Representative sources:

- Stockholm Resilience Centre planetary boundaries overview: https://www.stockholmresilience.org/research/planetary-boundaries.html
- Science Advances 2023 update: https://www.science.org/doi/10.1126/sciadv.adh2458

## Example 17: GDP To Well-Being / Beyond-GDP Frameworks

Source regime:

`R_old`: progress measured primarily by GDP or economic output.

Target regime:

`R_new`: progress measured by multidimensional well-being, inclusion, sustainability, distribution, resilience, and future outcomes.

Transition:

From production-output measurement to multidimensional social outcome measurement.

What changes:

- Lost measurement: single aggregate output as progress proxy.
- Gained measurement: welfare, distribution, future capacity, non-market dimensions.
- Broken comparison: GDP growth can coexist with declining well-being or resilience.
- Boundary import: normative social choice and multidimensional statistics.
- Collapse mode: economic growth measurement captures policy attention while hiding social/ecological degradation.

Why it fits:

The public system transitions from one class of value measurement to another, and the transition changes what policy can see.

Representative source:

- OECD Well-being and Beyond GDP: https://www.oecd.org/en/topics/policy-issues/well-being-and-beyond-gdp.html

## Example 18: Policing CompStat / Metrics Management

Source regime:

`R_old`: crime reduction and police management measured through reported crime statistics and performance meetings.

Target/captured regime:

`R_new`: measured crime statistics become managerial targets.

Transition:

From situational crime analysis to metric-managed accountability system.

What changes:

- Lost measurement: crime data as neutral situational awareness.
- Gained measurement: command-accountability and performance comparison.
- Broken comparison: reported crime trends may reflect reporting, classification, or enforcement incentives.
- Boundary import: bureaucratic incentives and street-level discretion.
- Collapse mode: metric capture or data manipulation.

Why it fits:

This is a Goodhart-class transition: a measurement set changes when it becomes an accountability/control regime.

Representative sources:

- Bureau of Justice Assistance CompStat report: https://bja.ojp.gov/sites/g/files/xyckuh186/files/Publications/PERF-Compstat.pdf
- Metrics management and bureaucratic accountability: https://ncdoj.gov/wp-content/uploads/2023/12/b323fb_bb54c8389f0144f98562896e2ddf8bd2.pdf

## Example 19: Commons Governance Rules-In-Use

Source regime:

`R_old`: resource governance measured by formal property type: state, private, or open access.

Target regime:

`R_new`: governance measured by rules-in-use, boundaries, monitoring, sanctions, conflict resolution, local rule fit, and nested institutions.

Transition:

From ownership-class measurement to institutional-process measurement.

What changes:

- Lost measurement: formal ownership as sufficient classification.
- Gained measurement: legitimacy, participation, enforcement fit, local ecological feedback.
- Broken comparison: two commons with similar legal forms may have different durability.
- Boundary import: local knowledge and shared-process legitimacy.
- Emergence/collapse reading: durable governance emerges through legitimate measurement of rule process, not through ownership class alone.

Why it fits:

The measurement set moves from static legal category to dynamic institutional capacity.

Representative source:

- Ostrom design principles summary: https://ostromworkshop.indiana.edu/courses-teaching/teaching-tools/ostrom-design/index.html

## Example 20: Time As Finality-Style Projection Obstruction

Source regime:

`R_old`: local projection/readout or endpoint measurement appears sufficient.

Target regime:

`R_new`: admissibility measured by whether local projections compose through a valid chain, span, or descent condition.

Transition:

From endpoint/readout measurement to path/transport/compatibility measurement.

What changes:

- Lost measurement: endpoint equivalence as sufficient.
- Gained measurement: compatibility of intermediate transitions.
- Broken comparison: two endpoints can match while their generating paths differ.
- Boundary import: admissibility condition for projection/transport.
- Collapse mode: observer-side finality hides source/process distinctions.

Why it fits:

This is the local repo analogue of the external measurement-transition frame. Collapse occurs when finality changes the measurement set in a way that erases process compatibility.

Representative local anchors:

- `time-as-finality/models/projection_obstruction_schema.py`
- `time-as-finality/models/po1_chained_projection.py`
- `time-as-finality/results/associated-sheaf-finality-witness-v0.1-results.md`

## Example 21: Temporal Issuance Source/Readout Split

Source regime:

`R_old`: novelty measured by observer readout, naming, access schedule, finite prefix, or finality.

Target regime:

`R_new`: novelty measured by source-side generation of a rule/witness/action not precontained in the operative completion class.

Transition:

From observer-novelty measurement to source-noncompletion measurement.

What changes:

- Lost measurement: observer surprise as sufficient.
- Gained measurement: source-side noncompletion witness or admissibility generation.
- Broken comparison: new-to-observer does not imply source emergence.
- Boundary import: source model, OSAG-like structure, class-relative completion family.
- Emergence reading: genuine issuance becomes a measurement-regime transition, not a raw event.

Why it fits:

This reinterprets Temporal Issuance as a source-regime measurement discipline rather than merely a novelty theory.

Representative local anchors:

- `temporal-issuance/FORMAL-OBJECT.md`
- `temporal-issuance/FORMAL-DEFINITION-REPAIR.md`
- `temporal-issuance/explorations/E087-online-issuance-formal-object-v0-1-2026-06-25.md`

## Example 22: GU Six-Axis Protocol

Source regime:

`R_old`: speculative bridge measured by verbal analogy or partial formal resemblance.

Target regime:

`R_new`: bridge measured across substrate, observer, pairing/interface, causal order, emergence, coordination, and positivity/state-space obligations.

Transition:

From analogy measurement to axis-specified obligation measurement.

What changes:

- Lost measurement: resemblance as sufficient.
- Gained measurement: axis-by-axis class-relative claim discipline.
- Broken comparison: two theories can share language while failing on substrate, observer, pairing, or order.
- Boundary import: exact mathematical interface and no-go/escape map.
- Collapse mode: bridge collapses into smuggled structure or unearned equivalence.

Why it fits:

The six-axis protocol is already a measurement-regime transition for speculative claims.

Representative local anchors:

- `gu-formalization/canon/six-axis-specification-protocol.md`
- `gu-formalization/canon/no-go-class-relative-map.md`
- `gu-formalization/lab/specifications/six-axis/six-axis-template.md`

## Pattern Table

| Pattern | Examples | Measurement Transition |
|---|---|---|
| Source replacement | Model collapse, language archive | Independent/living source -> self-output or record |
| Saturation escape | ML benchmarks, DORA | Old score loses discrimination -> richer measurement set |
| Target capture | Goodhart, CompStat, research metrics | Measure-as-observer -> measure-as-control |
| Class frontier | CALM, I-confluence, GU no-go maps | Operational success -> class-relative possibility |
| Dynamic capacity | Allostasis, ecological early warnings, supply-chain viability | Current state -> recovery/adaptation capacity |
| System coupling | Planetary boundaries, financial stress tests | Local metric -> coupled-system risk |
| Role/function shift | Functional diversity, commons governance | Object count/legal form -> function/process capacity |
| Source/readout split | Temporal Issuance, Time as Finality | Observer record -> source/process admissibility |

## Strongest Examples For The Next Paired-Contrast Run

### Pair 1: Model Collapse vs Language Vitality

Question:

When does a system mistake record/self-output for living independent source?

Expected payoff:

Sharp source-preservation test.

### Pair 2: Benchmark Saturation vs DORA

Question:

When does a score stop measuring excellence because the field adapted to the score?

Expected payoff:

Measurement-saturation and metric-capture classifier.

### Pair 3: Sepsis-3 vs Allostasis

Question:

When does clinical state measurement need to shift from symptom/set-point to dysfunction, load, and recovery capacity?

Expected payoff:

Capacity measurement under dynamic regulation.

### Pair 4: CVSS/EPSS vs Supply-Chain Viability

Question:

When does operational priority shift from static severity/efficiency to likelihood, exposure, viability, and actionability?

Expected payoff:

Action-oriented measurement-regime transition.

### Pair 5: CALM/I-Confluence vs Ostrom Governance

Question:

Can formal coordination frontiers and social legitimacy frontiers share a measurement-transition grammar?

Expected payoff:

Bridge between formal no-go accounting and institutional admissibility.

### Pair 6: Functional Diversity vs Planetary Boundaries

Question:

When does object-count measurement fail because the system property lives in function space or coupled safe-operating space?

Expected payoff:

Measurement transition from entity metrics to system-capacity metrics.

## Hypothesis Suggested By The Harvest

### H-MT-1: Measurement-Regime Transition Hypothesis

Many apparent cases of emergence or collapse are better classified as transitions between class-relative measurement regimes.

Emergence occurs when `R_new` legitimately gains measurements or admissibility predicates that cannot be factored through `R_old`'s completion family.

Collapse occurs when `R_new` absorbs, coarsens, captures, starves, or finalizes away the measurements needed to preserve generativity, source contact, resilience, legitimacy, or distinguishability.

### H-MT-2: Measurement Legitimacy Burden

Every transition `R_old -> R_new` carries a legitimacy burden:

- Why is `R_new` valid for the system?
- Who or what supplies the new measurement set?
- What old comparisons become invalid?
- What is preserved across the transition?
- What is lost, and is that loss productive abstraction or collapse?

### H-MT-3: Saturation/Capture Split

There are at least two different reasons a measurement regime fails:

- saturation: it loses discriminative power because progress outgrows the scale;
- capture: it loses validity because agents optimize against it.

Both require transition to a new regime, but they are not the same phenomenon.

## Provisional Verdict

This harvest strengthens the measurement-transition reframe.

The most general recurring shape is:

```text
R_old works locally or historically
  -> system adapts, scales, globalizes, saturates, or is targeted
  -> R_old loses validity or discriminative power
  -> R_new becomes necessary
  -> the transition is emergent, corrective, captured, or collapsing depending on
     what R_new preserves, loses, imports, and makes newly admissible
```

This suggests the next pre-repo experiment should be a paired-contrast test of measurement-regime transitions, not just obstruction/collapse packets.
