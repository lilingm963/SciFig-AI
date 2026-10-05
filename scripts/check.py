"""Validate public documentation contracts, with positive and negative calibration."""
import json,re,hashlib
from pathlib import Path
from urllib.parse import unquote,urlsplit
ROOT=Path(__file__).resolve().parent.parent
LOCALES=['en','zh','fr','es','it','de','ja','ko']
def validate_keys(text):
 keys=set()
 for line in text.splitlines():
  if not line or line.startswith('#'):continue
  k,*values=line.split('|')
  if k in keys or len(values)!=8 or any(not v.strip() for v in values):raise ValueError(k)
  keys.add(k)
 return keys
assert validate_keys('key|a|b|c|d|e|f|g|h')=={'key'}
for invalid in ['key|a|b|c','key|a|b|c|d|e|f|g|','key|a|b|c|d|e|f|g|h\nkey|a|b|c|d|e|f|g|h']:
 try:validate_keys(invalid)
 except ValueError:pass
 else:raise AssertionError('invalid translation accepted')
keys=validate_keys((ROOT/'content/translations.txt').read_text());assert len(keys)<=100
manifest=json.loads((ROOT/'content/media-manifest.json').read_text());assert len(manifest['videos'])==35
for locale in LOCALES:
 suffix='' if locale=='en' else '.'+locale
 text=(ROOT/f'docs/media-library{suffix}.md').read_text()
 for v in manifest['videos']:assert text.count('https://cdn.scifig.ai'+v['path'])==1,v['id']
 page=(ROOT/('index.html' if locale=='en' else locale+'/index.html')).read_text()
 assert '<h1>' in page and '<meta name="viewport"' in page and page.count('hreflang=')==9
 for path in [ROOT/f'README{suffix}.md',ROOT/f'docs/media-library{suffix}.md',ROOT/f'examples/README{suffix}.md']:
  for url in re.findall(r'\]\(([^)]+)\)',path.read_text()):
   if url.startswith(('http:','https:','#')):continue
   target=path.parent/unquote(urlsplit(url).path)
   assert target.exists(),f'{path.relative_to(ROOT)}: {url}'
for k in ['illustration','datachart','flowchart']:
 actual=hashlib.sha256((ROOT/f'assets/previews/{k}.jpg').read_bytes()).hexdigest()
 expected=next(v['sha256'] for v in manifest['files'] if v['path']==f'/images/media-kit/2026-10/posters/v4-{k}-tutorial.jpg')
 assert actual==expected,k
assert not list(ROOT.rglob('*.mp4'))
print(f'PASS: {len(keys)} synchronized keys; 8 localized pages, READMEs and example guides; 35 indexed videos; local links; curated preview hashes; no binary videos.')
