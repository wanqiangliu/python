# encoding:utf8
from random import randint
class Die():
	def __init__(self,sides=6):
		self.sides = sides
	def roll_die(self):
		x = randint(1,self.sides)
		print(x)

die = Die()
print("6 mian de dian shu :")
for i in range(0,10):
	die.roll_die()
print("\n10 mian de dian shu :")
die = Die(10)
for i in range(0,10):
	die.roll_die()
print("\n20 mian de dian shu:")
die = Die(20)
for i in range(0,10):
	die.roll_die()