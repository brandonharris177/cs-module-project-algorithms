'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     # Your code here
#     if n == 0:
#         return 1
#     if n < 0:
#         return 0

#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 2

#     print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


def eating_cookies(n, cache=None):
    # Your code here
    print(n)
    print("cache at top", cache)
    if n == 0:
        return 1
    if n < 0:
        return 0
    if cache is None:    
        cache = {}
    if n in cache:
        print("cache", cache[n])
        return cache[n]

    print("n", n)
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4
    print(eating_cookies(num_cookies))
    # print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")