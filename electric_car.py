from car_import import Car
#电池类
class Battery():
	def __init__(self,battery_size=70):
		self.battery_size = battery_size
	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + " -kMh battery.")
	def get_range(self):
		"""打印一条消息，指出电瓶的续航里程"""
		if self.battery_size == 70:
			range_mile = 240
		elif self.battery_size == 85:
			range_mile = 270
		else:
			range_mile = 0
		message = "This car can go approximately " + str(range_mile) + " miles on a full charge."
		print(message)

#类的继承
class ElectricCar(Car):
	"""电动车的独特之处"""
	def __init__(self,make,model,year):
		"""初始化父的属性,调用父类的__init__方法"""
		super().__init__(make,model,year)
		"""电池实例作为电动车的特有属性"""
		self.battery = Battery()
	"""定义子类特有的方法"""
	def reset_battery(self):
		self.battery.battery_size = 0
	"""重写父类的方法get_descripitve_name"""
	def get_descripitve_name(self):
		long_name = str(self.year) + " " + self.make
		return long_name