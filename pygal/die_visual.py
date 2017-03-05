import pygal
from die import Die

#创建D6,D10的骰子
die_1 = Die()
die_2 = Die(10)

#掷n次骰子并将结果保存在一个列表中
results = []
for roll_num in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides#最小为2最大为12
for value in range(2,max_result+1):
	frequencie = results.count(value)#每一面出现的次数
	frequencies.append(frequencie)

#绘制直方图可视化结果
hist = pygal.Bar()
hist.title = "Results of rolling one D6 and D10 50000 times."
hist.x_labels = list(str(x) for x in range(2,16+1)) #标签必须为字符串
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D10',frequencies)
hist.render_to_file('die_visual.svg')