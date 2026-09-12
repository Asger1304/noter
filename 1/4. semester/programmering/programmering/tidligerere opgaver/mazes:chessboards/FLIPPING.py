'''
    FLIPPING

    Consider a grid of size n x n, where each cell is either empty '.' or
    occupied 'x'.  You task is to perform d simulation steps. In each step a
    grid cell becomes 'x' if an odd number of neighboring cells on the grid 
    (up, down, left, right) are marked 'x' before the step. Otherwise,
    the cell becomes '.'. E.g., the below illustrates two simulation steps:

        .....       .....       ..x..
        .....       ..x..       .....
        ..x..  -->  .x.x.  -->  x...x
        .....       ..x..       .....
        .....       .....       ..x..
    
    Input:  First line an integer n (1 <= n <= 25), the size of the grid.
            The second line an integer d (1 <= d <= 10), the number of steps.
            The next n lines contains the grid, each line consisting of n 
            characters, which are either '.' or 'x'.

    Output: The grid after performing d simulation steps.

    Example:

      Input:  5
              2
              .....
              .....
              ..x..
              .....
              .....

      Output: ..x..
              .....
              x...x
              .....
              ..x..
'''


n=int(input())
d=int(input())
b=[]
for _ in range(n):
    b.append(list(input()))
boa=[[True if b[i][j]=="x" else False for i in range(n)] for j in range(n)]


def count_neigbors(i,j,board):
    S=[]
    if 0<=i-1<n:
        S.append((i-1,j))
    if 0<=i+1<n:
        S.append((i+1,j))
    if 0<=j-1<n:
        S.append((i,j-1))
    if 0<=j+1<n:
        S.append((i,j+1))
    h=0
    for s,g in S:
        if board[s][g]==True:
            h+=1
    return h


def new_board(bof):
    bos=[[count_neigbors(j,i,bof)%2==1 for i in range(n)] for j in range(n)]
    return bos

for _ in range(d):
    bog=new_board(boa)
    boa=bog
    #B=[["x" if boa[i][j] else "." for i in range(n)] for j in range(n)]
    #for l in B:
    #    print("".join(l))
    #print(25*"-")






B=[["x" if boa[i][j] else "." for i in range(n)] for j in range(n)]
for l in B:
    print("".join(l))
