#遍历字典中所有的键值对
user_0 = {
	'username' : 'efermi',
	'first' : 'enrico',
	'last' : 'fermi',
	'full_name' : 'efermi',
}
for k,v in user_0.items():
	print("\nKey: " + k)
	print("Value: " + v)
#遍历字典中所有的键(可用以下两种方式显式和隐式)
print("\n")
for k in user_0.keys():
	print(k.title())

for k in user_0:
	print(k.title())
#按顺序遍历字典中所有的键
print("\n")
for k in sorted(user_0.keys()):
	print(k.title())

#遍历字典中所有的值
print("\n")
for v in user_0.values():
	print(v)
#去掉值中的重复项
print("\n")
for v in set(user_0.values()):
	print(v)