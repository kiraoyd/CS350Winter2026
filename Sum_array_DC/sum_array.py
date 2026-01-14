def sum_array_dc(array, start, end):
    if start == end: #base case
        return array[start] #the data of array size 1, is the sum
    mid = (start + end) // 2 #calculate split point
    #hey kid, solve my left side data
    left_sum = sum_array_dc(array, start, mid) #not mid-1, all data is needed
    #hey kid, solve my right side data
    right_sum = sum_array_dc(array, mid+1, end)
    return left_sum + right_sum #I'll add them together
def main():
    data = [10,4,6,5,2,1]
    size = len(data)
    if size > 0:
        start = 0
        end = size - 1
        total = sum_array_dc(data, start, end)
        print(f"The sum of all data is: {total}")
    else:
        print("No data.")

main()