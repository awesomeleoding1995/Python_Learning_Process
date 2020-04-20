import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
	"""test the function get_formatted_name"""

	def test_first_last_name(self):

		formatted_name = get_formatted_name('eggy', 'zhang')
		self.assertEqual(formatted_name, 'Eggy Zhang')

unittest.main()