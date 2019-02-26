import user_story47 as user
import unittest
import datetime

# Test Case

class user_story47_Test(unittest.TestCase):

    def test_Marriage_befor_divorce(self): 
            self.assertEqual(user.Marriage_befor_divorce(family_list), 0)

    def test_Less_then_150_years_old(self):  
         self.assertEqual(user.test_Less_then_150_years_old(family_list), 0)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
