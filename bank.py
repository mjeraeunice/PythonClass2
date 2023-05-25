class Account:

    bank = "KCB"
    def __init__(self,account_number,withdrawals,deposits,loan_balance,balance):
        self.account_number = account_number
        self.deposits=[]
        self.withdrawals=[]
        self.loan_balance=0
        self.balance=0
    #Add a method check_balance which returns the account’s balance
    def check_balance(self):
        self.amount_deposited=2000
        self.amount_withdrawn=1200
        self.account_balance=self.deposits*self.amount_deposited-self.withdrawals*self.amount_withdrawn
        return self.account_balance
    #Update the deposit method to append each withdrawal transaction to the deposits list. Each transaction should be in form of a dictionary like this  
    #{"amount": amount,"narration": “deposit”}
    def open_account(self):
        return f"Nate opened a {self.bank} account {self.account_number} and deposited {self.deposit}ksh"
    def deposit(self,amount):
        self.balance += amount
        self.deposits.append({"amount": amount, "narration": "deposit"})
        return f"Deposit of {amount} successful"
    
#Update the withdrawal method to append each withdrawal transaction to the withdrawals list. Each transaction should be in form of a dictionary like like this 
#{"amount": amount,"narration": “withdrawal”}
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.withdrawals.append({"amount": amount, "narration": "withdrawal"})
            return f"Withdrawal of {amount} was successful"
        else:
            return "Insufficient balance"
#Add a new method  print_statement which combines both deposits and withdrawals into one list and, using a for loop, prints each transaction in a new line like this
#deposit - 100 withdrawal - 500
    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")

#Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
#Account has no outstanding loan
#Loan amount requested is more than 100 Customer has made at least 10 deposits.
#Amount requested is less than or equal to 1/3 of their total sum of all deposits.
#A successful loan increases the loan_balance by requested amount
    def borrow_loan(self):
        self.sum_deposits=self.deposits*self.amount_deposited
        self.loan_requested=8000
        if self.loan_balance=0:
            return (f" The customer can borrow")
        elif self.loan_requested>100 and 1/3*self.sum_deposits:
            return(f" The Customer can borrow")
        elif self.deposits>=10:
            return (f"The customer can borrow")
        print self.loan_balance+=self.loan_requested

#Add a repay_loan method with this functionality.A customer can repay a loan to reduce the current loan_balance
#Overpayment of a loan increases the accounts current balance
    def repay_loan(self):
        self.loan_repay=4500
        print(f"{self.loan_balance}-{self.loan_repay} is the
        current loan balance and the current account balance is
        {self.loan_repay}-{self.loan_balance}+{self.account_balance}")

#Add a transfer method which accepts two attributes (amount and instance of another account). 
# If the amount is less than the current instances balance, the method transfers the requested amount from the current account to the passed account. The transfer is accomplished by reducing the current account balance and depositing the requested amount to the passed account
    def transfer(self, amount, destination_account):
        if amount <= sum(self.deposits):
            self.withdrawal(amount)
            destination_account.deposit(amount)
            return "Transfer successful."
        else:
            return "Insufficient funds for transfer."
