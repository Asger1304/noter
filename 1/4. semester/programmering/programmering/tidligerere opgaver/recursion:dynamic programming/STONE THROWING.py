'''
    STONE THROWING

    Assume we have n points in the plane we can be in, and we start in an 
    arbitrary one of these points. In order to move from one point to another 
    point, we must throw a stone from the point we are in to the point we want
    to move to.  Unfortunately, throwing takes energy, so the next throw will 
    always be strictly shorter than the previous throw. I.e., moving from one 
    point p to another point q causes the next move to be strictly shorter than 
    the distance from p to q, and in particular we cannot move directly back 
    from q to p in the next move. The first throw can be of arbitrary length.

    As an example consider the following nine grid points below. 

        (3, 1) (3, 2) (3, 3)
        (2, 1) (2, 2) (2, 3)
        (1, 1) (1, 2) (1, 3)

    A possible longest valid point sequence is the following six points:

        (1, 1), (3, 3), (1, 2), (3, 2), (2, 1), (1, 1)

    The first move is from (1, 1) to (3, 3) with square distance 
    (3 - 1) ** 2 + (3 - 1) ** 2 = 8, and the next move is from (3, 3) to
    (1, 2) with square distance (1 - 3) ** 2 + (2 - 3) ** 2 = 5, and so on.
    Note that the point (1, 1) appears twice in the sequence.

    Input:  The first line contains an integer n, the number of points,
            where 1 <= n <= 100. The next n lines each contain two integers
            x and y, separated by a space, with the coordinates of the points. 
            It is guaranteed that all points are distinct.

    Output: The maximum number of points in a valid point sequence.

    Example:

      Input:  9
              1 1
              1 2
              1 3
              2 1
              2 2
              2 3
              3 1
              3 2
              3 3

      Output: 6
'''

from functools import cache
n=int(input())
squares=[]
for _ in range(n):
    squares.append(tuple(map(int,input().split())))

    
@cache
def sqdist(x,y):
    x1,y1=x
    x2,y2=y
    return (x1-x2)**2+(y1-y2)**2

dist_board=[[sqdist(x,y) for x in squares] for y in squares]
maxl=max([dist_board[i][j] for i in range(len(dist_board)) for j in range(len(dist_board[0]))])


def find(squares,ml):
    @cache
    def find_max(pos,ml):
        return 1+max([find_max(po,sqdist(po,pos)-1) for po in squares if  0<sqdist(po,pos)<=ml]+[0])
    return max([find_max(pos,ml) for pos in squares])
    
print(find(squares,maxl))
        
