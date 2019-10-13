def matrix_multiply(left: tuple, right: tuple) -> list:
    if len(left[0]) != len(right):
        raise ValueError
    else:
        result_matrix = [[0 for _ in range(len(left))] for _ in range(len(right[0]))]
        for i in range(len(left)):
            for j in range(len(right[0])):
                for n in range(len(right)):
                    result_matrix[i][j] += left[i][n] * right[n][j]

        return result_matrix


if __name__ == '__main__':
    matrix1 = ((1, 2, 3),
               (4, 5, 6))
    matrix2 = ((1, 2),
               (3, 4),
               (5, 6))
    print(matrix_multiply(matrix1, matrix2))
