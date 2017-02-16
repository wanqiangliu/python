def make_magician(magicianames):
	greater_magicians = []
	while magicianames:
		greater_magicians.append("the Great " + magicianames.pop().title())
	return greater_magicians

def show_magicians(magicianames):
	for magicianame in magicianames:
		print(magicianame)

magicianames = ['lwq','ljm','john']
great_magicianames = make_magician(magicianames[:])
show_magicians(great_magicianames)
show_magicians(magicianames)