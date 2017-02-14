active = True
while True:
	age = input("How old are you? ")
	if age == 'quit':
		active = False
	if active == False:
		break;
	else:
		age = int(age)
	if age < 3:
		print("Free!")
	elif age < 12:
		print("You need pay 10$!")
	else:
		print("You need par 15$!")
