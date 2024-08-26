from typing import List

from resources.recipe.entities.recipe import Recipe
from data.data import recipes

def get_all_recipes_use_case() -> List[Recipe]:
    return recipes
