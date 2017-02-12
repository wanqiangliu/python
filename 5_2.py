str1 = 'lwq'
str2 = 'LWQ'
if str1 == str2:
	print("equal!")
else:
	print("not equal!")

if str1 == str2.lower():
	print("equal!")
else:
	print("not equal!")

a = 10
b = 20
if a <= b:
	print("\na<=b!")
if b >= a:
	print("b>=a!")
if (a<=10) and (b>=20):
	print("True!")
else:
	print("False!")

nums = list(range(1,11))
num = 20
if num in nums:
	print("\n20 is in nums!")
else:
	print("\n20 is not in nums!")