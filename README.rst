.. image:: https://img.shields.io/pypi/v/recipe-scrapers.svg?
    :target: https://pypi.org/project/recipe-scrapers/
    :alt: Version
.. image:: https://travis-ci.org/hhursev/recipe-scrapers.svg?branch=master
    :target: https://travis-ci.org/hhursev/recipe-scrapers
    :alt: Travis
.. image:: https://coveralls.io/repos/hhursev/recipe-scraper/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/hhursev/recipe-scraper?branch=master
    :alt: Coveralls
.. image:: https://img.shields.io/github/license/hhursev/recipe-scrapers?
    :target: https://github.com/hhursev/recipe-scrapers/blob/master/LICENSE
    :alt: License
.. image:: https://img.shields.io/github/stars/hhursev/recipe-scrapers?style=social
    :target: https://github.com/hhursev/recipe-scrapers/
    :alt: Github


------


This repository is a fork from https://github.com/hhursev/recipe-scrapers

Unless the modifications included are critical to you please refer to the main repository

A simple web scraping tool for recipe sites.

How to use

.. code:: python

    from recipe_scrapers import scrape_me

    # give the url as a string, it can be url from any site listed below
    scraper = scrape_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')

    scraper.title()
    scraper.total_time()
    scraper.yields()
    scraper.ingredients()
    scraper.instructions()
    scraper.image()
    scraper.links()

Note: ``scraper.links()`` returns a dictionary object containing all of the <a> tag attributes. The attribute names are the dictionary keys.

Scrapers available for:
-----------------------

- `http://101cookbooks.com/ <http://101cookbooks.com/>`_
- `http://allrecipes.com/ <http://allrecipes.com/>`_
- `http://bbc.com/ <http://bbc.com/food/recipes>`_
- `http://bbc.co.uk/ <http://bbc.co.uk/food/recipes>`_
- `http://bbcgoodfood.com/ <http://bbcgoodfood.com>`_
- `http://bettycrocker.com/ <http://bettycrocker.com>`_
- `http://bonappetit.com/ <http://bonappetit.com>`_
- `https://www.budgetbytes.com/ <https://www.budgetbytes.com>`_
- `http://closetcooking.com/ <http://closetcooking.com>`_
- `http://cookstr.com/ <http://cookstr.com>`_
- `https://en.wikibooks.org/ <https://en.wikibooks.org>`_
- `http://epicurious.com/ <http://epicurious.com>`_
- `http://finedininglovers.com/ <https://www.finedininglovers.com>`_
- `https://food.com/ <https://www.food.com>`_
- `http://foodnetwork.com/ <http://www.foodnetwork.com>`_
- `http://foodrepublic.com/ <http://foodrepublic.com>`_
- `https://geniuskitchen.com/ <https://geniuskitchen.com>`_
- `http://giallozafferano.it/ <http://giallozafferano.it>`_
- `https://healthyeating.nhlbi.nih.gov/ <https://healthyeating.nhlbi.nih.gov>`_
- `https://www.hellofresh.com/ <https://www.hellofresh.com>`_
- `https://www.hellofresh.co.uk/ <https://www.hellofresh.co.uk>`_
- `https://inspiralized.com/ <https://inspiralized.com>`_
- `http://jamieoliver.com/ <http://www.jamieoliver.com>`_
- `https://www.thekitchn.com/ <https://www.thekitchn.com/>`_
- `https://www.matprat.no/ <https://www.matprat.no/>`_
- `http://mybakingaddiction.com/ <http://mybakingaddiction.com>`_
- `https://panelinha.com.br/ <https://panelinha.com.br>`_
- `http://paninihappy.com/ <http://paninihappy.com>`_
- `http://realsimple.com/ <http://www.realsimple.com>`_
- `https://www.seriouseats.com/ <https://www.seriouseats.com>`_
- `http://simplyrecipes.com/ <http://www.simplyrecipes.co>`_
- `http://steamykitchen.com/ <http://steamykitchen.com>`_
- `https://www.tastesoflizzyt.com <https://www.tastesoflizzyt.com>`_
- `http://tastykitchen.com/ <http://tastykitchen.com>`_
- `http://thepioneerwoman.com/ <http://thepioneerwoman.com>`_
- `https://www.thespruceeats.com/ <https://www.thespruceeats.com/>`_
- `http://thehappyfoodie.co.uk/ <http://thehappyfoodie.co.uk>`_
- `http://thevintagemixer.com/ <http://www.thevintagemixer.com>`_
- `http://tine.no/ <http://tine.no>`_
- `http://twopeasandtheirpod.com/ <http://twopeasandtheirpod.com>`_
- `http://whatsgabycooking.com/ <http://whatsgabycooking.com>`_
- `http://yummly.com/ <http://yummly.com>`_



