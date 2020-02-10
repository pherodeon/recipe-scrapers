
from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class VelocidadCuchara(AbstractScraper):

    @classmethod
    def host(self):
        return 'velocidadcuchara.com'

    def title(self):
        return self.soup.find('div',  attrs={'class':'ERSName'}).get_text()

    def total_time(self):
        return get_minutes(
            self.soup.find('time', attrs={'itemprop':'totalTime'}).get_text()
        )

    def prep_time(self):
        return get_minutes(
            self.soup.find('time', attrs={'itemprop':'prepTime'}).get_text()
        )
    
    def cook_time(self):
        return get_minutes(
            self.soup.find('time', attrs={'itemprop':'cookTime'}).get_text()
        )

    def yields(self):
        return self.soup.find('span', attrs={'itemprop':'recipeYield'}).get_text()

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'itemprop': 'ingredients'}
        )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.findAll(
            'li',
            {'itemprop': 'recipeInstructions'}
        )

        return [
            normalize_string(instruction.get_text())
            for instruction in instructions
        ]

    def ratings(self):
        return self.soup.find('div', attrs={'itemprop': 'ratingValue'})[0].get_text()

    def reviews(self):
        return self.soup.find('div', attrs={'itemprop': 'ratingValue'})[0].get_text()

    def notes(self):
        return self.soup.find('div', attrs={'class':'ERSNotes'}).get_text()
