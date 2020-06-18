'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# def sliding_window_max(nums, k):
#     # Your code here
#     count = 0
#     new_array = []

#     while k < len(nums) + 1:
#         # print(count, k)
#         new_array.append(max(nums[count: k]))
#         count = count+1
#         k = k + 1

#     # print(new_array)
#     return new_array

# # sliding_window_max([1, 3, -1], 3)

# if __name__ == '__main__':
#     # Use the main function here to test out your implementation 
#     arr = [1, 3, -1, -3, 5, 6, 7]
#     k = 3

#     print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")


def sliding_window_max(nums, k):
    # Your code here
    length = len(nums) - k + 1
    new_list = [0] * length
    count = 0

    while k < len(nums) + 1:
        # print(count, k)
        new_list[count] = max(nums[count: k])
        count = count+1
        k = k + 1

    # print(new_array)
    return new_list

# sliding_window_max([1, 3, -1], 3)

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7, 8, 4, 2, 1, 9, 3]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")