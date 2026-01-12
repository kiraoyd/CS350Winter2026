def selection_sort(array, n):
    start = 0
    #iterate each position in the array, to place the right value
    while start < n:
        index = start + 1
        min_loc = start
        #iterate remaining data, find location of min value
        while index < n:
            if array[min_loc] > array[index]:
                min_loc = index
            index += 1
        
        #swap min value found to correct position
        temp = array[start]
        array[start] = array[min_loc]
        array[min_loc] = temp

        start += 1

    #sorted!

def main():
    array = [8, 4, 1, 2, 3, 6, 7, 5]
    size = len(array)
    selection_sort(array, size)
    print(f"Sorted: {array}")

main()