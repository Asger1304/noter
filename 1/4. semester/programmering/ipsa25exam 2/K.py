'''
    COMMON

    You are given a list of n names, and for each name a list of preferences (an
    unordered list of distinct values). The goal is to find the largest k such
    that at least two names have k preferences in common. Your task is to find k
    and list all such subsets of k preferences shared by at least two names, and
    list the names who share these preferences.

    Input:  The first line is an integer n, where 2 <= n <= 100. The following
            n lines each contain a name followed by a list of one or more
            preferences, all separated by spaces. The names and preferences
            consist only of lower and upper case letters. The names are unique.
            Each name has between 1 and 100 distinct preferences.

    Output: The first line contains two space separated integers k and s, where 
            k is the size of the largest subset of preferences shared by at
            least two names, and s is the number of such distinct subsets of
            size k. The following 2 * s lines contain for each of these s
            subsets of preferences in lexicographical order two lines (the sets
            are ordered as if a set was a sorted list of preferences): The first
            line the preferences in alphabetical order, separated by spaces, and
            the second line all names sharing these preferences, in alphabetical
            order and separated by spaces. It is guaranteed that k >= 1.

    Example:

      Input:  5
              Brittany Pineberry Mohsina MonsteraDeliciosa Liam Guava Loganberry
              Melon StarApple Pineberry Adam Cherimoya Pineberry Lychee Melon
              Plum Guava Joshua MonsteraDeliciosa Plum Arthur Thimbleberry
              Damson Orange Date Tangerine

      Output: 3 1
              Guava Melon Pineberry Adam Liam
'''

from functools import cache

def memoize(f):
        # answers[args] = f(*args)
        answers = {}
        def wrapper(g,h,i):
                if (g,h,i) not in answers:
                        answers[(g,h,i)] = f(g,h,i)
                        answers[(h,g,i)] = f(g,h,i)
                return answers[(g,h,i)]
        return wrapper


@memoize
def is_i(g,h,i):
    return len([f for f in pp[g] if f in pp[h]])>=i












n=int(input())

pp={}
for _ in range(n):
    S=input().split()
    pp[S[0]]=set(S[1:])

max_good=0
key=list(pp.keys())
for i in range(100):
    #if any([len([f for f in pp[key[o]] if f in pp[key[j]]])>=i for j in range(len(key)) for o in range(j+1,len(key))]):
    if any([is_i(key[j],key[o],i) for j in range(len(key)) for o in range(j+1,len(key))]):
        continue
    else:
        max_good=i-1
        break





good_sets=[set([m for m in pp[key[f]] if m in pp[key[g]]]) for g in range(len(key)) for f in range(g+1,len(key)) if is_i(key[g],key[f],max_good)]
#[set([m for m in pp[key[f]] if m in pp[key[g]]]) for g in range(len(key)) for f in range(g+1,len(key)) if len([k for k in pp[key[f]] if k in pp[key[g]]])==max_good]

final_sets=[]
for s in good_sets:
    if s not in final_sets:
        final_sets.append(s)

final_final=[sorted(list(s)) for s in final_sets]
ff=final_final.sort()
print(f"{max_good} {len(final_sets)}")

for s in final_final:
    print(" ".join(sorted(s)))
    print(" ".join(sorted([g for g in pp if len([h for h in pp[g] if h in s])==max_good])))
