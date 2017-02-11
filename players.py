#列表的切片即列表的部分值
players = ['lwq','lwq1','lwq2','lwq3','lwq4']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[1:])
print(players[-3:])
#遍历切片中的元素
for player in players[-3:]:
	print(player)