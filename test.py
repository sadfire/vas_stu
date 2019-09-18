from random import randint, shuffle
from add_binary import add_binary
from copy import copy
from move_zeros import move_zeros


def test_add_binary():
    for index in range(1000):
        number1 = randint(1, 9999)
        number2 = randint(1, 9999)
        right_result = bin(number1 + number2)[2:]
        function_result = add_binary(bin(number1)[2:], bin(number2)[2:])
        if not right_result == function_result:
            print(f"answer =  {right_result} \n",
                  f"result = {function_result} \n", f"int numbers = {number1}, {number2} \n")


def test_move_zeros():
    for _ in range(1000):
        zeros = randint(1, 20)
        other_numbers = randint(1, 20)
        right_list = [1 for _ in range(other_numbers)] + [0 for _ in range(zeros)]
        shuffled_list = copy(right_list)
        shuffle(shuffled_list)
        result_list = move_zeros(copy(shuffled_list))
        if not right_list == result_list:
            print(f"right_list = {right_list} \n result_list = {result_list} \n shuffled_list = {shuffled_list} \n")


if __name__ == '__main__':
    test_move_zeros()
