#create account class with two attributes-balance and account number
#create method for debit credit and print
class account:
	def __init__(self,balance,accountno):
		self.balance=balance
		self.accountno=accountno
	def debit(self,amount):
		self.balance=self.balance-amount
		print("debited",amount)
	def credit(self,amount):
		self.balance=self.balance+amount
		print("credited",amount)
	def printbalance(self):
		print("accountno",self.accountno)
		print("balance",self.balance)
s1=account(50000,8984781826)
s1.debit(5000)
s1.credit(4000)
s1.printbalance()				

