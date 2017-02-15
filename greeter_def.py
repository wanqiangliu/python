#结合函数与while循环使用
def get_name(first_name,last_name):
	"""返回整洁的名字"""
	full_name = first_name + ' ' + last_name
	return  full_name.title()

while True:
	print("\nPlease enter your First Name:")
	print("(Enter 'q' at anytime to quit)")
	first_name = input("First Name: ")
	if first_name == 'q':
		break
	last_name = input("Last Name: ")
	if last_name == 'q':
		break
	format_name = get_name(first_name,last_name)
	print("Hello, " + format_name + "!")