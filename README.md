# Cartographic Context Protocol

Cartographic Context Protocol (CCP) is a small repository-navigation convention for AI agents and humans working in a shared territory — usually a codebase, but any curated directory tree qualifies.

It keeps project context explicit in files so a new session can orient before editing. It is not a security boundary, a memory system, or proof of any performance gain.

## Core idea

The territory carries its own map, and the map is layered:

- `WORLD_MAP.md` — the major regions of the territory and how they relate.
- `LEGEND.md` — one per significant directory: its purpose, local rules, and a machine-verified file inventory.
- `SYSTEM_FLOW.md` — runtime behavior (who owns which entrypoint, where state lives), separate from topology.
- `claims/` — work in flight: who is working on what, right now. See [COORDINATION.md](COORDINATION.md).

Agents follow a five-step loop before touching anything: **ORIENT → NAVIGATE → VERIFY → INTERPRET → EXECUTE.** The full loop, the three Laws of Navigation, and the file standards are in [SPEC.md](SPEC.md).

## Two kinds of truth

A map records two different things, and they rot at different speeds:

- **Map truth** — topology: what exists, where it lives, what the local rules are. Changes slowly. Trust the LEGEND; verify inventory mechanically.
- **State truth** — what is happening: open pull requests, running sessions, live database state, in-flight claims. Changes hourly. **Never act on a snapshot of state truth — re-read it live at the start of every session.**

Most coordination failures between parallel agents come from treating a snapshot of state truth as if it were map truth.

## When to use it

Use CCP when a territory is large enough that repeated orientation work is slowing down edits, or when more than one agent works the same territory and duplicate work has been observed. Keep the files short, current, and factual.

A useful test: if sessions keep re-deriving something that was already built, the map is missing a region. Add the region; don't re-derive faster.

## Files in this repository

| File | Contents |
|---|---|
| [SPEC.md](SPEC.md) | The protocol: files, the five-step loop, the three Laws, LEGEND and runtime-map standards |
| [COORDINATION.md](COORDINATION.md) | Multi-agent layer: the claims directory, pre-flight checks, one-owner-per-slice |
| [templates/](templates/) | Copy-paste starting points for `LEGEND.md` and claim files |
