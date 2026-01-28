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

def main():
    n = 5
    k = 3
    #ans = nchoose(n,k)
    #print(ans)

    table = [[-1]*(k+1) for _ in range(n+1)] #generates the matrix
    print(nchoose_memo(n,k, table))

main()

    