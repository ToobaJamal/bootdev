'''
Inside the loop, use the modulo operator to check if each number, i, is odd. If a number is odd, append it to the odd_numbers list.
'''

odd_numbers = []

# don't touch above this line

for i in range(0, 300):
    if i % 2 != 0:
        odd_numbers.append(i)

# don't touch below this line

print(odd_numbers)
