class Cell:
    def __init__(self, candidates: list = None, up=None, right=None,down=None, left=None):
        self.candidates: list = candidates
        self.unused_candidates: list = []
        self.excluded_cadidates: list = []
        self.up: Cell = up
        self.right: Cell = right
        self.down: Cell = down
        self.left: Cell = left
        self.list_neighbours: list = [self.up, self.right, self.down, self.left]

    def delete_candidate(self, candidate: int):
        if candidate in self.candidates:
            self.candidates.remove(candidate)

    def next(self):
        next_cell = self.right
        if next_cell is None:

    def update_list_neighbours(self):
        self.list_neighbours: list = [self.up, self.right, self.down, self.left]

    def append_filter(self, candidates: list):
        for candidate in candidates:
            if candidate not in self.excluded_cadidates:
                self.candidates.append(candidate)

    def _exclude_candidates(self, direction: int, candidate: int):
        next_cell = self.list_neighbours[direction]
        if next_cell is not None:
            next_cell.delete_candidate(candidate)
            next_cell._exclude_candidates(direction, candidate)

    def exclude_row_column_candidates(self, candidate: int):
        for direction in range(4):
            self._exclude_candidates(direction, candidate)


def exclude_box_candidates(i_index: int, j_index: int, sudoku_cells: list, candidate: int, current_cell: Cell):
    row_index = (i_index // 3) * 3
    column_index = (j_index // 3) * 3

    for n in range(3):
        for element in sudoku_cells[row_index + n][column_index:column_index+3]:
            if candidate in element.candidates:
                if current_cell != element:
                    element.delete_candidate(candidate)


def exclude_all_candidates(candidate: int, sudoku_cells: list, i_index: int, j_index: int, current_cell: Cell):
    sudoku_cells[i_index][j_index].exclude_row_column_candidates(candidate)
    exclude_box_candidates(i_index, j_index, sudoku_cells, candidate, current_cell)


def solve_sudoku(sudoku: list) -> list:
    sudoku_cells = []

    for i in range(9):
        sudoku_cells.append([])

        for j in range(9):
            current_cell = Cell(candidates=list(range(1, 10)))

            if j > 0:
                current_cell.left = sudoku_cells[i][j - 1]
                sudoku_cells[i][j - 1].right = current_cell

            if i > 0:
                current_cell.up = sudoku_cells[i - 1][j]
                sudoku_cells[i - 1][j].down = current_cell

            sudoku_cells[i].append(current_cell)

    for row_cells in sudoku_cells:
        for cell in row_cells:
            cell.update_list_neighbours()

    for i in range(9):
        for j, element in enumerate(sudoku[i]):
            if element != 0:
                current_cell = sudoku_cells[i][j]
                current_cell.candidates = [element]
                exclude_all_candidates(element, sudoku_cells, i, j, current_cell)

    corect_sudoku = False
    current_cell = sudoku_cells[0][0]
    while not corect_sudoku:
    #    if len(current_candidates) > 1:
    #        candidate = current_candidates[0]
    #        cell.unused_candidates = current_candidates
    #        cell.unused_candidates.remove(candidate)
    #    elif len(current_candidates) == 0:
            pass
    current_cell = current_cell.next


    return sudoku_cells


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
    for i in range(9):
        for j in range(9):
            print(solved_sudoku[i][j].candidates)
