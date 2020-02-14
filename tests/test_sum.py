from modules.sum import add_numbers

my_numbers = [12, 20, 13, 5, 4, 15]


def test_add_numbers_input():
    add_numbers(my_numbers)


def test_add_numbers_calculate():
    sum = add_numbers(my_numbers)

    actual_sum = 12 + 20 + 13 + 5 + 4 + 15

    assert sum == actual_sum, f"Expecting {actual_sum}, got {sum} instead"
