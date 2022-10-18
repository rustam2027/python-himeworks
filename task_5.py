def specialize(func, *args, **kwargs):
    def wrapper(*inner_args, **inner_kwargs):
        return func(*args, *inner_args, **kwargs, **inner_kwargs)
    return wrapper


def sum(a, b):
    return a + b


plus_one = specialize(sum, b=1)
print(plus_one(10))

just_two = specialize(sum, 1, 1)
print(just_two())

with_inner_kwargs = (specialize(sum, 2))
print(with_inner_kwargs(b=10))