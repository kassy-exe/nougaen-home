#!/usr/bin/env python3
"""Regenerate worker.js from index.html (the Cloudflare Worker embeds the page)."""
import json, pathlib
here = pathlib.Path(__file__).parent
html = (here / 'index.html').read_text(encoding='utf-8')
worker = (
    'const HTML = ' + json.dumps(html) + ';\n'
    'export default { async fetch() { return new Response(HTML, { headers: { "content-type": "text/html; charset=utf-8", "cache-control": "public, max-age=300" } }); } };\n'
)
(here / 'worker.js').write_text(worker, encoding='utf-8')
print('worker.js regenerated:', len(worker), 'bytes')
