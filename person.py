#函数返回字典
def person(fisrt_name,last_name):
	"""返回一个字典，其中包含有关一个人的信息"""
	person = {'first':fisrt_name,'last':last_name}
	return person

musician = person('wanqiang','liu')
print(musician)

#函数返回字典并结合可选值使用
def person2(fisrt_name,last_name,age=''):
	person = {'fisrt':fisrt_name,'last':last_name}
	if age:
		person['age'] = age
	return person

musician = person2('wanqiang','liu')
print(musician)
musician = person2('wangqiang','liu',26)
print(musician)

