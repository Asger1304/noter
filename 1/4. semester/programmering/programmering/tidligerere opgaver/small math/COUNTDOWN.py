'''
    COUNTDOWN

    Write code that reads an integer n from the input, and then prints a 
    decreasing sequence as described below starting with n and ending with 1, 
    one integer per line. 
    The sequence should be generated as follows: if the current number is even,
    the next number is n / 2; otherwise, the next number is n - 1.

    E.g., for input
       
        14

    you should print the lines

        14
        7
        6
        3
        2
        1

    Input:  A single line containing an integer n, where 1 <= n <= 1000.

    Output: As described above.

    Example:
    
      Input:  27

      Output: 27
              26
              13
              12
              6
              3
              2
              1

    Note: The below code already reads n.
'''


n = int(input())

L=[]
while n>0:
    L.append(n)
    if n%2==1:
        n=n-1
    else:
        n=n//2

for s in L:
    print(s)