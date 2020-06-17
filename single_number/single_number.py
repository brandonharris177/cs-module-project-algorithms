'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    count = 1
    newArray = []
    while len(newArray) == 0:
        # print(arr[0], arr[count])
        if count >= len(arr):
            newArray.append(arr[0])
        elif arr[0] == arr[count]:
            # print("fired", arr[0], arr[count])
            arr.pop(count)
            arr.pop(0)
            # print(arr)
            count = 1
        else:
            count = count+1
 
    # print(newArray)
    return newArray[0]
        
# single_number([1, 1, 2, 2, 3, 4, 4])


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")