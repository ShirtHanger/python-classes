import random

class Bank_Account():
    # Adds an ID to each instance of a class, could be useful for APIs and databases
    new_account_no = random.randint(111111111, 999999999)
    total_accounts = 0

    def __init__(self, owner, balance=0, has_overdraft=False):
        
        self.owner = owner
        self.balance = balance
        self.has_overdraft = has_overdraft
        self.account_no = Bank_Account.new_account_no
        
        Bank_Account.new_account_no = random.randint(111111111, 999999999)
        Bank_Account.total_accounts += 1

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}'s new balance is ${self.balance}")
        
    def withdraw(self, amount): 
        if self.has_overdraft == False and (self.balance - amount < 0):
            print(f"{self.owner}. Your balance is ${self.balance} and withdrawing more than that {amount} would not work out, just saying")
        else:
            self.balance -= amount
            print(f"{self.owner}'s new balance is ${self.balance}")

    def __str__(self):
        return f'Account <#{self.account_no}>, Balance - ${self.balance}, Owner - {self.owner}.'
    
    # A class method 
    # Returns the number of Bank_Account objects by checking the total_accounts variable

    @classmethod
    def get_total_Bank_Accounts(cls):
        # cls represents the Bank_Account class, used similarly to self above
        return f'We have {cls.total_accounts} Bank_Accounts... so far!'
    
    
alice_seymour = Bank_Account("Alice", 500)
bob_ross = Bank_Account("Bob", 1000)
charlie_woods = Bank_Account("Charlie", 750)
diana_prince = Bank_Account("Diana", 1200)

print(alice_seymour)
# print(bob_ross)
# print(charlie_woods)
# print(diana_prince)


# print(f"Initial balance: ${alice_seymour.balance}") 

# alice_seymour.deposit(250)
# print(f"Balance after deposit: ${alice_seymour.balance}")

alice_seymour.withdraw(1000) 
print(f"Balance after withdrawal: ${alice_seymour.balance}")