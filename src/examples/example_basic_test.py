# Method
def create_grocery_list_for_pancakes(servings: int) -> list:
    amount_per_serving = {
        "g flour": 50,
        "tsp(s) salt": 0.25,
        "eggs": 0.5,
        "ml milk": 80,
        "g butter": 5,
    }

    grocery_list = []

    for ingredient, amount in amount_per_serving.items():
        total_amount = amount * servings
        grocery_list.append(f"{total_amount} {ingredient}")

    return grocery_list


# Test
def test_create_grocery_list_for_pancakes() -> None:
    """Tests the grocery list creation."""
    groceries = create_grocery_list_for_pancakes(servings=4)
    assert groceries == [
        "200 g flour",
        "1.0 tsp(s) salt",
        "2.0 eggs",
        "320 ml milk",
        "20 g butter",
    ]
