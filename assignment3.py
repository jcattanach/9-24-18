# I still need to finish this ASSIGNMENT
#




class Bank_account:
    def __init__(self, firstName, lastName, middleName, account_type, balance, status):
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName
        self.account_type = account_type
        self.balance = balance
        self.status = status

    def __repr__(self):
        return "Name = {0} {1} {2}\nAccount type = {3} \nBalance = {4}\nStatus = {5}".format(self.firstName, self.middleName, self.lastName, self.account_type, self.balance, self.status)


user = Bank_account("John", "Doe", "Michael", "Checking", "100", "Open")

print(user)
