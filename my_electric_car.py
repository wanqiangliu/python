from car_import import ElectricCar

my_tesla = ElectricCar('tesla','model s','2016')
print(my_tesla.get_descripitve_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()