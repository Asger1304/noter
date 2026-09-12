'''
    RECURSIVE FUNCTION

    Consider the following recursively defined integer function 

        f(n) = f(n - 1) + 2 * f(n - 2) + 3 * f(n - 3)

    for n >= 3, and f(n) = 1 for 0 <= n < 3.

    Your task is to write a program that computes f(n).

    Input:

      A single line containing an integer n, where 1 <= n <= 10000.

    Output:

      f(n)

    Example:

      Input:  10

      Output: 2036
'''

import sys
def memoize(f):
  # answers[args] = f(*args)
  answers = {}
  def wrapper(*args):
    if args not in answers:
      answers[args] = f(*args)
    return answers[args]
  return wrapper

sys.setrecursionlimit(10**6)
n=int(input())
@memoize
def f(n):
    if n<3:
        return 1 
    else:
        return 3*f(n-3)+ 2*f(n-2) + f(n-1)

print(f(n))