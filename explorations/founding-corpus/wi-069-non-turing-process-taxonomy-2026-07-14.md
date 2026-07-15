# WI-069 Non-Turing Process Taxonomy

Status: exploratory correction / taxonomy note
Date: 2026-07-14
Work Card: WI-069

## Joe's Reframe

Joe's point:

> A hypercomputer is one example of a non-Turing machine: something that can decide problems a Turing machine cannot, such as halting-problem-style tasks. But there are many other ways systems are not captured by the strict universal-Turing-machine frame. Stochastic systems, continuous systems, and especially material-substrate processes like metabolism do not have to be reducible to mapping numbers to numbers. Metabolism transforms actual substances. That may be trivial in one sense, but it matters for classes of machines or systems.

This is important for WI-069 because recursive incentive transduction and catalytic transduction may often be "non-Turing" in the material/process sense, not the hypercomputation sense.

## Core Distinction

Do not collapse all "non-Turing" claims into hypercomputation.

There are at least two very different questions:

```text
1. Can the system compute a function no Turing machine can compute?
2. Is the system's important operation not well described as discrete symbolic function computation?
```

Hypercomputation addresses question 1.

Metabolism, photosynthesis, proof-of-work energy expenditure, immune response, markets, and governance often matter because of question 2.

## Taxonomy Of Non-Turing Senses

### 1. Hypercomputational Non-Turing

Claim:

The system decides or computes something outside Turing-computable functions.

Examples:

- halting-problem oracle;
- accelerating Turing machine;
- infinite-time computation;
- exact-real computation with noncomputable reals;
- other oracle-based models.

Key test:

Does it solve a non-recursive decision problem?

WI-069 relevance:

Usually not the central target. This is the strongest formal sense of non-Turing, but it is probably not what makes metabolism, photosynthesis, or Bitcoin important.

### 2. Super-Turing Efficiency Or Architecture

Claim:

The system may not compute uncomputable functions, but it differs from standard Turing-machine framing through parallelism, interactivity, embodiment, quantum speedups, probabilistic algorithms, or online operation.

Examples:

- quantum algorithms;
- massive parallelism;
- interactive computation;
- distributed systems;
- online learning agents;
- cyberphysical systems.

Key test:

Does the system change computational class, complexity, interaction pattern, or architecture while remaining within computable-function bounds?

WI-069 relevance:

Useful for agentic and distributed examples, but not enough for material transduction.

### 3. Stochastic Non-Turing

Claim:

The system depends on randomness, probability, noise, mutation, or sampling.

Important caveat:

Randomness alone does not automatically exceed Turing computation. Randomized Turing machines remain within the usual computability frame unless the randomness is treated as an oracle containing noncomputable information.

Examples:

- mutation and selection;
- stochastic optimization;
- probabilistic inference;
- thermal noise;
- random sampling.

Key test:

Is randomness merely a computational resource, or is it an uncomputable oracle / physical source whose material unpredictability matters?

WI-069 relevance:

Stochasticity often matters as source diversity or boundary import, not necessarily as hypercomputation.

### 4. Continuous / Analog Non-Turing

Claim:

The system evolves over continuous quantities, real-valued states, differential equations, fields, or analog dynamics.

Important caveat:

Continuity alone does not automatically imply hypercomputation. Computable analysis can model many continuous systems. Super-Turing claims usually require exact infinite precision, noncomputable initial data, or idealized dynamics.

Examples:

- analog circuits;
- fluid dynamics;
- continuous control systems;
- morphogenesis;
- differential-equation systems;
- field dynamics.

Key test:

Does the system rely on physically meaningful continuous dynamics that cannot be captured by the discrete model without losing the phenomenon, or does it require unrealistic exact real precision?

WI-069 relevance:

Important for substrate-dependent measurement regimes, but should be kept separate from halting-oracle claims.

### 5. Material-Transductive Non-Turing

Claim:

The system's central operation is not computing a function from symbols to symbols but transforming material, energy, or substrate.

Examples:

- metabolism transforms nutrients into ATP, biomass, heat, waste, repair;
- photosynthesis transforms light, water, and CO2 into chemical energy and biomass;
- nitrogen fixation transforms atmospheric nitrogen into biologically available compounds;
- proof-of-work transforms electricity and hardware depreciation into protocol-recognized costly work;
- manufacturing transforms raw material into artifacts;
- immune systems transform antigen exposure into clonal populations and memory.

Key test:

Would a purely symbolic simulation preserve the causal role of the material transformation, or only describe it?

WI-069 relevance:

This is central. Recursive incentive transduction often depends on material-transductive processes.

### 6. Constitutive-Substrate Non-Turing

Claim:

The particular material substrate is not incidental. It is constitutive of the function.

Examples:

- enzymes catalyzing reactions;
- membranes maintaining cellular identity;
- batteries storing electrochemical potential;
- photosynthetic pigments absorbing light;
- ASICs and energy markets in proof-of-work mining;
- soil microbial networks supporting fertility.

Key test:

Can the process be replaced by an abstract computation without losing what the system does?

WI-069 relevance:

This helps distinguish substrate-as-implementation from substrate-as-source.

### 7. Open / Interactive / World-Coupled Non-Turing

Claim:

The system is not a closed input-output function. It continuously exchanges matter, energy, information, incentives, or legitimacy with an environment.

Examples:

- markets;
- ecosystems;
- organisms;
- governance systems;
- supply chains;
- learning communities;
- AI agents using live tools or human feedback.

Key test:

Does the system's output change the future input distribution, measurement regime, or source boundary?

WI-069 relevance:

This is directly related to second- and third-order incentive effects.

### 8. Measurement-Regime-Transforming Non-Turing

Claim:

The system changes what counts as a valid measurement, comparison, admissible transition, or finality condition.

Examples:

- Bitcoin creates a protocol-native measurement of costly work and settlement;
- scientific paradigm shifts change what evidence counts;
- Sepsis-3 changes what the syndrome is measured as;
- DORA changes research assessment from journal proxy to contribution assessment;
- Temporal Issuance shifts novelty from observer surprise to source-side noncompletion.

Key test:

Does the process alter the class-relative measurement set itself?

WI-069 relevance:

This is the core measurement-transition frame.

## Where Metabolism Fits

Metabolism is not mainly interesting as hypercomputation.

It is interesting because it is:

- material-transductive;
- constitutive-substrate dependent;
- open/world-coupled;
- recursively capacity-generating.

Metabolism does not merely "map inputs to outputs."

It:

```text
transforms substances
maintains the organism
repairs structure
generates energy currency
supports future action
changes the organism's future state space
```

This makes it central to WI-069's recursive transduction theory.

## Where Bitcoin Fits

Bitcoin is not mainly interesting as hypercomputation either.

It is interesting because it is:

- material-transductive: electricity and hardware become protocol-recognized costly work;
- measurement-regime-transforming: proof-of-work creates a ledger-native measure of accumulated work;
- recursive-incentive-generating: monetary policy creates future mining, holding, infrastructure, and regulatory behavior;
- open/world-coupled: energy markets, hardware supply, regulation, exchanges, custody, and culture feed back into the system.

## Research Implication

WI-069 should stop treating "non-Turing" as one axis.

Future examples should classify which kind of non-Turing relation they involve:

```text
hypercomputational?
stochastic?
continuous/analog?
material-transductive?
constitutive-substrate?
open/world-coupled?
measurement-regime-transforming?
recursive-incentive-generating?
```

## Hypotheses

### NT-H1: Hypercomputation Is Not The Main Escape

Most important WI-069 examples are not non-Turing because they solve uncomputable functions. They are non-Turing because their central operation is material, open, transductive, or measurement-regime-transforming.

Falsification:

The strongest examples all reduce to formal hypercomputation or ordinary computable simulation without losing the phenomenon.

### NT-H2: Material Transduction Is A Distinct Class

Systems like metabolism, photosynthesis, and proof-of-work require a separate category because their function includes physical transformation, not merely symbolic representation.

Falsification:

Pure symbolic computation preserves every relevant causal and incentive role in the examples.

### NT-H3: Substrate-Relevance Test

A substrate is constitutive when replacing it with a symbolic simulation preserves description but not the system's role in its target regime.

Example:

A simulation of photosynthesis does not feed an ecosystem. A simulation of Bitcoin mining does not secure Bitcoin unless it participates in the real protocol with real resource expenditure.

Falsification:

No clear examples exist where symbolic description and substrate participation diverge.

### NT-H4: Measurement-Regime Transformation Is A Separate Escape

Some systems are "beyond Turing-machine framing" not because they compute more, but because they change the valid measurement/admissibility class.

Falsification:

Measurement-regime changes can always be reduced to ordinary fixed-class computation without losing the relevant emergence/collapse distinction.

## Recommended Vocabulary

Avoid using "non-Turing" alone.

Use more specific terms:

- `hypercomputational` for halting-problem/oracle-style claims;
- `stochastic` for randomness-dependent processes;
- `continuous/analog` for real-valued dynamics;
- `material-transductive` for substrate transformation;
- `constitutive-substrate` for processes where material participation matters;
- `open/world-coupled` for environment-changing systems;
- `measurement-regime-transforming` for systems that change what counts as measurable/admissible;
- `recursive-incentive-generating` for systems whose transduction drives second/third-order adaptive behavior.

## Provisional Verdict

This strengthens WI-069 by preventing a category error.

The new repo should not claim:

> These systems are non-Turing because they compute the halting problem.

It should claim, if warranted:

> Many open-ended systems are poorly captured by the closed universal-Turing-machine picture because their central operation is material transduction, world-coupled feedback, measurement-regime transformation, and recursive incentive generation rather than fixed input-output function computation.
