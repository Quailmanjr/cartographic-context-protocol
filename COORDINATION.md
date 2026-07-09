# CCP Coordination Layer

Maps tell an agent where things live. They do not tell it who is working on what right now. When several agents share a territory, that second question is the one that produces duplicate work — the observed failure mode is multiple parallel sessions independently building the identical change, each unable to see the others' intent.

This layer adds work-in-flight to the map. It is required whenever more than one agent (or one agent across parallel sessions) works the same territory.

## 1. The claims directory

`claims/` at the territory root. **One file per active task** — never a single shared ledger.

```
claims/
  fix-count-reconciliation.md
  lint-cat-a-cleanup.md
```

Each claim is small and fully self-contained:

```markdown
# fix-count-reconciliation
owner: <agent or session identifier>
started: 2026-07-09
updated: 2026-07-09
scope: web/src/features/pricing/, web/src/features/dashboard/counts*
artifact: branch claude/count-recon-20260709 → PR
```

Rules:

- **Partitioned by design.** One claim, one file. Two agents claiming different tasks never touch the same file, so claims cannot merge-conflict.
- **Scope is file territory.** A claim names the directories/files it intends to touch. Scopes of concurrent claims must not overlap; if they must, one agent owns the slice and the other hands off.
- **Claims die with the work.** Delete the claim file in the same change that completes the task (or when the PR merges). A claims directory that only grows is a ledger, and ledgers rot.
- **Stale claims are challengeable.** A claim whose `updated` stamp exceeds the territory's TTL (default: 48 hours) with no artifact progress may be flagged and, after surfacing to the territory owner, removed. Silence is not ownership.

### Why not one ledger file

A single shared work log that every task appends to becomes the busiest intersection in the territory: every merge conflicts every other open change on that one file, and remote sessions that branched before your append can't see it at all. That is the anti-pattern this layer exists to replace. Narrative history can still live in a log — but *coordination state* must be partitioned.

## 2. Pre-flight claim check

Before starting any task, an agent must:

1. Read `claims/` — is this scope, or an overlapping one, already claimed?
2. Scan open pull requests for the same scope — a PR is an implicit claim even if no claim file exists.
3. On collision: **defer or hand off.** Do not build a second copy "to be safe." A duplicate is not redundancy; it is review load and merge conflict.

Only after a clean pre-flight does the agent write its own claim and begin.

## 3. One owner per slice

- Every workstream slice has exactly one owning agent at a time.
- Owners declare non-overlapping file territory up front (the claim's `scope`).
- Work that naturally crosses a boundary is handed off to the neighboring owner, not absorbed.
- An orchestrating agent that spawns sub-agents is responsible for cutting non-overlapping scopes before dispatch — and is the reporting line for material findings, so surfacing happens once, deduplicated.

## 4. Autonomy tiers

Autonomy is earned by protocol compliance, not granted globally. A useful three-tier ladder:

| Tier | Condition | Behavior |
|---|---|---|
| **Ship** | Spec is explicit; agent is executing, not interpreting | Self-verify, complete the work on a branch, record decisions |
| **Review** | Agent filled gaps or made judgment calls | Complete the work, land it for the territory owner's review |
| **Blocked** | Cannot proceed without the owner | Stop and escalate; do not guess |

An agent qualifies for autonomous operation in a territory only while it (a) runs the five-step loop including a live state-truth read, (b) passes pre-flight claim checks, and (c) holds a non-overlapping scope. Violating any of the three drops the work to Review regardless of how explicit the spec was.

The backstop for runaway sessions is external (a watchdog that kills presence-without-progress), not reduced ambition. Scope boldly; watch mechanically.

## 5. Trailing-off recovery

An agent that announces work and then goes silent leaves an orphaned claim. The recovery rule: detection belongs to whoever did *not* open the work — a peer agent or a scheduled watcher flags the orphan to the territory owner after a fixed silence window, with a pointer to the claim and its last artifact. The owner then re-engages, reassigns, or lets it die. Deleting the claim without surfacing it is not permitted; that hides the failure the map exists to expose.
