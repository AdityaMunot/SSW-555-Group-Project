from UserStories import *
import unittest

# Test Case


class GedreaderTest(unittest.TestCase):
    def test_BirthDates(self): # testCase for Check Birth
        today = datetime.today()
        for i in individual_list:
            self.assertLess(datetime.strptime(i[3], "%Y %b %d"), today)

    def test_DeathDates(self): # testCase for Check Death
        today = datetime.today()
        for i in individual_list:
                if i[4] != "NA":
                        self.assertLess(datetime.strptime(i[4], "%Y %b %d"), today)

    def test_MarriedDates(self): # testCase for Check Married
        today = datetime.today()
        for i in family_list:
                self.assertLess(datetime.strptime(i[3], "%Y %b %d"), today)

    def test_DivorcedDates(self): # testCase for Check Divorce
        today = datetime.today()
        for i in family_list:
                if i[4] != "NA":
                        self.assertLess(datetime.strptime(i[4], "%Y %b %d"), today)

    def test_Divorce_before_death(self): # testCase for Check Divorce before death
        for i in family_list:
            self.assertEqual(i[4], "NA")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)