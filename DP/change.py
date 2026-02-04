#Naiive recursive soltion for Least Exact Change (LEC), 4,3, 1-coin problem
def change(n):
    #smallest subproblems have simple answers
    if n == 4 or n == 3 or n == 1:
        return 1
    if n == 2:
        return 2

    #kids job: if I pick up a coin to add to my LEC...
    #...which coin leads to the best answer?
    a = change(n-4) #LEC for remainder after picking up 4-coin
    b = change(n-3) #LEC for remainder after picking up 3-coin
    c = change(n-1) #LEC for remainder after picking up 1-coin

    #which kid found the best answer?
    min = a
    if b < a:
        min = b
    if c < min:
        min = c

    return 1 + min #include the coin picked up to make the kid

#Naiive recursive soltion for Least Exact Change (LEC), 4,3, 1-coin problem
def change_memo(n, table):

    #-------FIRST CHANGE: query the table------#
    if table[n] != -1:
        return table[n]

    #smallest subproblems have simple answers
    if n == 4 or n == 3 or n == 1:
        return 1
    if n == 2:
        return 2

    #kids job: if I pick up a coin to add to my LEC...
    #...which coin leads to the best answer?
    a = change_memo(n-4, table) #LEC for remainder after picking up 4-coin
    b = change_memo(n-3, table) #LEC for remainder after picking up 3-coin
    c = change_memo(n-1, table) #LEC for remainder after picking up 1-coin

    #which kid found the best answer?
    min = a
    if b < a:
        min = b
    if c < min:
        min = c

    #----SECOND CHANGE: update the table-------#
    ans = 1 + min
    table[n] = ans
    return ans #include the coin picked up to make the kid





def change_tab(n, table):
    index = 5 #smallest unsolved value of n

    while index <= n:
        #look back to query the table to the earlier solved subproblems
        a = table[index - 4]
        b = table[index -3]
        c = table[index -1]

        #compare
        least = a
        if b < least:
            least = b
        if c < least:
            least = c

        ans = 1 + least
        table[index] = ans

        index += 1
    
    #break the loop, I'm done
    return table[n]












#Should slow down considerably at n = 40
def main():
    n = 100
    #ans = change(n)
    #print(f"NAIVE: The least exact change has {ans} coins.")

    table = [-1] * (n+1)
    table[1] = 1
    table[2] = 2
    table[3] = 1
    table[4] = 1

    ans2 = change_memo(n,table)
    print(f"MEMO: LEC is {ans2}")

    ans3 = change_tab(n, table)
    print(f"TAB: LEC is {ans3}")

main()