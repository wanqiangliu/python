def get_city_country(city,country,population=0):
	if population:
		return city.title() + ", " + country.title() + " - " + "population " + str(population)
	else:
		return city.title() + ", " + country.title()