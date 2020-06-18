import math

radius = 3

print(f"{math.pi * radius * radius:.3f}")

# We'll say that a positive int divides itself
# if every digit in the number divides into the
# number evenly.
# So for example 128 divides itself
# since 1, 2, and 8 all divide into 128 evenly. 
# And we'll say that 0 does not divide into anything
# evenly, so no number with a 0 digit divides itself. 
# Write a function to determine if a number divides itself.
# [source - https://codingbat.com/prob/p165941]

#how are we going to parse out the number to consider each element seperatly
#modello seems like a good canidate to solve this probelem

def divides_self(num):

    # condition = True

    # this_list = str(num).split()

    # count = 0

    # for digit in this_list:
    #     while count < len(this_list) or condition != False:
    #         if int(digit) == 0:
    #             condition = False
    #         elif num % int(digit) == 0:
    #             condition = True
    #             count = count + 1
    #         elif num % int(digit) != 0:
    #             condition = False
    
    # if count == len(this_list):
    #     return True
    # else:
    #     return False

    if num == 0:
        return False

    if len(str(num)) == 1:
        return True

    for digit in str(num):
        digit_int = int(digit)
        if digit_int == 0 or num % digit != 0:
            return False
    
    return True


"""notes from 18/06/20"""

