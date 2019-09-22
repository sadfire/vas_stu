from typing import List, Tuple


# [(1, 3), (2, 6), (8, 10), (15, 18)] -> [(1, 6), (8, 10), (15, 18)]
def merger_ordered(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    new_intervals = []

    left_num = None
    right_num = None

    for interval in intervals:
        if right_num is not None and right_num > interval[0]:
            right_num = interval[1]
        elif left_num is not None:
            new_intervals.append((left_num, right_num))
            left_num = None
            right_num = None

        left_num = interval[0] if left_num is None else left_num
        right_num = interval[1] if right_num is None else right_num

    if left_num is not None and right_num is not None:
        new_intervals.append((left_num, right_num))

    return new_intervals


""" ToDo Homework """
def merge(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    new_intervals = []
    cash = {}
    for interval in intervals:
        begin, end = interval

    return new_intervals


if __name__ == '__main__':
    print(merger_ordered([(1, 2), (4, 4), (4, 10), (15, 18), (25, 25)]))
