from typing import List, Union


def add_numbers(nums: Union[List, int]) -> int:
    my_sum = 0
    for n in nums:
        my_sum = my_sum + n

    return my_sum
