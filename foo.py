#__name__表示模块名，在当前程序中直接执行模块名为__name__,若__name__.py被import到__name__test.py中则模块名变为foo
def fun(num):
	print(str(num))

print(__name__)
if __name__ == "__main__":
	num = input("Please enter your favoriate num: ")
	print("In __name__.py Your favoriate num is :")
	fun(num)