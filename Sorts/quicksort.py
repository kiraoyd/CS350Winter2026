def quicksort(array, start, end):
    if start >= end:
        return
    pivot_spot = partition(array, start, end)
    quicksort(array, start, pivot_spot-1) #left
    quicksort(array, pivot_spot+1, end) #right

#Lamuto's Partition
def partition(array, start, end):
    index =  start #not 0, could be any subarray
    pivot_spot = start
    pivot_val = array[end]
    while index < end:
        if array[index] <= pivot_val:
            #swap to behind pivot_spot
            temp = array[index]
            array[index] = array[pivot_spot]
            array[pivot_spot] = temp
            #increment pivot spot with swap
            pivot_spot += 1
        #increment index, it processes all data except pivot val
        index += 1

    #loop breaks, swap pivot val into place
    array[end] = array[pivot_spot]
    array[pivot_spot] = pivot_val

    #now the pivot_val is in the correct sorted spot
    return pivot_spot #need it's location to split on


