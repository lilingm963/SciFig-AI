"""Generate the eight-language public hub from reviewed content snapshots.
Run: python3 scripts/build.py. No network access or dependencies required.
"""
import json, html, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
LOCALES = ['en','zh','fr','es','it','de','ja','ko']
NAMES = ['English','中文','Français','Español','Italiano','Deutsch','日本語','한국어']
CONTENT = {locale:{} for locale in LOCALES}
for line in (ROOT/'content/translations.txt').read_text().splitlines():
    if not line or line.startswith('#'): continue
    key,*values = line.split('|')
    if len(values) != 8 or any(not v.strip() for v in values): raise ValueError(key)
    for locale,value in zip(LOCALES,values):
        if key in CONTENT[locale]: raise ValueError('duplicate '+key)
        CONTENT[locale][key] = value
MEDIA = json.loads((ROOT/'content/media-manifest.json').read_text())
UI = json.loads((ROOT/'content/media-translations.json').read_text())
CDN = 'https://cdn.scifig.ai'
REPO = 'https://github.com/lilingm963/SciFig-AI'
TEMPLATES = 'https://github.com/scifig-ai/scientific-poster-and-presentation-templates'
SKILL = 'https://github.com/lilingm963/scifig-ai-scientific-figure-skill'
BASE = 'https://lilingm963.github.io/SciFig-AI/'
def suffix(locale): return '' if locale=='en' else '.'+locale
def web(locale,path=''): return 'https://scifig.ai/'+('' if locale=='en' else locale+'/')+path+'?ref=github-resources'
def md(text,url): return f'[{text}]({url})'
def langnav(prefix=''):
    return ' · '.join(md(name,prefix+'README'+suffix(locale)+'.md') for locale,name in zip(LOCALES,NAMES))
def write(path,text):
    out=ROOT/path; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(text.rstrip()+'\n')
def link(text,url,cls=''): return f'<a class="{cls}" href="{html.escape(url,quote=True)}">{html.escape(text)}</a>'
def p(text): return '<p>'+html.escape(text)+'</p>'
for locale,t in CONTENT.items():
    s=suffix(locale); ui=UI[locale]; prefix="" if locale=="en" else "../"
    root = f'# SciFig\n\n{langnav()}\n\n## {t["headline"]}\n\n{t["intro"]}\n\n'+md(t['start'],web(locale))+' · '+md(ui['tutorialLink'],web(locale,'tutorials'))+' · '+md(t['media'],'docs/media-library'+s+'.md')+'\n\n'
    root += f'## {t["workspace"]}\n\n'
    cards=[]
    for name,key in [('Illustration','illustration'),('DataChart','datachart'),('FlowChart','flowchart')]:
        video = next(v for v in MEDIA['videos'] if v['name']==key+'Tutorial')
        root += f'### {name}\n\n{t[key]}\n\n'+f'[![{ui["videoNames"][key+"Tutorial"]}](assets/previews/{key}.jpg)]({CDN+video["path"]})\n\n'+md(t['workflow'],CDN+video['path'])+' · '+md(ui['tutorialLink'],web(locale,'tutorials'))+'\n\n'
        cards.append(f'<article><a href="{CDN+video["path"]}"><img src="{prefix}assets/previews/{key}.jpg" alt="{html.escape(ui["videoNames"][key+"Tutorial"],quote=True)}" width="640" height="360" loading="lazy"></a><div><h3>{name}</h3>{p(t[key])}{link(t["workflow"],CDN+video["path"])}</div></article>')
    root += t['review']+'\n\n'+f'## {t["examples"]}\n\n{t["synthetic"]}\n\n'+md(t['examples'],'examples/README'+s+'.md')+'\n\n'
    resources=[(t['templates'],t['templateBody'],TEMPLATES),(t['skill'],t['skillBody'],SKILL),(t['media'],t['mediaBody'],'docs/media-library'+s+'.md')]
    root += f'## {t["resources"]}\n\n'+''.join(f'### {title}\n\n{body}\n\n'+md(title,url)+'\n\n' for title,body,url in resources)
    root += f'## {t["author"]}\n\n{t["bio"]}\n\n'+md(t['about'],web(locale,'about'))+'\n\n'+f'## {t["license"]}\n\n{t["licenseBody"]}\n\n'+md(ui['licenseTitle'],web(locale,'media-kit')+'#usage')+' · '+md('MIT',SKILL+'/blob/main/LICENSE')+' · '+md(t['templates'],TEMPLATES+'/blob/main/LICENSE')+'\n\n'+f'## {t["feedback"]}\n\n{t["feedbackBody"]}\n\n'+md(t['feedback'],REPO+'/issues')+' · '+md(t['feedback'],web(locale,'contact'))+'\n\n'+f'## {t["updates"]}\n\n{t["updateBody"]}'
    write('README'+s+'.md',root)
    example=f'# {t["examples"]}\n\n{langnav()}\n\n{t["synthetic"]}\n\n'
    for key,title,prompt,steps in [('illustration','illustrationCase','figurePrompt','figureSteps'),('datachart','chartCase',None,'chartSteps'),('flowchart','flowCase','flowPrompt','flowSteps')]:
        example+=f'## {t[title]} · {key.title() if key=="illustration" else "DataChart" if key=="datachart" else "FlowChart"}\n\n### {t["input"]}\n\n'
        example+=t[prompt]+'\n\n' if prompt else md('synthetic-timeseries.csv','datachart/synthetic-timeseries.csv')+'\n\n'
        example+=f'### {t["steps"]}\n\n{t[steps]}\n\n'+md(t['workflow'],CDN+next(v['path'] for v in MEDIA['videos'] if v['name']==key+'Tutorial'))+'\n\n'
        if prompt: write('examples/'+key+'/prompt'+s+'.txt',t[prompt])
    example+=t['review']+'\n\n'+t['licenseBody']+'\n\n'+md(t['license'], '../docs/example-usage'+s+'.md')
    write('examples/README'+s+'.md',example)
    write('docs/example-usage'+s+'.md',f'# {t["license"]}\n\n{t["synthetic"]}\n\n{t["exampleUsage"]}\n\n'+md(ui['licenseTitle'],web(locale,'media-kit'))+'\n\n'+t['licenseBody'])
    library=f'# {t["media"]}\n\n'+ ' · '.join(md(n,'media-library'+suffix(l)+'.md') for l,n in zip(LOCALES,NAMES))+f'\n\n{t["mediaBody"]}\n\n{ui["languageNeutral"]}\n\n'
    library+=md(ui['downloadLanguage'],CDN+'/files/media-kit/2026-10/scifig-media-pack-'+locale+'.zip')+' · '+md(ui['downloadBrand'],CDN+'/files/media-kit/2026-10/scifig-brand-essentials.zip')+' · '+md(ui['licenseTitle'],web(locale,'media-kit'))+'\n\n'
    for cat in ['brand','workspaces','editing','tutorials','social','inputModes']:
        library+=f'## {ui[cat]}\n\n| {ui["videosTitle"]} | {ui["language"]} | {ui["duration"]} | {ui["format"]} | {ui["size"]} | {ui["download"]} |\n|---|---|---|---|---|---|\n'
        for v in MEDIA['videos']:
            if v['category']!=cat: continue
            library+=f'| {ui["videoNames"][v["name"]]} | {v["locale"] or ui["languageNeutral"]} | {v["duration"]:g} s | {v["aspectRatio"]} MP4 | {v["bytes"]/1000000:.2f} MB | '+md('MP4',CDN+v['path'])+' |\n'
        library+='\n'
    library+=f'## {ui["tutorials"]} · {ui["language"]}\n\n'
    for v in MEDIA['files']:
        if v['path'].endswith(('-'+locale+'.srt','-'+locale+'.vtt','-chapters-'+locale+'.txt')):
            library+='- '+md(v['path'].split('/')[-1],CDN+v['path'])+'\n'
    library+='\n'+f'## {ui["licenseTitle"]}\n\n{ui["licenseIntro"]}\n\n{t["exampleUsage"]}\n\n{ui["sourceNote"]}\n\n'+md(ui['licenseTitle'],web(locale,'media-kit'))
    write('docs/media-library'+s+'.md',library)
    langs=''.join(link(n,prefix+('' if l=='en' else l+'/'), 'current' if l==locale else '').replace('class="current"','class="current" aria-current="page"') for l,n in zip(LOCALES,NAMES))
    resourcehtml=''.join('<article class="resource"><div><h3>'+link(title, url if url.startswith('http') else REPO+'/blob/main/'+url)+'</h3>'+p(body)+'</div></article>' for title,body,url in resources)
    page=f'''<!doctype html><html lang="{locale if locale!='zh' else 'zh-Hans'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SciFig — {html.escape(t['headline'])}</title><meta name="description" content="{html.escape(t['intro'],quote=True)}"><link rel="stylesheet" href="{prefix}assets/hub.css"><link rel="canonical" href="{BASE+('' if locale=='en' else locale+'/')}">'''
    page+=''.join(f'<link rel="alternate" hreflang="{l if l!="zh" else "zh-Hans"}" href="{BASE+("" if l=="en" else l+"/")}">' for l in LOCALES)+f'<link rel="alternate" hreflang="x-default" href="{BASE}"></head><body><header><a class="brand" href="{prefix or "./"}">SciFig<span> / {html.escape(t["resources"])}</span></a><nav aria-label="{html.escape(t["languageLabel"],quote=True)}">{langs}</nav></header><main><section class="hero"><div class="eyebrow">{html.escape(ui["eyebrow"])}</div><h1>{html.escape(t["headline"])}</h1>{p(t["intro"])}<div class="actions">{link(t["start"],web(locale),"primary")}{link(t["examples"],REPO+"/blob/main/examples/README"+s+".md")}</div></section><section><h2>{html.escape(t["workspace"])}</h2><div class="grid">{"".join(cards)}</div><div class="note">{p(t["review"])}</div></section><section><h2>{html.escape(t["resources"])}</h2><div class="grid">{resourcehtml}</div></section><section class="split"><div><h2>{html.escape(t["author"])}</h2>{p(t["bio"])}{link(t["about"],web(locale,"about"))}</div><div class="note"><h2>{html.escape(t["updates"])}</h2>{p(t["updateBody"])}</div></section><section><h2>{html.escape(t["license"])}</h2>{p(t["licenseBody"])}{link(ui["licenseTitle"],web(locale,"media-kit"))}</section></main><footer>{p(t["feedbackBody"])}{link(t["feedback"],REPO+"/issues")} · {link("GitHub",REPO)} · {link(ui["tutorialLink"],web(locale,"tutorials"))}</footer></body></html>'
    write(('' if locale=='en' else locale+'/')+'index.html',page)
write('docs/media-naming.json',json.dumps([{'id':v['id'],'cdnPath':v['path'],'downloadName':'scifig-'+re.sub(r'(?<!^)(?=[A-Z])','-',v['name']).lower()+'-'+v['aspectRatio'].replace(':','x')+(('-'+v['locale']) if v['locale'] else '')+'-2026-10.mp4','sha256':v['sha256']} for v in MEDIA['videos']],ensure_ascii=False,indent=2))
write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+BASE+('' if l=='en' else l+'/')+'</loc></url>' for l in LOCALES)+'</urlset>')
write('llms.txt','# SciFig\n\nAI-assisted scientific illustrations, data charts and structured flowcharts.\n\n## Public resources\n- [Official platform](https://scifig.ai/)\n- [Three synthetic teaching examples]('+REPO+'/tree/main/examples)\n- [Media library]('+REPO+'/blob/main/docs/media-library.md)\n- [Templates]('+TEMPLATES+')\n- [Scientific Figure Skill]('+SKILL+')\n\nReview scientific content and sources. Editing/export varies by workflow. Media, templates and Skill have separate licenses. The Skill does not call a SciFig API. No blanket scientific-accuracy or journal-acceptance claim is made.\n')
print(f'Generated {len(LOCALES)} languages with {len(CONTENT["en"])} source keys and {len(MEDIA["videos"])} videos.')
