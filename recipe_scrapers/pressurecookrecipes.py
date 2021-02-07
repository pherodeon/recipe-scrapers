from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields

# TODO: define "wprm-recipe-container" scraper class and inherit from it


class PressureCookRecipes(AbstractScraper):

    @classmethod
    def host(self):
        return 'pressurecookrecipes.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.findAll(
            'div',
            {'class': 'wprm-recipe-total_time'})[0].get_text()
        )

    def prep_time(self):
        return get_minutes(self.soup.findAll(
            'div',
            {'class': 'wprm-recipe-prep_time'})[0].get_text()
        ) # 'wprm-recipe-details wprm-recipe-details-minutes wprm-recipe-prep_time wprm-recipe-prep_time-minutes'
    
    def cook_time(self):
        return get_minutes(
            self.soup.findAll(
            'div',
            {'class': 'wprm-recipe-cook_time-minutes'})[0].get_text()
        )

    def yields(self):
        self.soup.findAll(
            'div',
            {'class': 'wprm-recipe-servings'})[0].get_text()

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'class': 'wprm-recipe-ingredients'}
        )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.findAll(
            'li',
            {'class': 'wprm-recipe-instruction'}
        )

        return [
            normalize_string(instruction.get_text())
            for instruction in instructions
        ]

    def notes(self):
        # TODO:
        return 'not-available'

    def ratings(self):
	    # TODO: return as number
        return self.soup.findAll(
            'span',
            {'class': 'wprm-recipe-rating-average'}
        )[0].get_text()

    def reviews(self):
	    # TODO: return as number
        return self.soup.findAll(
            'span',
            {'class': 'wprm-recipe-rating-count'}
        )[0].get_text()

    def category(self):
        # TODO get from tags?
        return 'not-available'

    def cuisine(self):
        return 'not-available'

    def author(self):
        return self.soup.find('span', attrs={'class': 'wprm-recipe-author'}).get_text()

    def date_published(self):
        # TODO
        return 'not-available'
