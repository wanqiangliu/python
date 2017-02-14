prompt = "\nPlease enter a topping:"
prompt += "\n(Enter a 'quit' to end the program.) "
topping = ""
while topping != 'quit':
	topping = input(prompt)
	if topping != 'quit':
		print("We will add " + topping + " to the pizza!")