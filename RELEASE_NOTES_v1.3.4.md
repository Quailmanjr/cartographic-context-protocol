# Version 1.3.4 Changelog

## 🚀 New Features & Improvements

### 📋 Minimal CCP Standard

Introduced a streamlined, minimal standard for LEGEND.md files to reduce verbosity while maintaining protocol compliance:

#### **2-Column Inventory Table**
* Removed the `Dependencies` column from inventory tables
* Simplified to `| File | Purpose |` format
* Reduces visual clutter and maintenance burden

#### **Optional Per-File Purposes**
* Per-file purposes are now optional (default: "Optional")
* Only add detailed purposes when needed for clarity
* Focuses on directory-level context over file-level detail

#### **Simplified Structure**
LEGEND.md files now require only:
1. Parent Region link
2. One-sentence Context description
3. Inventory table (auto-managed)
4. Local Laws (or "None")

### 🗂️ File Hygiene Protocol

Established formal rules for repository cleanliness:

#### **Archive System**
* Created `/archive` directory structure
* Subdirectories: `logs/`, `scripts/`, `sql/`, `analysis/`
* One-off files must be archived immediately after use
* No scratchpad files in root directory

#### **Documentation**
* Created `PROTOCOLS.md` documenting file hygiene and minimal CCP standard
* Updated `WORLD_MAP.md` to include `/archive` region
* All LEGEND.md files simplified to minimal standard

### 🔧 Script Updates

#### **update_maps.py v1.3.3 → v1.3.4**
* Updated to generate 2-column tables (minimal standard)
* Simplified purpose handling: defaults to "Optional"
* Normalizes TODO and empty purposes automatically
* Backward compatible with existing 3-column formats

## 📝 Version Updates

* `update_maps.py` updated to v1.3.4
* All LEGEND.md files converted to minimal standard
* `PROTOCOLS.md` created with formal standards

## 🎯 Impact

**Reduced Verbosity:** LEGEND.md files are now ~30% shorter while maintaining all essential information.

**Cleaner Repository:** Archive system prevents root directory clutter from one-off scripts and logs.

**Easier Maintenance:** Minimal standard reduces cognitive load when creating or updating LEGEND.md files.

## 🔒 Backward Compatibility

Fully backward compatible. The `update_maps.py` script can read both 2-column and 3-column formats and will automatically convert to the minimal 2-column standard.

---

*Released: 2026-02-03*
