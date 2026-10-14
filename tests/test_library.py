import contextlib
import hashlib
import importlib.util
import io
import json
import pathlib
import tempfile
import threading
import unittest
import urllib.error
import urllib.request

SPEC = importlib.util.spec_from_file_location('library', pathlib.Path(__file__).parents[1] / 'scripts/library.py')
library = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(library)


class LibraryTests(unittest.TestCase):
    def setUp(self):
        scratch = library.ROOT / '.library-local' / 'tests'
        scratch.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=scratch)
        self.root = pathlib.Path(self.temp.name).resolve()
        self.old_root, self.old_manifest = library.ROOT, library.MANIFEST
        library.ROOT = self.root
        library.MANIFEST = self.root / 'catalog/skills.json'
        (self.root / 'catalog').mkdir()

    def tearDown(self):
        library.ROOT, library.MANIFEST = self.old_root, self.old_manifest
        if not self.root.is_relative_to(self.old_root / '.library-local' / 'tests'):
            raise ValueError('Test cleanup escaped its workspace')
        self.temp.cleanup()

    def fixture(self):
        folder = self.root / 'skills/test/example'
        folder.mkdir(parents=True)
        entry = folder / 'SKILL.md'
        entry.write_text('---\nname: example\ndescription: A focused example.\n---\n\nUse this example.\n', encoding='utf-8')
        item = dict(name='example', description='A focused example.', path='skills/test/example', category='test', origin=None,
                    files={'SKILL.md': hashlib.sha256(entry.read_bytes()).hexdigest()})
        library.MANIFEST.write_text(json.dumps(dict(skills=[item])), encoding='utf-8')
        return item, entry

    def test_integrity_detects_tampering(self):
        _, entry = self.fixture()
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(library.validate(), 0)
            entry.write_text(entry.read_text() + 'Changed instructions.', encoding='utf-8')
            self.assertEqual(library.validate(), 1)

    def test_manifest_cannot_escape_root(self):
        item, _ = self.fixture()
        item['path'] = '../outside'
        library.MANIFEST.write_text(json.dumps(dict(skills=[item])), encoding='utf-8')
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(library.validate(), 1)

    def test_uncataloged_skills_are_detected(self):
        self.fixture()
        folder = self.root / 'rogue'
        folder.mkdir()
        (folder / 'SKILL.md').write_text('Unregistered skill', encoding='utf-8')
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(library.validate(), 1)

    def test_imported_package_cannot_add_untracked_code(self):
        item, entry = self.fixture()
        item['origin'] = {'license_files': []}
        (entry.parent / 'SOURCE.json').write_text(json.dumps(item['origin']), encoding='utf-8')
        item['files']['SOURCE.json'] = library.digest(entry.parent / 'SOURCE.json')
        library.MANIFEST.write_text(json.dumps(dict(skills=[item])), encoding='utf-8')
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(library.validate(), 0)
            (entry.parent / 'unexpected.py').write_text('raise RuntimeError()', encoding='utf-8')
            self.assertEqual(library.validate(), 1)

    def test_preview_blocks_private_paths_and_scripts(self):
        (self.root / 'catalog/index.html').write_text('<h1>Catalog</h1>', encoding='utf-8')
        (self.root / '.private').mkdir()
        (self.root / '.private/config').write_text('private test value', encoding='utf-8')
        (self.root / 'helper.py').write_text('print(1)', encoding='utf-8')
        server = library.http.server.ThreadingHTTPServer(('127.0.0.1', 0), library.PreviewHandler)
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        base = f'http://127.0.0.1:{server.server_port}'
        try:
            with urllib.request.urlopen(base + '/') as response:
                self.assertIn(b'Catalog', response.read())
            for route in ['/.private/config', '/%2eprivate/config', '/.git/config', '/catalog/../.private/config', '/helper.py', '/catalog/', '/%2e%2e/secret.md']:
                with self.assertRaises(urllib.error.HTTPError) as failure:
                    urllib.request.urlopen(base + route)
                self.assertEqual(failure.exception.code, 404)
        finally:
            server.shutdown()
            server.server_close()
            worker.join(timeout=5)


if __name__ == '__main__':
    unittest.main()
