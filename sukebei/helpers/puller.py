"""
Pulls info for each nhentai related doujin
"""

import dataclasses
import json
from NHentai import NHentai

data = json.load(open('data.json'))
nhentai = NHentai()

def format_site_info(si): 
    si = dataclasses.asdict(si)
    del si["media_id"] 
    del si["characters"] 
    del si["parodies"] 
    del si["images"] 
    del si["total_favorites"] 
    si["tags"] = [t["name"] for t in si["tags"]] 
    si["artists"] = [a["name"] for a in si["artists"]] 
    si["languages"] = [l["name"] for l in si["languages"]] 
    del si["categories"] 
    if "characters" in si: 
        del si["characters"] 
    si["parodies"] = [p["name"] for p in si.get("parodies", [])] 
    si["groups"] = [g["name"] for g in si["groups"]] 
    return si

def annotate_item(item):
    if not item['link'].startswith('https://nhentai.net/g/'):
        return item

    item['site_info'] = format_site_info(nhentai.get_doujin(item['link'].split('/')[-1]))
    return item

loaded = []
for d in data['categories']:
    loaded.append({
        'name': d['name'],
        'items': [annotate_item(item) for item in d['items']]
    })

json.dump(loaded, open('annotated.json', 'w'), default=str, ensure_ascii=False)
