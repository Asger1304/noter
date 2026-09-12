
'''
    LARGEST DIVISIBLE

    Write a function largest_divisible(n, d) that takes two integers n and d,
    and returns the largest number less than or equal to n that is divisible by d.

    E.g., largest_divisible(23, 7) should return 21.

    Input:  A single line containing two integers n and d, separated by space,
            where 0 <= n <= 1000 and 1 <= d <= 1000.

    Output: The largest number less than or equal to n that is divisible by d.

    Example:  

      Input:  23 7
      
      Output: 21

    Note: The below code already reads n and d, and prints the result of 
    calling largest_divisible(n, d).
'''
from math import floor

def largest_divisible(n, d):
  i=0
  while True:
    if (n-i)%d==0:
      return n-i
    i+=1



n, d = map(int, input().split())
print(largest_divisible(n, d))
