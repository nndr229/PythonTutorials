class Bank:
    def __init__(self,name,initial_deposit):
        try:
            if type(self.name) == type("asdf"):
                self.name = name
                self.initial_deposit = initial_deposit
        except Exception as e:
            print(f"Error -- {name} is not a string!")

    def deposit(self,amount):
        self.initial_deposit += amount

        print(f"Your current balance after the deposit of {amount} is {self.initial_deposit}")
    
    def withdraw(self,amount):
        if amount > self.initial_deposit:
            print(f"Insufficient balance . It is {self.initial_deposit}")
            return 
        self.initial_deposit-=amount

        print(f"Balance is now {self.initial_deposit}")


if __name__ == "__main__":
    b = Bank("Nithin",1000)
    b.deposit(1000)
    print(b.initial_deposit)
    print()
    b.withdraw(2235235235)
    b.withdraw(450)