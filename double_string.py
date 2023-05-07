'''
Complete the double_string function. It takes a string as input and returns a "doubled" version (including spaces!).
'''

def double_string(string):
    doubled_string = ""
    for i in string:
        doubled_string += i*2
    return doubled_string
        


# Don't touch below this line

print(double_string("Hello there"))
print(double_string("General Kenobi"))
print(double_string("I've been trained in your Jedi arts"))
