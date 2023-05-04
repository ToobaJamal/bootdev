'''
There are number_of_employees employees, whose IDs are simply the numbers from 0 to number_of_employees - 1. Loop over each employee id and:

If the employee is a C-Level Executive add the c_level_bonus to the dollars_needed.
If the employee is a manager add the manager_bonus to the dollars_needed.
Otherwise, add the standard_bonus to the dollars_needed.
Use the variables given as necessary.
'''

number_of_employees = 102

c_level_bonus = 2000
manager_bonus = 1000
standard_bonus = 500

# C Level Executives
sarah_id = 1
mary_id = 2

# Managers
john_id = 6
bob_id = 44
joe_id = 18

dollars_needed = 0

# Don't touch above this line

for i in range(number_of_employees):
    if i == sarah_id or i == mary_id:
        dollars_needed += c_level_bonus
    elif i == john_id or i == bob_id or i == joe_id:
        dollars_needed += manager_bonus
    else:
        dollars_needed += standard_bonus
    

# Don't touch below this line

print(f"{dollars_needed} dollars are needed to fulfill all bonuses")
