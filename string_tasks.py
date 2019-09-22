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
def find_len_substring(string: str, unique_count: int) -> int:
    current_unique_chars = set()
    substring_len = 0
    max_substring_len = 0
    for char in string:
        if len(current_unique_chars) >= unique_count and char not in current_unique_chars:
            max_substring_len = max(max_substring_len, substring_len)
        elif len(current_unique_chars) == unique_count and char in current_unique_chars:
            substring_len += 1
        elif len(current_unique_chars) < unique_count and char not in current_unique_chars:
            substring_len += 1
            current_unique_chars





if __name__ == '__main__':
    print(find_len_max_substring("abcdbcdee"))
