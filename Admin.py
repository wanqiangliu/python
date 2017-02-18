class Usr():
	def __init__(self):
		self.login_attempts = 0

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

	def read_login_attempts(self):
		print("Now haved attempt " + str(self.login_attempts) + ".")

class Privileges():
	def __init__(self,privileges):
		self.privileges = privileges

	def show_privileges(self):
		for privilege in self.privileges:
			print(privilege)


class Admin(Usr):
	def __init__(self,privileges=[]):
		"""super必须紧随子类__init__后面，然后再定义子类特有的属性"""
		super().__init__()
		"""权限类作为Admin的属性"""
		self.privileges = Privileges(privileges)


