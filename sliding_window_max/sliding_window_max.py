'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    count = 0
    new_array = []

    while k < len(nums) + 1:
        # print(count, k)
        new_array.append(max(nums[count: k]))
        count = count+1
        k = k + 1

    # print(new_array)
    return new_array

# sliding_window_max([1, 3, -1], 3)

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
