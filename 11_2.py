import unittest
from city_functions import get_city_country

class CityTestCase(unittest.TestCase):
	def test_city_country(self):
		formatted_city_name = get_city_country('santiage','chile')
		self.assertEqual(formatted_city_name,"Santiage, Chile")

	def test_city_country_population(self):
		formatted_city_name = get_city_country('santiage','chile',population=5000000) 
		self.assertEqual(formatted_city_name,"Santiage, Chile - population 5000000")

	def test_city_country_population_3(self):
		formatted_city_name = get_city_country('santiage','chile',population=6000) 
		self.assertEqual(formatted_city_name,"Santiage, Chile - population 6000")

unittest.main()