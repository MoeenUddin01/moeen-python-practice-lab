

class BankAccount:
    def __init__(self,owner_name,initial_balance=0.0):
        self.owner_name=owner_name
        self.initial_balance=initial_balance


    def deposit(self,amount):
        if amount>0:
            self.initial_balance+=amount
            return self.initial_balance

    def get_balance(self):
        return self.initial_balance


if __name__=="__main__":
    print("testing the app")

    bank1=BankAccount("Moeen",100)

    

    print(bank1.get_balance())

    

    print(bank1.deposit(20))


    print(bank1.get_balance())
