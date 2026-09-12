'''
    DOUBLE WORDS

    Given a string find all words that appear twice in a row in the string.

    E.g., in the below string the words 'TREES' and 'BIRDS' appear twice in a row.

      THE FOREST CONTAINS TREES TREES TREES AND MORE TREES AND BIRDS BIRDS AND BIRDS

    Input:  A singe line containing a string of words separated by spaces. 
            Each word contains uppercase letters only.

    Output: A single line with the words that appear twice in a row in the 
            string, with no word repeated in the output, and the words appearing
            sorted in alphabetical order. If no word appears twice in a row,
            output '-'.

    Example:

      Input:  THE FOREST CONTAINS TREES TREES TREES AND MORE TREES AND BIRDS BIRDS AND BIRDS

      Output: BIRDS TREE
'''


isse=input().split()
dw=set()
for i in range(len(isse)-1):
    if isse[i]==isse[i+1]:
        print
        dw.add(isse[i])
if dw:
        print(" ".join(sorted(list(dw))))
else:
     print("-")
