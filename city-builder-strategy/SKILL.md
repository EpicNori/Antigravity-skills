---
name: city-builder-strategy
description: Generate playable city-builder, colony-sim, tactics, RTS, or turn-based strategy game prototypes with clear economies, production chains, map logic, AI loops, and readable UX. Use when Codex needs to design or implement strategy games, settlement-management systems, grid or tile maps, resource flows, faction rules, construction loops, or a compact vertical slice with meaningful player decisions.
---

# City Builder Strategy

## Overview

Build a narrow, playable vertical slice first. Favor legible systems, deterministic simulation, and clear player feedback over content breadth.

## Workflow

1. Identify the subgenre and player loop.
2. Reduce the request to one map, one faction, and one core win/lose condition.
3. Define the minimum system graph: resources, jobs, buildings, units, threats, and progression.
4. Implement the simulation before polish.
5. Add interface feedback so the player can understand state, bottlenecks, and consequences.
6. Validate pacing, deadlocks, and exploits with short playtest scenarios.

## Start By Framing The Slice

Write down these decisions before building:

- Subgenre: city builder, colony sim, RTS, tactics, grand strategy, or 4X-lite.
- Camera and space model: tile grid, node graph, world map, or lane-based battlefield.
- Loop length: 30-second tactical loop, 5-minute economy loop, or 20-minute scenario loop.
- Player verbs: place, zone, assign, build, move, research, trade, attack, pause.
- Pressure source: upkeep, enemy waves, morale, pollution, terrain, weather, or rival expansion.
- Success condition: survive N days, reach population target, hold territory, or outproduce opponent.

If the user asks for a large game, compress it into a prototype with:

- One biome or map.
- Three to five resources.
- Three building tiers at most.
- One enemy or rival behavior family.
- One progression layer.

## Build Systems In Dependency Order

Implement systems in this order unless the request strongly suggests otherwise:

1. Map representation and path or adjacency rules.
2. Resource simulation and storage limits.
3. Building placement and production logic.
4. Agent or unit task selection.
5. Threats, rival actions, or scenario events.
6. Economy tuning and progression gates.
7. Interface, readability, and moment-to-moment feedback.

Keep each system inspectable. Expose game state in simple panels, debug overlays, or logs while building.

## Economy Rules

Use conservative, understandable rules:

- Prefer a few strongly differentiated resources over many shallow ones.
- Keep production chains short in the first version.
- Make bottlenecks visible through missing inputs, idle workers, capped storage, or power shortages.
- Add upkeep to prevent infinite stockpiling from trivializing decisions.
- Ensure every important output has at least one counter-pressure: time, labor, space, energy, or risk.

For concrete economy and pacing patterns, read [references/genre-patterns.md](references/genre-patterns.md) and [references/balance-and-feedback.md](references/balance-and-feedback.md).

## AI And Simulation Guidance

Use the simplest behavior model that creates meaningful opposition:

- Workers: nearest valid job, priority queue, or assigned role.
- Enemies: wave scheduler, territory pressure, or target-value heuristic.
- Rivals: production race, expansion scoring, or scripted doctrine.

Avoid expensive full-world intelligence in early versions. Strategy games usually benefit more from predictable, readable opponents than from complex hidden logic.

## UX Requirements

A strategy prototype fails if the player cannot read causality. Always include:

- A visible resource bar.
- Build or action affordances with cost previews.
- State cues for blocked, idle, damaged, hungry, unpowered, or under-attack entities.
- A way to inspect why something is not working.
- A pause or slow-speed option if simulation complexity is non-trivial.

## Technical Guidance

- Prefer deterministic updates and a fixed simulation tick when possible.
- Separate simulation state from rendering state.
- Encode data tables for units, buildings, recipes, and upgrades instead of hardcoding repeated logic.
- Make tuning values easy to change from one place.
- Save complexity for later. Prototype depth through interacting rules, not through asset count.

If the implementation stack is web-based, keep rendering lightweight and prioritize input clarity, tile selection, overlays, and performant update loops.

## Validation

Run these checks before considering the prototype usable:

- The player can complete one full loop without hidden rules.
- The economy cannot soft-lock from the default starting state without player mistakes being visible.
- There is at least one interesting scarcity decision.
- Losing has a clear cause.
- The UI explains idle or failed actions.
- The simulation remains stable at increased game speed for several minutes.

## References

- Read [references/genre-patterns.md](references/genre-patterns.md) for genre-specific skeletons and feature cuts.
- Read [references/balance-and-feedback.md](references/balance-and-feedback.md) for tuning, telemetry, and anti-patterns.
