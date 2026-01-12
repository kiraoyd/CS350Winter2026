def linear_search(array, target, n):
    n = len(array)
    index = 0
    while index < n:
        #do my work
        if array[index] == target:
            return index
        index += 1

    return -1 #error flag

#f(n) = 3n + 2 + n
#f(n) = 4n + 2

