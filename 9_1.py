class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)

	def open_restaurant(self):
		print("Restaurant is opening!")

	def set_number_served(self,person_nums):
		self.number_served = person_nums

	def increment_number_serverd(self,person_nums):
		self.number_served += person_nums

	def read_serverd_number(self):
		print("Now having " + str(self.number_served) + "!")

restaurant = Restaurant('qiangqiang','French')
print(restaurant.restaurant_name + " have the " + restaurant.cuisine_type + "\n")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n")
restaurant_second = Restaurant('yipinmian','noodle')
restaurant_second.describe_restaurant()

restaurant.set_number_served(100)
restaurant.read_serverd_number()
restaurant.increment_number_serverd(8)
restaurant.read_serverd_number()

		