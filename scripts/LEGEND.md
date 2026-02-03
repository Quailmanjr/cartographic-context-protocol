# 📍 LEGEND: Scripts

**Parent Region:** [Root](file:///c:/cartographic-context-protocol/LEGEND.md)  
**Context:** Automation scripts for CCP installation and maintenance.

## 🏢 BUILDINGS (Files)

<!-- CCP_INVENTORY_START -->
| File | Purpose |
| :--- | :--- |
| `install_ccp.py` | Installs CCP into target repositories |
| `update_maps.py` | Auto-cartographer that updates LEGEND.md inventory blocks |
<!-- CCP_INVENTORY_END -->

## 🚧 LOCAL LAWS
* Python 3.8+ required
* Scripts must be idempotent (safe to run multiple times)
* `update_maps.py` must never overwrite human-written descriptions
