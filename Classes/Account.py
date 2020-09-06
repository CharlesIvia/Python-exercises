class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
            return f"Account owner: {self.owner} \nAccount balance: {self.balance}"

    def deposit(self, dep_amt):
        self.balance = self.balance + dep_amt
        print(f"A deposit of {dep_amt} was accepted.")

    def withdraw(self, wd_amt):
        if self.balance < wd_amt:
            print("You do not have enough money.")
        else:
            self.balance = self.balance - wd_amt
            print(f"You have withdrawn {wd_amt} from your account!")
