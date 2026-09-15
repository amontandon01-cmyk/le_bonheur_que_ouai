"""Set the canonical origin and indexing mode before publication. Standard library only."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlsplit
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]

def configure(base_url, production=False):
    parsed = urlsplit(base_url)
    if parsed.scheme != 'https' or not parsed.hostname or parsed.query or parsed.fragment or parsed.username:
        raise ValueError('Use an absolute HTTPS base URL without credentials, query or fragment.')
    base = base_url.rstrip('/') + '/'
    urls = []
    for path in sorted(ROOT.glob('*.html')):
        content = path.read_text(encoding='utf-8')
        match = re.search(r'<link rel="canonical" href="([^"]+)">', content)
        if not match:
            raise ValueError(f'Missing canonical: {path.name}')
        old_url = match.group(1)
        old_base = old_url if path.name == 'index.html' else old_url.rsplit('/', 1)[0] + '/'
        url = base if path.name == 'index.html' else base + path.name
        # Limit replacement to metadata, preserving existing image URLs and editorial links.
        content = re.sub(r'(<link rel="canonical" href=")[^"]+(">)', lambda m: m[1] + url + m[2], content)
        content = re.sub(r'(<meta property="og:url" content=")[^"]+(">)', lambda m: m[1] + url + m[2], content)
        content = re.sub(r'(<meta property="og:image" content=")([^"]+)(">)',
                         lambda m: m[1] + (base + m[2][len(old_base):] if m[2].startswith(old_base) else m[2]) + m[3], content)
        def rewrite_graph(match):
            def visit(value):
                if isinstance(value, dict):
                    return {key: visit(item) for key, item in value.items()}
                if isinstance(value, list):
                    return [visit(item) for item in value]
                if isinstance(value, str) and value.startswith(old_base):
                    return base + value[len(old_base):]
                return value
            data = visit(json.loads(match[1]))
            return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '</script>'
        content = re.sub(r'<script type="application/ld\+json">(.*?)</script>', rewrite_graph, content, flags=re.S)
        policy = 'index,follow,max-image-preview:large' if production else 'noindex,follow'
        content = re.sub(r'(<meta name="robots" content=")[^"]*(">)', lambda m: m[1] + policy + m[2], content)
        path.write_text(content, encoding='utf-8')
        urls.append(url)
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    if production:
        sitemap += ''.join(f'  <url><loc>{escape(url)}</loc></url>\n' for url in urls)
    sitemap += '</urlset>\n'
    (ROOT / 'sitemap.xml').write_text(sitemap, encoding='utf-8')
    robots = 'User-agent: *\nAllow: /\n'
    robots += f'Sitemap: {base}sitemap.xml\n' if production else '# Préproduction : noindex dans chaque page HTML.\n'
    (ROOT / 'robots.txt').write_text(robots, encoding='utf-8')
    print(f'{len(urls)} pages configured: {base} ({"production" if production else "preview"})')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--production', action='store_true')
    options = parser.parse_args()
    configure(options.base_url, options.production)
