#测试函数的测试用例
import unittest
from name_function import get_formatted_name

#print(dir(unittest.TestCase))
#测试用例NameTestCast,测试单元的函数名务必要用test_开头这样调用unittest才可以自动执行
class NameTestCast(unittest.TestCase):
	"""第一条测试单元，只测姓和名"""
	def test_first_last_name(self):
		formatted_name = get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')

	"""第二条测试单元，测试中间名"""
	def test_first_middle_last_name(self):
		formatted_name = get_formatted_name(
			'wolfgang','mozart','amadeus')
		self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

unittest.main()

		