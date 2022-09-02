import json

with open('scowl.txt') as f:
    text = f.read()

splittext = text.split('---')

textlist = splittext[1].split('\n')

alphaonly = [x.lower() for x in textlist if x.isalpha()]

res_dct = {alphaonly[i]:1 for i in range(0, len(alphaonly), 1)}

with open('scowl.json', 'w', encoding='utf-8') as f:
    json.dump(res_dct, f, ensure_ascii=False, indent=4)

print(len(alphaonly))