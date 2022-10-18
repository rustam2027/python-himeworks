def flatten(arr: list, depth=-2):
    if depth == -1:
        return [arr]
    else:
        if isinstance(arr, list):
            return_arr = []
            for i in arr:
                return_arr = return_arr + flatten(i, depth - 1)
            return return_arr
        else:
            return [arr]


print(flatten([1, 2, [4, 5], [6, [7]], 8], depth=2))