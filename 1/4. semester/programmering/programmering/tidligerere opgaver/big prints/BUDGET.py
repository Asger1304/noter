'''
    BUDGET

    Print a budget overview based on a list of transactions.
 
    Input:  A single line with a list of at most 100 transactions,
            each transaction a pair (value, text) where value is a
            number that is positive for an income and negative for
            an expense. The text is at most 35 characters long.
            Each value has absolute value <= 100_000.
            There is at least one income and one expense.

    Output: A print out of the budget as shown in the example below.
            Each line should be 50 characters long, except for
            the lines 'Income' and 'Expenses'. The budget should
            consist of three parts: Income, Expenses, and Total.
            Total is the sum of all values in the transactions.
            Income and expense tranactions should be ordered by
            decreasing absolute value, and alphabetically if
            several values are equal. 
            In lines with values, the text and value should be
            separated by a sequence of '.', with a SINGLE SPACE
            AT EACH END. Values should be printed with two decimals.

    Example:

      Input:  [(-500.00, 'Insurance'), (-2000.00, 'Food'), (-3500.00, 'Rent'),
               (-150.00, 'Hair cut'), (200.00, 'Loan'), (6000.00, 'Salary')]

      Output: ==================================================
              Income
              --------------------------------------------------
              Salary ................................... 6000.00
              Loan ...................................... 200.00
              ==================================================
              Expenses
              --------------------------------------------------
              Rent .................................... -3500.00
              Food .................................... -2000.00
              Insurance ................................ -500.00
              Hair cut ................................. -150.00
              ==================================================
              Total ...................................... 50.00
              ==================================================

    Note: The below code already handles reading the input.
'''


def budget(transactions):
        incomes=[(float(number),name) for number,name in transactions if number>0]
        expenses=[(float(number),name) for number,name in transactions if number<0]
        total=sum([float(trans[0]) for trans in transactions])

        expenses.sort(key=lambda x:x[1])
        expenses.sort(key=lambda x:x[0])
        incomes.sort(key=lambda x:x[1])
        incomes.sort(key=lambda x:x[0],reverse=True)

        print(50*"=")
        print("Income")
        print(50*"-")
        for i in incomes:
                print(f"{i[1]} {(48-len(i[1])-len(f"{i[0]:.2f}"))*"."} {i[0]:.2f}")
        print(50*"=")
        print("Expenses")
        print(50*"-")
        for i in expenses:
                print(f"{i[1]} {(48-len(i[1])-len(f"{i[0]:.2f}"))*"."} {i[0]:.2f}")
        print(50*"=")
        print(f"Total {(49-6-len(f"{total:.2f}"))*"."} {total:.2f}")
        print(50*"=")

        


budget(eval(input()))
