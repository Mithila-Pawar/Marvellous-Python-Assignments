class BankAccount:
    ROI = 10.5  

    def __init__(self):
        self.Name = input("Enter account holder's name: ")
        self.Amount = float(input("Enter initial amount: "))

    def Display(self):
        print(f"Name: {self.Name}")
        print(f"Amount: {self.Amount:.2f}")

    def Deposit(self):
        deposit_amount = float(input("Enter amount to deposit: "))
        self.Amount += deposit_amount
        print(f"Deposited {deposit_amount:.2f}. Updated balance: {self.Amount:.2f}")

    def Withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount > self.Amount:
            print("Insufficient funds.")
        else:
            self.Amount -= withdraw_amount
            print(f"Withdrew {withdraw_amount:.2f}. Updated balance: {self.Amount:.2f}")

    def CalculateIntrest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Calculated Interest: {interest:.2f}")
        return interest

print("\nAccount 1")
account1 = BankAccount()
account1.Display()
account1.Deposit()
account1.Withdraw()
account1.CalculateIntrest()
account1.Display()

print("\nAccount 2")
account2 = BankAccount()
account2.Display()
account2.Deposit()
account2.Withdraw()
account2.CalculateIntrest()
account2.Display()
