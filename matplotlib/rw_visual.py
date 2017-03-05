#绘制5000的随机漫步图
import matplotlib.pyplot as plt
from random_walk import RandomWalk
"""重复绘制随机漫步图"""
while True:
	rw = RandomWalk()
	rw.fill_walk();
	#设置随机漫步图的标题
	plt.title("random map",fontsize=10)
	#设置画布的大小,figsize对应参数分别为长和宽,dpi表示分辨率
	plt.figure(dpi=128,figsize=(10,6))
	#给随机漫步图着色
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.BuPu,edgecolor='none',s=1)
	#绘制起点和终点
	plt.scatter(0,0,c='green',edgecolor='none',s=100)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100)
	#隐藏x,y坐标只关心随机漫步的路径
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	#在matplotlib显示器中查看结果
	plt.show()
	keep_running = input("Make another walk?(y/n): ")
	if keep_running == 'n':
		break
