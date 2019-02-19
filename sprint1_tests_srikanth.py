from HW3AdityaMunot import *
import unittest

class TestSprint1(unittest.TestCase):

    def test_marriage_before_death_1(self):
        self.assertEqual(marriage_before_death(family_list, individual_list), 0)
        self.assertNotEqual(marriage_before_death(family_list, individual_list), 1)
        self.assertFalse(marriage_before_death(family_list, individual_list))
        self.assertIsNotNone(marriage_before_death(family_list, individual_list))
        self.assertIsNot(marriage_before_death(family_list, individual_list), '')
    
    def test_siblings_fewer_than_15(self):
        self.assertEqual(fewer_than_15_siblings(family_list),0)
        self.assertNotEqual(fewer_than_15_siblings(family_list),1)
        self.assertFalse(fewer_than_15_siblings(family_list))
        self.assertIsNotNone(fewer_than_15_siblings(family_list))
        self.assertIsNot(fewer_than_15_siblings(family_list), "")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

