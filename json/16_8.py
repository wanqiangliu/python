#设计countries的自动测试案例
import unittest
from countries import get_country_code

class TestGetCountryCode(unittest.TestCase):
	def setUp(self):
		self.country_name = ['China','United States','xx']

	def test_return_code(self):
		code = get_country_code(self.country_name[0])
		self.assertEqual(code,'cn')
		code = get_country_code(self.country_name[1])
		self.assertEqual(code,'us')

	def test_return_none(self):
		code = get_country_code(self.country_name[2])
		self.assertEqual(code,None)

unittest.main()
