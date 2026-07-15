"""Validate the structural shape of CL-001 packet files."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PACKET_DIR = ROOT / "packets" / "cl-001"

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


def front_matter_keys(text: str) -> set[str]:
    if not text.startswith("---\n"):
        return set()
    end = text.find("\n---\n", 4)
    if end == -1:
        return set()
    keys: set[str] = set()
    for line in text[4:end].splitlines():
        if ":" in line:
            keys.add(line.split(":", 1)[0].strip())
    return keys


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

    if errors:
        for error in errors:
            print(error)
        return 1

    print(f"Validated {len(packet_paths)} CL-001 packet files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
