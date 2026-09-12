'''
    CAPITALIZE

    Your task is to write a function capitalize(text, skip), that
    capitalizes the first letter in all words in text, except
    for the words contained in the set of words skip. The first
    word should always be capitalized. If skip is omitted from the
    function call, all words should be capitalized.

    Input:  A Python expression using the capitalize function.
            The text argument will only consist of words containing
            lower case letters, separated by spaces.            

    Output: The result of evaluating the input expression.

    Example:

       Input:  capitalize('this is a test', skip={'a', 'is'})

       Output: This is a Test

    Note: The below code already handles input and output.
'''


# insert code

def capitalize(text, skip=set()):
    te=text.split()
    sol=[te[i][0].upper()+te[i][1:] if te[i] not in skip or i==0  else te[i] for i in range(len(te))]
    return " ".join(sol)


print(eval(input()))
#print()