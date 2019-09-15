from typing import Generator
from random import randint


def find_majority(nums: Generator) -> int:
    generator_len = 0
    nums_dict = {}
    for num in nums:
        print(f"num = {num}")
        is_exsist = False
        for key in nums_dict.keys():
            if key == num:
                nums_dict[key] += 1
                is_exsist = True
        if not is_exsist:
            nums_dict[num] = 1
        generator_len += 1

    max_value = 0
    key_of_max_value = 0
    for key1, value1 in nums_dict.items():
        if value1 > max_value:
            max_value = value1
            key_of_max_value = key1

    return key_of_max_value if max_value > (generator_len / 2) else 'majority not found'


def random_list():
    for index in range(randint(5, 30)):
        yield randint(0, 1)


if __name__ == '__main__':
    print(find_majority(random_list()))
