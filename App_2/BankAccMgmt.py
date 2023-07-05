'''2.	Bank Account Management: Develop a bank account management system that allows users to create accounts,
deposit and withdraw money, and view their account details. '''

# Below is my code
class Account:
    Account_SrNo = 0

    def __init__(self, username, initialbalance):
        self.acc_no = self.Account_SrNo + 1
        self.username = username
        self.initialbalance = initialbalance

    def add_money(self, username, amount):
        new_balance = username.initialbalance + amount
        username.balance = new_balance
        return username.balance

    def withdraw_money(self, username, amount):
        if username.balance < amount:
            print(f"insufficient balance, your current balance is {username.balance}, Reenter lower amount")
        else:
            new_balance = username.balance - amount
            username.balance = new_balance
        return username.balance

# Here after corrected code by Chat GPT
class Account:
    Account_SrNo = 0

    def __init__(self, username, initialbalance):
        Account.Account_SrNo += 1
        self.acc_no = Account.Account_SrNo
        self.username = username
        self.balance = initialbalance

    def add_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        if self.balance < amount:
            print(f"Insufficient balance. Your current balance is {self.balance}. Please enter a lower amount.")
        else:
            self.balance -= amount

    def view_details(self):
        print(f"Account Number: {self.acc_no}")
        print(f"Username: {self.username}")
        print(f"Balance: {self.balance}")


# Mistakes i did 1) the username need not tobe include in method as these are intance method so
# it is going to use username of account class which is part of constructor
