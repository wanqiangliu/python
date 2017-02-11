#元组
dimensions = (200,60)
print( dimensions[0] )
print( dimensions[1] )
#不允许修改元组中的值
#dimensions[0] = 666

#遍历元组中的所有值
for dimension in dimensions:
	print( dimension )

#元组不允许直接修改单个元素，但可以通过给元组整体赋值的方式间接来改变元组中元素的值
dimensions = (400,80)
print( "modifyed dimensions:" + str(dimensions) )