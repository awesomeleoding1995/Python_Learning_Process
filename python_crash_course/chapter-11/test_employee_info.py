import unittest
from employee_info import Employee

class TestEmployee(unittest.TestCase):
	"""a test case aims at Employee class"""

	def setUp(self):
		"""set up testing example"""
		self.my_employee = Employee('eggy', 'zhang', 10000)
		self.employee_info = ['eggy', 'zhang', 10000]

	def test_give_default_raise(self):
		"""test the function of salary raise by default"""
		self.my_employee.give_raise()
		self.assertEqual(self.my_employee.annual_s, 15000)

	def test_give_custom_raise(self):
		"""test mannually increase salary"""
		self.my_employee.give_raise(10000)
		self.assertEqual(self.my_employee.annual_s, 20000)

unittest.main()
