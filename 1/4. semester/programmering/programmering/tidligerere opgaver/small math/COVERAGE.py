'''
    COVERAGE

    Given a set of n points and m circles, determine how many points are 
    contained in at least one circle. We say a point is contained in a circle 
    if it inside or on the boundary of the circle.

    E.g., if we have four points (0, 0), (0, 10), (10, 0), and (10, 10),
    and two circles with centers (1, 1) and (5, 12) and radii 5 and 6,
    respectively, then the first point is contained in the first circle,
    and the second and fourth points are contained in the second circle. 
    The third point is not contained in either circle. Thus, the answer is 3.

    Input:  The first line contains two integers n and m, separated by space,
            where 1 <= n <= 100 and 1 <= m <= 100. The next n lines contain 
            two integers x and y each, separated by space, representing the
            coordinates of a point. The next m lines contain three integers 
            cx, cy, and r each, separated by spaces, where (cx, cy) is the
            center of a circle with radius r.

    Output: An integer, the number of points contained in at least one circle.

    Example:

      Input:  4 2
              0 0
              0 10
              10 0
              10 10
              1 1 5
              5 12 6

      Output: 3
'''


n,m=tuple(map(int,input().split()))
points=[]
for _ in range(n):
    points.append(tuple(map(int,input().split())))
circles=[]
for _ in range(m):
    circles.append(tuple(map(int,input().split())))

def is_within(point,circle):
    x1,y1=point
    x2,y2,r=circle
    return (x1-x2)**2+(y1-y2)**2<=r**2
n=0
for point in points:
    if any([is_within(point,circle) for circle in circles]):
        n+=1

print(n)
    