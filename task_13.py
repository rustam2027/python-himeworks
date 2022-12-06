class chain_iter:

    def __init__(self, *args):
        self.iterables = args
        self.args_idex = 0
        self.observe = args[0].__iter__()

    def __next__(self):
        try:
            cur = next(self.observe)
        except StopIteration:
            try:
                self.args_idex += 1
                self.observe = self.iterables[self.args_idex].__iter__()
            except IndexError:
                raise StopIteration
            cur = next(self.observe)
        return cur

    def __iter__(self):
        return self


def chain(*args):
    return chain_iter(*args)


print(list(chain([1, 2, 3], ['a', 'b'])))
