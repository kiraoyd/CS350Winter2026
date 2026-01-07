#Iterative Version
def binary_search(sorted, target, n):
    start = 0
    end = n -1
    while start <= end:
        mid = (start + end) // 2 #integer divide
        if sorted[mid] == target:
            return mid #found!
        if sorted[mid] < target:
            start = mid + 1 #throws out the left (data too small)
        if sorted[mid] > target:
            end = mid - 1 #throws out the right (data too big)
        
    return -1 #target not found



#Recursive Version
def binary_wrapper(sorted, n, target):
    start = 0
    end = n- 1
    return binary_recursive(sorted, target, start, end)

def binary_recursive(sorted, target, start, end):
    mid = (start + end) // 2
    if sorted[mid] == target:
        return mid
    if sorted[mid] < target:
        return binary_recursive(sorted, target, mid + 1, end) 
        #throws out the left, recursing to the right
    if sorted[mid] > target:
        return binary_recursive(sorted, target, start, mid-1)
        #throws out the right recurses to the left
    return -1

def main():
    array = [8,9,10,11,12]
    target = 12 #should be found at index 4
    target_nope = 100 #should not be found
    size = len(array)
    result = binary_search(array, target, size)
    #Uncomment out the line below, and comment out the line above to run the recursive version
    #result = binary_wrapper(array, size, target)
    if result > 0:
        print(f"The target was found at index {result}")
    else:
        print("The target was not found.")

main()
    




