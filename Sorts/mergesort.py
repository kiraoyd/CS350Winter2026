#Recursive Divide and Conquer
#Works on the original input array
#using temp arrays at each recusive step
#O(n lgn) time complexity:
#work of merge over n, times height of recursive tree
def merge_sort(array, low, high):
    if low >= high:
        return

    mid = (low + high) // 2 #always splits down the middle
    merge_sort(array, low, mid) #left, carry mid with
    merge_sort(array, mid+1, high) #right

    #once the children return from sorting their left/right subarrays
    #merge them together!
    merge(array, low, mid, high)
    

#merge needs low, mid, high to establish the bounds of the parent array
#and to split that array, based on index, into the two subsarrays that 
#were sorted by this parents left and right kids
#Remember, we do the merge n the return...
#...relying that the kids already finished their sorting work
def merge(array, low, mid, high):
    temp = [] #an array to sort into

    #set pointers to distinguish the left/right subarrays
    a = low #start of the left child, ends at mid
    b = mid+1 #start of the right child, ends at high

    #loop, process both subarrays
    #as long as a and b are both in bounds of their subarrays...
    while a <= mid and b <= high:
        if array[a] <= array[b]:
            #left has the smallest data (or equal), add it
            temp.append(array[a])
            a += 1 #advance a to the next data item
        elif array[a] > array[b]:
            #right has the smallest data, add it
            temp.append(array[b])
            b += 1 #advance b to the next data item

    #Once this loop breaks, one of the subarrays is
    #fully processed, but it won't always be the same one

    #if it's the left subarray that still has data...
    #...a will be <= mid
    while a <= mid:
        temp.append(array[a])
        a += 1

    #if it's the right subarray that still has data...
    #... b will be <= high
    while b <= high:
        temp.append(array[b])
        b += 1

    #now everything is in temp, sorted, time to COPYBACK to original array
    temp_index = 0 #scan the temp array from start
    copy_to = low #start of the ACTUAL input array
    while temp_index < len(temp):
        array[copy_to] = temp[temp_index]
        copy_to += 1
        temp_index += 1



def main():
    test = [4,5,4,2,3,10,1,4,100]
    size = len(test)
    merge_sort(test, 0, size-1)
    print(test)

main()