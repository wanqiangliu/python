def make_album(singer_name,album_name,songs_num=''):
	if songs_num:
		album = {'singer':singer_name,'album':album_name,'songs':songs_num}
	else:
		album = {'singer':singer_name,'album':album_name}
	return album

while True:
	print("\nPlease enter album's info:")
	print("(Enter 'q' to enter the program.)")
	singer_name = input("singer_name: ")
	if singer_name == 'q':
		break
	album_name = input("album_name: ")
	if album_name == 'q':
		break;
	songs_num = input("songs_name: ")
	if songs_num == 'q':
		break;
	album = make_album(singer_name,album_name,songs_num)
	print(album)
