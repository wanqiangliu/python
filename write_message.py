#写入文件
file_name = 'programming.txt'
with open(file_name,'w') as file_object:
	file_object.write("I love programming")
#写入多行 由于write不会自动加换行所以需要在每行写入的内容后面加\n
with open(file_name,'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I cearteing new games.\n")
#追加到文件末尾
with open(file_name,'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")