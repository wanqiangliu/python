#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()
plt.title("Plot of RandWalk",fontsize=24)
plt.plot(rw.x_values,rw.y_values,linewidth=1)
plt.show()