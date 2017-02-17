class Usr():
	def __init__(self):
		self.login_attempts = 0

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

	def read_login_attempts(self):
		print("Now haved attempt " + str(self.login_attempts) + ".")
new_user = Usr()
for i in range(0,10):
	new_user.increment_login_attempts()
new_user.read_login_attempts()
new_user.reset_login_attempts()
new_user.read_login_attempts()


