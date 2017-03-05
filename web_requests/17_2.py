import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#获取Hacker News上当前最热门的500篇文件ID
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:",r.status_code)

#处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
x_values=[]

#获取前30条最热门文章
for submission_id in submission_ids[:5]:
	url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
	submission_r = requests.get(url)
	print("Submission status code",submission_r.status_code)
	response_dict = submission_r.json()
	x_values.append(response_dict['title'])
	submission_dict = {
		'label':response_dict['title'],
		'xlink':'http://news.ycombinator.com/item?id=' + str(submission_id),
		'value':response_dict.get('descendants',0),#用dict.get()获取评论数，如果没有则返回0
	}
	submission_dicts.append(submission_dict)

#submission_dicts = sorted(submission_dicts,key=itemgetter('value'),reverse=True)

#可视化
#可视化
my_style = LS('#332266',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45  #x左边斜45度
my_config.show_legend = False    #不显示图例
my_config.title_font_size = 24   #标题的大小
my_config.label_font_size = 14   #x,y轴标题的大小
my_config.major_label_font_size = 18  #突显出主刻度
my_config.truncate_label = 15    #x坐标只截取前15位字符超高的字符用...表示
my_config.width = 1000           #整个直方图的宽度
chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Comment story'
chart.x_labels = x_values
chart.add('',submission_dicts)
chart.render_to_file('17_2.svg')