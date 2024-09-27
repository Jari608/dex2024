# Red.


def test_calculate_cooking_time():
    # We expect that cooking 3 pancakes will take 12 minutes
    result = calculate_cooking_time(3)
    assert result == 12  # Each pancake takes 4 minutes (2 minutes per side)

    # We expect cooking 5 pancakes will take 20 minutes
    result = calculate_cooking_time(5)
    assert result == 20
