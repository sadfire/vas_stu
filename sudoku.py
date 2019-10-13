def solve_sudoku(sudoku: list) -> list:
    for i in range(9):
        for j in range(9):
            current_num = sudoku[i][j]
            possible_nums = set(range(1, 10)).symmetric_difference(set(get_row_nums(sudoku[i]) +
                                                                       get_column_nums(sudoku, j) + get_square_nums(sudoku, i, j)))
            if len(possible_nums) == 1:
                sudoku[i][j] = possible_nums.pop()
            else:
                sudoku[i][j] = possible_nums if current_num == 0 else current_num

    return sudoku


def get_column_nums(matrix: list, column_num: int) -> list:
    result = []

    for i_index in range(len(matrix)):
        for j_index in range(len(matrix)):

            if j_index == column_num:
                current_element = matrix[i_index][j_index]

                if str(current_element).isnumeric() and current_element:
                    result.append(current_element)
                break

    return result


def get_row_nums(row: list):
    result = []

    for element in row:
        if str(element).isnumeric() and element:
            result.append(element)

    return result


def get_square_nums(sudoku: list, i_index: int, j_index: int) -> list:
    result = []
    row_index = (i_index // 3) * 3
    column_index = (j_index // 3) * 3

    for n in range(3):
        for element in sudoku[row_index + n][column_index:column_index+3]:
            if str(element).isnumeric() and element:
                result.append(element)

    return result


if __name__ == '__main__':
    sudoku = [[0, 0, 0, 6, 0, 9, 0, 0, 0],
              [5, 0, 0, 0, 7, 0, 0, 0, 3],
              [0, 0, 0, 3, 0, 0, 2, 8, 9],
              [0, 9, 5, 0, 4, 0, 0, 3, 0],
              [3, 0, 7, 0, 2, 0, 0, 0, 0],
              [2, 0, 1, 0, 0, 0, 7, 0, 0],
              [0, 0, 6, 4, 0, 0, 0, 0, 0],
              [9, 5, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 5, 0, 0, 8]]

    solved_sudoku = solve_sudoku(sudoku)
    for element in solved_sudoku:
        print(f"{element} \n")
