# Green.


def calculate_cooking_time(num_pancakes: int) -> int:
    """Calculates the cooking time of a given number of pancakes.

    Args:
        num_pancakes (int): Number of pancakes.

    Returns:
        int: Cooking time.
    """
    return num_pancakes * 4  # 4 minutes per pancake (2 minutes per side)


def test_calculate_cooking_time():
    # We expect that cooking 3 pancakes will take 12 minutes
    result = calculate_cooking_time(3)
    assert result == 12  # Each pancake takes 4 minutes (2 minutes per side)

    # We expect cooking 5 pancakes will take 20 minutes
    result = calculate_cooking_time(5)
    assert result == 20
