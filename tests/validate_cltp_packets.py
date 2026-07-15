"""Validate the structural shape of CL-001 packet files."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PACKET_DIR = ROOT / "packets" / "cl-001"
SOURCE_INTAKE = ROOT / "evidence" / "cl-001-source-intake.md"
SOURCE_DOSSIER_TEMPLATE = ROOT / "evidence" / "cl-001-source-dossier-template.md"

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

    if "verdict: unscored" not in text:
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

    if errors:
        for error in errors:
            print(error)
        return 1

    print(
        f"Validated {len(packet_paths)} CL-001 packet files, "
        "source intake, and source dossier template."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
