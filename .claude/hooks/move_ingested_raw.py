from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ROOT / ".raw" / ".manifest.json"
INBOX_PREFIX = ".raw/inbox/"
INGESTED_PREFIX = ".raw/ingested/"
TEXT_SUFFIXES = {".md", ".json", ".txt", ".yml", ".yaml"}
BUCKET_MAP = {
    "chapter": "chapters",
    "appendix": "appendices",
    "preface": "preface",
}


def load_event() -> dict:
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def touched_path(event: dict) -> str:
    candidates = [
        event.get("tool_input", {}).get("file_path"),
        event.get("tool_response", {}).get("filePath"),
    ]
    for value in candidates:
        if value:
            return str(value).replace("\\", "/")
    return ""


def should_attempt(event: dict) -> bool:
    path = touched_path(event)
    if not path:
        return False
    normalized = path.lower()
    return any(token in normalized for token in ["/.raw/.manifest.json", "/wiki/", "/.raw/inbox/"])


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def parse_frontmatter(note_path: Path) -> dict:
    text = note_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    frontmatter = text[4:end].splitlines()
    data: dict[str, str] = {}
    for line in frontmatter:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def infer_destination(old_rel: str) -> str:
    filename = Path(old_rel).name
    source_dir = ROOT / "wiki" / "sources"
    domain = "unknown"
    module = "unknown"
    bucket = "misc"

    if source_dir.exists():
        for note in source_dir.rglob("*.md"):
            text = note.read_text(encoding="utf-8")
            if f"raw_file: {old_rel}" not in text:
                continue
            fm = parse_frontmatter(note)
            domain = fm.get("domain", domain)
            module = fm.get("module", module)
            subtype = fm.get("subtype", "")
            bucket = BUCKET_MAP.get(subtype, subtype or bucket)
            break

    if bucket == "misc":
        if re.match(r"^第[0-9一二三四五六七八九十]+章_", filename):
            bucket = "chapters"
        elif filename.startswith("附录"):
            bucket = "appendices"
        elif filename.startswith("前言"):
            bucket = "preface"

    return f"{INGESTED_PREFIX}{domain}/{module}/{bucket}/{filename}"


def rewrite_strings(obj, replacements: dict[str, str]):
    if isinstance(obj, str):
        for old, new in replacements.items():
            obj = obj.replace(old, new)
        return obj
    if isinstance(obj, list):
        return [rewrite_strings(item, replacements) for item in obj]
    if isinstance(obj, dict):
        return {key: rewrite_strings(value, replacements) for key, value in obj.items()}
    return obj


def rewrite_repo_text(replacements: dict[str, str]) -> int:
    updated = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        new_text = text
        for old, new in replacements.items():
            new_text = new_text.replace(old, new)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
    return updated


def move_ingested_sources() -> list[tuple[str, str]]:
    if not MANIFEST_PATH.exists():
        return []

    manifest = load_manifest()
    source_entries = manifest.get("sources", {})
    replacements: dict[str, str] = {}

    for old_rel in list(source_entries.keys()):
        if not old_rel.startswith(INBOX_PREFIX):
            continue
        new_rel = infer_destination(old_rel)
        old_path = ROOT / old_rel
        new_path = ROOT / new_rel
        new_path.parent.mkdir(parents=True, exist_ok=True)

        if old_path.exists() and not new_path.exists():
            old_path.rename(new_path)
        elif old_path.exists() and new_path.exists() and old_path.resolve() != new_path.resolve():
            raise RuntimeError(f"Destination already exists: {new_rel}")

        replacements[old_rel] = new_rel

    if not replacements:
        return []

    manifest = rewrite_strings(manifest, replacements)
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    rewrite_repo_text(replacements)
    return sorted(replacements.items())


def main() -> int:
    event = load_event()
    if not should_attempt(event):
        return 0

    moved = move_ingested_sources()
    if not moved:
        return 0

    message = "Moved ingested raw sources from inbox to ingested:\n" + "\n".join(
        f"- {old} -> {new}" for old, new in moved
    )
    print(
        json.dumps(
            {
                "systemMessage": message,
                "suppressOutput": True,
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": message,
                },
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
