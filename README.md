# Antigravity-skills

**454 AI coding skills in 14 categories**, including 427 imported packages and 27 original skills.

Browse the [Markdown skill index](CATALOG.md) to find a skill.

## Structure

- `skills/<category>/<skill-name>/`: imported skills with their supporting scripts, references, templates, legal notices, and `SOURCE.json` source records.
- Root-level skill directories: the original 27 skills, kept at their existing paths.

Read a skill's `SKILL.md` and prerequisites, then copy its whole directory into your agent's supported skill location. Keep its resources, source records, and legal notices together. Skills may require additional tools, credentials, or platform-specific dependencies.

## Sources and licenses

Imported packages are pinned to upstream commits in their `SOURCE.json` files. These records include the original entrypoint hash and any local adaptations. See [THIRD_PARTY_ATTRIBUTION.md](THIRD_PARTY_ATTRIBUTION.md) and each package's legal notices for its license. Upstream terms remain in effect.

The original 27 packages retain their previous attribution status and have not received a full retrospective dependency or provenance audit. Static import checks do not establish runtime correctness.
