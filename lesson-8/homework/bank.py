class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance


class Bank:
    def __init__(self, filename):
        self.filename = filename
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = str(len(self.accounts) + 1)
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        return account_number

    def view_account(self, account_number):
        return self.accounts.get(account_number, None)

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].balance += amount
            self.save_to_file()

    def withdraw(self, account_number, amount):
        if account_number in self.accounts and self.accounts[account_number].balance >= amount:
            self.accounts[account_number].balance -= amount
            self.save_to_file()

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            for acc in self.accounts.values():
                file.write(f"{acc.account_number},{acc.name},{acc.balance}\n")

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    account_number, name, balance = line.strip().split(',')
                    self.accounts[account_number] = Account(account_number, name, float(balance))
        except FileNotFoundError:
            pass

    def menu(self):
        while True:
            print("\nBank Application")
            print("1. Create Account")
            print("2. View Account")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter Name: ")
                initial_deposit = float(input("Enter Initial Deposit: "))
                account_number = self.create_account(name, initial_deposit)
                print(f"Account created successfully! Account Number: {account_number}")
            elif choice == '2':
                account_number = input("Enter Account Number: ")
                account = self.view_account(account_number)
                if account:
                    print(f"Account Details: {account.account_number}, {account.name}, {account.balance}")
                else:
                    print("Account not found.")
            elif choice == '3':
                account_number = input("Enter Account Number: ")
                amount = float(input("Enter Deposit Amount: "))
                self.deposit(account_number, amount)
                print("Deposit successful!")
            elif choice == '4':
                account_number = input("Enter Account Number: ")
                amount = float(input("Enter Withdrawal Amount: "))
                self.withdraw(account_number, amount)
                print("Withdrawal successful!")
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    bank = Bank("accounts.txt")
    bank.menu()
