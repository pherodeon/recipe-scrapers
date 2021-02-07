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

# %% Parameters

# TODO: move to config file
input_sources_folder = r"C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/_sources/"
# input_sources_folder = r"C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/_sources_test/"
output_base_folder = r"C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/"

# %% Local functions


def get_recipe_dict(link):
    """Wrapper around recipe_scrapers library

    Returns a dictionary with the scraped contents"""

    # Random wait to not overload any webpage
    # sleep(2 + rn.random()*6)
    scraper = scrape_me(link)
    
    dict_recipe = dict()

    # TODO: Is it possible to simplify this? sth *args, **kwargs based with a list of methods?
    # li_fields = ['title']
    # dict_recipe = {field:getattr(scraper, field)() for field in li_fields}
    dict_recipe['title'] = scraper.title()
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

    # TODO: if available, incorporate
    # *nutritional information* (pressurecookrecipes.com)
    # tools (pressurecookrecipes.com) 
    # youtube_link
    # List of tags

    #
    if dict_recipe['instructions_count'] < 1:
        print('Not saved : ' + link)
        return None
    else:
        return dict_recipe


def check_dir(base_dir):
    """Creates dir if not exists

    Requires path library"""
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    return base_dir


def read_links_file(S_LINKS_FILE):
    """Reads text files and returns a list of lines content"""

    # FOR DEBUG
    # li_links = read_links_file(input_sources_folder + "101cookbooks.txt")

    links = []
    with open(S_LINKS_FILE,'r',encoding='windows-1252') as input_file:
        for line in input_file:
            links.append(line.rstrip())
    return links


def write_recipe(recipe, output_base_dir):
    base_dir = output_base_dir + slugify(recipe['host']) + r'/'
    check_dir(base_dir)
    file_out = slugify(recipe['title']) + '.json'
    with open(base_dir + file_out, 'w', encoding='utf-8') as outfile: # 'iso-8859-1' 'windows-1252'
        json.dump(recipe, outfile, indent=2, ensure_ascii=False)


# give the url as a string, it can be url from any site listed below
# scraper = scrape_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')

# %% list of links to download

li_file_paths = glob.glob(input_sources_folder + r'\*.txt')
# li_file_paths = glob.glob(input_sources_folder + r'\**\*.txt', recursive=True)

li_links = []
for file in li_file_paths:
    li_links += read_links_file(file)

# TODO: remove already scraped recipes from li_links unless Overwrite = True

assert len(li_links) != 0, 'Error: link sources files are empty'

# Shuffle list to divide load between several pages
rn.shuffle(li_links)

li_scraped_recipes_raw = [get_recipe_dict(link) for link in li_links]
# Remove not valid links
li_scraped_recipes = list(filter(None, li_scraped_recipes_raw))

# TODO: protect against
# scrape_me
#   link not working
# Writer
#   "title" empty
#   dict_recipe empty
# TODO: move to another folder, import scrape_me from folder location

# %% Write output files

for recipe in li_scraped_recipes:
    write_recipe(recipe, output_base_folder)

