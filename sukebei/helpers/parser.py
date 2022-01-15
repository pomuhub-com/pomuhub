"""
Parses

title
===
<Name> <link> <tags>

into a structured format
"""
import json


def parse_item(it):
    parts = it.rsplit(' ', 2)
    if 'http' not in parts[1]:
        parts[1] = f'https://nhentai.net/g/{parts[1]}'
    return {
        'name': parts[0],
        'link': parts[1],
        'tags': parts[2].split(),
    }


raw = open('raw.txt').read().split('\n')

# Group into sections
sections = {}
current_section = None
buffer = []
prev = raw[0]

for line in raw[1:]:
    if line == '===':
        sections[current_section] = [b for b in buffer[:-1] if b.strip()]
        current_section = prev
        buffer = []
        prev = line
        continue

    buffer.append(line)
    prev = line

parsed = []
for sect_name, items in sections.items():
    parsed.append({
        'name': sect_name,
        'items': [parse_item(i) for i in items]
    })

print(json.dumps({
    'categories': parsed
}, indent=2, ensure_ascii=False))
