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
#当删除列表中的元素后不再使用它则用del来删除元素，如果删除列表中的元素后还将继续使用该元素则用pop
#删除列表中的某个元素
del motorcycles[2]
print(motorcycles)
#pop来删除列表末尾的元素
popped_motorcycle = motorcycles.pop();
print( motorcycles )
print( popped_motorcycle )
#pop来删除列表中任意位置的元素
second_element = motorcycles.pop(1)
print( motorcycles )
print( second_element )
#根据列表中的值来删除remove,只删除第一次出现的aima
motorcycles.insert(2,'aima')
print( motorcycles )
motorcycles.remove('aima')
print(motorcycles)

