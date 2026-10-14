"""Read public GitHub skill inventories; never execute downloaded content."""
import concurrent.futures
import json
import pathlib
import urllib.request

REPOSITORIES = [
    'openai/skills', 'anthropics/skills', 'vercel-labs/agent-skills',
    'vercel-labs/next-skills', 'supabase/agent-skills', 'trailofbits/skills',
    'wshobson/agents', 'github/awesome-copilot',
    'affaan-m/everything-claude-code', 'obra/superpowers',
    'sickn33/antigravity-awesome-skills', 'microsoft/skills',
    'firebase/agent-skills', 'TheQtCompanyRnD/agent-skills',
    'erkamyaman/ionic-capacitor-skills', 'gabriel-tutor/ionic-capacitor-skills',
]


def get_json(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'Antigravity-Skill-Library'})
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.load(response)


def inspect(repo):
    try:
        info = get_json('https://api.github.com/repos/' + repo)
        tree = get_json('https://api.github.com/repos/' + repo + '/git/trees/' + info['default_branch'] + '?recursive=1')
        return dict(repository=repo, commit=tree['sha'], branch=info['default_branch'],
                    license=(info.get('license') or {}).get('spdx_id'),
                    truncated=tree.get('truncated', False),
                    skills=[x['path'] for x in tree['tree'] if x['path'].endswith('/SKILL.md')],
                    licenses=[x['path'] for x in tree['tree'] if pathlib.PurePosixPath(x['path']).name.lower() in ('license', 'license.txt', 'license.md', 'notice', 'notice.md')])
    except Exception as exc:
        return dict(repository=repo, error=str(exc))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=pathlib.Path, required=True)
    args = parser.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(inspect, REPOSITORIES))
    args.output.write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')
    for result in results:
        print(result['repository'], result.get('license'), len(result.get('skills', [])), result.get('error', ''))
