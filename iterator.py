class my_range_iter:
    def __init__(self, my_range):
        self._range = my_range
        self._cursor = 0

    def __next__(self):
        result = self._range._begin + self._cursor
        if result == self._range._end:
            raise StopIteration
        self._cursor += 1
        return result


class my_range:
    def __init__(self, begin, end):
        self._begin, self._end = begin, end
        self._cursor = begin

    def __iter__(self):
        return my_range_iter(self)


def main():
    range_ = my_range(1, 100)

    iterator = iter(range_)
    while True:
        try:
            i = next(iterator)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
