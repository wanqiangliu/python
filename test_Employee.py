import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):

	def setUp(self):
		#初始化一个公共的实例供所有测试单元使用,从而不用每个测试单元都要初始化实例
		self.my_Employee = Employee('lwq',200000)

	def test_give_default_raise(self):
		sale = self.my_Employee.give_raise()
		self.assertEqual(sale,205000)

	def test_give_custom_raise(self):
		sale = self.my_Employee.give_raise(100000)
		self.assertEqual(sale,300000)
unittest.main()