print("You can enter 'q' to end the program.")
file_name = 'guest_book.txt'
with open(file_name,'w') as file_object:
	pass
while True:
	guest_name = input("Please enter your name: ")
	if guest_name == 'q':
		break
	else:
		text = ''
		print("Hello, " + guest_name)
		text = guest_name + " is comming.\n"
		with open(file_name,'a') as file_object:
			file_object.write(text)