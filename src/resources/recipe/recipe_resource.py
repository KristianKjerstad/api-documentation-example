from typing import List
from uuid import UUID
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, Response
from resources.recipe.entities.recipe import Recipe, RecipeCategories
from resources.recipe.use_cases.get_all_recipes_use_case import get_all_recipes_use_case
from resources.recipe.use_cases.get_one_recipe_use_case import get_one_recipe_use_case
router = APIRouter(tags=["recipes"], prefix="/recipes")

class NotFoundResponse(BaseModel):
    message: str

@router.get(
    "",
)
async def get_all(category: RecipeCategories = None) -> List[Recipe]:
    """Get all recipes"""

    all_recipes = get_all_recipes_use_case()
    if category is not None:
        filtered_recipes = [recipe for recipe in all_recipes if recipe.category == category]
        return filtered_recipes
    else:
        return all_recipes


@router.get("/{id}", status_code=200, responses={
    404: {
        "description": "Recipe not found",
        "model": NotFoundResponse,
       
    }
})
async def get_one(id: UUID) -> Recipe:
    recipe =  get_one_recipe_use_case(id=id)
    if recipe is None:
        raise HTTPException(status_code=404, detail={"message": "Recipe not found"})
    return recipe