---
artifact_type: primary_source_extraction
status: complete
lane: discovery
recipient_lane: 3
claim_status: none
evidence_grade: authoritative_primary_source_bounded
candidate_disposition: NARROWER_STRUCTURE_TRANSPORT_PROTOCOL
cl001_isolation: required
---

# TCP Primary Extraction

## Scope and source

Question: does TCP's reliable byte stream require an explanation beyond
ordinary transport-protocol engineering?

Primary source: IETF STD 7, RFC 9293, *Transmission Control Protocol (TCP)*,
August 2022: https://www.rfc-editor.org/rfc/rfc9293.html. This standards-track
specification replaces RFC 793's TCP requirements and consolidates later
standards-track updates. This read is isolated from CL-001 and makes no
cross-case synthesis.

## Extraction

- Section 2.2 specifies a reliable, in-order byte-stream service to
  applications, carried as TCP segments in IP datagrams.
- Reliability is implemented by detecting loss with sequence numbers,
  detecting errors with per-segment checksums, and correcting loss through
  retransmission.
- TCP is connection-oriented and maintains endpoint state. Sequence and
  acknowledgment numbers, receive windows, connection states, retransmission
  timing, and buffers are explicit protocol machinery rather than free
  properties of the underlying network.
- The checksum is mandatory at both sender and receiver. It detects corruption;
  it does not establish application truth or semantic correctness.
- The specification separately requires congestion control and permits
  multiple conforming algorithms. Reliable delivery therefore remains bounded
  by endpoint behavior, protocol requirements, resources, and failure modes.

## Absorber verdict

`NARROWER_STRUCTURE_TRANSPORT_PROTOCOL`.

RFC 9293 explains the transition through endpoint state, sequence space,
acknowledgment, error detection, retransmission, buffering, flow control, and
conformance rules. The application-visible stream is a typed transport
service, not conserved application meaning, proof of delivery to an acting
person, or an independently established agency surface. No additional
transduction primitive is forced by the source-grounded case.

The seed's recursive-growth and recruited-agent language is not established
by this specification. No CL-001 field, shared atlas structure, claim
promotion, or external action follows.

## Handoff

Retain TCP as an ordinary transport-protocol absorber control. Any later atlas
invariant must add more than the exact endpoint state, sequencing,
acknowledgment, checksum, retransmission, window, buffer, and conformance
machinery already specified by TCP.
