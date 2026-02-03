# Version 1.3.3 Changelog

## 🚀 New Features & Improvements

### ⚡ EFFICIENCY RULES (Anti-Repetition)

This release introduces three critical rules to prevent AI agents from getting stuck in "Verification Loops" where they repetitively scan the same directories, violating CCP's core efficiency goals.

#### 1. **MAP ONCE (Satellite Rule)**
* Agents must run `tree -L 2` or `ls -R` **ONCE** upon entering a directory to get a complete view
* The structure must be cached mentally—no repeated `ls` commands on already-seen subdirectories
* Deeper inspection should be done via `LEGEND.md` files, not filesystem re-scanning

#### 2. **CIRCUIT BREAKER**
* Running the **same command** on the **same path** twice in a row is now a **protocol violation**
* Agents must STOP IMMEDIATELY and either request wider scope or escalate to documentation
* This prevents infinite loops and enforces deliberate navigation

#### 3. **DISCOVERY EFFICIENCY**
* `LEGEND.md` must be prioritized as the first source of truth
* Brute-force filesystem scanning is only permitted when Legend files are missing or corrupted
* Reinforces the "Map Rot" rule: trust the Legend inventory as canonical

## 🎯 Impact

These rules directly address the problem of agents wasting tokens by repeatedly running directory listings instead of using the hierarchical navigation structure that CCP provides.

**Token Savings:** Estimated 60-80% reduction in repetitive filesystem operations during navigation tasks.

## 📝 Version Updates

* `SYSTEM_PROMPT.md` updated from v1.3.2 → v1.3.3
* New section added: "⚡ EFFICIENCY RULES (ANTI-REPETITION)"

## 🔒 Backward Compatibility

Fully backward compatible. These are additive behavioral constraints that enhance existing CCP rules without breaking previous implementations.

---

*Released: 2026-02-03*
