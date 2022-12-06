def coroutine(func):
    st = func()
    next(st)

    def return_func():
        return st

    return return_func


@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


st = storage()
print(st.send(42))
print(st.send(42))
