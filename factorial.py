'''
Complete the factorial() function. 
It should calculate the factorial of a number. 
A factorial of a number is the product of all positive integers less than or equal to that number.
'''

def factorial(num):
    factorial = 1
    for i in range(1, num +1):
        factorial *= i
    return factorial
