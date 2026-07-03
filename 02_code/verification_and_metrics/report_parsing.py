"""
Shared parsing helpers for extracting fields from auto_verifier_v2.py's generated
audit_*.md reports.

Previously, aggregate_pdc2021.py, operator_exposure_analysis.py, and
big_table_fractional_exposure.py each independently reimplemented the same regex
against the "Dataset & Audit Overview" markdown table. The matching/extraction logic is
consolidated here; each caller still supplies its own list of label strings to look up,
so a *label* rename in auto_verifier_v2.py's overview table must still be mirrored in
every caller's field list, but the regex and parsing rules change in one place only.

Targets the CURRENT table format (`**Label** | `value` |`). Does not match the older
bold-colon report format (`**Label:** `value``) used before that format change.
"""
import re
from pathlib import Path
from typing import Dict, Iterable, Optional

_OVERVIEW_RE_CACHE: Dict[str, re.Pattern] = {}


def _overview_pattern(label: str) -> re.Pattern:
    pattern = _OVERVIEW_RE_CACHE.get(label)
    if pattern is None:
        pattern = re.compile(rf"\*\*{re.escape(label)}\*\*\s*\|\s*`([^`]*)`")
        _OVERVIEW_RE_CACHE[label] = pattern
    return pattern


def extract_overview_fields(text: str, labels: Iterable[str]) -> Dict[str, Optional[str]]:
    """Returns {label: raw_string_value_or_None} for every requested label found in
    the report's Dataset & Audit Overview table. Values are raw strings (whitespace
    -stripped, % sign kept) -- callers decide their own float conversion and
    missing-field handling, since scripts differ on whether a missing field should be
    skipped, void the whole row, or default to 0."""
    result = {}
    for label in labels:
        m = _overview_pattern(label).search(text)
        result[label] = m.group(1).strip() if m else None
    return result


def extract_overview_fields_from_file(path: Path, labels: Iterable[str]) -> Dict[str, Optional[str]]:
    return extract_overview_fields(path.read_text(encoding="utf-8"), labels)


def to_float(value: Optional[str], strip_percent: bool = True) -> Optional[float]:
    """Best-effort string-to-float conversion: returns None for missing/unparseable
    values (e.g. 'N/A', 'N/A (skipped)') rather than raising."""
    if value is None:
        return None
    cleaned = value.rstrip("%") if strip_percent else value
    try:
        return float(cleaned)
    except ValueError:
        return None


_SKIPPED_PATTERN = re.compile(r"\*\*Skipped \(Complexity > 1000\):\*\*\s*(\d+)")


def extract_skipped_count(text: str) -> float:
    """The 'Skipped (Complexity > 1000)' count lives in the Audit Summary bullet
    list, not the Dataset & Audit Overview table, so it needs its own pattern."""
    m = _SKIPPED_PATTERN.search(text)
    return float(m.group(1)) if m else 0.0
