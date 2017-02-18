#使用类的实例
class Car():
	"""一次简单的汽车尝试"""
	def __init__(self,make,model,year):
		"""初始化汽车属性"""
		self.make = make
		self.model = model
		self.year = year
		#给属性指定默认值
		self.odometer_reading = 0

	def get_descripitve_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year) + " " + self.make.title() + " " + self.model
		return long_name

	def read_odometer_reading(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self,mileage):
		if mileage > self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer!")
	def increment_odometer(self,miles):
		self.odometer_reading += miles

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

my_new_car = Car('audi','a8','2016')
print(my_new_car.get_descripitve_name()) 
my_new_car.read_odometer_reading()
print("\n")
#修改属性的值 1、直接修改属性值
my_new_car.odometer_reading=180000
my_new_car.read_odometer_reading()
#2、通过方法修改属性的值
my_new_car.update_odometer(666)
my_new_car.read_odometer_reading()
#3、通过方法对属性的值进行递增
my_new_car.increment_odometer(100)
my_new_car.read_odometer_reading()
print("\n")
#子类实例化
my_tesla = ElectricCar('tesla','model s',2016)
#子类中只显示了year和make
print(my_tesla.get_descripitve_name())
my_tesla.battery.describe_battery()
#调用子类中特有的方法reset_battery
my_tesla.reset_battery()
my_tesla.battery.describe_battery()
#调用电池实例中的方法
my_tesla.battery.get_range()