import json

def get_stored_username():
	file_name = 'username.json'
	try:
		with open(file_name) as file_object:
			username = json.load(file_object)
	except FileNotFoundError as e:
		return None
	else:
		return username

def get_new_username():
	username = input("Please input your name: ")
	file_name = 'username.json'
	with open(file_name,'w') as file_object:
		json.dump(username,file_object)
		return username

def guest_user():
	username = get_stored_username()
	if username:
		msg = input("Is your name is " + username + "? (Y/N)")
		if msg.lower() == 'y':
			print("Welcome back, " + username + "!")
		else:
			username = get_new_username()
	else:
		username = get_new_username()
		print("We'll remeber you when you come back, " + username + "!")

guest_user()