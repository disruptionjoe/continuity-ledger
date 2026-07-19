---
source_id: active-dollar-evaluator-us-argentina-retail-20260719
source_type: primary, statistical, and institutionally authoritative
applies_to_packets: active-cl001-dollar-arm-pending
evidence_lanes: Frame adherence and declared-field guard; Evaluator sweep and population boundary; Constraint class and exit-cost interval; Typed measurement family; Loss, import, and access accounting; Falsifiers, open fields, and routing
provenance: Federal Reserve 2025 Diary of Consumer Payment Choice; Federal Reserve SHED 2025 Banking section; FDIC 2023 National Survey of Unbanked and Underbanked Households; BCRA Informe de Inclusion Financiera segundo semestre 2025; BCRA foreign trade and exchange regulations; U.S. International Trade Administration Argentina capital-controls note; retrieved 2026-07-19
extracted_by: Codex child run RUN-20260719-543
extracted_on: 2026-07-19
status: draft
claim_status: none
verdict: none
---

# Dollar Evaluator Sweep US/Argentina Retail Dossier

## Source Boundary

This draft dossier covers the active CL-001 dollar evaluator-sweep queue items
for U.S. retail and Argentine retail evaluator populations. It is scoped to
payment-instrument use, bank-account access, foreign-currency account access,
cash/electronic payment use, and exchange-access boundaries that could later
help bound dollar-arm exit-cost intervals.

Declared frame reference: `experiments/CL-001-phi-frame.md`.

Sources used:

- Federal Reserve Financial Services, "2025 Diary of Consumer Payment Choice",
  `https://www.frbservices.org/news/research/2025-findings-from-the-diary-of-consumer-payment-choice`.
- Board of Governors of the Federal Reserve System, "Report on the Economic
  Well-Being of U.S. Households in 2025 - Banking",
  `https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-banking.htm`.
- FDIC, "2023 FDIC National Survey of Unbanked and Underbanked Households",
  `https://www.fdic.gov/household-survey`.
- Banco Central de la Republica Argentina, "Informe de Inclusion Financiera,
  segundo semestre de 2025",
  `https://www.bcra.gob.ar/publicaciones/informe-de-inclusion-financiera-segundo-semestre-de-2025/`.
- Banco Central de la Republica Argentina, "Foreign trade and exchange
  regulations",
  `https://www.bcra.gob.ar/en/foreign-trade-and-exchange-regulations/`.
- International Trade Administration, "Argentina Eliminates Capital Controls
  and Payment Timelines",
  `https://www.trade.gov/market-intelligence/argentina-eliminates-capital-controls-and-payment-timelines`.

These sources are evaluator-population evidence and institutional orientation
sources. This dossier does not populate any active CL-001 packet field, does
not score any gate, and does not establish a dollar-arm exit-cost interval.

### Scoped Extraction

| Source-supported point | Packet field candidates | Evidence lane | Scope limit |
|---|---|---|---|
| The Federal Reserve Diary reports U.S. consumer payment-instrument mix and cash/card/mobile-phone use for the 2024 diary cycle. | `M1`, `Omega`, `L`, `V` | Evaluator sweep and population boundary; Typed measurement family | U.S. consumer payment behavior only; does not establish enforcement mechanism, appealability, bank-account access, or an exit-cost interval. |
| The 2025 SHED Banking section reports U.S. bank-account ownership, unbanked rates, overdraft exposure, nonbank check-cashing or money-order use, and fraud/loss recovery surfaces. | `L`, `I`, `P`, `V` | Loss, import, and access accounting; Constraint class and exit-cost interval | U.S. adult survey evidence; does not establish actual exclusion from retail dollar settlement or a legal remedy. |
| The FDIC household survey separates banked, underbanked, and unbanked household status and nonbank financial-service use. | `K0`, `L`, `I`, `V` | Evaluator sweep and population boundary; Loss, import, and access accounting | Household-level banking access evidence, not a direct measure of all retail settlement constraints. |
| The BCRA 2025 financial-inclusion report records account access, electronic payment use, foreign-currency account holding, and cash withdrawal behavior for Argentina. | `M1`, `Omega`, `L`, `I`, `V` | Evaluator sweep and population boundary; Typed measurement family | Argentina financial-system evidence; does not prove actual U.S.-dollar retail settlement availability or legal enforceability for every retail actor. |
| BCRA exchange-regulation material records foreign-exchange access conditions and authorized-entity routing for some operations. | `B`, `L`, `I`, `N`, `V` | Loss, import, and access accounting; Constraint class and exit-cost interval | Exchange-market access is not identical to retail settlement access, and it cannot be used as a legitimacy verdict. |
| The ITA note records the April 2025 removal of most Argentine currency controls as a trade-facing institutional update. | `L`, `I`, `N`, `V` | Falsifiers, open fields, and routing | U.S. government trade note, not Argentine primary law for every individual retail transaction. |

### Typed Quantities

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
| Cash payment share | Count share of consumer payments | Federal Reserve Diary. | Bank-account ownership, legal tender status, exchange restrictions, legitimacy. |
| Bank-account ownership | Survey status of checking, savings, or money-market account access | Federal Reserve SHED and FDIC survey. | Cash holding, foreign-currency account holding, Bitcoin UTXO state. |
| Underbanked status | Household use of nonbank financial services despite bank-account ownership | FDIC survey. | Exclusion, appealability, legal tender, price. |
| Foreign-currency account holding | Account-holding status in Argentina's financial system | BCRA financial-inclusion report. | U.S. retail bank access, cash use, Bitcoin custody, legitimacy. |
| Electronic payment activity | Account-based payment-use measure | BCRA financial-inclusion report. | Dollar-denominated settlement enforceability, Bitcoin confirmation, legal remedy. |
| Exchange-market access condition | Institutional condition for foreign-exchange operation | BCRA exchange-regulation material. | Retail transaction expectation, consumer fraud recovery, substrate merit. |

### Losses And Imports

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
| U.S. dollar evaluator evidence imports payment-instrument mix, account access, nonbank access, fraud exposure, and survey design. | `L`, `I`, `V` | Federal Reserve Diary, SHED, and FDIC survey. | Later packet work must identify which subset bounds exit cost for the declared retail settlement domain. |
| Argentine dollar evaluator evidence imports local banking infrastructure, electronic payment rails, foreign-currency accounts, exchange rules, and policy change timing. | `L`, `I`, `N`, `V` | BCRA reports and exchange-regulation page; ITA note. | Later packet work must distinguish peso-denominated electronic payment access from dollar-denominated retail settlement and savings access. |
| Foreign-currency accounts in Argentina are not themselves proof of dollar settlement continuation. | `M1`, `Omega`, `V` | BCRA financial-inclusion report. | Packet population must state whether the account surface supports price, save, and contract or only savings/investment posture. |
| Exchange-control relaxation may reduce an exit-cost burden, but it does not eliminate all institutional, market, compliance, or practical access costs. | `L`, `N`, `V` | BCRA and ITA institutional materials. | An exit-cost interval still needs a source-backed bounding method before any gate is scored. |

### Agency And Feedback Burden

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
| U.S. retail dollar evaluator surface. | Federal Reserve and FDIC sources support payment and account-access context. | Does not show a generated agency class, binding constraint class, or interval bound. | Ordinary consumer payment choice and bank-access analysis can absorb the evidence. |
| Argentine retail dollar evaluator surface. | BCRA sources support account, foreign-currency-account, electronic-payment, cash, and exchange-access context. | Does not show a stable U.S.-dollar retail settlement action space for all evaluator actors. | Ordinary dollarization, exchange regulation, or savings behavior can absorb the evidence. |
| Difference between U.S. and Argentine evaluator populations at fixed dollar substrate. | The source set creates a plausible population boundary for later comparison. | No later packet field is populated, and no fixed-`S0` interval has been calculated. | Population preference, inflation exposure, and exchange-market access may explain observed differences without substrate-bound constraint class movement. |

### What This Source Does Not Establish

This dossier does not populate any active CL-001 packet field. It does not score
any gate, issue a CL-001 verdict, accept a repo-owned claim, or establish the
dollar arm's fixed-`S0` evaluator result.

It does not establish:

- a dollar-arm binding constraint class;
- an exit-cost interval for U.S. retail or Argentine retail;
- that Argentine retail dollar use shares the same practical action space as
  U.S. retail dollar use;
- that payment behavior, account holding, foreign-currency account holding, and
  exchange-market access can be collapsed into one scalar;
- a legitimacy verdict about dollar settlement in either population;
- that evaluator differences are caused by population preference rather than
  substrate posture or institutional boundary; or
- that any active CL-001 gate can be scored.

### Falsifiers And Reopen Conditions

Reopen or supersede this dossier if:

- later packet work uses payment share, bank-account ownership, or
  foreign-currency account ownership as an exit-cost interval without a typed
  conversion map;
- Argentine evaluator evidence requires changing `R0`, `M1`, `Omega`, or the
  settlement-boundary role;
- a more authoritative Argentine primary source supersedes the ITA secondary
  trade note for individual dollar access;
- later source work shows that the selected U.S. or Argentine population boundary
  is not retail, not settlement-facing, or not fixed-`S0`;
- a source pass turns dollar access or appealability into a legitimacy claim; or
- this dossier is used as evidence that the dollar arm passes a CL-001 gate.

## No Claim Promotion

This source dossier cannot promote a CL-001 packet, gate, experiment verdict, or
repo-owned claim. It only records evaluator-population source extraction work
for later review.
