import unittest
from city_functions import city_country 

class CityFunctionsTestCase(unittest.TestCase):
	"""test code: city_functions"""


	def test_city_country(self):
		formatted_name = city_country('santiago', 'chile')
		self.assertEqual(formatted_name, 'Santiago, Chile - Population ')

	def test_city_country_population(self):
		formatted_name = city_country('santiago', 'chile', 500000)
		self.assertEqual(formatted_name, 'Santiago, Chile - Population 500000')

unittest.main()