#创建一个调查问卷的字典
responses = {}

#设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
	#获取字典中的key和value
	name = input("What's your name? ")
	response = input("Which mountain would you like to climb someday? ")
	#将key和value写入字典
	responses[name] = response
	#查看是否还有人要参与调查
	repeat = input("Would you like to let another person respond?(yes/no) ")
	if repeat == 'no':
		polling_active = False
#显示结果
for k,v in responses.items():
	print(k + " would like to cliemb " + v + ".")