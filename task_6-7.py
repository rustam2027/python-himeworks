def flatten(arr: list, depth=-2):
    if not isinstance(arr, list):
        return arr
    
    if depth == -1:
        return arr
    else:
        return_arr = []
        for i in arr:
            if isinstance(i, list):
                return_arr = return_arr + flatten(i, depth - 1)
            else:
                return_arr.append(i)
        return return_arr


print(flatten([1, 2, [4, 5], [6, [7]], 8], depth=2))
print(flatten(13))