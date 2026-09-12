'''
    DIAGONAL WORD

    Your task is to read a word from input and to print the word 
    diagonally in a square otherwise filled with '.'.

    Input:  A single line containing a string with 1 <= length <= 25 symbols,
            and all symbols being characters 'a'-'z' and 'A'-'Z'

    Output: Print length lines, each containing length symbols, all
            symbols being '.', except the diagonal top-left to bottom-right
            that should contain the input string.

    Example:

       Input:  Python

       Output: P.....
               .y....
               ..t...
               ...h..
               ....o.
               .....n
'''


word=list(input())
for i in range(len(word)):
    print(i*"."+word[i]+(len(word)-i-1)*".")

