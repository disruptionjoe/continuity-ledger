---
source_id: photosynthesis-psii-water-oxidation-core-2011-1970-2015
source_type: primary and review
applies_to_packets: cl001-oxygenic-photosynthesis
evidence_lanes: mechanism and transition boundary; typed measurement family; loss and import accounting; falsifiers and open fields
provenance: Umena et al. 2011 Nature; Kok, Forbush, and McGloin 1970 Photochemistry and Photobiology; Shen 2015 Annual Review of Plant Biology; Allen 2002 Cell
extracted_by: Codex child run RUN-20260715-441
extracted_on: 2026-07-15
status: draft
claim_status: none
verdict: none
---

# Photosynthesis Mechanism Dossier

## Source Boundary

This draft dossier covers the oxygenic photosynthesis mechanism queue item for
`cl001-oxygenic-photosynthesis`. It is scoped to light-driven water oxidation,
photosystem II, oxygen evolution, immediate electron/proton transfer products,
and typed biochemical quantities.

Sources used:

- Yasufumi Umena, Keisuke Kawakami, Jian-Ren Shen, and Nobuo Kamiya, "Crystal
  structure of oxygen-evolving photosystem II at a resolution of 1.9 angstrom",
  Nature 473, 55-60 (2011), `https://doi.org/10.1038/nature09913`.
- Bessel Kok, Bliss Forbush, and Marion McGloin, "Cooperation of charges in
  photosynthetic O2 evolution-I. A linear four step mechanism",
  Photochemistry and Photobiology 11, 457-475 (1970),
  `https://doi.org/10.1111/j.1751-1097.1970.tb06017.x`.
- Jian-Ren Shen, "The Structure of Photosystem II and the Mechanism of Water
  Oxidation in Photosynthesis", Annual Review of Plant Biology 66, 23-48
  (2015), `https://doi.org/10.1146/annurev-arplant-050312-120129`.
- John F. Allen, "Photosynthesis of ATP - Electrons, Proton Pumps, Rotors, and
  Poise", Cell 110, 273-276 (2002),
  `https://doi.org/10.1016/S0092-8674(02)00870-X`.

The Umena et al. and Kok et al. papers are used as primary mechanism sources for
photosystem II structure and oxygen evolution. The Shen and Allen reviews are
orientation sources for integrating water oxidation with the wider light
reactions; they cannot by themselves populate material packet fields unless a
later run traces the same point to admissible primary evidence.

This dossier does not establish carbon fixation, biomass production, ecological
agency, evolutionary history, organismal action spaces, or any CL-001 gate
result.

### Scoped Extraction

| Source-supported point | Packet field candidates | Evidence lane | Scope limit |
|---|---|---|---|
| Photosystem II is the photosynthetic water-oxidation site, and Umena et al. report a high-resolution structure resolving the catalytic Mn4CaO5 cluster and its surrounding ligands. | `S0`, `T`, `B`, `S1`, `V` | Mechanism and transition boundary; typed measurement family | Structural mechanism evidence only; does not establish organismal fitness, biomass production, ecological feedback, or agency. |
| Kok et al. model photosynthetic O2 evolution as cooperation of charges through a four-step sequence, giving a source for charge accumulation before O2 release. | `T`, `C`, `L`, `M0`, `M1` | Mechanism and transition boundary; continuity witness; loss and import accounting | Mechanism-level oxygen-evolution evidence; does not prove a broader continuity ledger or agency surface. |
| The source set supports a water-oxidation boundary in which water, absorbed light, redox cofactors, and catalytic protein structure are not interchangeable quantities. | `R0`, `K0`, `S0`, `M0`, `T`, `B` | Typed measurement family; mechanism and transition boundary | Does not yet specify the full packet source/target regimes or admissibility classes. |
| The review orientation sources connect water oxidation to electron transfer toward NADP+ and proton-gradient-coupled ATP formation in the light reactions. | `T`, `C`, `M1`, `L`, `I` | Mechanism and transition boundary; loss and import accounting | Orientation only until matched primary biochemical sources are selected for field population. |
| The immediate mechanism products include O2 evolution, reducing equivalents, and proton-gradient/ATP coupling rather than a single conserved scalar. | `M1`, `C`, `L`, `I` | Typed measurement family; continuity witness | Supports typed separation only; does not compare photon energy, chemical free energy, biomass, or agency as one unit. |

### Typed Quantities

| Quantity | Type or unit | Source context | Non-comparable with |
|---|---|---|---|
| Photon absorption | Electromagnetic energy event at pigment/protein complexes | Light-driven photosystem reactions. | Biomass, ecological opportunity, organismal agency, Bitcoin chainwork. |
| Water | Molecular substrate and electron source | Water oxidation at photosystem II. | Photon energy, O2, NADPH, ATP, agency. |
| Electrons | Redox transfer units | Water oxidation and downstream electron transfer. | Energy value, biomass mass, ecological fitness, action space. |
| Protons | H+ concentration and electrochemical-gradient contributors | Water oxidation and proton-gradient coupling. | Electrons, O2, ATP count, agency surface. |
| Mn4CaO5 cluster | Catalytic metal-oxo structure | Umena et al. PSII structure and Shen review. | Light energy, chemical free energy, organism-level agency. |
| S-state sequence | Redox/charge-accumulation state model | Kok et al. oxygen-evolution mechanism. | Biomass, ecological feedback, final CL-001 gate status. |
| Molecular oxygen | O2 product | Oxygen evolution from water oxidation. | ATP, NADPH, biomass, agency, value. |
| NADP+/NADPH | Redox cofactor pair | Orientation sources for light-reaction electron transfer. | Proton motive force, ATP, O2, biomass, agency. |
| ATP/ADP/Pi | Phosphorylation energy carrier system | Orientation sources for proton-gradient-coupled ATP synthesis. | Photon count, O2 molecules, carbon fixation, ecological agency. |

### Losses And Imports

| Loss or import | Applies to field | Source support | Open burden |
|---|---|---|---|
| The mechanism imports a highly structured photosynthetic apparatus, including pigments, photosystem II protein organization, catalytic metal cluster, membrane context, and cofactors. | `I`, `S0`, `B`, `V` | Umena et al. and Shen support PSII structural specificity. | Later packet work must record this apparatus as an import rather than treating sunlight alone as sufficient. |
| Light energy is not wholly preserved as one target product; heat, fluorescence, non-photochemical quenching, repair costs, and inefficiency remain outside this dossier. | `L`, `V` | The source set supports conversion mechanism, not a full loss budget. | Later evidence must quantify or explicitly leave open efficiency and dissipation. |
| Water oxidation supplies electrons and O2, but carbon fixation and biomass production require CO2, enzymes, nutrients, and cellular regulation not established here. | `I`, `M1`, `P`, `A` | This mechanism dossier does not include Calvin-cycle or ecological primary sources. | A later dossier must handle carbon fixation and biomass boundaries before agency claims. |
| Review-level integration imports synthesis across multiple studies. | `V` | Shen and Allen are review/orientation sources. | Material packet fields need primary-source traceability or explicit review-grade limits. |

### Agency And Feedback Burden

| Candidate surface or feedback | Source support | Missing burden | Null pressure |
|---|---|---|---|
| Light-driven water oxidation and electron/proton transfer as a biochemical conversion surface. | Primary PSII structure and oxygen-evolution mechanism sources support a physical conversion mechanism. | Does not establish that an organismal or ecological agency surface is created or recruited. | Solar heating of inert matter also converts light into physical change without agency; the packet must show more than energy absorption. |
| Proton-gradient/ATP coupling as immediate biochemical feedback. | Orientation sources support coupling in light reactions. | Needs primary biochemical source selection and must not become an agency claim by itself. | Ordinary biochemical-control and thermodynamic absorbers remain live. |
| Oxygen evolution as a downstream environmental effect. | Mechanism sources support O2 evolution from water oxidation. | Does not establish ecological action classes, atmospheric transformation, or evolutionary agency. | O2 production can be recorded as product without proving a continuity-ledger escape. |

### What This Source Does Not Establish

This dossier does not populate the oxygenic photosynthesis packet fields. It
does not score any gate, issue a CL-001 verdict, accept a repo-owned claim, or
establish an organismal/ecological agency-surface dossier.

It does not establish:

- carbon fixation, biomass accumulation, or growth boundaries;
- organismal behavior, ecological opportunity, or evolutionary feedback;
- complete efficiency, heat, repair, or dissipation accounting;
- a class-relative no-go or constructive escape witness;
- that photosynthesis should pass any CL-001 gate; or
- that the photosynthesis target differs from the solar-heating inert-matter
  null for a non-definitional reason.

### Falsifiers And Reopen Conditions

Reopen or supersede this dossier if:

- later review finds that the source set conflates water oxidation with carbon
  fixation, biomass, ecology, or agency;
- a better primary source replaces the review-level orientation sources for
  linear electron transport or ATP/NADPH coupling;
- the packet starts treating photon energy, redox cofactors, ATP, biomass, and
  agency as interchangeable quantities;
- loss and import accounting needs a primary efficiency or photoprotection
  source before field population; or
- null-packet construction shows that the same mechanism evidence can satisfy
  the target burden without a self-maintaining biochemical or ecological
  agency loop.

## No Claim Promotion

This source dossier cannot promote a CL-001 packet, gate, experiment verdict,
or repo-owned claim. It only records source extraction work for later review.
