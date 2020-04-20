import make_album

counter = 1
while counter < 4:
	print("Please enter the name of singer and album.")
	enter_singer = input("Singer name: ")
	enter_album = input("Album name: ")
	dic = make_album.make_album(singer_name = enter_singer, album_name = enter_album)
	print(dic)
	counter += 1