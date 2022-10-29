import functools


def deprecated(func=None, since="", will_be_removed=""):

    if func is None:
        return functools.partial(deprecated, since=since, will_be_removed=will_be_removed)

    def return_func(*args, **kwargs):
        since_text = "."
        will_be_removed_text = " in future versions."

        if since:
            since_text = f" since version {since}."

        if will_be_removed:
            will_be_removed_text = f" in version {will_be_removed}"

        func_name = getattr(func, "__name__")

        print(f"Warning: function {func_name} is deprecated{since_text} It will be removed{will_be_removed_text}")
        func(*args, *kwargs)
    return return_func


@deprecated(since="4.2.0", will_be_removed="5.0.1")
def bar():
    print("Hello from bar!")


@deprecated(will_be_removed="6.0.2")
def foo():
    print("Hello from foo!")


@deprecated(since="3.4.5")
def baz():
    print("Hello from baz!")


@deprecated
def dug():
    print("Hello from dug!")


bar()
foo()
baz()
dug()
