from HW3AdityaMunot import *
import unittest

# User Story 1


def CheckDates(edate):  # Check dates in gedcom file are before current date
    if edate == "NA":
        return edate
    else:
        edate = datetime.strptime(edate, "%Y %b %d")
        today = datetime.today()
        if edate > today:
            return "NA"
        else:
            return edate.strftime("%Y %b %d")

# User Story 6


def Divorce_before_death(divor, hid, wid):  # Check Divorce before death
    if divor == "NA":
        return divor
    else:
        for i in individual_list:
            if hid in i[0]:
                hdeath = i[4]
            if wid in i[0]:
                wdeath = i[4]
        if divor < hdeath and divor < wdeath:
            return divor
        else:
            return "NA"

# Test Case


class GedreaderTest(unittest.TestCase):
    def test_BirthDates(self):
        today = datetime.today()
        for i in individual_list:
            self.assertLess(datetime.strptime(CheckDates(i[3]), "%Y %b %d"), today)

    def test_DeathDates(self):
        today = datetime.today()
        for i in individual_list:
                if i[4] != "NA":
                        self.assertLess(datetime.strptime(CheckDates(i[4]), "%Y %b %d"), today)

    def test_MarriedDates(self):
        today = datetime.today()
        for i in family_list:
                self.assertLess(datetime.strptime(CheckDates(i[3]), "%Y %b %d"), today)

    def test_DivorcedDates(self):
        today = datetime.today()
        for i in family_list:
                if i[4] != "NA":
                        self.assertLess(datetime.strptime(CheckDates(i[4]), "%Y %b %d"), today)

    def test_Divorce_before_death(self):
        for i in family_list:
            self.assertEqual(Divorce_before_death(i[4], i[1], i[2]), "NA")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
