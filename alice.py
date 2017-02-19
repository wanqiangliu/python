#read()返回字符串，split返回列表
def count_words(file_name):
	try:
		"""计算文件中大致包含多少个单词"""
		with open(file_name) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + file_name + " does not exitst."
		print(msg)
	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + file_name + " has about " + str(num_words) + " words.")

filenames = ['alice.txt','a.txt','guest_book.txt']
for filename in filenames:
	count_words(filename)