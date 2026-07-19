---
source_id: active-bitcoin-evaluator-us-salvador-retail-20260719
source_type: primary, statistical, institutional, and protocol-operational
applies_to_packets: active-cl001-bitcoin-arm-pending
evidence_lanes: Frame adherence and declared-field guard; Evaluator sweep and population boundary; Constraint class and exit-cost interval; Typed measurement family; Loss, import, and access accounting; Agency surface and action-space burden; Falsifiers, open fields, and routing
provenance: Federal Reserve SHED 2025 Banking section; IRS Digital Assets guidance and virtual currency FAQ; El Salvador Asamblea Legislativa Bitcoin Law and 2025 reform decree materials; IMF El Salvador Selected Issues 2025; Bitcoin.org and Bitcoin Core protocol materials from the active Bitcoin enforcement dossier; retrieved 2026-07-19
extracted_by: Codex child run RUN-20260719-543
extracted_on: 2026-07-19
status: draft
claim_status: none
verdict: none
---

# Bitcoin Evaluator Sweep US/El Salvador Retail Dossier

## Source Boundary

This draft dossier covers the active CL-001 Bitcoin evaluator-sweep queue items
for U.S. retail and Salvadoran retail evaluator populations. It is scoped to
U.S. crypto use and tax/accounting treatment, Salvadoran Bitcoin legal/policy
context, adoption and financial-inclusion evidence, and the protocol sources
already cited by the active Bitcoin enforcement-mechanism dossier.

Declared frame reference: `experiments/CL-001-phi-frame.md`.

Sources used:

- Board of Governors of the Federal Reserve System, "Report on the Economic
  Well-Being of U.S. Households in 2025 - Banking",
  `https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-banking.htm`.
- Internal Revenue Service, "Digital assets",
  `https://www.irs.gov/filing/digital-assets`.
- Internal Revenue Service, "Frequently asked questions on virtual currency
  transactions",
  `https://www.irs.gov/individuals/international-taxpayers/frequently-asked-questions-on-virtual-currency-transactions`.
- Asamblea Legislativa de El Salvador, original Ley Bitcoin decree materials,
  `https://www.asamblea.gob.sv/sites/default/files/documents/decretos/FC7303D5-78F1-4D23-9467-5226F6EFD510.pdf`.
- Asamblea Legislativa de El Salvador, 2025 reform decree materials,
  `https://www.asamblea.gob.sv/sites/default/files/documents/decretos/FC2C7E66-490B-4420-B8B5-221C2F2A4C28.pdf`.
- International Monetary Fund, "El Salvador: Selected Issues",
  `https://www.imf.org/en/publications/cr/issues/2025/03/19/el-salvador-selected-issues-565394`.
- Bitcoin protocol and implementation sources already recorded in
  `evidence/cl-001-interval-sweep-dossiers/bitcoin-enforcement-mechanism-protocol.md`.

These sources are evaluator-population and institutional context for the
Bitcoin arm. This dossier does not populate any active CL-001 packet field,
does not score any gate, and does not establish a Bitcoin-arm exit-cost
interval.

### Scoped Extraction

| Source-supported point | Packet field candidates | Evidence lane | Scope limit |
|---|---|---|---|
| The 2025 SHED Banking section reports U.S. adult cryptocurrency use for investment, purchases/payments, and transfers, plus banked/unbanked differences. | `P`, `A`, `Omega`, `L`, `V` | Evaluator sweep and population boundary; Agency surface and action-space burden | Cryptocurrency category is broader than Bitcoin; self-reported survey evidence does not establish Bitcoin settlement use or protocol enforcement. |
| IRS digital-asset guidance identifies tax-reporting and income-reporting surfaces for digital-asset transactions. | `I`, `L`, `B`, `V` | Loss, import, and access accounting; Typed measurement family | Federal tax treatment is an institutional import around U.S. users, not Bitcoin protocol settlement or a legitimacy verdict. |
| IRS virtual-currency FAQ treats virtual currency under property-tax principles for federal income-tax purposes. | `M1`, `L`, `I`, `V` | Typed measurement family; Loss, import, and access accounting | Tax-accounting treatment is not a retail unit-of-account capable settlement record by itself. |
| El Salvador's original Bitcoin-law materials and 2025 reform materials establish a legal/policy boundary that changed over time. | `B`, `I`, `N`, `V` | Evaluator sweep and population boundary; Falsifiers, open fields, and routing | Legal status and acceptance obligations must be dated; packet work cannot silently treat 2021 and post-reform contexts as one evaluator state. |
| The IMF Selected Issues paper provides institutional analysis of Bitcoin, financial inclusion, adoption, remittances, public support, and risk in El Salvador. | `P`, `A`, `Omega`, `L`, `I`, `Z`, `V` | Agency surface and action-space burden; Loss, import, and access accounting | IMF institutional analysis is not Salvadoran legal authority and does not populate a packet field alone. |
| Existing Bitcoin protocol sources support protocol-validity and proof-of-work surfaces, but not U.S. or Salvadoran retail evaluator behavior. | `T`, `B`, `C`, `N`, `V` | Frame adherence and declared-field guard; Constraint class and exit-cost interval | The evaluator dossier must keep protocol evidence separate from population evidence. |

### Typed Quantities

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
| Cryptocurrency use share | Survey share of adults reporting use | Federal Reserve SHED. | Bitcoin UTXO state, chainwork, legal tender status, tax basis, legitimacy. |
| Crypto purchase/payment use | Survey-reported transaction use | Federal Reserve SHED. | Protocol validity, legal acceptance obligation, exchange price. |
| Digital-asset tax report | Tax-return reporting obligation or income category | IRS digital-asset guidance. | Settlement finality, unit-of-account capability, user preference. |
| Virtual currency as property | Federal income-tax treatment category | IRS FAQ. | Legal tender, UTXO, chainwork, action-space capability. |
| Bitcoin-law legal status | Salvadoran legal/policy category | Asamblea Legislativa materials. | Protocol validity, U.S. tax status, retail adoption. |
| Adoption/financial-inclusion assessment | Institutional analysis finding | IMF Selected Issues. | Gate verdict, exit-cost interval, legitimacy verdict. |

### Losses And Imports

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
| U.S. Bitcoin evaluator evidence imports a broader cryptocurrency survey category and federal tax/accounting treatment. | `I`, `L`, `V` | Federal Reserve SHED and IRS pages. | Later packet work must source Bitcoin-specific retail payment use, custody/key burden, fees, and exchange access. |
| Salvadoran Bitcoin evaluator evidence imports changing legal status, public-policy implementation, remittance/inclusion claims, and adoption evidence. | `B`, `I`, `L`, `P`, `V` | Asamblea and IMF materials. | Later packet work must date the evaluator state and decide whether the reform creates a frame-pressure stop condition. |
| Bitcoin use by retail actors imports wallets, keys, exchanges, custody, price volatility, network fees, taxation, and legal/institutional recourse. | `L`, `I`, `P`, `A`, `Omega`, `V` | IRS, IMF, and protocol materials. | None of these costs are yet converted into an exit-cost interval. |
| Protocol validity is not the same as population-level settlement access. | `T`, `B`, `N`, `V` | Existing Bitcoin mechanism dossier. | Later packet work must keep protocol exclusion and retail evaluator access separate. |

### Agency And Feedback Burden

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
| U.S. retail Bitcoin evaluator surface. | SHED supports low but nonzero cryptocurrency transaction use and bank-status differences; IRS supports tax/accounting imports. | Does not isolate Bitcoin from all cryptocurrency or show a generated action class. | Investment, tax, and speculative-asset absorbers remain live. |
| Salvadoran retail Bitcoin evaluator surface. | Asamblea and IMF sources support a distinctive legal/policy and adoption context. | Does not prove active retail Bitcoin settlement, agency generation, or current acceptance costs. | Public-policy implementation, subsidy, Chivo-wallet, remittance, and legal-status absorbers remain live. |
| Fixed-`S0` comparison across U.S. and Salvadoran populations. | The source set creates a plausible evaluator-population contrast around the same protocol substrate. | The 2025 legal reform may alter the evaluator boundary and must be dated before any packet population. | Variation may follow law, subsidy, wallet design, or institutional trust rather than evaluator preference at fixed substrate. |

### What This Source Does Not Establish

This dossier does not populate any active CL-001 packet field. It does not score
any gate, issue a CL-001 verdict, accept a repo-owned claim, or establish the
Bitcoin arm's fixed-`S0` evaluator result.

It does not establish:

- a Bitcoin-arm binding constraint class;
- an exit-cost interval for U.S. retail or Salvadoran retail;
- that U.S. cryptocurrency survey responses are Bitcoin-specific retail
  settlement evidence;
- that Salvadoran legal status, wallet adoption, remittances, and retail use can
  be collapsed into one scalar;
- that the 2025 reform is compatible with the same evaluator state as the 2021
  legal-tender launch;
- a legitimacy verdict about Bitcoin settlement in either population;
- that protocol unappealability is the same as retail actor exit cost; or
- that any active CL-001 gate can be scored.

### Falsifiers And Reopen Conditions

Reopen or supersede this dossier if:

- later packet work treats cryptocurrency-wide U.S. survey evidence as
  Bitcoin-specific without a bridge;
- Salvadoran legal or policy evidence requires changing `R0`, `M1`, `Omega`, or
  the settlement-boundary role;
- the 2025 reform makes the U.S./Salvador evaluator comparison a time-varying
  policy comparison rather than fixed-`S0` population sweep;
- later work treats IRS property-tax treatment or Salvadoran legal status as a
  legitimacy verdict;
- later packet population needs current fee, custody, exchange, wallet, or
  merchant-acceptance sources not listed here; or
- this dossier is used as evidence that the Bitcoin arm passes a CL-001 gate.

## No Claim Promotion

This source dossier cannot promote a CL-001 packet, gate, experiment verdict, or
repo-owned claim. It only records evaluator-population source extraction work
for later review.
