'''
    SELECT

    Write a function that reads a list of column names to extract from a table,
    and then reads a table, and extracts the required columns.

    Input:  Line 1: comma separated list of 1 or more columns to extract.
            Line 2: integer rows, the number of rows in the table.
            Line 3: comma separated list of column names in the table.
            Next rows lines: comma separated list of values for each table row.

            The table has between 1 and 10 columns, all columns have a
            unique column name, and there at most 100 rows in the table.
            At least one column should be extracted, and extracted columns
            are distinct.

    Output: For each row in the table, print a single line with the extracted
            column values in the requested order, separated by comma.

    Example:

      Input:  name,symbol
              5
              id,symbol,name,weight
              1,H,Hydrogen,1.008
              2,He,Helium,4.0026
              3,Li,Lithium,6.94
              4,Be,Beryllium,9.0122
              5,B,Boron,10.81

      Output: Hydrogen,H
              Helium,He
              Lithium,Li
              Beryllium,Be
              Boron,B
'''

ext=input().split(",")
n=int(input())
data=input().split(",")
dat=dict()
for d in data:
    dat[d]=[]
for _ in range(n):
    punkt=input().split(",")
    for i in range(len(data)):
        dat[data[i]].append(punkt[i])

for i in range(n):
    s=[dat[e][i] for e in ext]
    print(",".join(s))

