'''
Complete the purchase function. If the customer doesn't have enough money raise an exception with the text "not enough money".

Otherwise, return the amount of money the customer has leftover after completing the purchase.
'''

def purchase(price, money_available):
    if price > money_available:
        raise Exception("not enough money")
    else:
        print(money_available)


# Don't edit below this line


def test(price, money_available):
    try:
        print(f"Attempting to purchase an item for ${price} with ${money_available}")
        leftover = purchase(price, money_available)
        print(f"Success! There is ${leftover} leftover")
    except Exception as e:
        print(f"Purchase exception: {e}")
    print("---")


test(10.00, 20.00)
test(30.00, 20.00)
test(15.10, 15.10)
test(1430.00, 69.00)
