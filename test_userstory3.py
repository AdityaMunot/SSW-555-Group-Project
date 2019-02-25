from HW3AdityaMunot import *
import unittest


class TestBirth(unittest.TestCase):
	def test_normal(self):
		# havent added Errors like unbound and type cos we will be adding them in the future updates
		"""test for normal working and nothing if wrong"""
		self.assertEqual(birth_before_death("@I8@", "1906 AUG 15", "1956 FEB 11"), "1956 FEB 11")
		self.assertNotEqual(birth_before_death("@I8@", "1956 FEB 11", "1906 AUG 15"), "1906 AUG 15")

	def test_wrong(self):
		"""for death before birth"""
		self.assertEqual(birth_before_death("@I8@", "1956 FEB 11", "1906 AUG 15"),"NA")
		self.assertNotEqual(birth_before_death("@I8@", "1906 AUG 15", "1956 FEB 11"), "NA")
		self.assertTrue(birth_before_death("@I8@", "1956 FEB 11", "1906 AUG 15") == "NA")
		self.assertFalse(birth_before_death("@I8@", "1906 AUG 15", "1956 FEB 11")=="NA")


class TestMarriage(unittest.TestCase):
	def test_normal(self):
		# havent added Errors like unbound and type cos we will be adding them in the future updates
		"""test for normal working and nothing if wrong"""
		self.assertEqual(marriage_before_death("@F2@", "1993 APR 7", "@I4@", "@I5@"), "1993 APR 7")
		self.assertNotEqual(marriage_before_death("@F2@", "2010 APR 7", "@I4@", "@I5@"), "2010 APR 7")

	def test_wrong(self):
		"""for death before marriage"""
		self.assertEqual(marriage_before_death("@F2@","2010 APR 7","@I4@","@I5@"),"NA")
		self.assertNotEqual(marriage_before_death("@F2@", "1993 APR 7", "@I4@", "@I5@"), "NA")
		self.assertFalse(marriage_before_death("@F2@", "1993 APR 7", "@I4@", "@I5@")=="NA")


class TestBirth(unittest.TestCase):
	def test_normal(self):
		# havent added Errors like unbound and type cos we will be adding them in the future updates
		"""test for normal working and nothing if wrong"""
		self.assertEqual(marraige_before_birth("@F2@", "1993 APR 7", "@I4@", "@I5@"), "NA")
		self.assertNotEqual(marraige_before_birth("@F2@", "2010 APR 7", "@I4@", "@I5@"), "2010 APR 7")

	def test_wrong(self):
		"""for death before marriage"""
		self.assertEqual(marraige_before_birth("@F2@","2010 APR 7","@I4@","@I5@"),"NA")
		self.assertNotEqual(marraige_before_birth("@F2@", "1993 APR 7", "@I4@", "@I5@"), "1993 APR 7")
		self.assertTrue(marraige_before_birth("@F2@", "1993 APR 7", "@I4@", "@I5@") == "NA")


if __name__ == '__main__':
	main()
	unittest.main(exit=False, verbosity=2)