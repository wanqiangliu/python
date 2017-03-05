#显示立方值的散点图
import matplotlib.pyplot as plt
x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

#设置散点图的属性
plt.title("Cube Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Cube of Value",fontsize=14)
#绘制散点图
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.cool,edgecolor='none',s=20)
#设置坐标刻度
plt.tick_params(axis='both',which='major',labelsize='10')
#设置坐标范围
plt.axis([0,5000,0,125000000000])
plt.show()