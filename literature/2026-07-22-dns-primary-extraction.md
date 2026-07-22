---
artifact_type: primary_source_extraction
status: complete
lane: discovery
recipient_lane: 3
claim_status: none
evidence_grade: authoritative_primary_source_bounded
candidate_disposition: NARROWER_STRUCTURE_DISTRIBUTED_NAMING
cl001_isolation: required
---

# DNS Primary Extraction

## Scope and source

Question: does DNS hierarchical naming require an explanation beyond ordinary
distributed naming and database design?

Primary source: P. Mockapetris, RFC 1034, *Domain Names - Concepts and
Facilities*, November 1987:
https://www.rfc-editor.org/rfc/rfc1034.html. This read is isolated from CL-001
and makes no cross-case synthesis.

## Extraction

- Internet growth made centralized `HOSTS.TXT` distribution costly and delayed
  locally administered changes; RFC 1034 responds with a hierarchical name
  space and distributed database.
- The design distributes maintenance and name creation, uses local caching,
  and explicitly trades update speed and cache accuracy under source-controlled
  timeouts.
- DNS separates a tree-structured name space and typed resource records from
  name servers and resolvers. Zones delimit authoritative subsets and allow
  redundant service.
- Iterative referrals are required and recursive resolution is optional.
  Cached copies may remain stale while refresh is unavailable, so access and
  consistency are bounded operational properties, not perfect identity.
- Administrators define zone boundaries, master data, updates, and refresh
  policy; the system supplies standard record, query, and refresh formats.

## Absorber verdict

`NARROWER_STRUCTURE_DISTRIBUTED_NAMING`.

RFC 1034 explains the transition through hierarchical delegation, authoritative
zones, typed records, resolvers, referrals, caching, and refresh policy. These
mechanisms create a scalable naming service but do not establish truth of the
named resource, a newly recruited agent class, or an independent transduction
law. No CL-001 field, shared atlas structure, or claim promotion follows.

## Handoff

Retain DNS as an ordinary distributed-naming absorber control. Reopen only if
a later invariant adds more than delegation, authority, typed records,
resolution, caching, staleness, and refresh policy already supplied by DNS.
