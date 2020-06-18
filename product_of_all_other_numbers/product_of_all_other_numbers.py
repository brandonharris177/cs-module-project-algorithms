'''
Input: a List of integers
Returns: a List of integers
'''
# def product_of_all_other_numbers(arr):
#     # Your code here
#     new_list = []
#     total_product = 1
#     for x in arr: 
#         total_product = total_product * x  

#     for value in arr:
#         new_list.append(int(total_product/value))

#     # print(new_list)
#     return new_list

# # product_of_all_other_numbers([1, 2, 3, 4, 5])

# # product_of_all_other_numbers([2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8])

# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     # arr = [1, 2, 3, 4, 5]
#     arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

#     print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

# def product_of_all_other_numbers(arr):
#     # Your code here
#     new_list = [0] * len(arr)
#     count = 0

#     total_product = 1
#     for x in arr: 
#         total_product = total_product * x  

#     while count < len(arr):
#         new_list[count] = int(total_product/arr[count])
#         count += 1



#     # print(new_list)
#     return new_list

# # product_of_all_other_numbers([1, 2, 3, 4, 5])

# # product_of_all_other_numbers([2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8])

# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     arr = [1, 2, 3, 4, 5]
#     # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

#     print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

# def product_of_all_other_numbers(arr):
#     # Your code here
#     new_list = [0] * len(arr)
#     count = 0


#     for x in arr: 
#         left_arr = arr[0: x-1] 
#         right_arr = arr[x+1: len(arr)-1] 
#         total_product_left = 1
#         total_product_right = 1
#         for value in left_arr: 
#             total_product_left = total_product_left*value 
#         for num in right_arr: 
#             total_product_right = total_product_right*num 
#         x = total_product_left * total_product_right
        

#     # print(new_list)
#     return new_list

# # product_of_all_other_numbers([1, 2, 3, 4, 5])

# # product_of_all_other_numbers([2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8])

# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     arr = [1, 2, 3, 4, 5]
#     # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

#     print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")


def product_of_all_other_numbers(arr):
    r = [1]*len(arr)
    x = 1
    for i in range(1, len(arr)):
        r[i]=r[i-1]*arr[i-1]
    for j in range(int(len(arr))-1, 0, -1):
        x=x*arr[j]
        r[j-1]=x*r[j-1]

    # print(r)
    return r

product_of_all_other_numbers([1, 2])