# Сдвинуть все 0 в конец списка, без дополнительной памяти и без удаления из середины списка
def move_zeros(numbers: list) -> list:
    zero_index = None
    other_num_index = None
    num_of_zeros_in_a_row = 0

    for index in range(len(numbers)):
        if numbers[index] != 0:
            other_num_index = index

        if zero_index is not None and other_num_index is not None and zero_index < other_num_index:
            numbers[zero_index], numbers[other_num_index] = numbers[other_num_index], numbers[zero_index]

            zero_index = index - num_of_zeros_in_a_row
            if num_of_zeros_in_a_row != 0:
                num_of_zeros_in_a_row -= 1
            other_num_index = None

        if numbers[index] == 0 and zero_index != index:
            if zero_index is None:
                zero_index = index
            else:
                num_of_zeros_in_a_row += 1

    return numbers

if __name__ == '__main__':
    numbers = [0, 1, 1, 1]
    print(move_zeros(numbers))
