from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from resources.ingredient.entities.ingredient import Ingredient

from resources.ingredient.use_cases.get_all_ingredient_use_case import (
    get_all_ingredients_use_case,
)
from resources.ingredient.use_cases.get_one_ingredient_use_case import (
    get_one_ingredient_use_case,
)

router = APIRouter(tags=["ingredients"], prefix="/ingredients")


@router.get("")
async def get_all() -> List[Ingredient]:
    return get_all_ingredients_use_case()


@router.get("/{id}")
async def get_one(id: UUID) -> Ingredient:
    return get_one_ingredient_use_case(id=id)


@router.delete("/{id}")
async def delete_one(id: UUID):
    raise NotImplementedError
