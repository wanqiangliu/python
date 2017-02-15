def describe_pet(animal_type,pet_name):
	"""显示宠物的信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#位置实参保证实参的顺序和形参的顺序一样
describe_pet('hamster','harry')
describe_pet('dog','beibei')

#关键字实参,实参的顺序无关紧要
describe_pet(animal_type='cat',pet_name='jerry')
describe_pet(pet_name='jerry',animal_type='cat')

#函数定义时使用默认值,有默认值的形参要放到没默认值的形参后面
def describe_pet2(pet_name,animal_type='dog'):
	"""显示宠物的信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#使用默认值
describe_pet2('bei~')
#不使用默认值
describe_pet2('zhazha','bird')
describe_pet2(pet_name='zhazha',animal_type='bird')
describe_pet2('zhazha',animal_type='bird') #位置实参+关键字实参可以
#describe_pet2(pet_name='zhazha','bird')   #关键字实参+位置实参不可以


