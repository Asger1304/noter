'''
    FREQUENT

    Print the most frequent integer(s) occurring in a list of integers.

    Input:  A single line with n space separated positive integers,
            where 1 <= n <= 100.

    Output: If the most frequent integer(s) occur x times in the input,
            print all integers occurring x times in the input,
            one integer per line, and in increasing order.

    Example:

      Input:  1 2 2 300 2 5 5 300 4 4 4 4 1 2

      Output: 2
              4
'''


i=map(int,input().split())
d={}
for g in i:
        if g in d:
                d[g]+=1
        else: 
                d[g]=1

m=max([d[g] for g in d])
o=[g for g in d if d[g]==m]
out=sorted(o)
for s in out:
        print(s)

