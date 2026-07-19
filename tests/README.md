# Tests

This directory is reserved for deterministic checks owned by this repository,
including schema validators, fixture runs, and formal or executable absorber
tests.

Current checks:

- `validate_cltp_packets.py` verifies that the retired CL-001 packet files
  retain the full CLTP field set, ten charter gates, and explicit
  no-claim-promotion status. It also verifies that the retired source-intake
  contract names every packet and required evidence lane, and that the
  source-dossier template, manifest, and draft dossier files preserve the
  minimum extraction queue shape. The dossier checks also require manifest
  references to resolve to files, every draft dossier to remain manifest-listed,
  dossier `source_id` values to stay unique, dossier evidence lanes to match the
  intake contract, and dossier status, claim status, and verdict fields to stay
  non-promotional. It also checks that the active Interval Sweep scaffold exists
  and that the retired Bitcoin/photosynthesis scaffold remains marked retired.
