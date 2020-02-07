# from recipe_scrapers import scrape_me
from recipe_scrapers import scrape_me

import os
import json
from slugify import slugify

# give the url as a string, it can be url from any site listed below
# scraper = scrape_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')


def get_recipe_dict(link):
    scraper = scrape_me(link)

    dict_recipe = dict()
    dict_recipe['title'] = scraper.title()
    dict_recipe['total_time'] = scraper.total_time()
    dict_recipe['prep_time'] = scraper.prep_time()
    dict_recipe['cook_time'] = scraper.cook_time()
    dict_recipe['yields'] = scraper.yields()
    dict_recipe['ingredients'] = scraper.ingredients()
    dict_recipe['instructions'] = scraper.instructions()
    # dict_recipe['image'] = scraper.image()
    # dict_recipe['links'] = scraper.links()
    dict_recipe['ratings'] = scraper.ratings()
    dict_recipe['reviews'] = scraper.reviews()
    dict_recipe['source'] = link
    dict_recipe['host'] = scraper.host()

    # Type 'easyrecipe'; "wprm-recipe-container"
    # dict_recipe['Author'] = (True, 'span', 'itemprop', 'author')
    # dict_recipe['recipeType'] = (True, 'span', 'itemprop', 'recipeCategory')
    # dict_recipe['cuisine'] = (True, 'span', 'itemprop', 'recipeCuisine')
    # dict_recipe['Notes'] = (True, 'div', 'class', 'ERSNotes')


    # pendiente!!!! No está dentro de la receta !!! hay que cogerlo de fuera
    # !d_conf['date'         ] = (True  ,'div'  ,'itemprop' ,'datePublished'      )

    # recipe = bs.find('div', attrs={'class': 'easyrecipe'})

    return dict_recipe

# FOR DEBUG :
# link = 'https://www.101cookbooks.com/instant-pot-mushroom-stroganoff/'
# dict_recipe = get_recipe_dict(link)
# print(dict_recipe)


# Move to file
li_links = [
    'https://www.101cookbooks.com/instant-pot-congee-recipe/',
    'https://www.101cookbooks.com/instant-pot-brown-rice-bowl/',
    'https://www.101cookbooks.com/instant-pot-minestrone-soup-recipe/',
    'https://www.101cookbooks.com/instant-pot-chickpea-cauliflower-korma/',
    'https://www.101cookbooks.com/instant-pot-mushroom-stroganoff/',
    'https://www.101cookbooks.com/spicy-instant-pot-taco-soup-recipe/',
    'https://www.101cookbooks.com/instant-pot-chili-mac-recipe/'
    'https://www.101cookbooks.com/slow-cooker-black-bean-chili/'
]
li_scraped_recipes = [ get_recipe_dict(link) for link in li_links]


# TODO: proteger contra "title" vacío
#   quizás se pueda sacar de otro campo

def check_dir(base_dir):
    """Creates dir if not exists

    Requires path library"""
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    return base_dir

def write_recipe(recipe):
    base_dir = r'./' + slugify(recipe['host']) + r'/'
    check_dir(base_dir)
    file_out = slugify(recipe['title']) + '.json'
    with open(base_dir + file_out, 'w', encoding='utf-8') as outfile: # 'iso-8859-1' 'windows-1252'
        json.dump(recipe, outfile, indent=2, ensure_ascii=False)


for dict_recipe in li_scraped_recipes:
    write_recipe(dict_recipe)

