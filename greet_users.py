#向函数传递列表
def greet_users(users):
	for user in users:
		messeage = "Hello, " + user.title() + "!"
		print(messeage)

usernames = ['hannah','ty','margot']
greet_users(usernames)