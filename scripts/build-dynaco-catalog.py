#!/usr/bin/env python3
"""Copy Dynaco manuals and build the static catalog used by the website."""
from __future__ import annotations
import json, re, shutil, sys
from pathlib import Path

source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("../../dynaco-source/Manuals")
site = Path(__file__).resolve().parents[1]
target = site / "dynaco/documents/manuals"
catalog_path = site / "dynaco/documents/catalog.json"
target.mkdir(parents=True, exist_ok=True)

for path in sorted(source.glob("*.pdf"), key=lambda p: p.name.lower()):
    shutil.copy2(path, target / path.name)

def title_for(name: str) -> str:
    stem = Path(name).stem.replace("_", " ").replace("-", " ")
    stem = re.sub(r"\s+", " ", stem).strip()
    return stem

def kind_for(name: str) -> str:
    lower = name.lower()
    if "manual" in lower:
        return "Manual"
    if "sch" in lower or "schematic" in lower:
        return "Schematic"
    if "sm" in lower or "service" in lower:
        return "Service literature"
    return "Reference"

items = []
for path in sorted(target.glob("*.pdf"), key=lambda p: p.name.lower()):
    items.append({
        "title": title_for(path.name),
        "kind": kind_for(path.name),
        "filename": path.name,
        "source": f"Manuals/{path.name}",
        "url": f"manuals/{path.name}",
        "bytes": path.stat().st_size,
    })
catalog_path.write_text(json.dumps({"source": "scott-cothrell/Dynaco", "items": items}, indent=2) + "\n")
print(f"Cataloged {len(items)} manuals in {catalog_path}")
