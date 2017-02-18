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
	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85

#类的继承
class ElectricCar():
	"""电动车的独特之处"""
	def __init__(self):
		"""电池实例作为电动车的特有属性"""
		self.battery = Battery()

electricCar = ElectricCar()
electricCar.battery.get_range()
electricCar.battery.upgrade_battery()
electricCar.battery.get_range()