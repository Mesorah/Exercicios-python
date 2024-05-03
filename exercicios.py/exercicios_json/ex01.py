import json

with open('ex01.json', 'r', encoding='utf8') as arquivo:
    print(json.load(arquivo))