def flatten(List, depth=-1):
    if depth == 0:
        return List
    else:
        if isinstance(List, list):
            return_List = []
            for i in List:
                a = flatten(i, depth - 1)
                if isinstance(a, list):
                    return_List = return_List + flatten(i, depth - 1)
                else:
                    return_List.append(a)
            return return_List
        else:
            return List


print(flatten([1, 2, [4, 5], [6, [7]], 8], depth=1))