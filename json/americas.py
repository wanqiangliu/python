import pygal
wm = pygal.Worldmap()
wm.title = 'North,Central,and South America'
wm.add('North America',{'ca':34126000,'mx':113423000,'us':309349000})
wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South Ameriaca',['ar','bo','br','cl','co','ec','gf','gy',
	'pe','py','sr','sr','uy','ve'])
wm.add('Asia',{'cn':1300000000})
wm.render_to_file('americas.svg')