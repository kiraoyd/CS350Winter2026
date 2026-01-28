#HELPER FUNCTION
#Prints a 2D matrix cleanly in Python (thanks chatGPT)
def print_table(table):
    # Convert everything to strings
    str_table = [[str(item) for item in row] for row in table]

    # Find the max width of any cell
    max_width = max(len(item) for row in str_table for item in row)

    for row in str_table:
        print(" ".join(item.center(max_width) for item in row))


def nchoose(n,k):
    if n == k:
        return 1
    if k == 1:
        return n
    #probably redundant
    # if k == 0:
    #     return 1
    # if n == 0:
    #     return 1

    return nchoose(n-1, k-1) + nchoose(n-1, k)

def nchoose_memo(n,k, table):
    if table[n][k] != -1:
        #solved!
        return table[n][k]
    
    #otherwise, solve it!
    if n == k:
        return 1
    if k == 1:
        return n
    
    ans = nchoose_memo(n-1,k-1, table) + nchoose_memo(n-1, k, table)
    #add my answer to the table
    table[n][k] = ans
    return ans

def nchoose_tab(n,k,table):
    #Handle edge cases
    if n == k:
        return 1
    if k == 1:
        return n

    #----Initialize table with base case values---#
    #0 col
    col = 0
    row = 0
    row_max = n
    while row <= row_max:
        table[row][col] = 1
        row +=1

    #diagonal
    row = 0
    col = 0
    col_max = k
    while col <= col_max:
        table[row][col] = 1
        row += 1
        col += 1

    #-----Begin iterative Tabulation-----#
    #smallest unsolved subproblem, starts at 2 choose 1 thanks to base cases
    #is represented by n_row = 2, k_col = 1
    result = 0
    k_col = 1

    #Move from the smallest unsolved subproblem...
    #...down the rows of one entire column, then move on to the next column
    
    #iterate across the columns 
    while k_col <= k:
        n_row = 2
        #iterate down the rows
        while n_row <= n:
            table[n_row][k_col] = table[n_row-1][k_col-1] + table[n_row-1][k_col]
            n_row += 1
        k_col += 1

    #n_row and k_col go out of bounds, just use n and k to find the answer
    return table[n][k]
    

def main():
    #Try it on big values for n and k!
    #Memoized and Tabulated will run FAST
    #naiive, if uncommented, will get stuck
    n = 5
    k = 3

    #Naiive Recusrive call below:
    #ans = nchoose(n,k)
    #print(ans)

    table = [[-1]*(k+1) for _ in range(n+1)] #generates the matrix
    print(f"Memoized solution: {nchoose_memo(n,k, table)}")
    print_table(table)

    #Create new table for Tabulation
    tab_table = [[0]*(k+1) for _ in range(n+1)]
    print(f"Tabulated solution: {nchoose_tab(n,k, tab_table)}")
    print_table(table)

main()

    