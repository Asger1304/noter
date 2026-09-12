'''
    EXPAND

    In this task you are given a list of words of capital letters, some possibly
    abbreviated to <prefix>*, where <prefix> is a sequence of capital letters. 
    Your task is to expand all abbreviated strings to the most recently output 
    string with a matching prefix.

    Input:  The first line contains an integer n, where 1 <= n <= 100.
            The next n lines each contain a word with 1 to 25 characters, 
            all upper case letters, except the last character that can be '*'.

    Output: n lines, where the i'th output line equals the i'th input string
            if this string only contains upper case letters. If the i'th input 
            string ends with '*', the i'th output line equals the most recent 
            output line before the i'th output line with a prefix matching the 
            characters before '*' (possibly the empty string, like in the second 
            last input line in the example below). It is guaranteed that such a 
            line exists.

    Example:

      Input:  7
              AARHUS
              DENMARK
              COPENHAGEN
              DEN*
              A*
              *
              C*

      Output: AARHUS
              DENMARK
              COPENHAGEN
              DENMARK
              AARHUS
              AARHUS
              COPENHAGEN
'''


n=int(input())
L=[]
for i in range(n):
    S=input()
    if S[-1]=="*":
        for j in range(i)[::-1]:
            if S[:-1]==L[j][:len(S)-1]:
                L.append(L[j])
                break
    else:
        L.append(S)



for l in L:
    print(l)
