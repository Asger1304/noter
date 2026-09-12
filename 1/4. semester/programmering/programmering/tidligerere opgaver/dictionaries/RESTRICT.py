'''
    RESTRICT

    Create a function restrict(dictionary, keys) that takes a dictionary
    and a list of keys as arguments, and returns a new dictionary with
    all (key, value) items from the input dictionary where the key is
    also in keys.

    Input:  A single line with a Python expression using the function
            restrict.  The argument dictionary contains at most 100
            items and keys at most 100 keys.

    Output: The result of evaluating the input expression.  The items
            in the returned dictionary should be inserted in the same
            order as in the input dictionary.

    Example:

      Input:  restrict({'a': 1, 'b': 2, 'c': 3}, ['b', 'a', 'd'])

      Output: {'a': 1, 'b': 2}

    Note: The below code already reads and evaluates the input.
'''


def restrict(dictionary, keys):
    return {d:dictionary[d] for d in dictionary if d in keys}



print(eval(input()))
