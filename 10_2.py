file_name = 'learning_python.txt'
with open(file_name,'r') as file_object:
	lines = file_object.readlines()

new_line = ''
for line in lines:
	new_line = line.replace('Python','C++')
	print(new_line)