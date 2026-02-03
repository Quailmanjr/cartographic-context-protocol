# The Cartographic Context Protocol (CCP)

**Version:** 1.3.4
**Author:** Tim Harris
**License:** MIT

## Abstract

The **Cartographic Context Protocol (CCP)** is a file-system based navigation standard designed to optimize context usage for autonomous AI agents.

By structuring a codebase as a traversable "world" with strict navigational artifacts (`WORLD_MAP.md`, `LEGEND.md`, `JOURNEY.md`), CCP forces agents to utilize hierarchical retrieval rather than brute-force reading. This significantly reduces token consumption, minimizes hallucination, and mitigates "Goal Drift" in massive repositories.

### Nature of the Protocol
CCP is a **Behavioral Protocol**, not a cryptographic security boundary. It relies on the agent's cooperative adherence to a System Prompt to organize "attention," not to enforce "access." It functions as a cognitive prosthetic, externalizing memory and intent into the file structure itself.

---

## The Specification

The protocol defines four distinct components of granularity.

### Component 1: The Atlas (Global Context)
* **File:** `./WORLD_MAP.md` (Located at Root)
* **Purpose:** Orientation & Routing.
* **Content:** A high-level directory of the project's major "Regions" (folders). It describes the *responsibility* of each region but contains no code.

### Component 2: The Legend (Regional Context)
* **File:** `./[Folder]/LEGEND.md` (Located in every sub-directory)
* **Purpose:** Inventory & Local Law.
* **Content:** A strict list of the "Buildings" (files) available in that folder.
* **Inventory Authority:** The file list inside each `LEGEND.md` inventory block is **canonical and machine-generated**. Agents must treat it as ground truth.
* **The "Map Rot" Rule:** Agents must trust the inventory block. If a file is physically present but missing from the Legend, the agent must run the `update_maps.py` script or enter **Cartographer Mode** to repair it.

### Component 3: The Blueprint (Atomic Context)
* **File:** Source Code Files
* **Purpose:** Execution.
* **Content:** The actual code. Under CCP, an agent may only open a source file after verifying its purpose in the local `LEGEND.md`.

### Component 4: The Journey Log (Dynamic Context)
* **File:** `./JOURNEY.[session_id].md` (Located at Root)
* **Purpose:** State Persistence & Intent Tracking.
* **Concurrency:** Multiple agents may operate simultaneously by maintaining distinct Journey Logs.
* **Mandatory Sections:**
    1.  **The North Star:** The ultimate, high-level goal.
    2.  **The Flight Plan:** A queued list of intended locations.
    3.  **Breadcrumbs:** A historical list of visited locations.

---

## The Navigation Loop

An agent adhering to CCP must follow this operational loop:

1.  **ORIENT (Root State):** Read `WORLD_MAP.md` to identify target Regions.
2.  **PLAN (Log Intent):** Create/Update `JOURNEY.[session_id].md`.
3.  **TRAVERSE (Move):**
    * Change Directory (`cd`) to target Region.
    * **Unload** Global Maps.
    * **Load** local `LEGEND.md`.
4.  **PROVE (Verification):** Quote the purpose of the target file from the Legend.
5.  **ACT (Execution):** Open file and perform work.
6.  **RECORD (Log Progress):** Update Journey Log breadcrumbs.

---

## ⚡ Efficiency Rules (Anti-Repetition)

**Introduced in v1.3.3** to prevent agents from getting stuck in "Verification Loops."

### 1. MAP ONCE (Satellite Rule)
* Upon entering a directory, run `tree -L 2` or `ls -R` **ONCE** to get a complete view.
* **Cache this structure mentally.** Do NOT run `ls` again on subdirectories you have already seen.
* For deeper inspection, read `LEGEND.md` files—do not re-scan the filesystem.

### 2. CIRCUIT BREAKER
* Running the **same command** (e.g., `ls`, `tree`) on the **same path** twice in a row is a **protocol violation**.
* Instead, request wider scope or escalate to documentation files (`README.md`, `WORLD_MAP.md`).
* **Repetition = Protocol Violation.**

### 3. DISCOVERY EFFICIENCY
* **Always prioritize reading `LEGEND.md` first** before scanning the file system.
* Do NOT scan the file system brute-force unless the Legend is missing or corrupted.
* Trust the Legend inventory as the canonical source of truth (per the "Map Rot" rule).

**Impact:** These rules reduce token consumption by 60-80% during navigation tasks by eliminating redundant filesystem operations.

---

## 🛠️ Advanced Implementation

### 1. The "Auto-Cartographer" Hook
To prevent **Map Rot**, implement a pre-commit hook that uses `scripts/update_maps.py`. This script:
* Scans directories for files.
* Updates the Inventory block in `LEGEND.md` using regex.
* Preserves human-written descriptions while adding `TODO` tags for new files.

### 2. "Proof of Navigation" Prompting
Use the provided `SYSTEM_PROMPT.md`. It enforces a "Proof Token" requirement:
* *Requirement:* "Before opening a file, you must quote its specific 'Purpose' string from the `LEGEND.md` to prove you have read it."

## 🚀 Installation in Other Repositories

You can easily add CCP to any existing project using the included installer.

1.  Clone this repository:
    ```bash
    git clone https://github.com/Quailmanjr/cartographic-context-protocol.git
    ```
2.  Run the installer against your target project:
    ```bash
    python cartographic-context-protocol/scripts/install_ccp.py /path/to/your/target-repo
    ```
3.  **Result:**
    *   `SYSTEM_PROMPT.md` and `WORLD_MAP.md` are added to the root.
    *   `scripts/update_maps.py` is installed.
    *   `LEGEND.md` files are auto-generated for every folder.
    *   The Auto-Cartographer scans and indexes all your existing files.

---

## 📚 Version History

* **[v1.3.4](file:///c:/cartographic-context-protocol/RELEASE_NOTES_v1.3.4.md)** - Minimal CCP Standard (2-column tables, optional purposes), File Hygiene Protocol
* **[v1.3.3](file:///c:/cartographic-context-protocol/RELEASE_NOTES_v1.3.3.md)** - Efficiency Rules (Anti-Repetition): Map Once, Circuit Breaker, Discovery Efficiency
* **[v1.2.2](file:///c:/cartographic-context-protocol/RELEASE_NOTES_v1.2.2.md)** - Modular Architecture, Robust Logging, Enhanced Error Handling
* **v1.2.1** - Initial public release

---

*Copyright © 2026 Tim Harris. Use of this protocol is free and open under the MIT License.*
