#from gedcom_parser import *
from sprint2_userstories import *
import unittest

class TestSprint1(unittest.TestCase):

    def test_correct_gender_for_role(self):
        self.assertEqual(correct_gender_for_role(family_list, individual_list),("all gender roles in the families are correct"))
        self.assertNotEqual(correct_gender_for_role(family_list, individual_list), 1)
        self.assertTrue(correct_gender_for_role(family_list, individual_list))
        self.assertIsNotNone(correct_gender_for_role(family_list, individual_list))
        self.assertIsNot(correct_gender_for_role(family_list, individual_list), '')
    
    def test_unique_ids(self):
        self.assertEqual(unique_ids(family_list, individual_list), ("all IDs unique in Family and Individual list"))
        self.assertNotEqual(unique_ids(family_list, individual_list), 1)
        self.assertTrue(unique_ids(family_list, individual_list))
        self.assertIsNotNone(unique_ids(family_list, individual_list))
        self.assertIsNot(unique_ids(family_list, individual_list), "")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()