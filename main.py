def add_binary(left: str, right: str) -> str:
    result = list(left if len(left) > len(right) else right)

    mem = False
    for index in ...:

        right_val = False
        if index < len(right):
            right_val = right[index] == '1'

        left_val = False
        if index < len(left):
            left_val = left[index] == '1'

        if right_val and left_val:
            result[index] = '1' if mem else '0'
            mem = True
        elif not right_val and not left_val:
            result[index] = '1' if mem else '0'
            mem = False
        else:
            result[index] = "0" if mem else "1"

    if mem:
        result.insert(0, '1')

    return ''.join(result)

if __name__ == '__main__':
    a, b = 0b1111, 0x1111
    res = add_binary(bin(a)[2:], bin(b)[2:])
    print(res, '\n', bin(a + b)[2:])
