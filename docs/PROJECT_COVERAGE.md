# Project coverage

Reviewed on October 14, 2026. This document records reusable technology themes rather than publishing private repository names, paths, or specifications.

## Evidence and limits

- Listed 55 distinct accessible GitHub repositories across three connected accounts. Four were empty. Requested root `README.md` and `package.json` from the other 51; 45 READMEs and 23 package manifests were available at those paths. A missing file is not evidence that a project lacks that technology.
- Listed 16 local Codex project folders, plus a drive-root entry, and 21 cloud project entries. Project labels are topic hints, not verified implementation evidence.
- Searched the Downloads, Documents, OneDrive ChatGPT project folders, personal coding folders, and user skill directories. Found 12 local project manifests and 145 skill files with 35 distinct content hashes. The skills outside the main library were primarily duplicate library copies, built-in skills, and Pinokio skills. Additional Pinokio skill entrypoints were located separately.
- Three legacy Documents junctions for pictures/music/videos denied traversal. Some Codex project folders are no longer present in their registered locations. Dependencies, build outputs, vendored research checkouts, caches, and system directories were excluded.
- Queried connected GitHub code search for `SKILL.md`; it returned no results. This does not prove absence: indexing and private-file coverage are limited. A private agent-runtime README mentions draft skills; their directory contents could not be enumerated through this search.
- Inspected the recent Codex sidebar and three agent-related cloud chats. Their retrieved assistant replies contained content-reference markers rather than usable skill text. Full historical conversations, attachments, and private cloud skill drafts were not exhaustively extracted or copied.

## Technology-to-skill routes

| Observed theme | Useful catalog entrypoints | Coverage |
| --- | --- | --- |
| React, Vite, TypeScript, Tailwind | `react-patterns`, `react-performance`, `react-testing`, `typescript-advanced-types`, `tailwind-design-system`, `responsive-design` | Broad web coverage; check installed framework versions. |
| Firebase auth, Firestore, hosting, rules, emulators | `firebase-auth-basics`, `firebase-firestore`, `firestore-rules-creation`, `firebase-security-rules-auditor`, `firebase-hosting-basics` | Official Firebase collection. |
| Supabase, PostgreSQL, Stripe, backends | `supabase`, `supabase-postgres-best-practices`, `postgresql-table-design`, `stripe-integration`, `auth-implementation-patterns` | Database, authorization and payments. |
| Capacitor, Android/iOS, shared web/mobile apps | `ionic-capacitor`, `ionic-react`, `ionic-native-essentials`, `ionic-deep-links`, `ionic-supabase`, `ionic-firebase` | Preserve the existing architecture; a React Native skill is not a reason to migrate. |
| Python automation, installers, services | `generating-python-installer`, `python-packaging`, `python-resource-management`, `async-python-patterns`, `python-testing-patterns` | Implementation and testing workflows. |
| C++, Qt Quick/QML, CMake, automotive dashboards | `cpp-coding-standards`, `cpp-testing`, `qt-qml`, `qt-cmake-project`, `qt-qml-profiler`, `qt-qml-review`, `qt-qml-test` | Official Qt coding, profiling, review and documentation. |
| AI runtimes, MCP, retrieval, evaluation | `agent-architecture`, `agent-governance`, `agent-security-hardening`, `mcp-builder`, `rag-implementation`, `llm-evaluation`, `prompt-caching-strategy` | Architecture and engineering; private product requirements remain outside this library. |
| Speech and phone-driven coding | `speech`, `transcribe`, `chatgpt-apps`, `agent-architecture` | Speech output/transcription; realtime turn detection and telephony remain a gap. |
| Godot, browser 3D, CAD and printing | Original Godot/Web3D skills, `godot-gdscript-patterns`, `freecad-scripts`, `rhino3d-scripts`, `slang-shader-engineer` | Graphics covered; print-in-place tolerance and 3MF validation remain specialist gaps. |
| Minecraft servers and plugins | `minecraft-plugin-development`, `java-coding-standards`, `docker-patterns`, `bash-defensive-patterns` | Plugin coverage; Fabric internals and Android/Termux operations remain gaps. |
| Linux, homelab, deployment | `arch-linux-triage`, `debian-linux-triage`, `fedora-linux-triage`, `homelab-network-readiness`, `docker-patterns`, `github-actions-hardening` | Diagnostics and operations; Hyprland UI and Windows input automation remain gaps. |
| OSINT, clean-room protocol work, security | `osint-investigation`, `protocol-reverse-engineering`, `binary-analysis-patterns`, `security-threat-model`, `secret-scanning` | Method and review coverage within authorized tasks. |
| ERP, hospitality, dashboards, learning apps | `api-design-principles`, `architecture-patterns`, `kpi-dashboard-design`, `data-quality-frameworks`, `accessibility-compliance` | Generic engineering; domain workflows still need project context. |
| Documents, presentations and video | Existing PDF/PPTX/Typst/Remotion skills, `documentation-writer`, `architecture-decision-records`, `jupyter-notebook` | Original resource/provenance gaps are tracked separately. |

## Prioritized remaining gaps

1. Dedicated ArduPilot/MAVLink/SITL, geospatial maps, Cesium, and flight-simulation workflows. Graphics and C++ guidance does not substitute for these domains.
2. Electron/Tauri security and packaging, Windows automation, Hyprland, and Termux. Some matching aggregator skills were deferred pending per-skill upstream licensing review.
3. Roblox/Luau, Minecraft Fabric, realtime voice transport, and 3D-print validation. This import pass did not identify a verified, self-contained licensed package for these topics.

The wider discovery inventory is in `catalog/discovered-sources.json`; its paths include translations, nested modules and duplicates, not just unique reviewed skills. This is a substantial curated expansion, not a claim to contain every internet skill or inaccessible private draft.
