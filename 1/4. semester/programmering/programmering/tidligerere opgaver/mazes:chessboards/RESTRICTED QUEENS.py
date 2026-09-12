'''
    RESTRICTED QUEENS

    The k-RESTRICTED QUEENS problem is a variant of the eight queens
    puzzle, where we are given an n x n chessboard, and want to place
    a maximum number of k-RESTRICTED QUEENS, so that no k-restricted
    queen can reach another k-restricted queen in one move.
    A k-restricted queen is a queen that in one move can go at most k
    cells horizontally, vertically or diagonally.

    Note that n=8 and k=7 is the classic 8-queens puzzle.

    Input:  A line with two space separated integers n and k, where
            n is the size of the board, and k how far a queen can move.
            It is guaranteed that 2 <= k <= n <= 7.

    Output: The maximum number of k-restricted queens possible to
            place on an n x n chessboard.

    Examples:

      Input:  6 4

      Output: 8

        E.g. obtained by the following queen positions:

        Q....Q
        ..Q...
        ....Q.
        .Q....
        ...Q..
        Q....Q

      Input:  5 2

      Output: 5

        E.g. obtained by the following queen positions:

        .Q..Q
        .....
        Q....
        ..Q..
        ....Q

    Note: The below code already handles reading the input.
'''
def takes(boar,i,j,k,n):
    board=[[True if h else False for h in g] for g in boar ]
    for p in range(k+1):
      if i+p<n:
          board[i+p][j]=False
      if i-p>=0:
          board[i-p][j]=False
      if j+p<n:
          board[i][j+p]=False
      if j-p>=0:
          board[i][j-p]=False
      if i+p<n and j+p<n:
          board[i+p][j+p]=False
      if i-p>=0 and j-p>=0:
          board[i-p][j-p]=False
      if i-p>=0 and j+p<n:
          board[i-p][j+p]=False
      if i+p<n and j-p>=0:
          board[i+p][j-p]=False
    return board


def solution(n,k,q,boar):
    #for b in boar:
    #    print(b)
    #print(50*"-")
    if q==0:
       return True
    if sum([sum(l) for l in boar])<q:
        return False

    for i in range(n):
        for j in range(n):
          if boar[i][j]:
              if solution(n,k,q-1,takes(boar,i,j,k,n)):
                  return True
        
                              
    return False

    
    
def queens(n, k):
    for j in range(10,1,-1):
      board=[[True for _ in range(n)] for _ in range(n)]
      if solution(n,k,j,board):
          return j
    
        


n, k = map(int, input().split())
print(queens(n, k))
#n=7
#board=[[True for _ in range(n)] for _ in range(n)]

#print(solution(7,2,15,board))
