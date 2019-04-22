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
	
	def test_marriage_before_death(self):
		self.assertEqual(marriage_before_death(family_list, individual_list),(['@F4@'], " list of families who do not have marriage date before death date of one of the members"))
		self.assertNotEqual(marriage_before_death(family_list, individual_list), 1)
		self.assertTrue(marriage_before_death(family_list, individual_list))

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
		self.assertEqual(fewer_than_15_siblings(family_list), (['@F1@'], " list of families have 15 or more siblings"))
		self.assertNotEqual(fewer_than_15_siblings(family_list),1)
		self.assertTrue(fewer_than_15_siblings(family_list))


	def test_marr_before_14(self):
		a = [('Error,', '@F1@', 'married when less than 14'),
			 ('Error,', '@F4@', 'married when less than 14'),
			 ('Error,', '@F9@', 'married when less than 14')]
		self.assertEqual(list(marriage_under_age_14()), a)

	def test_parents_birth_bfr_death(self):
		self.assertEqual(list(parents_birth_before_death()), [('Error parent id', '@I3@', 'children born after parents death')])

	def test_no_bigamy(self):
		error = 1
		self.assertEqual(checked_no_bigamy, error)

	def test_parents_not_too_old(self):
		error = 4
		self.assertEqual(checked_parents_not_too_old, error)

	def test_Sibling_spacing(self):
		error = 4
		self.assertEqual(checked_Sibling_spacing, error)

	def test_Multiple_birth(self):
		error = 1
		self.assertEqual(checked_Multiple_birth, error)

	def test_correct_gender_for_role(self):  # test case for user story 21
		self.assertEqual(checked_correct_gender_for_role, 1)

	def test_unique_ids(self):  # test case for user story 22
		self.assertEqual(check_unique_ids, 0)

	def test_birth_before_death(self):
		"""for death before birth US US 02"""
		self.assertEqual(birth_before_death(individual_list), [
						 ('Error: User', '@I6@', 'was dead before birth'), ('Error: User', '@I11@', 'was dead before birth')])

	def test_birth_before_marriage(self):
		"""test birth before marriage US 03"""
		self.assertEqual((birth_before_marriage(individual_list, family_list)), [
						 ('Error: User', '@F1@', 'was born before marraige'), ('Error: User', '@F4@', 'was born before marraige')])

	def test_sibling_should_not_mawrry(self):
		self.assertEqual(sibling_should_not_mawrry(),[('Error both are sibblings but married', '@I7@', '@I8@')])

	def test_first_cousin_should_not_marry(self):
		self.assertEqual(first_cousin_should_not_marry(),[])
		"""
		# This is the demonstration test case when you run Family-cousins marry.ged (Did it in another gedcom because the gedcom had becoming really confusing one change and it was breaking everything)
		self.assertEqual(first_cousin_should_not_marry(),[('Error US 19 first cousins are getting married', '@F3@')])
		"""

	def test_male_last_names(self):  # test user story 16 test case
		self.assertEqual(male_last_names(individual_list, family_list), ('error in family','@F2@', ' male child last name not the same as fathers last name'))
		self.assertNotEqual(male_last_names(individual_list, family_list), 1)
		self.assertTrue(male_last_names(individual_list, family_list))
		self.assertIsNotNone(male_last_names(individual_list, family_list))
		self.assertIsNot(male_last_names(individual_list, family_list), '')
	
	def test_no_marriage_to_children(self):  #test User story 17 test case 

		self.assertEqual(check_no_marriage_to_children, 0)

	def test_living_married(self):
		"""US 30 List of living Married"""
		self.assertEqual(list_living_married(),['@I5@', '@I11@'])

	def test_unique_name(self):
		"""US 25 List of Unique First names"""
		self.assertEqual(unique_first_name(), ['Michael', 'Holly', 'Jim', 'Pam', 'Dwight', 'Andy', 'Ryan', 'Kelly', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P9', 'P10', 'P11', 'P12', 'P13', 'Cousin', 'P14', 'P15', 'Kappa', 'Krappa', 'Suhas', 'Tina', 'Kim', 'Duhas', 'Fuhas', 'Guhas', 'Huhas', 'Juhas', 'Kuhas', 'Kij', 'Lifu', 'Kifu', 'Fuli', 'Kuli', 'Kuli'])

# For User Story 23 8
class TestBirthDay(unittest.TestCase):
	def test_unique_name_and_birthday(self):
		self.assertEqual(Unique_name_and_birthday(individual_list), "Error: US23 Kuli Halpert Birth at 2009 OCT 13 have been duplicated ")

	def test_birth_before_mariage_of_parents(self):
		self.assertEqual(Birth_before_mariage_of_parents(individual_list,family_list), "Error: US08 Kuli Halpert Birth before marriage of parents")

# User Story 20
	def test_aunts_and_uncles(self):
		error = 2
		self.assertEqual(check_Aunts_and_uncles, error)
# User Story 31
	def test_list_living_single(self):
		listsingle = ['@I13@']
		self.assertEqual(living_single, listsingle)


if __name__ == '__main__':
	unittest.main(exit=False, verbosity=2)
