'''
    ABC PERMUTATIONS

    Given three integers a, b, and c, print in alphabetical order all possible 
    strings containing a, b and c occurrences of 'A', 'B' and 'C', respectively.

    Input:  A single line with three integers a, b, and c separated by spaces,
            where a >= 0, b >= 0, c >= 0 and 1 <= a + b + c <= 10.
            
    Output: All possible strings, one string per line, containing a occurrences 
            of 'A', b occurrences of 'B', and c occurrences of 'C'. The strings 
            should be printed in alphabetical order, without any repetitions.
  
    Example:

      Input:  2 1 1

      Output: AABC
              AACB
              ABAC
              ABCA
              ACAB
              ACBA
              BAAC
              BACA
              BCAA
              CAAB
              CABA
              CBAA
'''

import itertools
a, b, c = map(int, input().split())

pos=a*["A"]+b*["B"]+c*["C"]
perm=sorted(set(itertools.permutations(pos)))
for i in perm:
    print("".join(i))
