import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ",r.status_code)

#将API响应存储在一个变量中,将JSON信息转化为一个python字典
response_dict = r.json()
print("Total repositories:",response_dict['total_count'])

#探索有关仓库的信息,最受欢迎的python项目存储在字典列表中
repo_dicts = response_dict['items']
#打印字典列表的个数
print("Repositories returned:",len(repo_dicts))

#研究第一个仓库
"""
repo_dict = repo_dicts[0]
print("\nKeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)
"""
#添加自定义工具提示
names,plot_dicts = [],[]
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	plot_dict={
		'value':repo_dict['stargazers_count'],
		'label':repo_dict['description'],
		'xlink':repo_dict['html_url'],
	}
	plot_dicts.append(plot_dict)

#可视化
my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')