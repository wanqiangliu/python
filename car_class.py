#使用类的实例
class car():
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

my_new_car = car('audi','a8','2016')
print(my_new_car.get_descripitve_name()) 
my_new_car.read_odometer_reading()
#修改属性的值 1、直接修改属性值
my_new_car.odometer_reading=180000
my_new_car.read_odometer_reading()
#2、通过方法修改属性的值
my_new_car.update_odometer(666)
my_new_car.read_odometer_reading()
#3、通过方法对属性的值进行递增
my_new_car.increment_odometer(100)
my_new_car.read_odometer_reading()