#编写清晰的程序
name  = input("Please enter your name: ")
print("Hello," + name + "!")

#若提示信息过长时需要用如下方式进行编写
prompt = "If you tell us who you are,wo can personalize the message you see."
prompt += "\n What's your name? "
name = input(prompt)
print("Hello, " + name + "!")
