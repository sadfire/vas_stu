from typing import Generator, Optional
from random import randint


def find_majority(nums: Generator) -> Optional[str]:
    generator_len = 0
    frequency = {}

    max_value = (None, None)

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
        generator_len += 1

        if max_value[1] is None or max_value[1] < frequency[num]:
            max_value = num, frequency[num]

    return max_value[0] if max_value is not None and max_value[1] > (generator_len / 2) else None


def random_list():
    for index in range(randint(5, 30)):
        yield randint(0, 1)


if __name__ == '__main__':
    print(find_majority(random_list()))
