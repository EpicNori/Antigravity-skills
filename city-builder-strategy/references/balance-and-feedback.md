# Balance And Feedback

## Tuning Heuristics

- Make one resource the early bottleneck and one the mid-game bottleneck.
- Keep build times short enough that the player sees plan-result feedback quickly.
- Use storage caps to force expansion choices.
- Price upgrades so they compete with survival or military spending.
- Add maintenance to powerful buildings or units.

## Telemetry To Expose

Track or display:

- Net income per resource.
- Worker or unit idle time.
- Average travel time.
- Build queue length.
- Storage saturation.
- Damage or incident frequency.

These numbers reveal whether the game is about planning, throughput, or firefighting.

## Readability Rules

- Show input shortages at the point of failure.
- Use distinct silhouettes or colors for production, housing, military, and support structures.
- Surface ETAs for construction, crafting, movement, or research.
- Prefer one strong warning over many low-value alerts.

## Common Failure Modes

- Snowball economy with no upkeep or threat pressure.
- Hidden prerequisites that make the player think the game is bugged.
- Worker AI that thrashes between equally valid jobs.
- Pathfinding cost dominating the simulation tick.
- Combat resolving too quickly for the player to react.
- Late resources that matter only because the design says they should.

## Fast Playtest Prompts

Use short scenarios:

- "Can a new player understand the first three minutes without narration?"
- "What is the first resource shortage, and does it create a decision?"
- "Can the player recover from one mistake?"
- "Can the player tell why they lost?"
