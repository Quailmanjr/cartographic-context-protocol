# Case Study: Fixing the Labor Tax Bug

* **Problem:** The plumbing estimator was double-taxing labor in the bid summary.
* **Standard Approach:** Agent reads 15 files to find the calculation. **Cost: 12k tokens.**
* **CCP Approach:** Agent reads `WORLD_MAP`, identifies `/src/lib/pricing` as the "Logic District." Reads `LEGEND.md`, identifies `tax-logic.ts`. **Cost: 2k tokens.**
* **Efficiency Gain:** 83% token reduction.
