'''
Bank Account
•	Create a class called BankAccount with the following attributes:
        o	account_holder: Name of the account holder.
        o	balance: Account balance (default is 0).
•	Write methods for:
        o	deposit(amount): Adds money to the balance.
        o	withdraw(amount): Deducts money from the balance, ensuring the balance doesn’t go negative.
        o	display_balance(): Shows the current balance.
•	Create an instance of BankAccount, deposit some money, withdraw an amount, and check the balance.

'''

class Bank_acc:
    def __init__(self, acc_holder, balance = 0):
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amount):
        if (amount > 0):
            self.balance += amount
            print(f"The amount deposited is: ${amount}.\n The updated balance in your account is: ${self.balance}")
        else:
            print("The deposited amount must be greater than zero.")

    def withdraw(self, amount):
        if (amount > 0 and amount <= self.balance):
            self.balance -= amount
            print(f"The amount withdrawn is: ${amount}.\n The remaining balance in your account is: ${self.balance}")
        elif (amount > self.balance):
            print("Insufficient funds for withdrawl.")
        else:
            print("The withdrawl amount must be greater than zero.")

    def display_balance(self):
        print(f"The current balance in your account is: ${self.balance}.")

account = Bank_acc("Harsh Shokeen", 9999)

account.deposit(999)

account.withdraw(99)

account.display_balance()