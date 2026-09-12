'''
    CALCULATE

    Read from input a line containing three values: two integers a and b, and a
    character operator which is either '+', '-', or 'x', where 'x' denotes
    multiplication. Print the result of evaluating the expression a operator b.
       
    Input:  A single line 'a b operator' where a and b are integers, 0 <= a <= 100
            and 0 <= b <= 100, and operator is one of '+', '-', or 'x'

    Output: The result of evaluating the expression a operator b.

    Example:
    
      Input:  30 50 -
      Output: -20

      Input:  19 17 +
      Output: 36

      Input:  7 6 x
      Output: 42    
'''


a,b,o=tuple(input().split())
a=int(a)
b=int(b)
if o=="+":
    print(a+b)
elif o=="-":
    print(a-b)
else:
    print(a*b)
