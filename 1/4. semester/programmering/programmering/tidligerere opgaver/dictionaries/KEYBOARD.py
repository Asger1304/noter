'''
    KEYBOARD

    Assume the placement of letters on a keyboard is described as

        Q..W..E..R..T..Y..U..I..O..P
        .A..S..D..F..G..H..J..K..L..
        ..Z..X..C..V..B..N..M.......

    where '.' indicates spaces between keys. We define the (Manhattan)
    distance between two keys to be the number of columns plus rows to
    be moved from getting from one key to the other, e.g. from 'S' to
    'C' one has to move 4 columns to the right and 1 row down, i.e.
    the distance is 4 + 1 = 5. 

    Input:  The first line contains an integer n, the number of rows
            in the layout. Then follows n lines describing the layout
            of the n rows of the keyboard layout, where 1 <= n <= 10.
            All rows have equal length and only contain '.' and a subset
            of the letters 'A' to 'Z'.  A letter occurs at most once on
            the keyboard.

    Output: A distance table between all pairs of keys.
            Rows and columns should be sorted alphabetically.

    Example:

      Input:  3
              A.B.C
              .D.E.
              F.G.H

      Output:    A  B  C  D  E  F  G  H
              A  0  2  4  2  4  2  4  6
              B  2  0  2  2  2  4  2  4
              C  4  2  0  4  2  6  4  2
              D  2  2  4  0  2  2  2  4
              E  4  2  2  2  0  4  2  2
              F  2  4  6  2  4  0  2  4
              G  4  2  4  2  2  2  0  2
              H  6  4  2  4  2  4  2  0
'''


n=int(input())
board=[]
for _ in range(n):
    board.append(list(input()))

catalog={}
for j in range(n):
    for i in range(len(board[0])):
        if board[j][i]!=".":
            catalog[board[j][i]]=(i,j)


def manhat(a,b):
        x1,y1=catalog[a]
        x2,y2=catalog[b]
        return abs(x1-x2)+abs(y1-y2)


bogs=sorted(list(catalog.keys()))



print(" "+" ".join(bogs))
for h in bogs:
     print(h+" "+" ".join([str(manhat(h,b)) for b in bogs]))
