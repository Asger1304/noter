'''
    DENSE SAMPLE

    Given a list of positive weights, the task is to find a subsequence (sample)
    of the weights such that 1) the subsequence has minimum sum, 2) among every
    three consecutive weights in the lists, at least one of them is in the 
    sample. It is guaranteed that there is a unique minimum weight solution.

    Input:  A single Python list L of integers (weights), where 
            3 <= len(L) <= 100 and all elements are between 1 and 1000.

    Output: A single line with a Python list of strictly increasing indexes 
            into L defining a sample, where the weights in the sample have
            minimum sum, and among every three consecutive indexes into L, 
            at least one is in the sample.

    Example:

      Input:  [7, 5, 7, 5, 7, 6, 7]

      Output: [1, 4]

      Explanation: In the input list L, L[1] + L[4] = 5 + 7 = 12 achieves the 
      minimum possible weight sum, if for all three consecutive indexes at least 
      one index is in the sample.
    
    Note: The below code already reads the input list L.
'''
from functools import cache

L = eval(input())

def find_min(L):
    @cache
    def smallest_sum(i,c):
        if i==len(L):
            return 0
        elif c==2:
            return L[i]+smallest_sum(i+1,0)
        else:
            return min([smallest_sum(i+1,c+1),L[i]+smallest_sum(i+1,0)])
        
    def find_best_seq(i,c):
        if i==len(L):
            return []
        elif c==2:
            return [i]+find_best_seq(i+1,0)
        elif smallest_sum(i+1,c+1)<=L[i]+smallest_sum(i+1,0):
            return find_best_seq(i+1,c+1)
        else:
            return [i]+find_best_seq(i+1,0)

    return find_best_seq(0,0)

print(find_min(L))
        
        

    
