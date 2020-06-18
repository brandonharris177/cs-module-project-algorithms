'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     # Your code here

#     length = len(arr)
#     new_arr = [0] * length
#     count = 0

#     for value in arr:
#         if value != 0:
#             new_arr[count] = value
#             count = count +1

#     # print(new_arr)
#     return new_arr

# # moving_zeroes([0, 3, 1, 0, -2])

# if __name__ == '__main__':
#     # Use the main function here to test out your implementation
#     arr = [0, 3, 1, 0, -2]

#     print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

def moving_zeroes(arr):
    start = 0
    end = len(arr)-1

    while start < end:
        if arr[end] == 0:
            end -=1
        elif arr[start] != 0:
            start +=1
        elif arr[start] == 0 and arr[end] != 0:
            arr[start], arr[end] = arr[end], arr[start]
            end -=1
            start +=1
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")