#嵌套的使用
#列表中嵌套字典的应用
aliens = []
#创建30个外星人
for aliens_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
#修改前3个外星人的属性
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['points'] = 15
		alien['speed'] = 'fast'

#显示前5个外星人
for alien in aliens[:5]:
	print(alien)
print("....")
#显示一共创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)) + "\n")

#字典中嵌套列表的应用
#example 1
pizza = {
	'crust' : 'thick',
	'toppings' : ['mushroom','extra cheese'],
}
print("You order a " + pizza['crust'] + "-crust pizza" + 
	"with the following toppings:")
for topping in pizza['toppings']:
	print(topping)
#example 2
favorite_language = {
	'jen' : ['python','ruby'],
	'sarah' : ['c'],
	'edward' : ['ruby','go'],
	'phil' : ['python','haskell'],
}

#就算列表中只有一个元素，想访问这一个元素的值也需要用languages[0],不能直接用languages
for name,languages in favorite_language.items():
	if len(languages) == 1:
		print("\n" + name.title() + 
			"'s favorite language is " + 
			languages[0].title() + ".")
	else:
		print("\n" + name.title() + 
			"'s favorite language are :")
		for language in languages:
			print("\t" + language.title())

#字典中嵌套字典的应用
print("\n")
users = {
	'liuwanqiang' : {
	'first' : 'wanqiang',
	'last' : 'liu',
	'location' : 'beijing',
	},
	'lingjimei' : {
	'first' : 'jimei',
	'last' : 'ling',
	'location' : 'beijing',
	},
}
for username,user_info in users.items():
	print("\nUserName: " + username)
	full_name = user_info['last'] + user_info['first']
	location = user_info['location']

	print("\nFullName: " + full_name)
	print("\tLocation: " + location)