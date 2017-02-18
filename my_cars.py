#import car_import 导入整个模块
#from car_import import * 导入整个模块的所有类
from car_import import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen','beetle',2016)
print(my_beetle.get_descripitve_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descripitve_name())