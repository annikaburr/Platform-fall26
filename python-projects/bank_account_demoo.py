from bank_account import BankAccount

account = BankAccount("1234", 100)
print(account)

def deposit(self, amount):
    self.balance += amount


def withdrawl(self, amount):
    if self.balance >= amount:
        self.balance -= amount


def get_balance():
    return self.balance
