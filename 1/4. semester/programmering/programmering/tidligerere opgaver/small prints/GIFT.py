'''
    GIFT

    Write code to print an n x n grid of characters, like in the example below,
    where all characters are 'o', except for position (i, j) which should 
    contain 'X', and the remaining of row i should contain '-' and the remaining 
    of column j should contain '|'. The upper left corner is position (0, 0).

    E.g., for n = 6, i = 2, and j = 3, you should print

      ooo|oo
      ooo|oo
      ---X--
      ooo|oo
      ooo|oo
      ooo|oo
    
    Input:  The input consists of three lines, each containing an integer.
            The first line contains n, 1 <= n <= 25, and the next two lines
            contain i and j, respectively, 0 <= i < n and 0 <= j < n.

    Output: Print an n x n grid of characters, i.e., n lines each containing n 
            characters. The grid should contain 'o' at all positions, except 
            column j in row i should contain 'X', and the remaining of row i
            should contain '-' and the remaining of column j should contain '|'.

    Example:

      Input:  6
              2
              3

      Output: ooo|oo
              ooo|oo
              ---X--
              ooo|oo
              ooo|oo
              ooo|oo    
'''


n=int(input())
i=int(input())
j=int(input())

board=[["|" if _==j else "o" for _ in range(n)] for _ in range(n)]
board[i]=["-" for _ in range(n)]
board[i][j]="X"




for l in board:
    print("".join(l))