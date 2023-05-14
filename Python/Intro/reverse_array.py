'''
Let's write a function that takes an array as input and returns a new array except all the items are in reverse order.
'''

def reverse_array(items):
    return items[::-1]
        
        


# Don't touch below this line


def test(items):
    items_copy = items[:]
    reversed = reverse_array(items)
    print(f"{items_copy} reversed is: {reversed}")


test(["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"])
test(["Haste Potion", "Longsword", "Iron Bar", "Leather Scraps"])
test([1, 2, 300, 4, 5])
test(["now!", "order", "reverse", "in", "is", "Array", "This"])
test(["Kite Shield", "Iron Breastplate", "Healing Potion", "Shortsword"])
