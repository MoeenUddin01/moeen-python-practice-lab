from account import BankAccount

def main():
    print("_----- welcome to the bank app ------")
    my_account=BankAccount("Moeen Uddin",200)
    print (my_account.get_balance())
    print(my_account.deposit(1000))
    print(my_account.get_balance())
    return main


if __name__=="__main__":
    main()