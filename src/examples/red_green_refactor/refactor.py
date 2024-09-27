# Green.


def calculate_cooking_time(num_pancakes: int, time_per_side: int = 2) -> int:
    """Calculates the cooking time of a given number of pancakes.

    Args:
        num_pancakes (int): Number of pancakes.
        time_per_side (int, optional): Defaults to 2.

    Returns:
        int: Cooking time.
    """
    total_time_per_pancake = time_per_side * 2  # Flip once, so 2 sides
    return num_pancakes * total_time_per_pancake


def test_calculate_cooking_time():
    # We expect that cooking 3 pancakes will take 12 minutes
    result = calculate_cooking_time(3)
    assert result == 12  # Each pancake takes 4 minutes (2 minutes per side)

    # We expect cooking 5 pancakes will take 20 minutes
    result = calculate_cooking_time(5)
    assert result == 20

    # Test with a custom time per side, e.g., 3 minutes per side
    result = calculate_cooking_time(3, time_per_side=3)
    assert result == 18  # 6 minutes per pancake (3 minutes per side)
