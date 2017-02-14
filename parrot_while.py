#直接通过输入的值来退出，拓展性不好message != 'quit' and message1 != 'quit' and message2 != 'quit' 
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
	#避免退出时打印quit
	if message != 'quit':
		print(message)