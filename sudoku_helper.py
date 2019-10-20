
def get_box_map() -> Dict[Tuple[int, int], int]:
    result = {}

    boxes_row = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}]
    boxes_column = {(0, 1, 2): {0, 3, 6}, (3, 4, 5): {1, 4, 7}, (6, 7, 8): {2, 5, 8})

    for row_index in range(9):
        for column_index in range(9):
            result[(row_index, column_index)] = boxes_column[column_index]).intersect(boxes_row[row_index // 3])

    return result

def get_box_indexes() -> Dict[int, List[Tuple[int, int]]]:
    pass

def get_row_indexes() -> Dict[int, List[Tuple[int, int]]]:
    pass

def get_column_indexes() -> Dict[int, List[Tuple[int, int]]]:
    pass

class State(Enum):
    Used = 0
    Unused = 1
    Expire = 2

class Cell:
    def __init__(self, prev: "Cell"):
        self.candidates = {i: State.Unused for i in range(9)}
        self.prev = prev

    @property
    def current(self):
        for candidate, state in self.candidates.items():
            if state == State.Used:
                return candidate
        return None

    def expire(self, candidate):
        self.candidates[candidate] = Expire

    def delete(self, candidate):
        self.candidates.pop(candidate)

    def refresh(self, candidates):
        for candidates, state in self.candidats.items():
            if state in (State.Expire, State.Used):
                candidates[candidate] = State.Unused

def exclude(sudoku, row, column, cell):
    box = box_indexes[(row, column)]

    for i, j in set(box_indexes[box] + columns[column] + row_indexes[row]):
        sudoku[i][j].expire(cell.current)

def main():
    sudoku = [[Cell() for i in range(0, 9)] for range(0, 9)]

    box_indexes = get_box_indexes()
    columns_indexes = get_column_indexes()
    row_indexes = get_row_indexes()
