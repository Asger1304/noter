''' 
    MISSING RECTANGLE CORNER

    A rectangle has four corners (x1, y1), (x1, y2), (x2, y1) and (x2, y2),
    for four integers x1, x2, y1, and y2, where x1 != x2 and y1 != y2.
    Your task is to find the missing corner, given three of the corners.

    Input:  Three lines, each line containing two integers x and y,
            separated by a space, representing a corner point (x, y). 
            It is guaranteed that the three input points are the
            corners of a rectangle as defined above.

    Output: A single line with two integers x and y, separated by a space,
            representing the missing corner point (x, y).

    Example:

      Input:  2 5
              4 3
              4 5

      Output: 2 3
'''

x1=tuple(map(int,input().split()))
x2=tuple(map(int,input().split()))
x3=tuple(map(int,input().split()))

z=[x1,x2,x3]
x=[f[0] for f in z]
y=[f[1] for f in z]


def get_unique(L):
        g={}
        for s in L:
                if s in g:
                        g[s]+=1
                else:
                    g[s]=1
        for h in g:
               if g[h]==1:
                      return h

print(str(get_unique(x))+" "+str(get_unique(y)))



    
