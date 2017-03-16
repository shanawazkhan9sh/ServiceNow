import random
import unittest
import xmlrunner
from django.test import TestCase

class BasicTestCase(TestCase):
	def test_addition(self):
		self.assertEqual(1 + 2, 4)

	def test_sub(self):
		self.assertEqual(5 - 2, 4)

	def test_mul(self):
		self.assertEqual(5 * 2, 4)

	def test_upper(self):
		self.assertEqual("nishant".upper(), "NISHANT")
		
if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)

