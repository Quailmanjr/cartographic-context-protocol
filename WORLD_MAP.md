# 🗺️ WORLD MAP

**Project Name:** Cartographic Context Protocol
**North Star:** Provide a file-system based navigation standard for AI agents to optimize context usage and reduce token consumption

## 🏗️ REGIONS (Top-Level Directories)

### `/templates`
* **Responsibility:** Holds template files for LEGEND.md and WORLD_MAP.md used during CCP installation
* **Key Artifacts:** `LEGEND.template.md`, `WORLD_MAP.template.md`
* **Access Rules:** Read-only templates, used by installation scripts

### `/scripts`
* **Responsibility:** Contains automation scripts for CCP installation and maintenance
* **Key Artifacts:** `install_ccp.py`, `update_maps.py`
* **Access Rules:** Execute with appropriate permissions, modifies target repositories

### `/docs` (Implicit)
* **Responsibility:** Documentation files including protocol specifications and guides
* **Key Artifacts:** `README.md`, `SYSTEM_PROMPT.md`, `CONTEXT.md`, `RELEASE_NOTES_*.md`, `CCP_CASE_STUDY.md`
* **Access Rules:** Read-only for reference, update when protocol changes

## 🧭 CRITICAL PATHS
* **Entry Point:** `README.md` (Protocol specification and overview)
* **Config:** `SYSTEM_PROMPT.md` (Behavioral rules for CCP-compliant agents)
* **Installation:** `scripts/install_ccp.py` (Installs CCP into target repositories)
* **Maintenance:** `scripts/update_maps.py` (Auto-cartographer for Legend updates)
