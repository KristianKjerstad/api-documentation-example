
from uuid import UUID


from resources.recipe.entities.recipe import Recipe
from data.data import recipes

def get_one_recipe_use_case(id: UUID) -> Recipe:
    for recipe in recipes:
        if recipe.id == id:
            return recipe
    return None
