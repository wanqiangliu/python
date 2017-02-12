alien_0 = {'color':'green','points':5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
#访问字典中的值
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
#向字典中添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#创建空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
#修改字典中的值
alien_0['color'] = 'yellow'
print(alien_0)
#修改字典中的值的实际应用
alien_0 = {'x_position':0,'y_positon':25,'speed':'medium'}
print("Original x-positon: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))
#删除键值对
alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)