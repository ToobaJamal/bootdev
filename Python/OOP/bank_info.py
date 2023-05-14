'''
Challenge
Complete the BankAccount class.

Constructor
Initialize private class variables __account_number to account_number, and __balance to initial_balance.

Public getters
Define getter methods get_account_number, and get_balance that return the values of the private variables.

deposit method
It should accept an amount as input and add it to the account balance.

withdraw method
It should accept an amount and check if there is enough money in the account for the withdrawal.

If there are not enough funds it should raise a ValueError exception with the message "Insufficient funds". Otherwise, it should deduct the amount from the balance.
'''

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient funds")
