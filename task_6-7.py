def flatten(arr, depth=-1):
    if depth == 0:
        return arr
    else:
        if isinstance(arr, list):
            return_arr = []
            for i in arr:
                a = flatten(i, depth - 1)
                if isinstance(a, list):
                    return_arr = return_arr + flatten(i, depth - 1)
                else:
                    return_arr.append(a)
            return return_arr
        else:
            return arr


print(flatten([1, 2, [4, 5], [6, [7]], 8], depth=1))