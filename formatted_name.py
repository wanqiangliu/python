#函数返回值的使用
def get_formatted_name(fist_name,last_name):
	"""返回整洁的名字"""
	full_name = fist_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('wanqiang','liu')
print(musician)

#函数形参中设置可选值让函数调用更灵活,中间名字在函数调用中如果有则以实参传入，如果没有则可以不传
def get_formatted_name2(fist_name,last_name,middle_name=''):
	if middle_name:
		full_name = fist_name + ' ' + middle_name + ' ' + last_name
		return full_name.title()
	else:
		full_name = fist_name + ' ' + last_name
		return full_name.title()

musician2 = get_formatted_name2('wangqiang','liu','qiang')
print(musician2)
musician3 = get_formatted_name2('wangqiang','liu')
print(musician3)