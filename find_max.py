'''
Our players want a way to see their strongest attack from their last combat.

Let's add another function to analyze data from our combat log.

Complete the find_max function that looks at each number in a list and returns the maximum value. If no maximum is found it just returns negative infinity.
'''

def find_max(nums):
    max_so_far = float("-inf")
    for i in nums:
        if i > max_so_far:
            max_so_far = i
    return max_so_far

# Don't touch below this line


def test(nums):
    max = find_max(nums)
    print(f"The max of {nums} is {max}")


test([1, 2, 3, 4, 5])
test([1, 2, 300, 4, 5])
test([1, 20, 3, 4, 5])
test([-1, 2, 3, 4, 5])
test([1, 2, 3, 21, 18])
test([])
