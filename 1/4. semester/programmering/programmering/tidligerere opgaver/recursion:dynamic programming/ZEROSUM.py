'''
    ZEROSUM

    Given a list of integers, find three integers in the list that sum to zero.

    Input:  A single line with n distinct integers separated by spaces, where
            3 <= n <= 5000 and each integer is in the range -10**10 to 10**10.
            It is guaranteed that the input contains a unique solution, i.e., 
            three exist integers x < y < z in the list such that x + y + z = 0.

    Output: A single line with the three integers that sum to zero, 
            separated by spaces and in increasing order.

    Example:

      Input:  -67 3 -11 -93 -32 7 9 -36 53 -12

      Output: -12 3 9
'''
def memoize(f):
        # answers[args] = f(*args)
        answers = {}
        def wrapper(*args):
                if args not in answers:
                        answers[args] = f(*args)
                return answers[args]
        return wrapper




import sys
sys.setrecursionlimit(10**5)

L=sorted(list(set(map(int,input().split()))))

def Z_sum(L):
        @memoize
        def isthere(i,n,s):
                if n==0:  
                        if s==0:
                                return []
                        else:
                                return None
                if i==len(L):
                        return None
                if len(L)-i<n:
                        return None
                solution=isthere(i+1,n,s)
                if solution != None:
                        return solution
                solution=isthere(i+1,n-1,s-L[i])
                if solution !=None:
                        return solution +[L[i]]

        g=isthere(0,3,0)

        return sorted(g)
print(" ".join(map(str,Z_sum(L))))

