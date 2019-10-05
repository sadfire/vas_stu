import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        count = 1000
        while count != 0:
            res = func(*args, **kwargs)
            count -= 1
        print(time.time() - start)
        return res
    return wrapper

def find_len_max_substring(string: str) -> int:
    current_chars = []
    substrings_len = None
    for char in string:
        if char in current_chars:
            substrings_len = max(substrings_len, len(current_chars)) \
                if substrings_len is not None \
                else len(current_chars)

            current_chars = [char, ]
        else:
            current_chars.append(char)

    return substrings_len


""" ToDo Homerwork find max substring with unique count chars"""


def find_len_substring_fast(string: str, unique_count: int) -> int:
    current_unique_chars = []
    substring_len = 0
    max_substring_len = 0

    for char in string:
        if len(current_unique_chars) > unique_count and char not in current_unique_chars:
            max_substring_len = max(max_substring_len, substring_len)
            del current_unique_chars[0]
            substring_len -= 1
            current_unique_chars.append(char)

        elif len(current_unique_chars) > unique_count and char in current_unique_chars:
            pass

        elif len(current_unique_chars) <= unique_count and char in current_unique_chars:
            substring_len += 1

            max_substring_len = max(max_substring_len, substring_len)

        elif len(current_unique_chars) <= unique_count and char not in current_unique_chars:
            substring_len += 1
            current_unique_chars.append(char)

            max_substring_len = max(max_substring_len, substring_len)

    return max_substring_len

@timer
def find_len_substring_fastfast(string: str, unique_count: int) -> int:
    cash = set()
    order = []
    substring: str = ""
    result = 0

    if len(string) < unique_count:
        return len(string)

    for index, char in enumerate(string):
        if len(order) == 0 or char != order[-1]:
            order.append(char)

        cash.add(char)

        while len(cash) > unique_count:
            symbol = order.pop(0)
            if len(order) == 0:
                substring = ""
            else:
                substring = substring[substring.find(order[0]):]

            if symbol not in order:
                cash.remove(symbol)

        substring += char
        result = max(result, len(substring))

    return result


if __name__ == '__main__':
    inp = "000000000000000000000000000011111111111111111111111111111111111000000000000000000000000000000000000000111111111111111111112222222222222222222333333333333333333333444444444444444444444455134235235333333333333333333"
    count = 2
    find_len_substring_fastfast(inp, count)
