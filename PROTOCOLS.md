# CCP Protocols and Standards

## File Hygiene

One-off scripts, logs, and analysis files often clutter the root directory during development. To maintain a clean repository, follow these rules:

1.  **Immediate Archival**: Files created for a specific one-time task (e.g., debug logs, data migration scripts, schema checks) must be moved to the `archive/` directory immediately after their utility is exhausted.
    *   Logs go to `archive/logs/`
    *   Scripts go to `archive/scripts/`
    *   SQL dumps go to `archive/sql/`
    *   Data analysis files go to `archive/analysis/`

2.  **No Root Clutter**: Do not commit `debug.log`, `temp.txt`, or similar scratchpad files to the root directory. If a file is needed temporarily, add it to `.gitignore` or clean it up before committing.

3.  **Naming Convention**: Archive files should retain descriptive names so they can be identified later if needed.

---

## Cartographic Context Protocol (CCP) - Minimal Standard

To keep CCP efficient, LEGEND files follow a minimal required standard:

1. **Parent Region**: Link to the parent `LEGEND.md` (or `None (root)`).
2. **Context**: One short sentence describing the directory's responsibility.
3. **Local Laws**: A few bullets for local constraints or "none" if not applicable.
4. **Inventory Table**: The CCP inventory block between `<!-- CCP_INVENTORY_START -->` and `<!-- CCP_INVENTORY_END -->`.

**Per-file purposes are optional.** If present, keep them concise. Do not add per-file detail unless needed for clarity or explicitly requested.

### Example Minimal LEGEND.md

```markdown
# 📍 LEGEND: Example Directory

**Parent Region:** [Root](file:///path/to/parent/LEGEND.md)  
**Context:** Brief one-sentence description of this directory's responsibility.

## 🏢 BUILDINGS (Files)

<!-- CCP_INVENTORY_START -->
| File | Purpose |
| :--- | :--- |
| `example.py` | Optional brief purpose |
<!-- CCP_INVENTORY_END -->

## 🚧 LOCAL LAWS
* Constraint 1
* Constraint 2
* Or "None" if no special rules apply
```

---

## Version Control

* All version numbers must be synchronized across `README.md`, `SYSTEM_PROMPT.md`, and release notes
* Every protocol change requires a corresponding `RELEASE_NOTES_vX.X.X.md` file
* Update the Version History section in `README.md` when releasing new versions

---

## Repository Self-Compliance

This repository must dogfood CCP:
* Every directory must have a `LEGEND.md` file
* Follow the Navigation Loop when making changes
* Use the Efficiency Rules to avoid repetitive operations
* Archive one-off files immediately after use
