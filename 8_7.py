def make_album(singer_name,album_name,songs_num=''):
	if songs_num:
		album = {'singer':singer_name,'album':album_name,'songs':songs_num}
	else:
		album = {'singer':singer_name,'album':album_name}
	return album

album = make_album('zhoujielun','qilixiang')
print(album)
album = make_album('wuyuetian','zizhuang',10)
print(album)