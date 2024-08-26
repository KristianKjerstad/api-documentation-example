
from uuid import uuid4
from resources.ingredient.entities.ingredient import Ingredient, IngredientCategories
from resources.recipe.entities.recipe import Recipe, RecipeCategories, RecipeIngredient, RecipeTypes


chicken = Ingredient(id=uuid4(), name="Chicken", category=IngredientCategories.MEAT)
onion = Ingredient(id=uuid4(), name="Onion", category=IngredientCategories.VEGETABLES_AND_FRUIT)
garlic = Ingredient(id=uuid4(), name="Garlic", category=IngredientCategories.VEGETABLES_AND_FRUIT)
ginger = Ingredient(id=uuid4(), name="Ginger", category=IngredientCategories.VEGETABLES_AND_FRUIT)
tomato = Ingredient(id=uuid4(), name="Tomato", category=IngredientCategories.VEGETABLES_AND_FRUIT)
curry_powder = Ingredient(id=uuid4(), name="Curry Powder", category=IngredientCategories.CONDIMENTS)
coconut_milk = Ingredient(id=uuid4(), name="Coconut Milk", category=IngredientCategories.PANTRY_ESSENTIALS)
salt = Ingredient(id=uuid4(), name="Salt", category=IngredientCategories.CONDIMENTS)
pepper = Ingredient(id=uuid4(), name="Pepper", category=IngredientCategories.CONDIMENTS)
oil = Ingredient(id=uuid4(), name="Oil", category=IngredientCategories.PANTRY_ESSENTIALS)
flour = Ingredient(id=uuid4(), name="Flour", category=IngredientCategories.PANTRY_ESSENTIALS)
milk = Ingredient(id=uuid4(), name="Milk", category=IngredientCategories.PANTRY_ESSENTIALS)
eggs = Ingredient(id=uuid4(), name="Eggs", category=IngredientCategories.PANTRY_ESSENTIALS)
butter = Ingredient(id=uuid4(), name="Butter", category=IngredientCategories.PANTRY_ESSENTIALS)
sugar = Ingredient(id=uuid4(), name="Sugar", category=IngredientCategories.PANTRY_ESSENTIALS)
chili_powder = Ingredient(id=uuid4(), name="Chili Powder", category=IngredientCategories.CONDIMENTS)
cumin = Ingredient(id=uuid4(), name="Cumin", category=IngredientCategories.CONDIMENTS)
tomato_paste = Ingredient(id=uuid4(), name="Tomato Paste", category=IngredientCategories.PANTRY_ESSENTIALS)
heavy_cream = Ingredient(id=uuid4(), name="Heavy Cream", category=IngredientCategories.PANTRY_ESSENTIALS)
cilantro = Ingredient(id=uuid4(), name="Cilantro", category=IngredientCategories.VEGETABLES_AND_FRUIT)
kidney_beans = Ingredient(id=uuid4(), name="Kidney Beans", category=IngredientCategories.PANTRY_ESSENTIALS)
paprika = Ingredient(id=uuid4(), name="Paprika", category=IngredientCategories.CONDIMENTS)
salmon = Ingredient(id=uuid4(), name="Salmon", category=IngredientCategories.MEAT)
pasta = Ingredient(id=uuid4(), name="Pasta", category=IngredientCategories.PANTRY_ESSENTIALS)
cream = Ingredient(id=uuid4(), name="Double cream", category=IngredientCategories.PANTRY_ESSENTIALS)
dill = Ingredient(id=uuid4(), name="Dill", category=IngredientCategories.CONDIMENTS)
lemon = Ingredient(id=uuid4(), name="Lemon", category=IngredientCategories.VEGETABLES_AND_FRUIT)
ground_beef = Ingredient(id=uuid4(), name="Ground Beef", category=IngredientCategories.MEAT)
lasagna_noodles = Ingredient(id=uuid4(), name="Lasagna Noodles", category=IngredientCategories.PANTRY_ESSENTIALS)
ricotta_cheese = Ingredient(id=uuid4(), name="Ricotta Cheese", category=IngredientCategories.PANTRY_ESSENTIALS)
mozzarella_cheese = Ingredient(
    id=uuid4(), name="Mozzarella Cheese", category=IngredientCategories.PANTRY_ESSENTIALS
)
parmesan_cheese = Ingredient(id=uuid4(), name="Parmesan Cheese", category=IngredientCategories.PANTRY_ESSENTIALS)
marinara_sauce = Ingredient(id=uuid4(), name="Marinara Sauce", category=IngredientCategories.PANTRY_ESSENTIALS)
basil = Ingredient(id=uuid4(), name="Basil", category=IngredientCategories.CONDIMENTS)
oregano = Ingredient(id=uuid4(), name="Oregano", category=IngredientCategories.CONDIMENTS)

ingredients = [
        chicken,
        onion,
        garlic,
        ginger,
        tomato,
        curry_powder,
        coconut_milk,
        salt,
        pepper,
        oil,
        salmon,
        pasta,
        cream,
        dill,
        lemon,
        ground_beef,
        lasagna_noodles,
        ricotta_cheese,
        mozzarella_cheese,
        parmesan_cheese,
        marinara_sauce,
        basil,
        oregano,
        flour,
        cilantro,
        kidney_beans,
        paprika,
        milk,
        eggs,
        butter,
        sugar,
        chili_powder,
        cumin,
        tomato_paste,
        heavy_cream,
    ]

chicken_curry = Recipe(
        id=uuid4(),
        name="Chicken Curry",
        type=RecipeTypes.MAIN_COURSE,
        category=RecipeCategories.FOOD,
        image_link="https://www.themealdb.com/images/media/meals/yxsurp1511304301.jpg",
        recipe_steps=[
            "Heat oil in a pot and sauté 1 onion, 2 cloves of garlic, and a 1 inch piece of ginger until golden.",
            "Add 500g chicken and cook until browned.",
            "Stir in curry powder, 1 can of tomatoes and a pinch of salt and pepper.",
            "Pour in 400ml coconut milk and simmer until chicken is cooked through.",
            "Serve with rice.",
        ],
        ingredients=[
            RecipeIngredient(ingredient_uuid=chicken.id),
            RecipeIngredient(ingredient_uuid=onion.id),
            RecipeIngredient(ingredient_uuid=garlic.id),
            RecipeIngredient(ingredient_uuid=ginger.id),
            RecipeIngredient(ingredient_uuid=tomato.id),
            RecipeIngredient(ingredient_uuid=curry_powder.id),
            RecipeIngredient(ingredient_uuid=coconut_milk.id),
            RecipeIngredient(ingredient_uuid=salt.id),
            RecipeIngredient(ingredient_uuid=pepper.id),
            RecipeIngredient(ingredient_uuid=oil.id),
        ],
    )

pasta_with_salmon = Recipe(
    id=uuid4(),
    name="Pasta with Salmon",
    type=RecipeTypes.MAIN_COURSE,
    category=RecipeCategories.FOOD,
    image_link="https://www.themealdb.com/images/media/meals/wvqpwt1468339226.jpg",
    recipe_steps=[
        "Cook 400g pasta according to package instructions.",
        "In a pan, cook 2 filets of salmon until flaky.",
        "Add 300ml cream, a pinch of dill, and lemon juice from one lemon to the salmon and stir until combined.",
        "Mix the cooked pasta with the salmon sauce and serve.",
    ],
    ingredients=[
        RecipeIngredient(ingredient_uuid=salmon.id),
        RecipeIngredient(ingredient_uuid=pasta.id),
        RecipeIngredient(ingredient_uuid=cream.id),
        RecipeIngredient(ingredient_uuid=dill.id),
        RecipeIngredient(ingredient_uuid=lemon.id),
    ],
)

lasagna = Recipe(
    id=uuid4(),
    name="Lasagna",
    type=RecipeTypes.MAIN_COURSE,
    category=RecipeCategories.FOOD,
    image_link="https://www.themealdb.com/images/media/meals/rvxxuy1468312893.jpg",
    recipe_steps=[
        "Preheat oven to 375°F (190°C).",
        "In a pan, cook 400g ground beef until browned.",
        "Layer lasagna noodles, marinara sauce, ricotta cheese, mozzarella, and ground beef in a baking dish.",
        "Repeat layers and top with parmesan cheese.",
        "Bake for 45 minutes or until golden and bubbling.",
        "Garnish with basil and oregano.",
    ],
    ingredients=[
        RecipeIngredient(ingredient_uuid=ground_beef.id),
        RecipeIngredient(ingredient_uuid=lasagna_noodles.id),
        RecipeIngredient(ingredient_uuid=ricotta_cheese.id),
        RecipeIngredient(ingredient_uuid=mozzarella_cheese.id),
        RecipeIngredient(ingredient_uuid=parmesan_cheese.id),
        RecipeIngredient(ingredient_uuid=marinara_sauce.id),
        RecipeIngredient(ingredient_uuid=basil.id),
        RecipeIngredient(ingredient_uuid=oregano.id),
    ],
)

recipes = [
    chicken_curry,
    pasta_with_salmon,
    lasagna
]