# Third-Party Skill Attribution

These imported skills were added on May 30, 2026 as markdown-only imports.

Selection rule:
- Prefer active public repositories with MIT licenses.
- Use GitHub stars as a popularity proxy because direct download counts are not consistently available for `SKILL.md` repositories.
- Exclude or trim ecosystems that depend on proprietary runtimes, non-markdown installers, or local automation servers when that would make the imported skill misleading here.

Import rule:
- Only markdown content was imported into this repository.
- Non-markdown scripts, plugin manifests, binary assets, and engine-side automation helpers were intentionally omitted to keep this repository md-based.

## Imported From `jame581/GodotPrompter`

Source:
- [jame581/GodotPrompter](https://github.com/jame581/GodotPrompter)

Repository snapshot at research time:
- License: `MIT`
- Stars: `156`
- Last updated: `2026-05-30`

Imported skills:
- `3d-essentials`
- `player-controller`
- `camera-system`
- `physics-system`
- `ai-navigation`
- `animation-system`
- `procedural-generation`
- `godot-optimization`
- `shader-basics`
- `particles-vfx`

## Imported From `freshtechbro/claudedesignskills`

Source:
- [freshtechbro/claudedesignskills](https://github.com/freshtechbro/claudedesignskills)

Repository snapshot at research time:
- License: `MIT`
- Stars: `180`
- Last updated: `2026-05-30`

Imported skills:
- `threejs-webgl`
- `react-three-fiber`
- `babylonjs-engine`
- `playcanvas-engine`
- `web3d-integration-patterns`

## Considered But Not Imported

- `Besty0728/Unity-Skills`
  Reason: very popular (`1127` GitHub stars as of May 30, 2026) but most high-value modules are tightly coupled to its Unity REST server and editor automation flow, so importing the markdown alone here would create misleading or partially dead skills.
- `Randroids-Dojo/skills`
  Reason: useful engine-specific material, but the strongest Unreal/Godot entries are still more workflow- and script-coupled than the selected GodotPrompter and web-3D skills.
- `abagames/headless-godot-skill-kit`
  Reason: valuable headless workflow, but it depends on accompanying Godot patch/test scripts; omitted to keep this import strictly markdown-only and self-consistent.
