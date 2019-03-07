from HW3AdityaMunot import *


def CheckDates(Tlist):  # User Story 1
    # Check dates in gedcom file are before current date
    today = datetime.today()
    for i in Tlist:
        if i[3] != "NA":
            tdate = datetime.strptime(i[3], "%Y %b %d")
            if tdate > today:
                i[3] = "NA"
                print(
                    f"Error: US1- {i[0]} date {i[3]} is after current Date {today} ")
        else:
            print(f"Error: US1- {i[0]} date is not mentioned ")
        if i[4] != "NA":
            tdate = datetime.strptime(i[4], "%Y %b %d")
            if tdate > today:
                i[4] = "NA"
                print(
                    f"Error: US1- {i[0]} date {i[4]} is after current Date {today} ")
    return Tlist


def Divorce_before_death(family_list):  # User Story 6
    # Check Divorce before death
    for i in family_list:
        if i[4] != "NA":
            for j in individual_list:
                if i[1] in j[0]:
                    hdeath = j[4]
                if i[1] in j[0]:
                    wdeath = j[4]
            if i[4] > hdeath and i[4] > wdeath:
                i[4] = "NA"
                print(f"Error: US6- Divorce date {i[4]} is After Death ")
    return family_list


def Marriage_before_divorce(family_list):  # User Story 4
    for i in family_list:
        if i[4] != "NA":
            Mdate = datetime.strptime(i[3], "%Y %b %d")
            Ddate = datetime.strptime(i[4], "%Y %b %d")
            if Mdate > Ddate:
                i[4] = "NA"
                print(
                    f"Error: US4- Family {i[0]} is Divorce date {i[4]} is before Marriage ")
    return family_list


def lessthen150(individual_list):  # User Story 7
    for i in individual_list:
        age = calculate_age(i[3], i[4])
        if type(age) == int:
            if (age > 150):
                i[3] = "NA"
                print(
                    f"Error: US7- Individual {i[0]} age is greater than 150 years ")
    return individual_list


def marriage_before_death(family_list, individual_list):  # user story 05
    l = list()
    for i in individual_list:
        if i[5] is not "NA" and i[4] is not "NA":
            for j in family_list:
                if i[5] == j[0] and i[0] == j[1]:
                    if j[3] > i[4]:
                        l.append(j[0])
    return l, " list of families who do not have marriage date before death date of one of the members"


def fewer_than_15_siblings(family_list):  # user story 15
    l = list()
    for i in family_list:
        if len(i[5]) > 15:
            l.append(i[0])
    return l, " list of families have more than 15 siblings"


def birth_before_death(id, birth, death):  # user story 02
    """Check if death before birth"""
    if birth < death:  # if real person
        return death
    else:  # if not a real person put death = NA and add the error
        print("Error: User", id, "was dead before birth")
        return "NA"


def birth_before_marriage(id, marriage, husbandid, wifeid):  # user story 03
    """Check if married before birth"""
    for i in individual_list:
        if husbandid in i:
            husbandbirth = i[5]
        if wifeid in i:
            wifebirth = i[5]
    # compare the deaths
    if husbandbirth < marriage and wifebirth < marriage:
        # if real family
        return marriage
    else:
        # if not a real family, return marriage as NA
        print("Error: Family", id, " member was married before being born")
        return "NA"


def marriage_before_death(id, marriage, husbandid, wifeid):  # user story 05
    """Check if death before marriage"""
    # find husband death & wife death
    for i in individual_list:
        if husbandid in i:
            husbanddeath = i[4]
        if wifeid in i:
            wifedeath = i[4]
    # compare the deaths
    if marriage < husbanddeath and marriage < wifedeath:
        # if real family
        return marriage
    else:
        # if not a real family, return marriage as NA
        print("Error: Family", id, "was dead before marriage")
        return "NA"

# Running User Stories


CheckedIndividuals = CheckDates(individual_list)  # Running User Story 1
CheckedFamilylist = CheckDates(family_list)  # Running User Story 1
Checked_Div_bef_dea = Divorce_before_death(family_list)  # Running User Story 6
Checked_Mar_bef_div = Marriage_before_divorce(family_list)  # Running User Story 4
checked_Les_Th_150 = lessthen150(individual_list)  # Running User Story 7
