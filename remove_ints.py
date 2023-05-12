'''
Write a function called remove_nonints() that removes all the non-integer types from an array.
'''

def remove_nonints(nums):
    non_ints = []
    for i in nums:
        if type(i) != int:
            non_ints.append(i)
    return non_ints
