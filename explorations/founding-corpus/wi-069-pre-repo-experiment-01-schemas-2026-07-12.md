# Schemas

Status: v0 schemas
Date: 2026-07-12

## ObstructionTransitionPacket

```text
ObstructionTransitionPacket =
  (example_id,
   domain,
   local_data,
   local_validity,
   cover_or_context,
   compatibility_relation,
   attempted_globalization,
   obstruction,
   obstruction_visibility,
   class_K,
   no_go_statement,
   escape_move,
   imported_structure,
   residue,
   transition_type,
   first_test)
```

### Field Meanings

`local_data`

The local states, observations, rules, samples, agents, records, constraints, or behaviors.

`local_validity`

Why the local pieces look admissible or functional before closure is attempted.

`cover_or_context`

The contexts over which local data is distributed: nodes, observers, communities, generations, environments, regimes, markets, jurisdictions, cells, or time windows.

`compatibility_relation`

The relation required for local pieces to cohere.

`attempted_globalization`

The closure, completion, reconciliation, factorization, finality, consensus, or class-level model that tries to make the local pieces globally coherent.

`obstruction`

What blocks, distorts, or exposes the attempted globalization.

`obstruction_visibility`

Whether the obstruction is formal, measurable, empirical, institutional, semantic, or only inferred.

`class_K`

The class of systems or models within which the no-go or collapse claim is being assessed.

`no_go_statement`

The sharpest version of the impossibility or absorber claim.

`escape_move`

How the system exits, weakens, extends, or changes the class.

`imported_structure`

Any source, rule, data, legitimacy, energy, intervention, or observer structure supplied from outside the apparent loop.

`residue`

What survives the no-go or attempted closure and cannot be erased without losing the phenomenon.

`transition_type`

One or more of:

- local-compatible/global-obstructed;
- class no-go/class exit;
- obstruction relocation;
- absorbed obstruction;
- emergent obstruction;
- semantic obstruction;
- productive obstruction;
- terminal class kill;
- recursive source collapse;
- productive closure;
- terminal closure;
- captured closure.

`first_test`

The first theorem, executable fixture, case discriminator, or falsification test.

## BoundaryImportPacket

```text
BoundaryImportPacket =
  (example_id,
   apparent_loop,
   native_domain,
   imported_domain,
   imported_input,
   import_role,
   what_breaks_if_hidden,
   accounting_burden,
   legitimacy_of_import)
```

### Import Roles

- generation;
- diversity;
- admissibility;
- memory;
- provenance;
- intervention;
- energy;
- legitimacy;
- reconciliation;
- observer validation;
- measurement calibration;
- environmental coupling.

## Closure Classification

```text
ClosureClass =
  productive_closure | terminal_closure | captured_closure | closure_ambiguous
```

### Productive Closure

Closure that enables identity, memory, action, repair, reproduction, or legitimate coordination while preserving future generativity.

### Terminal Closure

Closure that exhausts future admissibility, variation, or source growth.

### Captured Closure

Closure that preserves a structure by losing legitimacy, plurality, source openness, or adaptive capacity.

### Closure Ambiguous

Closure whose effect depends on class choice or unresolved evidence.

## Completion-Factorization Test

Question:

> Does the process factor through one fixed completed object plus access, projection, naming, schedule, consensus, or finality maps?

```text
source transition -> fixed completion -> readout/finality/action
```

If yes, emergence is weakened or collapses relative to that class.

If no, identify the missing datum:

- source growth;
- rule formation;
- boundary import;
- obstruction residue;
- nontrivial transport;
- class exit;
- productive closure.

## No-Go / Escape Ledger

```text
NoGoEscapeLedger =
  (example_id,
   killed_class,
   assumptions_doing_work,
   killed_claim,
   surviving_claim,
   escape_condition,
   escape_cost,
   constructive_status,
   iteration_risk)
```

## Scoring Rubric

Each field is 0 to 3.

`field_fillability`

- 0: mostly empty
- 1: filled by analogy only
- 2: mostly concrete
- 3: concrete and independently checkable

`non_metaphor_specificity`

- 0: metaphorical
- 1: suggestive
- 2: domain-specific but not formal
- 3: formal, measurable, or operational

`absorber_resistance`

- 0: completely owned by existing field
- 1: mostly owned
- 2: adds cross-domain structure
- 3: clearly needs the accounting object

`fixture_readiness`

- 0: no obvious test
- 1: case narrative only
- 2: diagram/schema/simulation possible
- 3: theorem, executable model, or dataset fixture plausible

`cross_domain_usefulness`

- 0: isolated
- 1: analogy only
- 2: portable primitive
- 3: strong donor for general schema

`north_star_relevance`

- 0: not relevant
- 1: background
- 2: supports a sub-hypothesis
- 3: directly pressures the North Star
