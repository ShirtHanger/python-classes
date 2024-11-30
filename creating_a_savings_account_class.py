import random

from creating_a_bank_account_class import *

class Savings_Account(Bank_Account):
    # add additional parameters AFTER those in the superclass
    def __init__(self, owner, balance=0, has_overdraft=False):
        # always call the superclass's __init__ first
        Bank_Account.__init__(self, owner, balance, has_overdraft)
        # No new methods/attributes this time

        
    def withdraw(self):
        print(f'No withdrawals permitted, {self.owner}, this is a savings account')
 
 
sierra_knox = Savings_Account("Sierra", 1000)

sierra_knox.withdraw()