'''
Write a loop that counts down from 10 to 1. At each iteration it should print:

NUM...

Where NUM is the current number in the countdown. However, when NUM is 1, it should instead print:

NUM... Blastoff!"
'''

for i in range(10, 0, -1):
    if i == 1:
        print(f"{i}... Blastoff!")
    else:
        print(f"{i}")
