#使用任意数量的关键字实参
def build_profile(first,last,**user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for k,v in user_info.items():
		profile[k] = v
	return profile

user_profile = build_profile('wanqiang','lwq',age=26,field='physics')
print(user_profile)