"""Report review markers without executing skill code or printing matched secrets."""
import collections
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
MARKERS = {
    'remote-shell-installer': re.compile(r'(?:curl|wget)[^\n]*\|\s*(?:sh|bash)|\birm\b[^\n]*\|\s*iex', re.I),
    'git-push-example': re.compile(r'\bgit push\b'),
    'verification-bypass-example': re.compile(r'--no-verify|--allow-unauthenticated'),
    'instruction-override-language': re.compile(r'ignore (?:all |any )?(?:previous|prior|system) instructions|disable (?:all )?(?:security|safety)', re.I),
    'possible-credential-example': re.compile(r'AKIA[A-Z0-9]{16}|ghp_[A-Za-z0-9]{36}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
}


def scan():
    skills = json.loads((ROOT / 'catalog/skills.json').read_text(encoding='utf-8'))['skills']
    findings = []
    files_scanned = 0
    for skill in skills:
        folder = ROOT / skill['path']
        # Inspect imported resources and legacy resources, including code blocks.
        for path in sorted(folder.rglob('*')):
            if not path.is_file() or path.suffix.lower() not in {'.md', '.txt', '.py', '.sh', '.ps1', '.js', '.mjs', '.cjs', '.ts', '.json', '.yaml', '.yml', '.html'}:
                continue
            try:
                lines = path.read_text(encoding='utf-8-sig').splitlines()
            except UnicodeError:
                continue
            files_scanned += 1
            for number, line in enumerate(lines, 1):
                for kind, pattern in MARKERS.items():
                    if pattern.search(line):
                        findings.append(dict(skill=skill['name'], path=path.relative_to(ROOT).as_posix(), line=number, kind=kind))
    report = dict(files_scanned=files_scanned,
                  interpretation='Review markers, not confirmed vulnerabilities. Documentation can intentionally show unsafe examples; inspect context. No matching text or credential values are stored.',
                  runtime='Upstream code was not executed; this is a limited pattern scan, not a complete security audit.',
                  counts=dict(collections.Counter(f['kind'] for f in findings)), findings=findings)
    (ROOT / 'catalog/security-scan.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'findings'}, indent=2))
    return report


if __name__ == '__main__':
    scan()
