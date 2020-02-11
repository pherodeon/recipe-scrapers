"""

TODO: If file exists, read file instead of scraping again, unless overwrite=True
TODO: catch errors
TODO: public move to github public account / rename this account
TODO: move all utilities outside this repository
 - install your fork as a library
 - import from another folder
TODO move "FOR DEBUG" to testing utilities

"""

# from recipe_scrapers import scrape_me
from recipe_scrapers import scrape_me

import os
import glob
import json
from slugify import slugify

# from time import sleep, time
import random as rn

# give the url as a string, it can be url from any site listed below
# scraper = scrape_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')

# Parameters
input_sources_folder = r"C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/_sources/"
output_base_folder = r"C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/"


def get_recipe_dict(link):
    """Wrapper around recipe_scrapers library

    Returns a dictionary with the scraped contents"""

    # Random wait to not overload webpage
    # sleep(2 + rn.random()*6)
    scraper = scrape_me(link)
    
    dict_recipe = dict()

    # TODO: Is it possible to simplify this?
    dict_recipe['title'] = scraper.title()
    print(dict_recipe['title']) # For live-view
    dict_recipe['total_time'] = scraper.total_time()
    dict_recipe['prep_time'] = scraper.prep_time()
    dict_recipe['cook_time'] = scraper.cook_time()
	# TODO: return yields as number
    dict_recipe['yields'] = scraper.yields()
    dict_recipe['ingredients'] = scraper.ingredients()
    dict_recipe['instructions'] = scraper.instructions()
    dict_recipe['ratings'] = scraper.ratings()
    dict_recipe['reviews'] = scraper.reviews()
    dict_recipe['source'] = link
    dict_recipe['cuisine'] = scraper.cuisine()
    dict_recipe['category'] = scraper.category()
    dict_recipe['host'] = scraper.host()
    dict_recipe['host'] = scraper.host()

    # Derived fields
    dict_recipe['ingredients_count'] = len(dict_recipe['ingredients'])
    dict_recipe['instructions_count'] = len(dict_recipe['instructions'])

    # Data from scrape_me not used.
    # TODO: How to add a link to a picture in a json file?
    # dict_recipe['image'] = scraper.image()
    # dict_recipe['links'] = scraper.links()
	
	# TODO: Data from easyrecipe, not scraped:
    # Type 'easyrecipe'; "wprm-recipe-container"


    return dict_recipe

# %% list of links to download
def read_links_file(S_LINKS_FILE):
    """Reads text files and returns a list of lines content"""

    # FOR DEBUG
    # li_links = read_links_file(input_sources_folder + "101cookbooks.txt")

    links = []
    with open(S_LINKS_FILE,'r',encoding='windows-1252') as input_file:
        for line in input_file:
            links.append(line.rstrip())
    return links


li_file_paths = glob.glob(input_sources_folder + r'\**\*.txt', recursive=True)


li_links = []
for file in li_file_paths:
    li_links += read_links_file(file)

# TODO: remove already scraped recipes from li_links unless Overwrite = True


# Shuffle list to divide load between several pages
rn.shuffle(li_links)

li_scraped_recipes = [get_recipe_dict(link) for link in li_links]

# TODO: protect against
# scrape_me
#   link not working
# Writer
#   "title" empty
#   dict_recipe empty
# TODO: move to another folder, import scrape_me from folder location


def check_dir(base_dir):
    """Creates dir if not exists

    Requires path library"""
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    return base_dir

# %% Data analysis
"""

# %% Writes recipes summary csv file
li_fields = ['title', 'yields', 'ratings', 'reviews', 'prep_time', 'cook_time', 'total_time', 'host', 'source']

with open(s_json_recipe_dir + s_host + '.csv', mode='w', newline='\n', encoding='windows-1252') as output_file:
    output_file_writer = csv.writer(output_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    output_file_writer.writerow(li_fields)
    # TODO: replace writerow by auxiliary function using li_fields
    for recipe in dict_results:
        output_file_writer.writerow([ \
            dict_results[recipe]['title'], \
            # TODO: dict_results[recipe]['Author'], \
            # TODO: dict_results[recipe]['recipeType'], \
            # TODO: dict_results[recipe]['cuisine'], \
            # TODO: count of ingredients
            # TODO: count of instructions
            dict_results[recipe]['yields'], \
            dict_results[recipe]['ratings'], \
            dict_results[recipe]['reviews'], \
            dict_results[recipe]['prep_time'], \
            dict_results[recipe]['cook_time'], \
            dict_results[recipe]['total_time'], \
            dict_results[recipe]['host'], \
            dict_results[recipe]['source'] ])
        #output_file_writer.writerow([recipe['Name'], recipe['time_prep'], recipe['time_cook'], recipe['time_total']])
        #print(dict_results[recipe]['Name'])#, recipe['time_prep'], recipe['time_cook'], recipe['time_total'])


# Remove rows with sweets and desserts
s_flt = "almíbar|Batido|Brownie|Bizco|Cake|Caramel|Carbón|Chocolate|Coca|Dulce" + \
            "|Flan|Gallet|Gofre|Helado|Magdalena|Mermelada|Natilla|Navidad|Nocilla" + \
            "|Nugget|Palmer|Pan|Plumcake|Strudel|Sorbete|Tarta|Zumo"

df = pd.read_csv( sFileIn + '.csv', sep=';', \
                         encoding='windows-1252') #'windows-1252')


# remove outliers
df = df[df.i_time_prep  < df.i_time_prep.quantile(.9) ]
df = df[df.i_time_cook  < df.i_time_cook.quantile(.9) ]
df = df[df.i_time_total < df.i_time_total.quantile(.9) ]

# Remove rows with zeros:
df = df[df.i_time_prep  > 0 ]
df = df[df.i_time_cook  > 0 ]
df = df[df.i_time_total > 0 ]

df_flt = df[df['Name'].str.contains(s_flt, case=False)==False]
df_flt.to_csv(sFilePrefix + sFileIn + '_flt.csv', sep =';', encoding='windows-1252')

df_flt_neg = df[df['Name'].str.contains(s_flt, case=False)==True]
df_flt_neg.to_csv(sFilePrefix + sFileIn + '_flt_neg.csv', sep =';', encoding='windows-1252')


#df.hist(column=['i_time_prep','i_time_cook','i_time_total'], bins=40) 
df.hist(column=['i_time_prep','i_time_cook','i_time_total'], bins=range(0, 80, 5))

df.hist(column=['ratingValue', 'ratingCount'], bins=40)
"""

# %% Write output files

def write_recipe(recipe, output_base_dir):
    base_dir = output_base_dir + slugify(recipe['host']) + r'/'
    check_dir(base_dir)
    file_out = slugify(recipe['title']) + '.json'
    with open(base_dir + file_out, 'w', encoding='utf-8') as outfile: # 'iso-8859-1' 'windows-1252'
        json.dump(recipe, outfile, indent=2, ensure_ascii=False)


for recipe in li_scraped_recipes:
    write_recipe(recipe, output_base_folder)

