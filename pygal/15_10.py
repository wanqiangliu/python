import pygal
import matplotlib.pyplot as plt
from random_walk import RandomWalk
from die import Die

rw = RandomWalk(100)
rw.fill_walk()
#绘制直方图显示随机漫步的结果
hist = pygal.Bar()
hist.title = "Results of Random Walk."
hist.x_labels = list(str(x) for x in rw.x_values) #标签必须为字符串
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('Random Walk',rw.y_values)
hist.render_to_file('random_walk.svg')

#绘制散点图显示掷骰子的情况
die = Die()
results = []
for roll_num in range(5000):
	result = die.roll()
	results.append(result)

x_values = list(range(1,7))
y_values = []
for value in x_values:
	y_values.append(results.count(value))
"""绘制折线图"""
plt.plot(x_values,y_values,linewidth=1)
"""绘制散点图"""
#plt.scatter(x_values,y_values,c=x_values,cmap=plt.cm.BuPu,edgecolor='none',s=10)
plt.show()
