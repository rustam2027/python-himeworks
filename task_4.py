
def reverse_dict(dict):
    """Reverse dictionary

    >>> reverse_dict({1: "one", 2: "two", 3: "three"})
    {'one': 1, 'two': 2, 'three': 3}

    >>> reverse_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832})
    {97832: ('Ivanov', 'Kuznecov'), 55521: 'Petrov'}
    """

    return_dict = {}
    items = dict.items()
    is_more_than_two_values = {}
    for key, element in items:
        if element in return_dict:
            if is_more_than_two_values[element]:
                return_dict[element] = (*return_dict[element], key)
            else:
                return_dict[element] = (return_dict[element], key)
            is_more_than_two_values[element] = True
        else:
            is_more_than_two_values[element] = False
            return_dict[element] = key
    return return_dict


if __name__ == "__main__":
    import doctest

doctest.testmod()

print(reverse_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}))
print(reverse_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832, "Sidorov": 97832}))
print(reverse_dict({(1, 2): 97832, "Petrov": 55521, (2, 3): 97832, (4, 5): 97832}))
