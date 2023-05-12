'''
Write a function called divide_list() that takes a list and a number as input. 
The function creates a new list that contains all the elements of the original list except they have been divided by the second input.
'''

def divide_list(nums, divisor):
    divided_nums = []
    for i in nums:
        divided_nums.append(i / divisor)
    return divided_nums
