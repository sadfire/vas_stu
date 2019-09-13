def move_zeros(numbers: list) -> list:
    number_of_zeros = 0
    for index in range(len(numbers)):
        if numbers[index - number_of_zeros] == 0:
            numbers.pop(index - number_of_zeros)
            numbers.append(0)
            number_of_zeros += 1
    return numbers


if __name__ == '__main__':
    numbers = [6, 0, 0, 0, 0, 0, 0, 3, 4, 0, 9, 0]
    print(move_zeros(numbers))
