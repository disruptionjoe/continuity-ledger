# Retired CL-001: Bitcoin / Photosynthesis Pair And Null

Status: retired founding experiment.

Retired: 2026-07-16, Joe direct chat, with the founding case pair and prior
CL-001. This file is retained as provenance for the scaffold that existed before
the charter amendment. It is not the active CL-001 experiment, cannot authorize
packet population, and cannot issue a verdict. Current CL-001 work starts from
`experiments/CL-001-interval-sweep.md`.

## Objective

Determine whether Continuity Ledger Transaction Packet v0.1 captures a
nontrivial shared structure across Bitcoin proof-of-work and oxygenic
photosynthesis while rejecting matched conversion-only nulls.

## Cases

- Target A: Bitcoin proof-of-work as implemented by the Bitcoin protocol and
  participant ecology.
- Target B: oxygenic photosynthesis and its biological/ecological agency loop.
Floor nulls (zero weight toward a positive verdict; specified by stipulated
absence, so their agency-gate failure is analytic):

- Floor Null A: energy-consuming hash computation with no persistent consensus,
  settlement, issuance, or participant policy surface.
- Floor Null B: solar heating of inert matter with no self-maintaining
  biochemical or ecological agency loop.

Near-miss nulls (load-bearing controls; specified positively as named real
systems, selected because they might genuinely pass):

- Near-Miss Null A: Bitcoin testnet or a regtest chain. Full consensus,
  settlement, issuance, participant ecology, and proof-of-work; economically
  worthless coins. If CLTP scores it the same as mainnet, the ledger tracks
  protocol structure rather than agency.
- Near-Miss Null B: Rayleigh-Benard convection or a solar pond. Real
  dissipative structure, self-organization, and far-from-equilibrium ordering;
  no metabolism, no heredity. If CLTP cannot distinguish photosynthesis from
  it, that is an earned `KILL`.

## Rules

- Use primary technical and scientific sources for material claims.
- Populate target packets independently before comparison.
- Do not use `energy`, `value`, `information`, or `agency` as an untyped bridge.
- Record losses and external imports before scoring agency or escape.
- State the relevant class-relative constraint without claiming either target
  violates a theorem it merely changes class around.
- Score nulls with the same gates and standards.

## Preregistered Decision

- `SHARED_STRUCTURE`: both targets pass all load-bearing gates, both
  **near-miss** nulls fail at least the agency or feedback gate for a
  non-definitional reason, both floor nulls fail, and the common fields impose
  at least one constraint not supplied by ordinary causal description.
- `NARROWER_STRUCTURE`: a useful typed subset survives, or the structure works
  in one domain but not the other.
- `KILL`: the common packet is vacuous, metaphor-dependent, unable to reject
  the floor nulls, unable to discriminate a near-miss null from its target, or
  unable to admit any near-miss null at all.

Floor nulls carry zero weight toward `SHARED_STRUCTURE`. Their failure is
analytic and establishes only that the packet rejects the trivial case. A run
that rejects the floor nulls and stops has not run a control.

Amended 2026-07-16 (Joe direct chat) before any packet field was populated or
any gate scored. Prior wording required "both nulls" to fail for a
non-definitional reason while specifying both nulls by stipulated absence,
which made this branch unreachable. See `governance/CHARTER.md` > Amendments.

## Required Output

Four frozen case packets, a field-by-field contrast matrix, absorber analysis,
gate receipts, and one explicit verdict. No claim promotion is authorized by
the run alone.

## Current Construction Artifacts

- `packets/cl-001/` holds the four CL-001 target and matched-null packet
  construction files.
- `evidence/cl-001-source-intake.md` defines the source-intake burden for
  later packet population.
- `evidence/cl-001-source-dossier-template.md` defines the source extraction
  record that future source passes must fill before packet fields move.
- `evidence/cl-001-source-dossier-manifest.md` binds the dossier queue to the
  four packet ids while all exact source selections remain pending.
- `tests/validate_cltp_packets.py` checks that each packet keeps the full
  field, gate, source-intake, and dossier-manifest shape before scoring.

### Not Yet Constructed

The 2026-07-16 amendment added near-miss nulls. Nothing for them exists yet:

- no packet files for Near-Miss Null A or Near-Miss Null B;
- no entries for them in `evidence/cl-001-source-dossier-manifest.md`; and
- no source dossiers.

The two existing null construction dossiers under `evidence/cl-001-dossiers/`
belong to the floor nulls and cite this repository's own packet files as their
provenance. They are construction records, not source extractions, and they
carry zero weight toward a positive verdict.

Constructing the near-miss nulls is the load-bearing remaining work in CL-001.
Until it exists, the run can reject the trivial case and nothing more.
