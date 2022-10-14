def reverse_dict(dict):
    """Reverse dictionary
    
    >>> reverse_dict({1: "one", 2: "two", 3: "three"})
    {'one': 1, 'two': 2, 'three': 3}
    
    >>> reverse_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832})
    {97832: ('Ivanov', 'Kuznecov'), 55521: 'Petrov'}
    """

    return_dict = {}
    items = dict.items()
    for elements in items:
        if elements[1] in return_dict:
            return_dict[elements[1]] = (return_dict[elements[1]], elements[0])
        else:
            return_dict[elements[1]] = elements[0]
    return return_dict


if __name__ == "__main__":
    import doctest

doctest.testmod()

print(reverse_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}))