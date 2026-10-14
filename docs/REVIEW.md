# Review record — October 14, 2026

## Result

The library contains 454 skills: 427 newly imported packages from ten upstream repositories and 27 preserved root-level packages. The imported packages carry 2,694 tracked resources, including their source records, legal notices, scripts, references, and templates. All package paths and file hashes are available in `catalog/skills.json`.

The local documentation catalog provides search, category filtering, and imported/existing filtering. Its style is documented in `style.md`. No project backend, database security rules, application deployment, or user-wide skill installation was changed. The update uses the existing `main` branch. Publishing follows the user's explicit request; no new branch is created.

## Validation

- Repository validation checks all 454 entrypoints: YAML, names, imported metadata schema, manifest coverage, resource hashes, source records, legal notices, and explicit entrypoint documentation links. Results are in `catalog/validation.json`.
- The bundled Codex skill-creator validator checks all 427 imports separately. Results are in `catalog/codex-validation.json`.
- Five local tests exercise tampering detection, manifest path containment, uncataloged skills, untracked executable resources, and the preview server's access restrictions. Run `python -m unittest discover -s tests -v` after installing validation dependencies.
- A headless Edge check loaded all 454 records, found 15 Firebase search matches, selected 26 desktop/system skills, selected all 27 legacy skills, checked HTML-like search input, followed a skill link, and checked the page at a 390px viewport. No page JavaScript errors occurred. Desktop and mobile screenshots were visually inspected.
- `git diff --check` checks the tracked changes. Third-party supporting code was copied as data; it was not executed or runtime-tested.

## Security review boundaries

`python scripts/scan_library.py` scans text and code resources for a limited set of review markers. The report is `catalog/security-scan.json`. It does not establish the absence of secrets, malicious instructions, dependency vulnerabilities, or runtime defects.

The scan found 23 Git-push examples and three remote shell-installer examples. These occur in upstream documentation and reference snippets, not in an executed import hook. Two possible-credential matches were inspected: one is a hardcoded-key example in a secret-detection guide; the other is only a private-key header marker, without key material, in a vulnerability example. Matching values are not printed into the scan report.

Remote shell-installer examples remain in Cloudflare sandbox references, Render deployment instructions, and Sentry installation instructions. Inspect and verify any installer before executing it. Deployment and Git examples do not override the user's instruction against unrequested pushes. Some skills require particular MCP servers, CLIs, platforms, credentials, or explicitly authorized agent delegation; copying a package does not supply those prerequisites or permissions.

The preview serves only selected documentation file types, rejects dot paths and traversal, disables directory listing, and binds to `127.0.0.1`. It is a local documentation viewer, not production hosting.

## Repairs and exclusions

- Quoted a description containing an unescaped colon in the existing `threejs-builder/SKILL.md`, repairing invalid YAML without changing its guidance.
- Normalized imported custom frontmatter fields into string metadata. Compatibility information is retained under metadata to satisfy the bundled Codex validator. Two Qt review descriptions spell out a comparison instead of using an angle bracket.
- Retained complete package resources and ancestor legal notices. Pinned out-of-package documentation links to the exact upstream revision where the referenced target exists.
- Added Git attributes to preserve imported package bytes across checkouts. Existing skill entrypoints use LF endings so their recorded hashes remain stable across platforms.
- Excluded one duplicate `security-review` import. Deferred seven candidates lacking a complete license file in their package ancestry and 19 mixed-license aggregator candidates. The discovery inventory retains their locations; exclusions are recorded in `catalog/not-imported.json`.

## Remaining work

The original 27 skills were cataloged and had entrypoint YAML checked, but their existing supporting files have not received a full dependency, licensing, or integrity reconstruction. Earlier Markdown-only imports may still mention resources that were never copied. These packages are explicitly marked `existing-unreviewed`.

Project inspection covered accessible manifests, documentation, and a small relevant cloud-chat sample. It did not extract every historical chat, unavailable project folder, private draft skill, or file on the computer. Dedicated coverage gaps are listed in `docs/PROJECT_COVERAGE.md`. The wider upstream inventory includes translations and duplicate bundle paths; its size must not be presented as a count of reviewed unique skills.
