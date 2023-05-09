'''
Complete the make_purchases function. It accepts a list of dictionaries representing purchase orders. 
You can take a look at the test suite for an example of the shape of the data.

It returns a list of floats representing the amount of money left in each customer's account after completing a purchase. 
The returned list may be smaller because it will only contain the leftover amounts of the customers who were able to successfully complete a purchase.

make_purchases() should create an empty list of "leftovers", and then loop over each order, running the purchase() function for each one. 
If an exception is raised, print:

Purchase exception: ERROR
Where ERROR is the exception's text.
'''

def make_purchases(purchase_orders):
    leftovers = []
    for order in purchase_orders:
        try:
            leftover = purchase(order["price"], order["money_available"])
            leftovers.append(leftover)
        except Exception as e:
            print(f"Purchase exception: {str(e)}")
            continue
    return leftovers



# Don't edit below this line


def main():
    print("Making purchases...")
    leftovers = make_purchases(
        [
            {"price": 10.00, "money_available": 125.00},
            {"price": 5.00, "money_available": 2.00},
            {"price": 20.01, "money_available": 5.20},
            {"price": 1.04, "money_available": 254.00},
            {"price": 40.20, "money_available": 6.00},
            {"price": 16.00, "money_available": 235.01},
            {"price": 10.70, "money_available": 254.10},
            {"price": 12.00, "money_available": 2.30},
        ]
    )
    print("Purchases complete!")
    print("Leftover amounts for successful purchases:")
    for leftover in leftovers:
        print(f" * {leftover:.2f}")


def purchase(price, money_available):
    if money_available < price:
        raise Exception(f"{money_available:.2f} is not enough for {price:.2f}")
    return money_available - price


main()
