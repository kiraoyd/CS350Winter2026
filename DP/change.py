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

#Should slow down considerably at n = 40
def main():
    n = 10
    ans = change(n)
    print(f"The least exact change has {ans} coins.")

main()