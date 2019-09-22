from typing import List, Tuple


# [(1, 3), (2, 6), (8, 10), (15, 18)] -> [(1, 6), (8, 10), (15, 18)]
def merge(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    new_intervals = []

    left_num = None
    right_num = None

    for index in range(len(intervals) + 1):
        try:
            if right_num > intervals[index][0]:
                right_num = intervals[index][1]

            else:
                new_intervals.append((left_num, right_num))
                left_num = None
                right_num = None

        except:
            if left_num and right_num is not None:
                new_intervals.append((left_num, right_num))

        left_num = intervals[index][0] if left_num is None else left_num
        right_num = intervals[index][1] if right_num is None else right_num

    return new_intervals


if __name__ == '__main__':
    print(merge([(1, 3), (2, 6), (5, 10), (15, 18), (17, 25)]))
