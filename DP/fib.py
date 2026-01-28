#naiive recursive
# Big O (2^n)
def fib(n):
    if n == 0 or n == 1:
        return n
    ans = fib(n-1) + fib (n-2)
    return ans

# Memoized version
# Big O (n)
def fib_memo(n, array):
    #Is this n already solved?
    if array[n] != -1:
        return array[n]
    #if not, solve it
    ans = fib_memo(n-1, array) + fib_memo(n-1, array)
    array[n] = ans #add my answer to array
    return ans #give my answer to my parent

def fib_tab(n, table):
    index = 2
    while index <= n:
        table[index] = table[index -1] + table[index - 2]
        index += 1
    print(table) #should be full of answers

    return table[n]

def main():
    n = int(input())
    array = [-1] * (n+1) #generate solution array
    #populate known base case solution values
    array[0] = 0
    array[1] = 1
    
    #ans = fib_memo(n, array)
    ans = fib_tab(n, array)
    print(f"The {n} fibonacci number is: {ans}")

main()
