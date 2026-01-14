def quicksort(array, start, end):
    if start >= end:
        return
    pivot_spot = partition(array, start, end)
    quicksort(array, start, pivot_spot-1) #left
    quicksort(array, pivot_spot+1, end) #right

def partition(array, start, end):
    pass #attempt at homefirst
    # will push full code later this week