# from recipe_scrapers import scrape_me
from recipe_scrapers import scrape_me

# give the url as a string, it can be url from any site listed below
# scraper = scrape_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')

link = 'https://www.101cookbooks.com/instant-pot-mushroom-stroganoff/'

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

print(dict_recipe)
