# CCP Specification

The protocol in full. The framing is geographic: directories are regions, files are buildings, constraints are local laws, and fixing a stale map is Cartographer Mode.

## 1. Map files

| File | Location | Role |
|---|---|---|
| `WORLD_MAP.md` | territory root | Major regions, how they relate, where to start |
| `LEGEND.md` | every significant directory | The directory's purpose, local laws, file inventory |
| `SYSTEM_FLOW.md` | highest coherent runtime boundary (e.g. `docs/`) | Runtime behavior: entry ownership, state boundaries, data contracts, seams |
| `claims/` | territory root | Work in flight — see [COORDINATION.md](COORDINATION.md) |
| `SYSTEM_MAP.md` (optional) | territory root | Architecture diagrams and schema, when topology alone isn't enough |
| Orientation snapshot (optional) | gitignored, e.g. `CCP_BRIEF.md` | Machine-regenerated orientation digest for fast session starts |

## 2. The five-step loop

Every agent, every territory, every session:

1. **ORIENT** — Read `WORLD_MAP.md` (or regenerate and read the orientation snapshot). Then read **state truth live**: current branch and remote head, open pull requests touching your scope, the `claims/` directory. Never orient from a cached snapshot of state.
2. **NAVIGATE** — Read `LEGEND.md` in any directory before opening source files there.
3. **VERIFY** — Check the directory's real inventory against the LEGEND. If they disagree, fix the LEGEND before proceeding (Cartographer Mode) — preferably with the territory's update script so the inventory block stays machine-generated.
4. **INTERPRET** — For behavior questions (routes, ownership, data flow), read `SYSTEM_FLOW.md` before deep source inspection.
5. **EXECUTE** — Only then open source files.

## 3. The three Laws of Navigation

1. **NO BLIND ENTRY** — No source file until the directory's `LEGEND.md` is read.
2. **VERIFY BEFORE TRUST** — Real inventory must match LEGEND inventory; fix mismatches before proceeding.
3. **MINIMAL LEGENDS** — LEGENDs stay small (see §4). Detail that isn't load-bearing is rot waiting to happen.

## 4. Minimal LEGEND standard

Every `LEGEND.md` contains, in order:

1. **Parent Region** — link to the parent `LEGEND.md`, or `None (root)`.
2. **Context** — one short sentence describing the directory's responsibility.
3. **Local Laws** — a few bullets for local constraints, or "none".
4. **Inventory** — a machine-generated block between `<!-- CCP-START -->` and `<!-- CCP-END -->` markers, maintained by an update script rather than by hand.

Per-file purposes are optional; when present, keep them concise. A template is at [templates/LEGEND.md](templates/LEGEND.md).

## 5. Runtime map standard

For territories with meaningful runtime behavior, `SYSTEM_FLOW.md` answers four questions:

1. **Entry Ownership** — which route, command, or entrypoint is owned by which module.
2. **State Boundary** — where mutable runtime state lives.
3. **Data Contract** — which tables, views, RPCs, APIs, or files each surface depends on.
4. **Architectural Seams** — where canonical and legacy patterns overlap.

Use it for behavior-oriented work. Do not nest runtime maps by default; add one for a subsystem only when it is independently complex.

## 6. Map truth vs. state truth

The load-bearing distinction of v2.

- **Map truth**: topology — what exists, where it lives, the local laws. It changes slowly, the LEGEND system defends it (machine-generated inventory cannot rot), and a session may trust it after VERIFY.
- **State truth**: what is happening — open PRs, running sessions, claims, live database contents, deployment state. It changes hourly and **no file snapshot of it may be trusted**. ORIENT must re-read state truth from the live source (the VCS remote, the PR list, the claims directory, the live service) at the start of every session, and again before any decision that depends on it.

Corollary for prose: any semantic assertion in a map file that describes state ("the board is frozen", "X is unmerged", "Y is the current blocker") must carry a date stamp, and a reader must treat it as a hypothesis to re-verify, never a fact to act on.

## 7. Cartographer Mode

Fixing the map is part of the work, not an interruption to it.

- Inventory drift: run the territory's update script (e.g. `scripts/update_maps.ps1` / `update_maps.py`) so inventory blocks stay machine-generated.
- Semantic drift: correct the sentence, stamp the date. Delete wrong claims rather than annotating around them — a correction that leaves the wrong claim in place will be re-read without its correction.
- A change in behavior, architecture, or protocol requires the corresponding map update in the same change set.

## 8. Scope: territory is not just code

Any curated directory tree an agent operates in is territory: a scheduled-task directory, a shared handoff folder, a memory store, an operations workspace. These deserve the same treatment as code — a `WORLD_MAP.md`, LEGENDs, and claims — because they exhibit the same failure without one: sessions re-derive what already exists.

The diagnostic is repetition: **if the same design, tool, or decision keeps being reinvented, the map is missing a region.** The fix is cartographic (add the region, write the LEGEND), not archaeological (dig it up again, faster, each time).
