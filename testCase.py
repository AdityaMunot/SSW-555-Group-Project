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

    def test_Divorce_before_death(self):  # testCase for Check Divorce before death
        for i in family_list:
            self.assertEqual(i[4], "NA")

    def test_Marriage_before_divorce(self): # testCase for Check Marriage before death
        for i in family_list:
            if i[4] != "NA":
                self.assertLess(datetime.strptime(i[3], "%Y %b %d"), datetime.strptime(i[4], "%Y %b %d"))

    def test_lessthen150(self): # testCase for Check age less than 150
        for i in individual_list:
            self.assertLess(calculate_age(i[3], i[4]), 150)

    def test_marriage_before_death(self): #test case for user story 05, marriage before death
        self.assertEqual(marriage_before_death(family_list, individual_list),([], " list of families who do not have marriage date before death date of one of the members"))
        self.assertNotEqual(marriage_before_death(family_list, individual_list), 1)
        self.assertTrue(marriage_before_death(family_list, individual_list))
        self.assertIsNotNone(marriage_before_death(family_list, individual_list))
        self.assertIsNot(marriage_before_death(family_list, individual_list), '')
    
    def test_siblings_fewer_than_15(self): #test case for user story 15, fewer than 15 siblings
        self.assertEqual(fewer_than_15_siblings(family_list), ([], " list of families have more than 15 siblings"))
        self.assertNotEqual(fewer_than_15_siblings(family_list),1)
        self.assertTrue(fewer_than_15_siblings(family_list))
        self.assertIsNotNone(fewer_than_15_siblings(family_list))
        self.assertIsNot(fewer_than_15_siblings(family_list), "")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
