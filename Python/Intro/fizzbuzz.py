'''
Write a program from scratch that loops over all the numbers from 1-99 inclusive and prints them. 
If the number is a multiple of 3, instead of printing the number, print "fizz". If the number is a multiple of 5, instead print "buzz". 
If it is a multiple of 3 and 5 then instead print "fizzbuzz".
'''

for i in range(1, 100):
    if i%3 == 0:
        print("fizz")
    elif i%5 == 0:
        print("buzz")
    elif i%3 == 0 and i%5 == 0:
        print("fizzbuzz")
    else:
        print(i)
