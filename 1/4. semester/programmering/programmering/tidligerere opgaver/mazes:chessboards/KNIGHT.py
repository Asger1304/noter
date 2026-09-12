'''
    KNIGHT

    Given an n x n chessboard with a single knight at position (i, j), 
    determine the possible positions of the knight after d moves.

    A knight's movement is: it moves two squares vertically and one square
    horizontally, or two squares horizontally and one square vertically 
    If 'K' marks the position of the knight before the move, then 'X' are the
    possible positions after one move.
    
        ........
        ..X.X...
        .X...X..
        ...K....
        .X...X..
        ..X.X...
        ........
        ........

    and after two moves:

        X.X.X.X.
        ...X...X
        X.X.X.X.
        .X.X.X.X
        X.X.X.X.
        ...X...X
        X.X.X.X.
        .X.X.X..

    Input:  A single line with four integers n, i, j and d, separated by spaces,
            where n is the size of the board, (i, j) is the position of the
            knight, and d is the number of moves. We assume i is the row number,
            j is the column number, and the top-left cell is (0, 0).
            It is guaranteed that 5 <= n <= 100, 0 <= i < n, 0 <= j < n, 
            and 0 <= d <= 100.

    Output: The n x n board after d moves, where the possible knight positions 
            are marked by 'X', and all other cells are marked by '.'.
            Only mark positions where the knight can be after _exactly_ d moves.

    Example:

      Input:  8 3 3 2

      Output: X.X.X.X.
              ...X...X
              X.X.X.X.
              .X.X.X.X
              X.X.X.X.
              ...X...X
              X.X.X.X.
              .X.X.X..
'''


n,i,j,d=tuple(map(int,input().split()))


Board=[[False for _ in range(n)] for _ in range(n)]
Board[i][j]=True

def next_valid(b):
    S=[[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i-1>=0 and j-2>=0 and b[i-1][j-2]:
                S[i][j]=True
            elif i+1<n and j-2>=0 and b[i+1][j-2]:
                S[i][j]=True
            elif i+1<n and j+2<n and b[i+1][j+2]:
                S[i][j]=True
            elif i-1<n and j+2<n and b[i-1][j+2]:
                S[i][j]=True

            elif i+2<n and j+1<n and b[i+2][j+1]:
                S[i][j]=True
            elif i+2<n and j-1>=0 and b[i+2][j-1]:
                S[i][j]=True
            elif i-2>=0 and j+1<n and b[i-2][j+1]:
                S[i][j]=True
            elif i-2>=0 and j-1>=0 and b[i-2][j-1]:
                S[i][j]=True
    return S


for _ in range(d):
    Board=next_valid(Board)












TB=[["X" if k else "." for k in l] for l in Board]
for t in TB:
    print("".join(t))
