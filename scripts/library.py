"""Build, search, validate, and preview the skill library without running skills."""
from __future__ import annotations

import argparse
import collections
import hashlib
import http.server
import json
import pathlib
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'catalog' / 'skills.json'


def load():
    return json.loads(MANIFEST.read_text(encoding='utf-8'))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build():
    data = load()
    groups = collections.defaultdict(list)
    for skill in data['skills']:
        groups[skill['category']].append(skill)
    lines = ['# Skill catalog', '',
             f"{len(data['skills'])} skills. Reviewed on {data['review_date']}.", '',
             'Import review is static; runtime tools, credentials, and platform requirements still apply.', '',
             '| Category | Skills |', '| --- | ---: |']
    for group, skills in sorted(groups.items()):
        lines.append(f'| [{group}](#{group}) | {len(skills)} |')
    for group, skills in sorted(groups.items()):
        lines += ['', f'## {group}', '', '| Skill | Purpose | Source / license |', '| --- | --- | --- |']
        for skill in sorted(skills, key=lambda x: x['name']):
            desc = ' '.join(skill['description'].split()).replace('|', '\\|')
            if len(desc) > 240:
                desc = desc[:237].rsplit(' ', 1)[0] + '...'
            origin = skill['origin']
            source = f"[{origin['repository']}]({origin['url']}) / {origin['license']}" if origin else 'Existing library; provenance audit pending'
            lines.append(f"| [{skill['name']}]({skill['path']}/SKILL.md) | {desc} | {source} |")
    (ROOT / 'CATALOG.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f"Built CATALOG.md with {len(data['skills'])} skills across {len(groups)} categories.")


def validate():
    try:
        import yaml
    except ImportError:
        raise SystemExit('Install validation dependencies: python -m pip install -r requirements-dev.txt')
    data = load()
    errors, warnings, seen = [], [], set()
    allowed = {'name', 'description', 'license', 'compatibility', 'metadata', 'allowed-tools'}
    listed = set()
    for skill in data['skills']:
        raw_folder = ROOT / skill['path']
        folder = raw_folder.resolve()
        if not folder.is_relative_to(ROOT) or any(p.is_symlink() for p in [raw_folder, *raw_folder.parents] if p.is_relative_to(ROOT)):
            errors.append(f"{skill['name']}: package escapes library")
            continue
        entry = folder / 'SKILL.md'
        listed.add(entry)
        if skill['name'] in seen:
            errors.append(f"Duplicate name: {skill['name']}")
        seen.add(skill['name'])
        if not entry.is_file():
            errors.append(f"{skill['name']}: missing SKILL.md")
            continue
        text = entry.read_text(encoding='utf-8-sig')
        match = re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)', text, re.S)
        try:
            meta = yaml.safe_load(match[1]) if match else None
            if not isinstance(meta, dict):
                raise ValueError('Missing metadata mapping')
            if meta.get('name') != skill['name']:
                raise ValueError('Manifest and skill name differ')
            if not isinstance(meta.get('description'), str) or not meta['description'].strip():
                raise ValueError('Missing description')
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', meta['name']) or len(meta['name']) > 64:
                raise ValueError('Invalid portable name')
            if skill['origin'] and (set(meta) - allowed or len(meta['description']) > 1024):
                raise ValueError('Nonportable imported metadata')
        except (ValueError, TypeError, yaml.YAMLError) as exc:
            errors.append(f"{skill['name']}: {exc}")
        for relative, expected in skill['files'].items():
            raw_path = folder / relative
            path = raw_path.resolve()
            linked = any(p.is_symlink() for p in [raw_path, *raw_path.parents] if p.is_relative_to(folder))
            if not path.is_relative_to(folder) or not path.is_file() or linked:
                errors.append(f"{skill['name']}: missing or unsafe resource {relative}")
            elif digest(path) != expected:
                errors.append(f"{skill['name']}: changed resource {relative}; review before updating hashes")
        if skill['origin']:
            extra_files = {p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file()} - set(skill['files'])
            for relative in sorted(extra_files):
                errors.append(f"{skill['name']}: untracked package resource {relative}")
            source = folder / 'SOURCE.json'
            if not source.is_file() or json.loads(source.read_text(encoding='utf-8')) != skill['origin']:
                errors.append(f"{skill['name']}: missing or inconsistent SOURCE.json")
            for relative in skill['origin']['license_files']:
                if not (folder / relative).is_file():
                    errors.append(f"{skill['name']}: missing legal notice {relative}")
        # Explicit relative documentation links in the entrypoint, excluding code
        # fences, placeholders, anchors, remote links, and documented runtime paths.
        prose = re.sub(r'```.*?```', '', text, flags=re.S)
        prose = re.sub(r'`[^`]*`', '', prose)
        for href in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', prose):
            path = unquote(href.split('#', 1)[0])
            if not path or re.match(r'^[a-z][a-z0-9+.-]*:|^[/~]|[{}<>*`]', path, re.I):
                continue
            if not (folder / path).exists():
                warnings.append(f"{skill['name']}: unresolved entrypoint documentation link {href}")
    actual = {p.resolve() for p in ROOT.glob('*/SKILL.md')} | {p.resolve() for p in (ROOT / 'skills').rglob('SKILL.md')}
    for entry in actual - listed:
        errors.append(f'Uncataloged entrypoint: {entry.relative_to(ROOT)}')
    report = dict(skills=len(data['skills']), errors=errors, warnings=warnings,
                  checked='YAML, names, package inventory, resource hashes, source records, legal notices, entrypoint documentation links',
                  limits='Static validation does not execute upstream scripts, prove runtime behavior, or audit every instruction.')
    (ROOT / 'catalog' / 'validation.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
    return 1 if errors else 0


def search(query):
    for skill in load()['skills']:
        if query.casefold() in ' '.join([skill['name'], skill['description'], skill['category']]).casefold():
            print(f"{skill['name']} [{skill['category']}] {skill['path']}/SKILL.md")


class PreviewHandler(http.server.SimpleHTTPRequestHandler):
    """Serve documentation on loopback, excluding Git/config and executable files."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def send_head(self):
        decoded = unquote(urlsplit(self.path).path)
        parts = pathlib.PurePosixPath(decoded).parts
        if any(part.startswith('.') or part == '..' for part in parts if part != '/'):
            self.send_error(404)
            return None
        path = (ROOT / decoded.lstrip('/')).resolve()
        if not path.is_relative_to(ROOT) or any(p.is_symlink() for p in [path, *path.parents] if p.is_relative_to(ROOT)):
            self.send_error(404)
            return None
        if decoded == '/':
            self.path = '/catalog/index.html'
        elif not path.is_file() or path.suffix.lower() not in {'.md', '.json', '.html', '.css'}:
            self.send_error(404)
            return None
        return super().send_head()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('build')
    commands.add_parser('validate')
    find = commands.add_parser('search')
    find.add_argument('query')
    serve = commands.add_parser('serve')
    serve.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    if args.command == 'build':
        build()
    elif args.command == 'validate':
        return validate()
    elif args.command == 'search':
        search(args.query)
    else:
        server = http.server.ThreadingHTTPServer(('127.0.0.1', args.port), PreviewHandler)
        print(f'Skill catalog: http://127.0.0.1:{args.port}', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.server_close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
