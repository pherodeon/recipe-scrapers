# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:55:32 2020

@author: arosso
"""

from recipe_scrapers import scrape_me

# give the url as a string, it can be url from any site listed below
# scraper = scrape_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')
scraper = scrape_me('https://www.101cookbooks.com/instant-pot-mushroom-stroganoff/')

dict_recipe = dict()
dict_recipe['title']        = scraper.title()
dict_recipe['total_time']   = scraper.total_time()
dict_recipe['yields']       = scraper.yields()
dict_recipe['ingredients']  = scraper.ingredients()
dict_recipe['instructions'] = scraper.instructions()
#dict_recipe['image']        = scraper.image()
#dict_recipe['links']        = scraper.links()

print(dict_recipe)





