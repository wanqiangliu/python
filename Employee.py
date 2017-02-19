class Employee():
	def __init__(self,name,sale):
		self.name = name
		self.sale = sale
	
	def give_raise(self,increment_sale=5000):
		self.sale += increment_sale
		return self.sale