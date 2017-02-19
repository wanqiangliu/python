#读取整个文件,未指定文件路径默认在file_reader.py所在的路径查找
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())
#指定路径
path = r'/Users/lwq/python/python_work'
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)

#逐行读取,rstrip()消除因为文件中的换行符导致的空白行而不消除本行原有的空格,只能在with代码段里面使用file_object对象
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
	for line in file_object:
		print(line.rstrip())

#readlines读取文件中的每一行，readline只读取一行，在with代码段外使用文件内容
with open(file_name) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())  #如果用strip会将本行应有的空格也去掉