'''
Write a function called find_min() that finds the smallest number in an array
'''

def find_min(nums):
    min = float("inf")
    for i in nums:
        if i < min:
            min = i
    return min
