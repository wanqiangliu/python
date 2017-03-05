#使用scatter()绘制散点图并设置其样式
import matplotlib.pyplot as plt
#通过x轴的数据自动计算y轴的数据值
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
"""
数据点默认为蓝色的点黑色的轮廓，edgecolor选项可讲黑色的轮廓删除,从而就只剩蓝色的实心点了
c选项设置颜色，可直接指定颜色名称或者用自定义颜色c=(0,0,0.8)
c设置成一个数值y值列表，再设置cmap参数告诉pyplot使用哪个颜色映射
"""
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.BuPu,edgecolor='none',s=10)
#设置图标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
#设置刻度标记的大小,x、y轴都影响只显示主刻度
plt.tick_params(axis='both',which='major',labelsize=20)
#设置x,y坐标的取值范围
plt.axis([0,1000,0,1000000])
#plt.show()
plt.savefig('squares_plot.png',bbox_inches='tight')