# Antigravity-skills

A curated library of **454 AI coding skills across 14 categories**: 427 new imports and 27 existing skills. The expansion is based on accessible coding repositories, local project manifests, and Codex project context, reviewed on October 14, 2026.

Start with the [categorized catalog](CATALOG.md), [project coverage and remaining gaps](docs/PROJECT_COVERAGE.md), or [review results and limitations](docs/REVIEW.md).

## Structure

- `skills/<category>/<skill-name>/`: newly imported packages, including scripts, references, templates, legal notices, and `SOURCE.json` provenance records.
- Existing root-level skill directories: preserved at their original paths for compatibility.
- `catalog/skills.json`: metadata, source commits, paths, and resource SHA-256 hashes.
- `catalog/discovered-sources.json`: wider upstream discovery inventory, including collections that were not imported.
- `catalog/not-imported.json`: candidate exclusions and their reasons.
- `CATALOG.md`: generated Markdown index; edit metadata in the manifest, then rebuild it.
- `scripts/library.py`: catalog generation, search, validation, and a local documentation preview.

## Find and use a skill

```powershell
python scripts/library.py search firebase
python scripts/library.py search qml
python scripts/library.py search testing
```

Read the selected `SKILL.md` and its prerequisites. Copy the **whole skill directory**, including its `SOURCE.json` and legal notices, into your agent's supported skill directory when you want to install it. Select individual skills for each project; this repository is the library, not an automatically activated global installation. For Codex, use the installed skill-installer with the exact package path from the catalog, or copy it into your configured skills folder. Newly installed skills become available on the next turn.

An import is not authorization to run a script, change a service, send a message, deploy, publish, create a branch, or push. Follow the user's current task and repository instructions. Read a packaged helper before running it and check its runtime requirements; availability of a Markdown skill does not imply its MCP tools or credentials are installed.

## Validate and preview

Python 3.10 or newer is required. Build, search, and preview use the standard library. Validation additionally uses PyYAML:

```powershell
python -m pip install -r requirements-dev.txt
python scripts/library.py validate
python scripts/library.py build
python scripts/library.py serve --port 8765
```

Open [the local catalog](http://127.0.0.1:8765). The preview binds only to loopback and rejects Git/config paths, directory listings, and executable files. Stop it with Ctrl+C. Visual conventions are recorded in [style.md](style.md).

## Provenance and maintenance

Imports are pinned to immutable upstream commits. The original entrypoint SHA-256 is stored in `SOURCE.json`; installed resource hashes are stored in the catalog. Imported frontmatter was normalized for portable Agent Skills metadata, with custom fields retained under `metadata`. Documentation links outside a copied package were pinned to upstream where the referenced file exists.

Use [THIRD_PARTY_ATTRIBUTION.md](THIRD_PARTY_ATTRIBUTION.md) and each package's legal notices for licensing. There is no blanket license replacing upstream terms. The original 27 skills retain their previous attribution status; they have not received a full retrospective provenance or resource audit.

`python scripts/discover_sources.py --output <local-output.json>` refreshes public GitHub inventories without changing skills. Public API rate limits can apply. Review upstream diffs and license changes before updating a package; do not overwrite local changes or regenerate integrity hashes merely to make validation pass.

Private project code, internal specifications, account identifiers, credentials, and conversation transcripts were not added to this public library. No backend rules were changed.
