'''
    SET

    Your task is to maintain a set of integers, initially empty,
    under "insert" and "delete" commands. "insert <value>" inserts
    a value into the set (if the value already is in the set,
    nothing is changed), and "delete <value>" removes the value
    from the set (if the value is not in the set, nothing is changed).

    Input:  The first line contains an integer n, where 1 <= n < = 100.
            The following n lines each contain a command "insert <value>"
            or "delete <value>", where <value> is an integer.

    Output: A single line containing the final content of the set
            in sorted order separated by spaces.

    Example:

       Input:  7
               insert 3
               insert 2
               insert 3
               delete 3
               insert 5
               delete 4
               insert 1

       Output: 1 2 5
'''


n=int(input())
S=set()
for i in range(n):
        com,num=tuple(input().split())
        num=int(num)
        if com=="insert":
                S.add(num)
        elif com=="delete":
                if num in S:
                        S.remove(num)
S1=sorted(S)
for s in S1:
        print(s,end=" ")

    

