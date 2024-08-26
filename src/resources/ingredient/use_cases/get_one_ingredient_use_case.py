from uuid import UUID

from resources.ingredient.entities.ingredient import Ingredient
from data.data import ingredients

def get_one_ingredient_use_case(id: UUID) -> Ingredient:
    for ingredient in ingredients:
        if id == ingredient.id:
            return ingredient
    raise Exception("Could not find ingredient with given ID")
