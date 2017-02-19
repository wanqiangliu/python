#使用try-except代码块
def isnum(s):
 	try:
 		float(s)
 		return True
 	except ValueError as e:
 		print(type(e))
 		return False
	
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!\n")

print("Give me two numbers,and I'll divide them.")
print("You can enter a 'q' to end the programming.")
while True:
	number1 = input("\nFirst number: ")
	if number1 == 'q':
		break
	elif isnum(number1) == False:
		print("Inviad number!")
		continue
	number2 = input("Second number: ")
	if number2 == 'q':
		break
	elif isnum(number2) == False:
		print("Inviad number!")
		continue
	try:
		answer = int(number1)/int(number2)
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(answer)
