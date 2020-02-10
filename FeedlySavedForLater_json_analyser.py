'''Reading


author : arosso
'''
# %% Libraries
import json
import re
import pandas as pd

# %% File reading

s_file = r'C:/Users/arosso/Dropbox/02_PROG/Python/web_scraping/RSS_feeds/FeedlySavedForLater1576052675954_mod.json'

with open(s_file, encoding='utf-8-sig') as json_file: #windows-1252,'utf-8'
     dict_recipe = json.load(json_file)
     

# %% Select vcuch recipes

#pattern = r'\.[a-zA-Z0-9-]{1,61}[a-zA-Z0-9]+\.[a-zA-Z]+'
pattern = r'\.[a-zA-Z0-9-]+\.[a-zA-Z]+'

## Debug
recipe = dict_recipe[0]
peter = re.search(pattern, recipe['url'])[0]

li = []
dict_urls = {}
list_vcuch = []
for recipe in dict_recipe:
    # print(recipe['url'])
    #print(re.match(r'\.[a-zA-Z0-9-]{1,61}[a-zA-Z0-9]+\.[a-zA-Z]+', recipe['url']))
    match      = re.search(pattern, recipe['url'])
    if match is not None:
        li.append((recipe['url'], match[0]))
        dict_urls[recipe['url']] = match[0]
        print(match[0])
        if match[0] == '.velocidadcuchara.com':
            list_vcuch.append(recipe['url'])

# %% 
#df = pd.DataFrame.from_records(dict_urls)

# %% 
with open('vcuch_result.txt','w+') as outfile:
    for recipe in list_vcuch:
        outfile.write(f'{recipe}\n')

