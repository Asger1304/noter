'''
    CAPITALS

    Remove all lower case letters from a string.

    Input:  A single line with a string containtin lower and capital letters,
            and length between 1 and 100.

    Output: The input string with all lower case letters removed.

    Example:

      Input:  ComeLateAndStartSleeping

      Output: CLASS
'''


i=input()
s=list(i)
out=[f for f in s if f==f.upper()]
print("".join(out))
