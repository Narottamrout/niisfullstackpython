class account:
	def __init__(self,accountno,balance,amount):
		self.accountno=accountno
		self.balance=balance
		self.amount=amount
	def debit(self):
		print("debit",self.balance-self.amount)
	def credit(self):
		print("credit",self.balance+self.amount)	
s1=account(123456,10000,5000)
s1.debit()
s1.credit()		