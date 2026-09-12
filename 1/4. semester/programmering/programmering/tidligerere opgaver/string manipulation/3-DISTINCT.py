'''
    3-DISTINCT

    Given a string, print all distinct substrings containing exactly 
    3 distinct letters. For example, the string SUMMER has 5 such
    substrings: MER, MMER, SUM, SUMM, and UMME (in alphabetic order).

    Input:  A singe line with a string of length at most 100 and 
            only containing letters A-Z.

    Ouput:  All distinct substrings containing exactly 3 distinct letters,
            sorted in alphabetic order with one substring per line.

    Example:

      Input:  SUMMER

      Output: MER
              MMER
              SUM
              SUMM
              UMME
'''
def uniques(s):
    return len(set(s))

I=input()
w=[]
for i in range(len(I)-2):
        if uniques(I[i:i+3])==3:
                w.append(I[i:i+3])
        j=1
        while True:
                if i+3+j<=len(I) and uniques(I[i:i+3+j])<=3:
                        if uniques(I[i:i+3+j])==3:
                                w.append(I[i:i+3+j])
                        j+=1
                        continue
                
                break

sw=sorted(set(w))
for g in sw:
       print(g)
    





    
