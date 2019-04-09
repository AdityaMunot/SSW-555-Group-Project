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

	def test_marr_before_14(self):
		a = [('Error,', '@F1@', 'married when less than 14'),
			 ('Error,', '@F4@', 'married when less than 14')]
		self.assertEqual(list(marriage_under_age_14()), a)

	def test_parents_birth_bfr_death(self):
		self.assertEqual(list(parents_birth_before_death()), [])

	def test_no_bigamy(self):
		error = 0
		self.assertEqual(checked_no_bigamy, error)

	def test_parents_not_too_old(self):
		error = 5
		self.assertEqual(checked_parents_not_too_old, error)

	def test_Sibling_spacing(self):
		error = 4
		self.assertEqual(checked_Sibling_spacing, error)

	def test_Multiple_birth(self):
		error = 0
		self.assertEqual(checked_Multiple_birth, error)

	def test_correct_gender_for_role(self):  # test case for user story 21
		self.assertEqual(correct_gender_for_role(
		    family_list, individual_list), ('all gender roles in the families are correct'))
		self.assertNotEqual(correct_gender_for_role(family_list, individual_list), 1)
		self.assertTrue(correct_gender_for_role(family_list, individual_list))
		self.assertIsNotNone(correct_gender_for_role(family_list, individual_list))
		self.assertIsNot(correct_gender_for_role(family_list, individual_list), '')

	def test_unique_ids(self):  # test case for user story 22
		self.assertEqual(unique_ids(family_list, individual_list),
		                 ("all IDs unique in Family and Individual list"))
		self.assertNotEqual(unique_ids(family_list, individual_list), 1)
		self.assertTrue(unique_ids(family_list, individual_list))
		self.assertIsNotNone(unique_ids(family_list, individual_list))
		self.assertIsNot(unique_ids(family_list, individual_list), "")

	def test_birth_before_death(self):
		"""for death before birth US US 02"""
		self.assertEqual(birth_before_death(individual_list), [
		                 ('Error: User', '@I5@', 'was dead before birth'), ('Error: User', '@I11@', 'was dead before birth')])

	def test_birth_before_marriage(self):
		"""test birth before marriage US 03"""
		self.assertEqual((birth_before_marriage(individual_list, family_list)), [
		                 ('Error: User', '@F4@', 'was born before marraige'), ('Error: User', '@F1@', 'was born before marraige')])

	def test_sibling_should_not_mawrry(self):
		self.assertEqual(sibling_should_not_mawrry(),[('Error both are sibblings but married', '@I7@', '@I8@')])

	def test_first_cousin_should_not_marry(self):
		self.assertEqual(first_cousin_should_not_marry(),[('Error US 19 first cousins are getting married', '@F3@')])

	def test_male_last_names(self):  # test user story 16 test case
		self.assertEqual(male_last_names(individual_list, family_list), ('error in family','@F2@', ' male child last name not the same as fathers last name'))
		self.assertNotEqual(male_last_names(individual_list, family_list), 1)
		self.assertTrue(male_last_names(individual_list, family_list))
		self.assertIsNotNone(male_last_names(individual_list, family_list))
		self.assertIsNot(male_last_names(individual_list, family_list), '')
	
	def test_no_marriage_to_children(self):  #test User story 17 test case 
		self.assertEqual(no_marriage_to_children(individual_list , family_list), ("No individuals in family are married to parents."))
		self.assertNotEqual(no_marriage_to_children(individual_list , family_list), 1)
		self.assertTrue(no_marriage_to_children(individual_list , family_list))
		self.assertIsNotNone(no_marriage_to_children(individual_list , family_list))
		self.assertIsNot(no_marriage_to_children(individual_list , family_list), "")
	
# For User Story 23 8
class TestBirthDay(unittest.TestCase):
	def test_unique_name_and_birthday(self):
		self.assertEqual(Unique_name_and_birthday(individual_list), "")

	def test_birth_before_mariage_of_parents(self):
		self.assertEqual(Birth_before_mariage_of_parents(individual_list,family_list), "Error: Krappa Chino Birth at 2018 SEP 7 have been duplicated ")

# User Story 21
	def test_aunts_and_uncles(self):
		self.assertEqual(Aunts_and_uncles(individual_list,family_list), "Error: Aunts and uncles shouldn't marry their nieces or nephews @I8@ and @I7@ shouldn't been married ")
		
"""
	

"""



if __name__ == '__main__':
	unittest.main(exit=False, verbosity=2)
