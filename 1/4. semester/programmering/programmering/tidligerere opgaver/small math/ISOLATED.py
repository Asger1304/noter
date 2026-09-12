'''
    ISOLATED

    Given a set of n points and a distance d, report the number of isolated 
    points, i.e., the number of points where all other points have Euclidean
    distance at least d to the point.

    Input:  The first line contains an integer n, 0 <= n <= 100,
            the number of points.
            The second line contains an integer d, 1 <= d <= 10_000,
            the distance.
            The next n lines each contains a point consisting of two space
            separated integers x and y, -1000 <= x <= 1000 and
            -1000 <= y <= 1000. Points are not necessarily distinct.

    Output: A single integer, the number of points where all other points have
            Euclidean distance at least d to the point.

    Example: 

      Input:  4
              4
              -3 0
              0 0
              3 3
              3 -3

      Output: 2

      The only isolated points are (3, 3) and (3, -3). They both have (0, 0)
      as the nearest point, with distance sqrt(18) > d = 4.
'''
from math import sqrt

n=int(input())
d=int(input())
points=[]
for _ in range(n):
    points.append(tuple(map(int,input().split())))

def dist(a,b):
    x1,y1=a
    x2,y2=b
    return sqrt((x1-x2)**2+(y1-y2)**2)

count=0
for i in range(len(points)):
    if all([dist(points[i],points[j])>=d for j in range(len(points)) if j!=i]):
        count+=1
print(count)