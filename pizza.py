#传递任意数量的实参，形参为一个元组
def make_pizza(*toppings):
	"""概述要制作的披萨"""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
#结合使用位置实参和任意数量实参
def make_pizza2(size,*toppings):
	"""概述要制作的披萨"""
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

make_pizza2(14,'pepperoni')
make_pizza2(16,'mushrooms','green peppers','extra cheese')