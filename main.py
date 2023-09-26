class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount} into account {self.__account_number}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount} from account {self.__account_number}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Balance: ${self.__account_balance}")

# Testing the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    account1 = BankAccount("12345", "John Doe", 1000)

    # Display initial balance
    account1.display_balance()

    # Make deposits and withdrawals
    account1.deposit(500)
    account1.withdraw(200)
    account1.withdraw(1500)

    # Display updated balance
    account1.display_balance()