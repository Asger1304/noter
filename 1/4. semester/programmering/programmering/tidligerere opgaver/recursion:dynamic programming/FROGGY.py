'''
    FROGGY

    You are jumping around on an integer grid. At each time step you can jump to 
    a grid cell within distance d of your current position, where the distance 
    between two grid cells is the Euclidean distance between the cell centers. 
    You can freely choose your start position. At each step exactly one grid 
    cell is green. If you are on the green cell, you get a point. 
    What is the maximum number of points you can get, if you know the positions 
    of all green cells in advance?

    Input:  The first line contains two integers n and d, where 1 <= n <= 25 is
            the number of time steps, and 1 <= d <= 25 is the jump radius.
            Each of the following n lines contains two integers x and y, 
            where 0 <= x <= 25 and 0 <= y <= 25, where the i'th line is 
            the position of the green cell at time step i.

    Output: A single integer, the maximum number of points you can get.

    Example: 
    
      Input:  3 5
              5 0
              0 5
              5 10

      Output: 2

      In this example we have n = 3 points and jump radius d = 5.
      You can start at (5, 0) [that is green and score a point],
      jump to (5, 5) [not scoring a point, since (0, 5) is now green], and then
      jump to (5, 10) [scoring a point, since this cell is now green]. 
      In total you score 2 points, and this is the best possible.
'''
from functools import cache
from math import sqrt

n,d=tuple(map(int,input().split()))
points=[]
for _ in range(n):
    points.append(tuple(map(int,input().split())))

def sqdist(x,y):
    x1,y1=x
    x2,y2=y
    return sqrt((x1-x2)**2+(y1-y2)**2)

def jump_sum(points,default_jump):
    @cache
    def jumps(i,default_jump,actual_jump,point):
        if i==n-1:
            return 0
        return max( [jumps(i+1,default_jump,actual_jump+default_jump,point),1+jumps(i+1,default_jump,default_jump,points[i+1]) if sqdist(points[i+1],point)<=actual_jump else jumps(i+1,default_jump,actual_jump+default_jump,point)])
    
    
    
    return 1+max([jumps(i,default_jump,default_jump,points[i]) for i in range(len(points))])

print(jump_sum(points,d))



