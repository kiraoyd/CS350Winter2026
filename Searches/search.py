def linear_search(array, target, n):
    index = 0
    while index < n:
        #do my work
        if array[index] == target:
            return index
        index += 1

    return -1 #error flag

