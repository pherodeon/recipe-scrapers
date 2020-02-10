'''

TODO: public move to github public account / rename this account

TODO: move all utilities outside this repository
 - install your fork as a library
 - import from another folder

'''

# from recipe_scrapers import scrape_me
from recipe_scrapers import scrape_me

import os
import glob
import json
from slugify import slugify

# give the url as a string, it can be url from any site listed below
# scraper = scrape_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')

# Parameters
input_sources_folder = r"C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/_sources/"
output_base_folder = r"C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/"


def get_recipe_dict(link):
    """Wrapper around recipe_scrapers library"""
    # FOR DEBUG : link = 'https://www.101cookbooks.com/instant-pot-mushroom-stroganoff/'
	# dict_recipe = get_recipe_dict(link)
	# print(dict_recipe)
	
    scraper = scrape_me(link)

    dict_recipe = dict()
    dict_recipe['title'] = scraper.title()
    dict_recipe['total_time'] = scraper.total_time()
    dict_recipe['prep_time'] = scraper.prep_time()
    dict_recipe['cook_time'] = scraper.cook_time()
	# TODO: return yields as number
    dict_recipe['yields'] = scraper.yields()
    # TODO: read ingredients, instructions as list + count
    dict_recipe['ingredients'] = scraper.ingredients()
    dict_recipe['instructions'] = scraper.instructions()
	# TODO: improve ratings, reviews (all = -1)
    dict_recipe['ratings'] = scraper.ratings()
    dict_recipe['reviews'] = scraper.reviews()
    dict_recipe['source'] = link
    dict_recipe['host'] = scraper.host()

    # Data from scrape_me not used.
    # TODO: How to add a link to a picture in a json file?
    # dict_recipe['image'] = scraper.image()
    # dict_recipe['links'] = scraper.links()
	
	# TODO: Data from easyrecipe, not scraped:
    # Type 'easyrecipe'; "wprm-recipe-container"
    # dict_recipe['author'] = (True, 'span', 'itemprop', 'author')
    # dict_recipe['type'] = (True, 'span', 'itemprop', 'recipeCategory')
    # dict_recipe['cuisine'] = (True, 'span', 'itemprop', 'recipeCuisine')
    # dict_recipe['notes'] = (True, 'div', 'class', 'ERSNotes')
    # dict_recipe['date'] = (True  ,'div'  ,'itemprop' ,'datePublished'      )
    # recipe = bs.find('div', attrs={'class': 'easyrecipe'})

    return dict_recipe


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
    li_links.append(read_links_file(file))

# TODO: remove already scraped recipes from li_links unless Overwrite = True

# The core of this script in only one line!
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


def write_recipe(recipe, output_base_dir):
    base_dir = output_base_dir + slugify(recipe['host']) + r'/'
    check_dir(base_dir)
    file_out = slugify(recipe['title']) + '.json'
    with open(base_dir + file_out, 'w', encoding='utf-8') as outfile: # 'iso-8859-1' 'windows-1252'
        json.dump(recipe, outfile, indent=2, ensure_ascii=False)


for recipe in li_scraped_recipes:
    write_recipe(recipe, output_base_folder)

