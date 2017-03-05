import json
import pygal
from pygal.style import LightColorizedStyle as LCS,RotateStyle as RS #设置世界地图的样式,LightColorizedStyle背景色和RotateStyle每个国家的颜色
from countries import get_country_code

#将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

cc_populations = {}
#打印每个国家2010年的人口数量
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		population = int(float(pop_dict['Value']))#由于浮点数不能直接转换为整数所以先转为float再用int保留整数部分
		country_name = pop_dict['Country Name']
		#获取国别码
		code = get_country_code(country_name)
		if code:
			print(code + ":" + str(population))
			cc_populations[code] = population
		else:
			print('ERROR - ' + country_name)

#将人口按数量分为3组，少于1000万，介于1000万到10亿之间，超过10亿的
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
for cc,pop in cc_populations.items():
	if pop<10000000:
		cc_pops_1[cc] = pop
	elif pop<1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop 
#查看每组分别包含多少国家
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

"""绘制世界地图，表示全球2010各国人口的数量"""
wm_style = RS('#336699',base_style=LCS)
wm = pygal.Worldmap(style=wm_style)
wm.title = 'World Population in 2010,by Country'
wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)
wm.render_to_file('world_population.svg')