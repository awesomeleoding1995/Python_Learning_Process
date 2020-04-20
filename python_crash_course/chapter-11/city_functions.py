def city_country(city, country, population=''):
	"""describe the city and country"""

	formatted_name = city + ', ' + country + ' - population ' + str(population)
	return formatted_name.title()