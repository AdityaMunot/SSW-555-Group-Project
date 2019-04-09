"""
Project 03: Parsing, Retrieving Data and printing in pretty table.

Author: Aditya R Munot, Shrey S Vaity, Srikanth Kamath, Tianhao Hao
"""
# Importing file
from prettytable import PrettyTable
from datetime import date, datetime


def familyList():  # Initialising a empty list for family
    familylist = ["NA" for i in range(6)]
    familylist[5] = []
    return familylist


def individualList():  # Initialising a empty list for family
    return ["NA" for i in range(7)]


def Getname(individualList, IDnumber):  # Name of Individual
    for i in individualList:
        if(i[0] == IDnumber):
            return i[1]


def calculate_age(dob, dod):  # Calculate Age using Date of birth & Death
    if dob != "NA":
        birth_time = datetime.strptime(dob, "%Y %b %d")
        dod = str(dod)
        if dod == "NA":
            today = date.today()
            age = today.year - birth_time.year - \
                ((today.month, today.day) < (birth_time.month, birth_time.day))
            if age > 0:
                return age
            else:
                return 'NA'
        else:
            death_time = datetime.strptime(dod, "%Y %b %d")
            age = death_time.year - birth_time.year - \
                ((death_time.month, death_time.day) <
                 (birth_time.month, birth_time.day))
            if age > 0:
                return age
            else:
                return 'NA'
    else:
        return "NA"


def checkAlive(dod):
    if dod == "NA":
        return True
    else:
        return False


def Gedreader(path):  # parsing the gedcom file
    try:
        fp = open(path)
    except FileNotFoundError:
        raise FloatingPointError(" Can't open:", path)
    else:
        indiValue = 0
        famValue = 0
        individual_list = []
        family_list = []
        indiData = individualList()
        famData = familyList()
        for line in fp:
            s = line.split()
            if(s != []):
                if(s[0] == '0'):
                    if(indiValue == 1):
                        individual_list.append(indiData)
                        indiData = individualList()
                        indiValue = 0
                    elif(famValue == 1):
                        family_list.append(famData)
                        famData = familyList()
                        famValue = 0
                    if(s[1] in ['NOTE', 'HEAD', 'TRLR']):
                        pass
                    else:
                        if(s[2] == 'INDI'):
                            indiValue = 1
                            indiData[0] = (s[1])
                        elif(s[2] == 'FAM'):
                            famValue = 1
                            famData[0] = (s[1])

                elif(s[0] == '1'):
                    if(s[1] == 'NAME'):
                        s[3] = s[3].replace("/", "")
                        indiData[1] = s[2] + " " + s[3]
                    elif(s[1] == 'SEX'):
                        indiData[2] = s[2]
                    elif(s[1] == 'BIRT'):
                        dateID = 'BIRT'
                    elif(s[1] == 'DEAT'):
                        dateID = 'DEAT'
                    elif(s[1] == 'MARR'):
                        dateID = 'MARR'
                    elif(s[1] == 'DIV'):
                        dateID = 'DIV'
                    elif(s[1] == 'FAMS'):
                        indiData[5] = s[2]
                    elif(s[1] == 'FAMC'):
                        indiData[6] = s[2]
                    elif(s[1] == 'HUSB'):
                        famData[1] = s[2]
                    elif(s[1] == 'WIFE'):
                        famData[2] = s[2]
                    elif(s[1] == 'CHIL'):
                        famData[5].append(s[2])

                if(s[0] == '2'):
                    if(s[1] == 'DATE'):
                        date = s[4] + " " + s[3] + " " + s[2]
                        if(dateID == 'BIRT'):
                            indiData[3] = date
                        elif(dateID == 'DEAT'):
                            indiData[4] = date
                        elif(dateID == 'MARR'):
                            famData[3] = date
                        elif(dateID == 'DIV'):
                            famData[4] = date
                    elif(s[1] == '_MARNM'):
                        newname = indiData[1].split()
                        indiData[1] = newname[0] + " " + s[2]
        return individual_list, family_list


# Function calling
individual_list, family_list = Gedreader(input("Enter GedCom File Location: "))
#individual_list, family_list = Gedreader("My-Family-25-Mar-2019-960.ged")
