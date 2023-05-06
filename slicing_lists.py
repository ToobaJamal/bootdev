'''
First, print a slice of the champions list that starts with the third item in the list.
Next, print a slice of the champions list that ends with the third item from the end of the list.
Last, print a slice of the champions list that skips every odd numbered index.
'''

champions = [
    "Thrundar",
    "Morgate",
    "Gandolfo",
    "Thraine",
    "Norwad",
    "Gilforn",
]

# don't touch above this line

print(champions[2:])
print(champions[:4])
print(champions[0:5:2])
