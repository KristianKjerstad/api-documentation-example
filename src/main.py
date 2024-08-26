import uvicorn

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resources.ingredient import ingredient_resource
from resources.recipe import recipe_resource

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

public_routes = APIRouter()
public_routes.include_router(recipe_resource.router)
public_routes.include_router(ingredient_resource.router)
app.include_router(public_routes)



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
