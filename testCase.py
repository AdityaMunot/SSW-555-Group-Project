from UserStories import *
import unittest

# Test Case


class GedreaderTest(unittest.TestCase):
    def test_BirthDates(self):  # testCase for Check Birth
        today = datetime.today()
        for i in CheckedIndividuals:
            if i[3] != "NA":
                self.assertLess(datetime.strptime(i[3], "%Y %b %d"), today)

    def test_DeathDates(self):  # testCase for Check Death
        today = datetime.today()
        for i in CheckedIndividuals:
            if i[4] != "NA":
                self.assertLess(datetime.strptime(i[4], "%Y %b %d"), today)

    def test_MarriedDates(self):  # testCase for Check Married
        today = datetime.today()
        for i in CheckedFamilylist:
            if i[3] != "NA":
                self.assertLess(datetime.strptime(i[3], "%Y %b %d"), today)

    def test_DivorcedDates(self):  # testCase for Check Divorce
        today = datetime.today()
        for i in CheckedFamilylist:
            if i[4] != "NA":
                self.assertLess(datetime.strptime(i[4], "%Y %b %d"), today)

    # testCase for Check Divorce before death
    def test_Divorce_before_death(self):
        for i in Checked_Div_bef_dea:
            self.assertEqual(i[4], "NA")

    # testCase for Check Marriage before death
    def test_Marriage_before_divorce(self):
        for i in Checked_Mar_bef_div:
            if i[4] != "NA":
                self.assertLess(datetime.strptime(
                    i[3], "%Y %b %d"), datetime.strptime(i[4], "%Y %b %d"))

    def test_lessthen150(self):  # testCase for Check age less than 150
        for i in checked_Les_Th_150:
            age = calculate_age(i[3], i[4])
            if i[3] != "NA" and age != "NA":
                self.assertLess(age, 150)

    # test case for user story 15, fewer than 15 siblings
    def test_siblings_fewer_than_15(self):
        temp = ['@F1@']
        if Checked_fewer_than_15_siblings:
            self.assertEqual(Checked_fewer_than_15_siblings, temp)

    def test_parents_birth_bfr_death(self):
        self.assertEqual(list(parents_birth_before_death()), [])

    def test_marr_before_14(self):
        a = [('Error,', '@F1@', 'married when less than 14'),
             ('Error,', '@F4@', 'married when less than 14')]
        self.assertEqual(list(marriage_under_age_14()), a)

    def test_no_bigamy(self):
        error = 0
        self.assertEqual(checked_no_bigamy, error)

    def test_parents_not_too_old(self):
        error = 3
        self.assertEqual(checked_parents_not_too_old, error)

    class TestBirth(unittest.TestCase):
        def test_wrong(self):
            """for death before birth"""
            self.assertEqual(birth_before_death(individual_list), [('Error: User', '@F4@', 'was dead before birth'),
                                                                   ('Error: User', '@F1@', 'was dead before birth')])

    class TestMarriage(unittest.TestCase):
        def test_normal(self):
            # havent added Errors like unbound and type cos we will be adding them in the future updates
            self.assertEqual((birth_before_marriage(individual_list, family_list)), [
                             ('Error: User', '@I5@', 'was dead before birth')])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
