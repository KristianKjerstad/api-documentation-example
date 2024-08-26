from typing import List

from resources.ingredient.entities.ingredient import Ingredient
from data.data import ingredients

def get_all_ingredients_use_case() -> List[Ingredient]:
    return ingredients

