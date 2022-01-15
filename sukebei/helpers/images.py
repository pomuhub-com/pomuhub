"""
Pulls images from an annotated.json
"""

import requests
import json
import os

try:
    os.mkdir('images')
except: pass

x = json.load(open('annotated.json'))

for category in x:
    for i in category['items']:
        if 'site_info' in i:
            cover = i['site_info']['cover']['src']
            id = cover.split('/')[-2]
            with open(f'images/{id}.jpg', 'wb') as f:
                f.write(requests.get(cover).content)
