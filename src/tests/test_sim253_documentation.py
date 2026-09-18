from pathlib import Path
import re


DOC_PATH = Path(__file__).resolve().parents[2] / "docs" / "sim253.md"

EXPECTED_SEQUENCE_HEADINGS = [
    "### SEQUENCE 01 — Regional Autonomy (SD)",
    "### SEQUENCE 02 — Settlement Distribution (SD ⊗ AB)",
    "### SEQUENCE 03 — Urban Mosaic (AB ⊗ SD)",
    "### SEQUENCE 04 — Community Scale (SD → AB)",
    "### SEQUENCE 05 — Transportation Networks (DE)",
    "### SEQUENCE 06 — Density & Sacred (SD ⊗ AB)",
    "### SEQUENCE 07 — Nucleus & Activity (AB ⊗ DE)",
    "### SEQUENCE 08 — Housing & Demographics (AB ⊗ SD)",
    "### SEQUENCE 09 — Work & Institutions (AB ⊗ DE)",
    "### SEQUENCE 10 — Paths & Streets (AB)",
    "### SEQUENCE 11 — Community Spaces (AB ⊗ DE)",
    "### SEQUENCE 12 — Life & Death (SD ⊗ AB)",
    "### SEQUENCE 13 — Family & Play (AB)",
    "### SEQUENCE 14 — Work & Commerce (AB ⊗ DE)",
    "### SEQUENCE 15 — Services & Rest (DE)",
    "### SEQUENCE 16 — Building Complex (AB ⊗ DE)",
    "### SEQUENCE 17 — Site & Form (AB)",
    "### SEQUENCE 18 — Envelope & Roof (AB)",
    "### SEQUENCE 19 — Circulation & Gradient (AB ⊗ DE)",
    "### SEQUENCE 20 — Rooms & Light (AB ⊗ DE)",
    "### SEQUENCE 21 — Sleep & Service (AB ⊗ DE)",
    "### SEQUENCE 22 — Work & Independence (AB)",
    "### SEQUENCE 23 — Outdoor Rooms (AB ⊗ SD)",
    "### SEQUENCE 24 — Gardens & Hearth (AB ⊗ SD)",
    "### SEQUENCE 25 — Workspace Layout (AB)",
    "### SEQUENCE 26 — Volume & View (AB)",
    "### SEQUENCE 27 — Volume & View (alt) (AB)",
    "### SEQUENCE 28 — Thick Walls & Storage (AB ⊗ DE)",
    "### SEQUENCE 29 — Structural Principle (DE)",
    "### SEQUENCE 30 — Roof & Floor Layout (DE)",
    "### SEQUENCE 31 — Foundation & Frame (DE)",
    "### SEQUENCE 32 — Openings (DE)",
    "### SEQUENCE 33 — Columns & Services (DE ⊗ SD)",
    "### SEQUENCE 34 — Surfaces & Finishes (DE)",
    "### SEQUENCE 35 — Outdoor Details (DE ⊗ SD)",
    "### SEQUENCE 36 — Ornament & Life (DE ⊗ AB)",
]


def _load_document() -> str:
    return DOC_PATH.read_text(encoding="utf-8")


def test_sim253_sequence_headings_match_index() -> None:
    document = _load_document()

    headings = re.findall(r"^### SEQUENCE \d{2} .*?$", document, flags=re.MULTILINE)
    assert headings == EXPECTED_SEQUENCE_HEADINGS


def test_sim253_pattern_references_cover_all_253_patterns() -> None:
    document = _load_document()

    covered_patterns = {
        int(match) for match in re.findall(r"\*\*APL(\d{3})\b", document)
    }

    for start, end in re.findall(r"\*\*Patterns: APL(\d{3})(?:[–-]APL(\d{3}))?\*\*", document):
        range_end = end or start
        covered_patterns.update(range(int(start), int(range_end) + 1))

    expected_patterns = set(range(1, 254))
    assert covered_patterns == expected_patterns


if __name__ == "__main__":
    test_sim253_sequence_headings_match_index()
    test_sim253_pattern_references_cover_all_253_patterns()
    print("sim253 documentation checks passed")
