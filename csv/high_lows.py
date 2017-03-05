#解析.csv类型的文件
import csv
import matplotlib.pyplot as plt  #from matplotlib import pyplot as plt
from datetime import datetime

file_name = 'sitka_weather_07-2014.csv'
#获取文件头
with open(file_name) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	#获取文件中每天的最高气温、日期、最低气温
	dates,highs,lows = [],[],[]	
	for row in reader:
		try:		
			current_date = datetime.strptime(row[0],'%Y-%m-%d')	
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date,'missing date')
		else:
			highs.append(high)
			lows.append(low)
			dates.append(current_date)

#打印文件头及其位置
for index,colum_header in enumerate(header_row):
	print(index,colum_header)

#绘制气温图表
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)#默认为y轴坐标值,x轴的值为从0开始到最后一个y值结束y值的个数
plt.plot(dates,lows,c='blue',alpha=0.5)
#填充最高和最低气温之间的区域
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
#设置图形的格式
plt.title("Daily high and low temperature,July 2014",fontsize=24)
plt.xlabel('',fontsize=16)
#绘制斜的日期标签
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)#x,y轴均采用主刻度，刻度大小为16
plt.show()

