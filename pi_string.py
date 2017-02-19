#将文件中的内容拼接成字符串并打印
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
	lines = file_object.readlines()

#变量在使用前必须先定义 
pi_string = ''
for line in lines:
	pi_string += line.strip()
print(pi_string,len(pi_string))
