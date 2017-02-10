#sorted是python提供的外部函数可临时改变列表元素的顺序，sort是列表自带的内部函数来永久性改变列表元素的顺序
#sort进行永久性排序
print("sort:")
cars = ['bmw','audi','toyota','subaru']
print(cars)
#正序从小到大
cars.sort()
print(cars)
#逆序从大到小
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)
print("-----------------------------\n")
print("sorted:")
#sorted进行临时性排序
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list:")
print(cars)
print("sorted nixu:")
print(sorted(cars,reverse=True))
print("-----------------------------\n")
#直接用reverse来永久性改变列表元素的顺序逆序，但可随时恢复到原来的排序顺序即再次对列表调用reverse()即可
cars = ['bmw','audi','toyota','subaru']
print( cars )
cars.reverse() #列表元素逆序输出
print( cars )
cars.reverse() #列表元素还原成最原始的顺序
print( cars )
print("-----------------------------\n")
#用len来计算列表的长度
cars = ['bmw','audi','toyota','subaru']
length = len( cars )
print( "list length is " + str(length) )
