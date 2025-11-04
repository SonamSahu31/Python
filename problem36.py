#create account class with 2 attributes - balance & account no. 
#create method for debit, credit & printing the balance.

class account:
    def __init__(self , bal, acc):
        self.balance = bal   #attribute
        self.account_no = acc   #attribute

        
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debit")
        print("total balance = ", self.get_balance())

    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credit")
        print("total balance = ", self.get_balance())

    
    def get_balance(self):
        return self.balance

acc1 = account(100000 , 1234)
# print("Your bank balance : ",acc1.balance)
# print("Your account number : ",acc1.account_no) 
acc1.debit(1000)
acc1.credit(500)       