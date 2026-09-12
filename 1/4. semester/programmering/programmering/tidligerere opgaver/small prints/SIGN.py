'''
    SIGN

    Your task is to print the sign of each integer in a list.

    Input:  A Python list of integers L.

    Output: For each integer in L print x, followed by "is" and the sign,
            where sign is either "zero", "negative" or "positive".

    Example:

       Input:  [2, 1, -3, 0, -4, 42]

       Output: 2 is positive
               1 is positive
               -3 is negative
               0 is zero
               -4 is negative
               42 is positive

    Note: The below code already reads the list L from input.
'''


L = eval(input())

for l in L:
        if l>0:
                print(f"{l} is positive")
        elif  l<0:
                print(f"{l} is negative")
        else:
                print(f"{l} is zero")

