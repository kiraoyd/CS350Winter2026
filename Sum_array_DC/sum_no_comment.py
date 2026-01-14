def sum_array_dc(array, start, end):
    if start == end: 
        return array[start] 
    mid = (start + end) // 2 
    left_sum = sum_array_dc(array, start, mid) 
    right_sum = sum_array_dc(array, mid+1, end)
    return left_sum + right_sum 

