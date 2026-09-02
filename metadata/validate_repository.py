"""Validate canonical metadata, paths, links, difficulty placement, and artifacts."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def markdown_link_failures() -> list[str]:
    failures: list[str] = []
    markdown = [
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    ]
    for document in markdown:
        for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#")):
                continue
            resolved = (document.parent / target).resolve()
            if not resolved.exists():
                failures.append(f"{document.relative_to(ROOT)} -> {target}")
    return failures


def main() -> None:
    problems = json.loads((ROOT / "metadata/problems.json").read_text(encoding="utf-8"))
    errors: list[str] = []
    paths: set[str] = set()
    leetcode_numbers: set[str] = set()
    for item in problems:
        path = item["path"]
        if path in paths:
            errors.append(f"duplicate metadata path: {path}")
        paths.add(path)
        if not (ROOT / path).is_file():
            errors.append(f"missing problem file: {path}")
        readme_path = item.get("readme_path")
        if not readme_path:
            errors.append(f"missing readme metadata: {path}")
        elif not (ROOT / readme_path).is_file():
            errors.append(f"missing problem README: {readme_path}")
        elif Path(readme_path).parent != Path(path).parent:
            errors.append(f"solution/README directory mismatch: {path}")
        if item["platform"] == "LeetCode":
            number = str(item["number"])
            if number in leetcode_numbers:
                errors.append(f"duplicate LeetCode number: {number}")
            leetcode_numbers.add(number)
            expected = item["difficulty"].lower()
            if not path.startswith(f"leetcode/{expected}/"):
                errors.append(f"difficulty/path mismatch: {path}")
    errors.extend(f"broken markdown link: {failure}" for failure in markdown_link_failures())
    forbidden = ("*.cpp", "*.cc", "*.exe", "*.drawio", "*.pyc", "a.out", "tempCodeRunnerFile.*")
    for pattern in forbidden:
        for path in ROOT.rglob(pattern):
            if path.is_file() and ".git" not in path.parts:
                errors.append(f"forbidden artifact: {path.relative_to(ROOT)}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"metadata_records={len(problems)}")
    print(f"leetcode_unique={len(leetcode_numbers)}")
    print("metadata_paths=valid")
    print("difficulty_paths=valid")
    print("markdown_links=valid")
    print("forbidden_artifacts=none")


if __name__ == "__main__":
    main()
