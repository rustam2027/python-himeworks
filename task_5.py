def specialize(func, *args, **kwargs):
    def func1(*args1):
        return func(*args, *args1, **kwargs)
    return func1


def sum(a, b):
    return a + b


plus_one = specialize(sum, b=1)
print(plus_one(10))