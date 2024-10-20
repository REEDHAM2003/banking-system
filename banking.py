class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount:.2f}. Current balance: {self.balance:.2f}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew {amount:.2f}. Current balance: {self.balance:.2f}")
        else:
            print("Insufficient balance or invalid amount!")

    def check_balance(self):
        print(f"Current balance: {self.balance:.2f}")

def create_account():
    account_number = input("Enter your account number: ")
    account_holder = input("Enter your name: ")
    return BankAccount(account_number, account_holder)

def main():
    print("Welcome to the Banking System")
    account = None
    
    while True:
        print("\n1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            account = create_account()
            print(f"Account created for {account.account_holder} with account number {account.account_number}")
        elif choice == '2':
            if account:
                try:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                except ValueError:
                    print("Please enter a valid amount!")
            else:
                print("No account found! Please create an account first.")
        elif choice == '3':
            if account:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Please enter a valid amount!")
            else:
                print("No account found! Please create an account first.")
        elif choice == '4':
            if account:
                account.check_balance()
            else:
                print("No account found! Please create an account first.")
        elif choice == '5':
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
