"""Validate the structural shape of CL-001 packet files."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PACKET_DIR = ROOT / "packets" / "cl-001"
SOURCE_INTAKE = ROOT / "evidence" / "cl-001-source-intake.md"
SOURCE_DOSSIER_TEMPLATE = ROOT / "evidence" / "cl-001-source-dossier-template.md"
SOURCE_DOSSIER_MANIFEST = ROOT / "evidence" / "cl-001-source-dossier-manifest.md"
SOURCE_DOSSIER_DIR = ROOT / "evidence" / "cl-001-dossiers"
ACTIVE_CL001_EXPERIMENT = ROOT / "experiments" / "CL-001-interval-sweep.md"
RETIRED_CL001_EXPERIMENT = (
    ROOT / "experiments" / "CL-001-bitcoin-photosynthesis-pair-and-null.md"
)

REQUIRED_FRONT_MATTER = (
    "packet_id",
    "status",
    "packet_role",
    "experiment",
    "evidence_grade",
    "verdict",
)

REQUIRED_FIELDS = (
    "R0",
    "K0",
    "S0",
    "M0",
    "T",
    "B",
    "R1",
    "K1",
    "S1",
    "M1",
    "C",
    "L",
    "I",
    "P",
    "A",
    "Omega",
    "N",
    "X",
    "F",
    "Z",
    "V",
)

REQUIRED_GATES = (
    "Typing gate",
    "Provenance gate",
    "Transduction gate",
    "Continuity gate",
    "Loss/import gate",
    "Agency gate",
    "No-go/escape gate",
    "Feedback gate",
    "Absorber gate",
    "Neutrality gate",
)

REQUIRED_SOURCE_INTAKE_LANES = (
    "Mechanism and transition boundary",
    "Regime and class definition",
    "Typed measurement family",
    "Loss and import accounting",
    "Agency surface and action space",
    "Class-relative no-go or constraint",
    "Feedback and recurrence",
    "Absorber and null pressure",
    "Falsifiers and open fields",
)

REQUIRED_DOSSIER_SECTIONS = (
    "## Required Dossier Metadata",
    "## Required Dossier Sections",
    "### Source Boundary",
    "### Scoped Extraction",
    "### Typed Quantities",
    "### Losses And Imports",
    "### Agency And Feedback Burden",
    "### What This Source Does Not Establish",
    "### Falsifiers And Reopen Conditions",
    "## No Claim Promotion",
)

REQUIRED_DOSSIER_METADATA = (
    "source_id",
    "source_type",
    "applies_to_packets",
    "evidence_lanes",
    "provenance",
    "extracted_by",
    "extracted_on",
    "status",
)

REQUIRED_DOSSIER_MANIFEST_SECTIONS = (
    "## Purpose",
    "## Packet Coverage",
    "## Dossier Queue",
    "## Symmetry Checks",
    "## No Claim Promotion",
)

REQUIRED_DOSSIER_FRONT_MATTER = (
    "source_id",
    "source_type",
    "applies_to_packets",
    "evidence_lanes",
    "provenance",
    "extracted_by",
    "extracted_on",
    "status",
    "claim_status",
    "verdict",
)

REQUIRED_DOSSIER_FILE_SECTIONS = (
    "## Source Boundary",
    "### Scoped Extraction",
    "### Typed Quantities",
    "### Losses And Imports",
    "### Agency And Feedback Burden",
    "### What This Source Does Not Establish",
    "### Falsifiers And Reopen Conditions",
    "## No Claim Promotion",
)

MANIFEST_DOSSIER_PATH_RE = re.compile(r"`(evidence/cl-001-dossiers/[^`]+\.md)`")


def front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    return values


def front_matter_keys(text: str) -> set[str]:
    return set(front_matter(text))


def split_front_matter_list(value: str) -> list[str]:
    return [
        item.strip()
        for item in re.split(r"[;,]", value)
        if item.strip()
    ]


def validate_packet(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    keys = front_matter_keys(text)
    for key in REQUIRED_FRONT_MATTER:
        if key not in keys:
            errors.append(f"{path.relative_to(ROOT)} missing front matter key {key}")

    if "## CLTP Fields" not in text:
        errors.append(f"{path.relative_to(ROOT)} missing CLTP Fields section")

    if "## Gate Receipts" not in text:
        errors.append(f"{path.relative_to(ROOT)} missing Gate Receipts section")

    for field in REQUIRED_FIELDS:
        if f"`{field}`" not in text:
            errors.append(f"{path.relative_to(ROOT)} missing field `{field}`")

    for gate in REQUIRED_GATES:
        if gate not in text:
            errors.append(f"{path.relative_to(ROOT)} missing {gate}")

    if "## No Claim Promotion" not in text:
        errors.append(f"{path.relative_to(ROOT)} missing No Claim Promotion section")

    # Scope this to parsed front matter, not a whole-file substring scan. A
    # scan passes whenever the literal appears anywhere -- prose, a table cell,
    # a fenced block -- so a packet could carry `verdict: SHARED_STRUCTURE` in
    # its front matter and still validate. This is the guard on a source
    # verdict, so it has to read the field it claims to read.
    if front_matter(text).get("verdict") != "unscored":
        errors.append(f"{path.relative_to(ROOT)} is not explicitly unscored")

    return errors


def validate_source_intake(packet_paths: list[Path]) -> list[str]:
    errors: list[str] = []
    if not SOURCE_INTAKE.exists():
        return [f"Missing source intake contract: {SOURCE_INTAKE.relative_to(ROOT)}"]

    text = SOURCE_INTAKE.read_text(encoding="utf-8")
    for path in packet_paths:
        packet_text = path.read_text(encoding="utf-8")
        packet_id = front_matter(packet_text).get("packet_id", "")
        if not packet_id:
            errors.append(f"{path.relative_to(ROOT)} missing packet_id for intake check")
            continue
        if packet_id not in text:
            errors.append(
                f"{SOURCE_INTAKE.relative_to(ROOT)} missing packet id {packet_id}"
            )

    for lane in REQUIRED_SOURCE_INTAKE_LANES:
        if lane not in text:
            errors.append(f"{SOURCE_INTAKE.relative_to(ROOT)} missing lane {lane}")

    required_phrases = (
        "not evidence",
        "score any gate",
        "No Claim Promotion",
        "Pending exact source pass.",
    )
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(f"{SOURCE_INTAKE.relative_to(ROOT)} missing phrase {phrase}")

    return errors


def validate_source_dossier_template() -> list[str]:
    errors: list[str] = []
    if not SOURCE_DOSSIER_TEMPLATE.exists():
        return [
            "Missing source dossier template: "
            f"{SOURCE_DOSSIER_TEMPLATE.relative_to(ROOT)}"
        ]

    text = SOURCE_DOSSIER_TEMPLATE.read_text(encoding="utf-8")
    for section in REQUIRED_DOSSIER_SECTIONS:
        if section not in text:
            errors.append(
                f"{SOURCE_DOSSIER_TEMPLATE.relative_to(ROOT)} missing {section}"
            )

    for field in REQUIRED_DOSSIER_METADATA:
        if f"`{field}`" not in text:
            errors.append(
                f"{SOURCE_DOSSIER_TEMPLATE.relative_to(ROOT)} missing metadata `{field}`"
            )

    required_phrases = (
        "does not score any gate",
        "cannot promote a CL-001 packet",
        "Secondary orientation sources cannot populate material packet fields",
    )
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(
                f"{SOURCE_DOSSIER_TEMPLATE.relative_to(ROOT)} missing phrase {phrase}"
            )

    return errors


def validate_source_dossier_manifest(packet_paths: list[Path]) -> list[str]:
    errors: list[str] = []
    if not SOURCE_DOSSIER_MANIFEST.exists():
        return [
            "Missing source dossier manifest: "
            f"{SOURCE_DOSSIER_MANIFEST.relative_to(ROOT)}"
        ]

    text = SOURCE_DOSSIER_MANIFEST.read_text(encoding="utf-8")
    keys = front_matter_keys(text)
    for key in ("artifact_type", "status", "experiment", "claim_status", "verdict"):
        if key not in keys:
            errors.append(
                f"{SOURCE_DOSSIER_MANIFEST.relative_to(ROOT)} "
                f"missing front matter key {key}"
            )

    for section in REQUIRED_DOSSIER_MANIFEST_SECTIONS:
        if section not in text:
            errors.append(
                f"{SOURCE_DOSSIER_MANIFEST.relative_to(ROOT)} missing {section}"
            )

    for path in packet_paths:
        packet_text = path.read_text(encoding="utf-8")
        packet_id = front_matter(packet_text).get("packet_id", "")
        if not packet_id:
            errors.append(f"{path.relative_to(ROOT)} missing packet_id for manifest")
            continue
        if packet_id not in text:
            errors.append(
                f"{SOURCE_DOSSIER_MANIFEST.relative_to(ROOT)} "
                f"missing packet id {packet_id}"
            )
        if str(path.relative_to(ROOT)).replace("\\", "/") not in text:
            errors.append(
                f"{SOURCE_DOSSIER_MANIFEST.relative_to(ROOT)} "
                f"missing packet file {path.relative_to(ROOT)}"
            )

    for lane in REQUIRED_SOURCE_INTAKE_LANES:
        if lane.lower() not in text.lower():
            errors.append(
                f"{SOURCE_DOSSIER_MANIFEST.relative_to(ROOT)} missing lane {lane}"
            )

    required_phrases = (
        "not evidence",
        "does not score any gate",
        "Pending exact source selection.",
        "No Claim Promotion",
        "cannot promote a CL-001 packet",
    )
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(
                f"{SOURCE_DOSSIER_MANIFEST.relative_to(ROOT)} missing phrase {phrase}"
            )

    manifest_dossier_paths = {
        (ROOT / raw_path).resolve()
        for raw_path in MANIFEST_DOSSIER_PATH_RE.findall(text)
    }
    dossier_paths = {
        path.resolve() for path in SOURCE_DOSSIER_DIR.glob("*.md")
    } if SOURCE_DOSSIER_DIR.exists() else set()

    if not manifest_dossier_paths:
        errors.append(
            f"{SOURCE_DOSSIER_MANIFEST.relative_to(ROOT)} "
            "does not reference any draft dossier files"
        )

    for path in sorted(manifest_dossier_paths):
        if not path.exists():
            errors.append(
                f"{SOURCE_DOSSIER_MANIFEST.relative_to(ROOT)} references missing "
                f"dossier {path.relative_to(ROOT)}"
            )

    for path in sorted(dossier_paths - manifest_dossier_paths):
        errors.append(
            f"{path.relative_to(ROOT)} is not referenced by "
            f"{SOURCE_DOSSIER_MANIFEST.relative_to(ROOT)}"
        )

    return errors


def validate_source_dossiers(packet_paths: list[Path]) -> list[str]:
    errors: list[str] = []
    if not SOURCE_DOSSIER_DIR.exists():
        return errors

    packet_ids = {
        front_matter(path.read_text(encoding="utf-8")).get("packet_id", "")
        for path in packet_paths
    }
    source_ids: dict[str, Path] = {}
    allowed_lanes = {lane.lower() for lane in REQUIRED_SOURCE_INTAKE_LANES}

    for path in sorted(SOURCE_DOSSIER_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        keys = front_matter_keys(text)
        values = front_matter(text)

        for key in REQUIRED_DOSSIER_FRONT_MATTER:
            if key not in keys:
                errors.append(f"{path.relative_to(ROOT)} missing front matter key {key}")

        for section in REQUIRED_DOSSIER_FILE_SECTIONS:
            if section not in text:
                errors.append(f"{path.relative_to(ROOT)} missing {section}")

        applies_to = values.get("applies_to_packets", "")
        applies_to_packets = split_front_matter_list(applies_to)
        if not applies_to_packets:
            errors.append(f"{path.relative_to(ROOT)} does not name a packet")
        for packet_id in applies_to_packets:
            if packet_id not in packet_ids:
                errors.append(
                    f"{path.relative_to(ROOT)} applies to unknown packet {packet_id}"
                )

        source_id = values.get("source_id", "")
        if source_id in source_ids:
            errors.append(
                f"{path.relative_to(ROOT)} duplicates source_id {source_id} "
                f"from {source_ids[source_id].relative_to(ROOT)}"
            )
        elif source_id:
            source_ids[source_id] = path

        if values.get("status") != "draft":
            errors.append(f"{path.relative_to(ROOT)} is not status: draft")

        if values.get("claim_status") != "none":
            errors.append(f"{path.relative_to(ROOT)} can move claim status")

        if values.get("verdict") != "none":
            errors.append(f"{path.relative_to(ROOT)} can move verdict status")

        lanes = split_front_matter_list(values.get("evidence_lanes", ""))
        if not lanes:
            errors.append(f"{path.relative_to(ROOT)} does not name evidence lanes")
        for lane in lanes:
            if lane.lower() not in allowed_lanes:
                errors.append(
                    f"{path.relative_to(ROOT)} uses unknown evidence lane {lane}"
                )

        required_phrases = (
            "does not populate",
            "does not score any gate",
            "cannot promote a CL-001 packet",
        )
        for phrase in required_phrases:
            if phrase not in text:
                errors.append(f"{path.relative_to(ROOT)} missing phrase {phrase}")

    return errors


def validate_cl001_experiment_state() -> list[str]:
    errors: list[str] = []
    if not ACTIVE_CL001_EXPERIMENT.exists():
        return [
            "Missing active CL-001 scaffold: "
            f"{ACTIVE_CL001_EXPERIMENT.relative_to(ROOT)}"
        ]

    active_text = ACTIVE_CL001_EXPERIMENT.read_text(encoding="utf-8")
    active_required = (
        "status: active_scaffold",
        "# CL-001: Interval Sweep",
        "dollar",
        "Bitcoin",
        "`T` as the only free field",
        "## No Claim Promotion",
        "cannot populate a CL-001 packet",
    )
    for phrase in active_required:
        if phrase not in active_text:
            errors.append(
                f"{ACTIVE_CL001_EXPERIMENT.relative_to(ROOT)} missing phrase {phrase}"
            )

    if not RETIRED_CL001_EXPERIMENT.exists():
        errors.append(
            "Missing retired CL-001 scaffold: "
            f"{RETIRED_CL001_EXPERIMENT.relative_to(ROOT)}"
        )
        return errors

    retired_text = RETIRED_CL001_EXPERIMENT.read_text(encoding="utf-8")
    retired_required = (
        "Status: retired founding experiment.",
        "not the active CL-001 experiment",
        "experiments/CL-001-interval-sweep.md",
    )
    for phrase in retired_required:
        if phrase not in retired_text:
            errors.append(
                f"{RETIRED_CL001_EXPERIMENT.relative_to(ROOT)} "
                f"missing phrase {phrase}"
            )

    return errors


def main() -> int:
    if not PACKET_DIR.exists():
        print(f"Missing packet directory: {PACKET_DIR.relative_to(ROOT)}")
        return 1

    packet_paths = sorted(
        path for path in PACKET_DIR.glob("*.md") if path.name != "README.md"
    )
    if not packet_paths:
        print(f"No packet files found in {PACKET_DIR.relative_to(ROOT)}")
        return 1

    errors: list[str] = []
    for path in packet_paths:
        errors.extend(validate_packet(path))
    errors.extend(validate_source_intake(packet_paths))
    errors.extend(validate_source_dossier_template())
    errors.extend(validate_source_dossier_manifest(packet_paths))
    errors.extend(validate_source_dossiers(packet_paths))
    errors.extend(validate_cl001_experiment_state())

    if errors:
        for error in errors:
            print(error)
        return 1

    print(
        f"Validated {len(packet_paths)} CL-001 packet files, "
        "source intake, source dossier template, source dossier manifest, "
        "source dossiers, and experiment state."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
