#使用continue关键字
current_numbser = 0
while current_numbser < 10:
	current_numbser += 1
	if current_numbser % 2 == 0:
		continue
	else:
		print(current_numbser)

#避免死循环
num = 1
while num < 5:
	print(num)
	num += 1 #这块没有则会陷入死循环
