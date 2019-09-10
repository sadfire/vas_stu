from random import randint
from main import add_binary


def test_add_binary():
    for index in range(1000):
        number1 = randint(1, 9999)
        number2 = randint(1, 9999)
        right_result = bin(number1 + number2)[2:]
        function_result = add_binary(bin(number1)[2:], bin(number2)[2:])
        if not right_result == function_result:
            print(f"answer =  {right_result} \n",
                  f"result = {function_result} \n", f"int numbers = {number1}, {number2} \n")


if __name__ == '__main__':
    test_add_binary()
