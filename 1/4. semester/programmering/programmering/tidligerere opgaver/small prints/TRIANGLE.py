'''
    TRIANGLE

    For an input string s of length n, print n lines, where the i'th
    line contains the first i characters of s.

    Input:  A single line with a string of length between 1 to 100,
            only containing alphanumeric characters.

    Output: If the input string s contains n characters, the output
            consists of n lines, the i'th line containing the first
            i characters of s.

    Example:

      Input:  abcdef

      Output: a
              ab
              abc
              abcd
              abcde
              abcdef
'''


i=input()
for s in range(len(i)):
    print(i[:s+1])
