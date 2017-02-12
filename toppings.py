#if中!=的使用
requested_topping = 'mushrooms'
if requested_topping != "mushrooms":
	print("Hold the anchovies!")
else:
	print("Please Hold the mushrooms as soon as possible!")
#检查列表中的特殊元素
requested_toppings = ['mushroom','green peppers','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry,we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!") 

#确定列表是否为空 如果为空执行else中的语句,非空执行if中的语句
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
else:
	print("\nAre you sure you want a plain pizza!")

print("\n")
#使用多个列表
available_toppings = ['mushroom','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushroom','french fries','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry,we don't have " + requested_topping + '.')
print("\nFinished making your pizza!")
