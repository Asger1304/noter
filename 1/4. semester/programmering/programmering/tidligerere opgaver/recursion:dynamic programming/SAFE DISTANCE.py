'''
    SAFE DISTANCE

    Your task is to write a function safe_distance(target, vectors), where
    target is a point/tuple (x, y) and vectors is a list of distinct vectors,
    each a tuple (x, y).  The function should return the smallest Euclidean
    distance from target to a point in the plane that is a sum of a subset
    of the vectors. 

    For target = (9, 10) and vectors = [(2, -5), (3, 4), (7, 3)],
    the point closest to target is (10, 7) = (3, 4) + (7, 3) with
    distance sqrt((9 - 10) ** 2 + (10 - 7) ** 2) = sqrt(10) = 3.162.

    Input:  A single line with a Python tuple (target, vectors).
            target is an integer tuple (x, y), with -100 <= x <= 100
            and -100 <= y <= 100, and vectors is a list of distinct
            integer tuples (x, y), with len(vectors) <= 50 and 
            -10 <= x <= 10 and -10 <= y <= 10.

    Ouput:  Distance from target to a closest point in the plane that
            is the sum of a subset of vectors.  The distance should be
            printed with 3 decimals.

    Example:

       Input:  ((9, 10), [(2, -5), (3, 4), (7, 3)])
 
       Output: 3.162

    Note: The below code already handles the input and output.
'''

from math import sqrt

def safe_distance(target, vectors):
    sub=subsets(vectors)
    del sub[0]
    sums=[leng_sum_set(l,target) for l in sub]
    return sqrt(min(sums))


def leng(x_1,x_2):
    x1,y1=x_1
    x2,y2=x_2
    return (x1-x2)**2+(y1-y2)**2

def subsets(L):
    # Base case: the only subset of an empty list is the empty list itself.
    if L == []:
        return [[]]
    # Recursive case: get all subsets of the tail of L.
    rest = subsets(L[1:])
    # For each subset in the result, add the first element to create a new subset.
    return rest + [[L[0]] + subset for subset in rest]

def leng_sum_set(L,target):
    x=sum([s[0] for s in L])
    y=sum([s[1] for s in L])
    return leng((x,y),target)




    


target, vectors = eval(input())
distance = safe_distance(target, vectors)
print('%.3f' % distance)
