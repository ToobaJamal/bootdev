'''
Write a function called number_sum(n) that adds up all the numbers from 1 to n.
'''

def number_sum(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum
