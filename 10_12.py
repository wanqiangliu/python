import json
filename = 'love_num.json'
try:
	with open(filename) as file_object:
		num = json.load(file_object)
		print("I know your favorite number is " + num)
except FileNotFoundError as e:
	with open(filename,'w') as file_object:
		num = input("What's your favorite number? ")
		json.dump(num,file_object)
