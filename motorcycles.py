motorcycles = ['honda','yamaha','suzuki']
print( motorcycles )
#修改列表中的元素
motorcycles[0] = 'ducati'
print( motorcycles )
#末尾添加元素
motorcycles.append('liebao')
print( motorcycles )
#创建空列表后逐个追加到列表中
motorcycles = []
print( motorcycles )
motorcycles.append('aima')
motorcycles.append('jiebao')
motorcycles.append('bmw')
print( motorcycles )
#在列表的任何位置插入新值
motorcycles.insert(2,'feige')
print( motorcycles )
motorcycles.insert(-2,'xiaoniao')
print( motorcycles )
#删除列表中的某个元素
del motorcycles[2]
print(motorcycles)