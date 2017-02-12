#访问复制的列表、删除原列表
users = ['zhangsan','admin','lisi','wangwu']
for user in users[:]:
	if user == 'admin':
		print("Hello admin,would you like to see a status report?")
	else:
		print("Hello " + user + ",thank you for logging in again")
	users.remove(user)
	if users:
		print("remove:" + user)
	else:
		print("We need to find some users!")
print("-----------------------\n")
#逆序访问 逆序如果用range想访问下标为0的元素则range的第二个参数为-1
users = ['zhangsan','admin','lisi','wangwu']
for i in range(len(users)-1,-1,-1):
	user = users[i]
	if users[i] == 'admin':
		print("Hello admin,would you like to see a status report?")
	else:
		print("Hello " + users[i] + ",thank you for logging in again")
	users.remove(users[i])
	if users:
		print("remove:" + user)
	else:
		print("We need to find some users!")