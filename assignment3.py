class Bank_account:
    def __init__(self, firstName, lastName, middleName, account_type, balance):
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName
        self.account_type = account_type
        self.balance = balance
        self.status = "Open"

    def whithdraw(self, amount):
        self.balance = self.balance - amount

    def positive_transfer(self, other_account, amount):
        other_account.balance = other_account.balance - amount
        self.balance = self.balance + amount
        print("Your balance in this account is: {0}".format(self.balance))

    def negative_transfer(self, other_account, amount):
        other_account.balance = other_account.balance + amount
        self.balance = self.balance - amount
        print("Your balance in this account is: {0}".format(self.balance))

    def overdraft():
        if self.balance < 0:
            self.balance = self.balance - 35

    def __repr__(self):
        return "Name = {0} {1} {2}\nAccount type = {3} \nBalance = {4}\nStatus = {5}".format(self.firstName, self.middleName, self.lastName, self.account_type, self.balance, self.status)

user1 = Bank_account("John", "Doe", "Michael", "Checking", 100)
user2 = Bank_account("John", "Doe", "Michael", "Saving", 400)

user2.negative_transfer(user1, 30)
