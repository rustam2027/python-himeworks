class cycle_iter:

    def __init__(self, list):
        self.iterable = list
        self.temp_iterable = list.__iter__()
        self.observe = 0

    def __next__(self):
        try:
            cur = next(self.temp_iterable)
        except StopIteration:
            self.temp_iterable = self.iterable.__iter__()
            cur = next(self.temp_iterable)
        finally:
            return cur

    def __iter__(self):
        return self


def take(seq, n):
    res = []
    for i in range(n):
        try:
            res.append(next(seq))
        except StopIteration:
            break

    return res


def cycle(list):
    return cycle_iter(list)


for i in cycle([1, 2, 3]):
    print(i)
