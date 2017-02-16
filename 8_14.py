def make_car(type,user,**car_info):
	cars = {}
	cars['type'] = type
	cars['user'] = user
	for k,v in car_info.items():
		cars[k] = v
	return cars

cars = make_car('B','xue fu lai',color = 'bule',tow_package=True)
print(cars)