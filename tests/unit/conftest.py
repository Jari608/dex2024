import pytest

from typing import List, Dict


@pytest.fixture
def meal_plan() -> List[Dict]:
    return [
        {"weekday": "Monday", "recipy": "Pasta Carbonara", "persons": 4},
        {"weekday": "Tuesday", "recipy": "Sweet Patato Curry", "persons": 3},
        {"weekday": "Wednesday", "recipy": "Kale Stew", "persons": 4},
        {"weekday": "Thursday", "recipy": "Pasta Chicken Pesto", "persons": 2},
        {"weekday": "Friday", "recipy": "Burritos", "persons": 4},
        {"weekday": "Saturday", "recipy": "Pancakes", "persons": 2},
        {"weekday": "Sunday", "recipy": "Beef Stew", "persons": 2},
    ]


@pytest.fixture
def recipies() -> Dict[str, Dict]:

    pasta_carbonara: dict = {
        "Pancetta (g)": 50,
        "Pecorino Cheese (g)": 25,
        "Parmesan Cheese (g)": 25,
        "Eggs": 1,
        "Spaghetti (g)": 100,
        "Garlic Cloves": 0.5,
        "Unsalted Butter (g)": 25,
        "Salt (g)": 1,
        "Pepper (g)": 1,
    }

    sweet_patato_curry: dict = {
        "Sweet Potato (g)": 150,
        "Coconut Milk (ml)": 100,
        "Red Curry Paste (g)": 20,
        "Chickpeas (g)": 50,
        "Onion": 0.5,
        "Garlic Cloves": 1,
        "Ginger (g)": 5,
        "Spinach (g)": 50,
        "Vegetable Oil (ml)": 10,
        "Salt (g)": 1,
        "Pepper (g)": 1,
    }

    kale_stew: dict = {
        "Kale (g)": 150,
        "Potatoes (g)": 200,
        "Smoked Sausage (g)": 75,
        "Onion": 0.5,
        "Garlic Cloves": 1,
        "Butter (g)": 20,
        "Milk (ml)": 50,
        "Salt (g)": 1,
        "Pepper (g)": 1,
    }

    pasta_chicken_pesto: dict = {
        "Chicken Breast (g)": 100,
        "Pasta (g)": 100,
        "Pesto (g)": 30,
        "Parmesan Cheese (g)": 20,
        "Cherry Tomatoes": 4,
        "Olive Oil (ml)": 10,
        "Garlic Cloves": 1,
        "Salt (g)": 1,
        "Pepper (g)": 1,
    }

    burritos: dict = {
        "Tortilla Wraps": 1,
        "Ground Beef (g)": 100,
        "Black Beans (g)": 50,
        "Cheddar Cheese (g)": 30,
        "Sour Cream (g)": 20,
        "Lettuce (g)": 30,
        "Tomato": 0.5,
        "Onion": 0.5,
        "Garlic Cloves": 1,
        "Olive Oil (ml)": 10,
        "Salt (g)": 1,
        "Pepper (g)": 1,
    }

    pancakes: dict = {
        "Flour (g)": 100,
        "Milk (ml)": 150,
        "Eggs": 1,
        "Butter (g)": 25,
        "Sugar (g)": 10,
        "Salt (g)": 1,
    }

    beef_stew: dict = {
        "Beef (g)": 150,
        "Potatoes (g)": 100,
        "Carrots (g)": 50,
        "Onion": 0.5,
        "Garlic Cloves": 1,
        "Tomato Paste (g)": 20,
        "Beef Broth (ml)": 150,
        "Olive Oil (ml)": 10,
        "Thyme (g)": 1,
        "Bay Leaf": 1,
        "Salt (g)": 1,
        "Pepper (g)": 1,
    }

    return {
        "Pasta Carbonara": pasta_carbonara,
        "Sweet Potato Curry": sweet_patato_curry,
        "Kale Stew": kale_stew,
        "Pasta Chicken Pesto": pasta_chicken_pesto,
        "Burritos": burritos,
        "Pancakes": pancakes,
        "Beef Stew": beef_stew,
    }


@pytest.fixture
def grocery_list() -> Dict:
    return {
        "Pancetta (g)": 200,
        "Pecorino Cheese (g)": 100,
        "Parmesan Cheese (g)": 140,
        "Eggs": 6,
        "Spaghetti (g)": 400,
        "Garlic Cloves": 14.0,
        "Unsalted Butter (g)": 100,
        "Salt (g)": 18,
        "Pepper (g)": 16,
        "Kale (g)": 600,
        "Potatoes (g)": 1000,
        "Smoked Sausage (g)": 300,
        "Onion": 5.0,
        "Butter (g)": 130,
        "Milk (ml)": 500,
        "Chicken Breast (g)": 200,
        "Pasta (g)": 200,
        "Pesto (g)": 60,
        "Cherry Tomatoes": 8,
        "Olive Oil (ml)": 80,
        "Tortilla Wraps": 4,
        "Ground Beef (g)": 400,
        "Black Beans (g)": 200,
        "Cheddar Cheese (g)": 120,
        "Sour Cream (g)": 80,
        "Lettuce (g)": 120,
        "Tomato": 2.0,
        "Flour (g)": 200,
        "Sugar (g)": 20,
        "Beef (g)": 300,
        "Carrots (g)": 100,
        "Tomato Paste (g)": 40,
        "Beef Broth (ml)": 300,
        "Thyme (g)": 2,
        "Bay Leaf": 2,
    }


@pytest.fixture
def grocery_list_bonus() -> Dict:
    return {
        "Pancetta (g)": 100,
        "Pecorino Cheese (g)": 100,
        "Parmesan Cheese (g)": 20,
        "Eggs": 2,
        "Spaghetti (g)": 200,
        "Garlic Cloves": 2,
        "Unsalted Butter (g)": 100,
        "Salt (g)": 2,
        "Pepper (g)": 2,
        "Kale (g)": 600,
        "Potatoes (g)": 200,
        "Smoked Sausage (g)": 300,
        "Onion": 1.0,
        "Butter (g)": 50,
        "Milk (ml)": 300,
        "Chicken Breast (g)": 200,
        "Pasta (g)": 200,
        "Pesto (g)": 60,
        "Cherry Tomatoes": 8,
        "Olive Oil (ml)": 20,
        "Tortilla Wraps": 4,
        "Ground Beef (g)": 400,
        "Black Beans (g)": 200,
        "Cheddar Cheese (g)": 120,
        "Sour Cream (g)": 80,
        "Lettuce (g)": 120,
        "Tomato": 2.0,
        "Flour (g)": 200,
        "Sugar (g)": 20,
        "Beef (g)": 300,
        "Carrots (g)": 100,
        "Tomato Paste (g)": 40,
        "Beef Broth (ml)": 300,
        "Thyme (g)": 2,
        "Bay Leaf": 2,
    }


@pytest.fixture
def pantry() -> Dict:
    return {
        "Pancetta (g)": 100,
        "Parmesan Cheese (g)": 20,
        "Eggs": 2,
        "Spaghetti (g)": 200,
    }
