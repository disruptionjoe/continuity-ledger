---
artifact_type: primary_source_extraction
status: complete
lane: discovery
recipient_lane: 3
claim_status: none
evidence_grade: authoritative_primary_source_bounded
candidate_disposition: NARROWER_STRUCTURE_LEGAL_OPERATIONAL_SETTLEMENT
cl001_isolation: required
---

# Fedwire Primary Extraction

## Scope and sources

Question: does Fedwire finality need an explanation beyond payment-system law
and central-bank operations?

Authoritative sources:

- Federal Reserve Board, *Fedwire Funds Transfer System: Assessment of
  Compliance with the Core Principles for Systemically Important Payment
  Systems*: https://www.federalreserve.gov/paymentsystems/fedfunds_coreprinciples.htm
- Regulation J, 12 CFR part 210, subpart B:
  https://www.federalreserve.gov/frrs/regulations/reg-j-collection-of-checks-and-other-items-by-federal-reserve-banks-and-funds-transfers-through-fedwire.htm
- Federal Reserve Board, *Fedwire Funds Services*:
  https://www.federalreserve.gov/paymentsystems/fedfunds_about.htm

This discovery read is isolated from CL-001 and makes no cross-case synthesis.

## Extraction

- Fedwire is a real-time gross settlement credit-transfer service. A
  participant instructs a Reserve Bank to debit its account and credit another
  participant's Reserve Bank account.
- Payment to the receiving participant is final and irrevocable when its
  account is credited or the payment order is sent to it, whichever is earlier.
- Regulation J governs the parties' rights and obligations and has the force
  and effect of federal law. Operating Circular 6 supplies service rules.
- Orders must satisfy security procedures and message format; a sender needs
  account funds or overdraft capacity, and a Reserve Bank may reject an order.
- Eligibility depends on maintaining an account with a Reserve Bank (subject to
  the service's rules), so access and settlement capability are institutionally
  bounded rather than universal.

## Absorber verdict

`NARROWER_STRUCTURE_LEGAL_OPERATIONAL_SETTLEMENT`.

The sources fully explain the transition through account entries, legal rules,
operational acceptance, security controls, liquidity/credit capacity, and the
central-bank settlement platform. “Finality” here is typed settlement finality,
not metaphysical finality, universal irreversibility, or an independent agency
surface. Continuity Ledger can record entitlement, imports, and access limits,
but no additional transduction primitive is forced.

The seed's recursive-growth and recruited-agent language is not established by
these sources. No CL-001 field, shared atlas structure, claim promotion, or
external action follows.

## Handoff

Retain Fedwire as an ordinary legal-operational absorber control. Any later
atlas invariant must add more than Regulation J, Reserve Bank account posting,
security/message admission, liquidity capacity, and settlement finality.
