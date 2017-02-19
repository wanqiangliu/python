def count_words(file_name):
	try:
		with open(file_name) as file_object:
			contents = file_object.read()
	except FileNotFoundError as e:
		pass
	else:
		print(file_name + " has " + str(contents.lower().count('the')) + " 'the' words.")

file_names = ['alice.txt','a.txt','guest_book.txt']
for file_name in file_names:
	count_words(file_name)