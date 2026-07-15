# Tests

This directory is reserved for deterministic checks owned by this repository,
including schema validators, fixture runs, and formal or executable absorber
tests.

Current checks:

- `validate_cltp_packets.py` verifies that CL-001 packet files retain the full
  CLTP field set, ten charter gates, and explicit no-claim-promotion status
  before any packet is scored. It also verifies that the CL-001 source-intake
  contract names every packet and required evidence lane, and that the
  source-dossier template, manifest, and draft dossier files preserve the
  minimum extraction queue shape.
