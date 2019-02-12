"""
Parsing the Gedcom File and print the result

Author: Aditya R Munot
"""
import re

Tags = {"HEAD": "0", "TRLR": "0", "NOTE": "0", "NAME": "1", "SEX": "1",
        "BIRT": "1", "DEAT": "1", "FAMC": "1", "FAMS": "1", "MARR": "1",
        "HUSB": "1", "WIFE": "1", "CHIL": "1", "DIV": "1", "DATE": "2"}


def Gedreader(path):
    try:
        fp = open(path)
    except FileNotFoundError:
        raise FloatingPointError(" can't open:", path)

    else:
        for line in fp:
            print("-->", line.strip())
            x = re.split("\s", line.strip(), 3)
            if Tags.get(x[1]) == x[0] or x[-1] == "INDI" or x[-1] == "FAM":
                valid = 'Y'
            else:
                valid = 'N'
            x.insert(2, valid)
            y = "|".join(x)
            print('<--', y)


Gedreader(input("Enter the path for Gedcom file:"))
