#通过运用标志来退出while循环
prompt = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
	message = input(prompt)
	if message != 'quit':
		print(message)
	else:
		active = False
