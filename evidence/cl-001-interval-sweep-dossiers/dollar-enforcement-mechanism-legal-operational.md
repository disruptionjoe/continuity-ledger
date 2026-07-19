---
source_id: active-dollar-enforcement-uscode5103-rege-ofac501-20260719
source_type: primary and institutionally authoritative
applies_to_packets: active-cl001-dollar-arm-pending
evidence_lanes: Frame adherence and declared-field guard; Mechanism and transition boundary; Settlement regime and class definition; Typed measurement family; Loss, import, and access accounting; Constraint class and exit-cost interval; Agency surface and action-space burden; Falsifiers, open fields, and routing
provenance: 31 U.S.C. 5103 via uscode.house.gov; 12 CFR Part 1005 and 12 CFR 1005.11 via eCFR and CFPB Regulation E index; 31 CFR 501.806 and 31 CFR 501.807 via eCFR; retrieved 2026-07-19
extracted_by: Codex child run RUN-20260719-534
extracted_on: 2026-07-19
status: draft
claim_status: none
verdict: none
---

# Dollar Enforcement Mechanism Legal-Operational Dossier

## Source Boundary

This draft dossier covers the active CL-001 dollar enforcement-mechanism queue
item. It is scoped to legal-tender recognition, consumer electronic-fund-transfer
error procedures, and OFAC blocking/unblocking or delisting procedures as
institutional surfaces around dollar-denominated retail settlement.

Declared frame reference: `experiments/CL-001-phi-frame.md`.

Sources used:

- U.S. Code, 31 U.S.C. 5103, "Legal tender",
  `https://uscode.house.gov/view.xhtml?edition=prelim&path=/prelim@title31/subtitle4`.
- Consumer Financial Protection Bureau, "12 CFR Part 1005 - Electronic Fund
  Transfers (Regulation E)",
  `https://www.consumerfinance.gov/rules-policy/regulations/1005/`.
- eCFR, 12 CFR Part 1005, especially section 1005.11, "Procedures for resolving
  errors", `https://www.ecfr.gov/current/title-12/chapter-X/part-1005`.
- eCFR, 31 CFR 501.806, "Procedures for unblocking property believed to have
  been blocked and reported in error due to mistaken identity or typographical
  or similar errors",
  `https://www.ecfr.gov/current/title-31/subtitle-B/chapter-V/part-501/subpart-E/section-501.806`.
- eCFR, 31 CFR 501.807, "Procedures governing delisting from the Specially
  Designated Nationals and Blocked Persons List or any other list of sanctioned
  persons or property maintained by the Office of Foreign Assets Control",
  `https://www.ecfr.gov/current/title-31/subtitle-B/chapter-V/part-501/subpart-E/section-501.807`.

The sources are primary legal or institutionally authoritative orientation
sources for the dollar arm. They do not by themselves establish the complete
retail dollar substrate, actual financial-institution behavior, current
population-specific exit costs, or a CL-001 packet field.

### Scoped Extraction

| Source-supported point | Packet field candidates | Evidence lane | Scope limit |
|---|---|---|---|
| 31 U.S.C. 5103 identifies United States coins and currency, including Federal Reserve notes, as legal tender for debts, public charges, taxes, and dues. | `R1`, `K1`, `M1`, `Omega`, `V` | Settlement regime and class definition; Typed measurement family | Legal-tender currency recognition only; does not establish universal merchant acceptance, account transfer rules, banking access, legitimacy, or population exit costs. |
| CFPB Regulation E covers consumer electronic fund and remittance-transfer contexts including ATMs, direct deposit, point-of-sale transfers, remittances, telephone transfers, and related disclosure, liability, cancellation, and error-resolution topics. | `R0`, `K0`, `B`, `M1`, `Omega`, `V` | Settlement regime and class definition; Mechanism and transition boundary | Consumer electronic-fund-transfer scope only; does not cover cash, all bank-account closure, all payment networks, sanctions, or non-US retail settlement. |
| 12 CFR 1005.11 sets procedural duties for resolving covered consumer electronic-fund-transfer errors, including notice, investigation, reporting, and timing structure. | `T`, `B`, `L`, `I`, `P`, `V` | Mechanism and transition boundary; Loss, import, and access accounting; Agency surface and action-space burden | Supports an appealable dispute surface for covered consumer EFT errors; does not prove discretionary settlement acceptance or all forms of dollar exclusion. |
| 31 CFR 501.806 provides an administrative route for release of property believed to have been blocked in error due to mistaken identity, typographical, or similar errors. | `T`, `B`, `L`, `I`, `N`, `V` | Mechanism and transition boundary; Loss, import, and access accounting; Constraint class and exit-cost interval | Sanctions-blocking procedure only; does not establish ordinary retail denial, actual release rates, or general bank discretion. |
| 31 CFR 501.807 provides a petition path for administrative reconsideration from OFAC sanctions-list designation or other listed/identified sanctioned-person or property status. | `T`, `B`, `N`, `X`, `V` | Constraint class and exit-cost interval; Falsifiers, open fields, and routing | Supports the existence of an administrative reconsideration route; does not quantify practical access, cost, delay, likelihood, or legitimacy. |
| The source set makes institutional procedures part of the dollar-arm burden rather than a pure protocol rule. | `I`, `L`, `Z`, `V` | Loss, import, and access accounting; Falsifiers, open fields, and routing | This is a dossier-level extraction boundary, not a packet claim that dollar enforcement is discretionary and appealable in every case. |

### Typed Quantities

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
| U.S. coins and currency | Legal-tender monetary instrument | 31 U.S.C. 5103 legal-tender recognition. | Bitcoin UTXOs, hashwork, energy, legitimacy, agency. |
| Electronic fund transfer | Consumer-account transfer category | CFPB Regulation E and eCFR Part 1005 scope. | Cash settlement, sanctions blocking, proof-of-work, legal tender. |
| Notice of error | Consumer procedural claim record | 12 CFR 1005.11 error-resolution process. | Final settlement, legal entitlement, market price, legitimacy. |
| Blocked property | Legal/institutional status of property under OFAC-administered sanctions rules | 31 CFR 501.806 and related reporting/unblocking procedures. | Ordinary payment failure, consumer dispute, Bitcoin invalid transaction. |
| Petition for administrative reconsideration | Administrative request process | 31 CFR 501.807 delisting/reconsideration route. | Protocol validation, market exit cost, legitimacy verdict. |
| U.S. dollars | Denomination used in legal, reporting, and account contexts | Legal tender and OFAC value-reporting contexts. | Chainwork, joules, agency surface, settlement confidence. |

### Losses And Imports

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
| Dollar recognition imports sovereign legal-tender status and institutional enforcement rather than a self-contained protocol rule. | `I`, `K1`, `M1`, `V` | 31 U.S.C. 5103. | Later packet work must separate legal tender from account access, merchant acceptance, and retail payment-network acceptance. |
| Consumer EFT error resolution imports a regulated financial institution, consumer-account scope, notice timing, documentation, and procedural response. | `I`, `L`, `B`, `P`, `V` | 12 CFR Part 1005 and section 1005.11. | Later packet work must bound which retail dollar transactions are inside Regulation E and which are outside it. |
| OFAC blocking imports sanctions authority, compliance intermediaries, reporting procedures, and property-status records. | `I`, `L`, `N`, `V` | 31 CFR 501.806. | Later packet work must not generalize sanctions blocking into all dollar exclusion without additional sources. |
| OFAC reconsideration imports administrative review, submitted evidence, agency discretion, possible meetings, written decision, and timing/cost burdens not quantified here. | `I`, `L`, `X`, `V` | 31 CFR 501.807. | Later evaluator dossiers must bound practical exit-cost intervals rather than treating appealability as costless. |
| None of the cited sources supplies population-specific dollar exit-cost intervals for US retail or Argentine retail evaluators. | `L`, `N`, `V` | The source set is mechanism/procedure-level, not statistical or population-level. | Evaluator-sweep dossiers remain required before any fixed-`S0` population comparison. |

### Agency And Feedback Burden

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
| Consumer error-resolution procedure as an appealable recognition surface. | Regulation E section 1005.11 supports a formal procedure for covered EFT error notices, investigation, and response. | Does not prove a new or durably recruited agency class; it may only describe consumer-protection procedure. | Ordinary regulated-dispute resolution can absorb the finding without supporting a CLTP agency surface. |
| OFAC unblocking and delisting routes as administrative appeal surfaces. | 31 CFR 501.806 and 501.807 support request or petition routes in sanctions contexts. | Does not establish ordinary retail dollar access or practical success rates. | Administrative-law procedure may absorb appealability without supporting the broader dollar substrate claim. |
| Legal-tender recognition as a continuation surface for debts and public obligations. | 31 U.S.C. 5103 supports the legal-tender status of U.S. coins and currency. | Does not establish account access, international retail settlement, merchant acceptance, or a generated action class. | Ordinary sovereign money law can explain recognition without continuity-ledger escape. |
| Candidate discretionary and appealable dollar exclusion. | The source set supports some human/institutional procedure and review routes. | Does not establish that discretion and appealability are the binding dollar-arm constraint class across the declared retail settlement domain. | A narrower procedural-dispute absorber remains live. |

### What This Source Does Not Establish

This dossier does not populate any active CL-001 packet field. It does not score
any gate, issue a CL-001 verdict, accept a repo-owned claim, or establish the
dollar arm's candidate enforcement posture.

It does not establish:

- that all dollar exclusions are discretionary, appealable, or institutionally
  reversible;
- that covered consumer EFT procedures represent the whole retail dollar
  settlement domain;
- actual bank-account access, account closure, sanctions-blocking frequency,
  appeal success, practical delay, cost, or population-specific exit-cost
  intervals;
- Argentine retail dollar access, dollarization, inflation, capital controls, or
  informal-market behavior;
- a legitimacy verdict about dollar settlement;
- an agency-generation result, class-relative no-go, or constructive escape
  witness; or
- that the dollar arm differs from the Bitcoin arm for a non-frame artifact
  reason.

### Falsifiers And Reopen Conditions

Reopen or supersede this dossier if:

- later source work shows the cited procedures are outside the declared retail
  settlement domain;
- packet population uses this dossier to claim dollar discretion or
  appealability without a narrower field-specific source;
- evaluator-sweep evidence requires `R0`, `M1`, `Omega`, or the settlement
  boundary role to vary;
- a better exact legal-operational source supersedes one of the cited sources;
- later review finds the dossier treats a legal remedy as a practical remedy
  without evidence of cost, timing, and access; or
- the dollar arm cannot be stated without a legitimacy verdict.

## No Claim Promotion

This source dossier cannot promote a CL-001 packet, gate, experiment verdict, or
repo-owned claim. It only records source extraction work for later review.
