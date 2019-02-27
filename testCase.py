from UserStories import *
import unittest

# Test Case


class GedreaderTest(unittest.TestCase):
    def test_BirthDates(self):  # testCase for Check Birth
        today = datetime.today()
        for i in individual_list:
            self.assertLess(datetime.strptime(i[3], "%Y %b %d"), today)

    def test_DeathDates(self):  # testCase for Check Death
        today = datetime.today()
        for i in individual_list:
            if i[4] != "NA":
                self.assertLess(datetime.strptime(i[4], "%Y %b %d"), today)

    def test_MarriedDates(self):  # testCase for Check Married
        today = datetime.today()
        for i in family_list:
            self.assertLess(datetime.strptime(i[3], "%Y %b %d"), today)

    def test_DivorcedDates(self):  # testCase for Check Divorce
        today = datetime.today()
        for i in family_list:
            if i[4] != "NA":
                self.assertLess(datetime.strptime(i[4], "%Y %b %d"), today)

    # testCase for Check Divorce before death
    def test_Divorce_before_death(self):
        for i in family_list:
            self.assertEqual(i[4], "NA")

    # testCase for Check Marriage before death
    def test_Marriage_before_divorce(self):
        for i in family_list:
            if i[4] != "NA":
                self.assertLess(datetime.strptime(
                    i[3], "%Y %b %d"), datetime.strptime(i[4], "%Y %b %d"))

    def test_lessthen150(self):  # testCase for Check age less than 150
        for i in individual_list:
            self.assertLess(calculate_age(i[3], i[4]), 150)

    # test case for user story 15, fewer than 15 siblings
    def test_siblings_fewer_than_15(self):
        self.assertEqual(fewer_than_15_siblings(family_list),
                         ([], " list of families have more than 15 siblings"))
        self.assertNotEqual(fewer_than_15_siblings(family_list), 1)
        self.assertTrue(fewer_than_15_siblings(family_list))
        self.assertIsNotNone(fewer_than_15_siblings(family_list))
        self.assertIsNot(fewer_than_15_siblings(family_list), "")


class TestBirth(unittest.TestCase):
    def test_normal(self):
        # havent added Errors like unbound and type cos we will be adding them in the future updates
        """test for normal working and nothing if wrong"""
        self.assertEqual(birth_before_death(
            "@I8@", "1906 AUG 15", "1956 FEB 11"), "1956 FEB 11")
        self.assertNotEqual(birth_before_death(
            "@I8@", "1956 FEB 11", "1906 AUG 15"), "1906 AUG 15")

    def test_wrong(self):
        """for death before birth"""
        self.assertEqual(birth_before_death(
            "@I8@", "1956 FEB 11", "1906 AUG 15"), "NA")
        self.assertNotEqual(birth_before_death(
            "@I8@", "1906 AUG 15", "1956 FEB 11"), "NA")
        self.assertTrue(birth_before_death(
            "@I8@", "1956 FEB 11", "1906 AUG 15") == "NA")
        self.assertFalse(birth_before_death(
            "@I8@", "1906 AUG 15", "1956 FEB 11") == "NA")


class TestMarriage(unittest.TestCase):
    def test_normal(self):
        # havent added Errors like unbound and type cos we will be adding them in the future updates
        """test for normal working and nothing if wrong"""
        self.assertEqual(marriage_before_death(
            "@F2@", "1993 APR 7", "@I4@", "@I5@"), "1993 APR 7")
        self.assertNotEqual(marriage_before_death(
            "@F2@", "2010 APR 7", "@I4@", "@I5@"), "2010 APR 7")

    def test_wrong(self):
        """for death before marriage"""
        self.assertEqual(marriage_before_death(
            "@F2@", "2010 APR 7", "@I4@", "@I5@"), "NA")
        self.assertNotEqual(marriage_before_death(
            "@F2@", "1993 APR 7", "@I4@", "@I5@"), "NA")
        self.assertFalse(marriage_before_death(
            "@F2@", "1993 APR 7", "@I4@", "@I5@") == "NA")


class TestBirth(unittest.TestCase):
    def test_normal(self):
        # havent added Errors like unbound and type cos we will be adding them in the future updates
        """test for normal working and nothing if wrong"""
        self.assertEqual(marraige_before_birth(
            "@F2@", "1993 APR 7", "@I4@", "@I5@"), "NA")
        self.assertNotEqual(marraige_before_birth(
            "@F2@", "2010 APR 7", "@I4@", "@I5@"), "2010 APR 7")

    def test_wrong(self):
        """for death before marriage"""
        self.assertEqual(marraige_before_birth(
            "@F2@", "2010 APR 7", "@I4@", "@I5@"), "NA")
        self.assertNotEqual(marraige_before_birth(
            "@F2@", "1993 APR 7", "@I4@", "@I5@"), "1993 APR 7")
        self.assertTrue(marraige_before_birth(
            "@F2@", "1993 APR 7", "@I4@", "@I5@") == "NA")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
