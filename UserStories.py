from HW3AdityaMunot import *


def CheckDates(Tlist):  # Check dates in gedcom file are before current date
    today = datetime.today()
    for i in Tlist:
        if i[3] != "NA":
            tdate = datetime.strptime(i[3], "%Y %b %d")
            if tdate > today:
                i[3] = "NA"
                print(
                    f"Error: US1- {i[0]} date {i[3]} is after current Date {today} ")
        else:
            print(f"Error: US1- {i[0]} date is not mentioned")
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
                        print("Error: ", j[0],
                              "family has death before marriage")
                        l.append(j[0])
    return l, " list of families who do not have marriage date before death date of one of the members"


def fewer_than_15_siblings(family_list):  # user story 15

    l = list()
    for i in family_list:
        if len(i[5]) >= 15:
            print("Error: ", i[0],
                  "family has more than 15 or greater siblings")
            l.append(i[0])
    return l, " list of families have more than 15 siblings"


def birth_before_death(individual_list):
    """Check if death before birth"""
    l = []
    for i in individual_list:
        id = i[0]
        if i[3] != "NA" and i[4] != "NA":
            birth = datetime.strptime(i[3], "%Y %b %d")
            death = datetime.strptime(i[4], "%Y %b %d")
            if birth > death:  # if real person
                val = ("Error: User", id, "was dead before birth")
                l.append(val)
    return l


def birth_before_marriage(individual_list, family_list):  # user story 03
    """Check if married before birth"""
    l = []
    for i in individual_list:
        if i[3] != "NA":
            birth = datetime.strptime(i[3], "%Y %b %d")
            ind_id = i[0]
            for j in family_list:
                if (i[0] == j[1] or i[0] == j[2]) and j[3] != "NA":
                    marriage = datetime.strptime(j[3], "%Y %b %d")
                    if birth > marriage:
                        val = ("Error: User", ind_id, "was dead before birth")
                        l.append(val)
    return l

# Running User Stories


CheckedIndividuals = CheckDates(individual_list)  # Running User Story 1
CheckedFamilylist = CheckDates(family_list)  # Running User Story 1
Checked_Div_bef_dea = Divorce_before_death(family_list)  # Running User Story 6
Checked_Mar_bef_div = Marriage_before_divorce(
    family_list)  # Running User Story 4
checked_Les_Th_150 = lessthen150(individual_list)  # Running User Story 7
Checked_marriage_before_death = marriage_before_death(
    family_list, individual_list)  # Running User 05
Checked_fewer_than_15_siblings = fewer_than_15_siblings(
    family_list)  # Running User Story 15

print(birth_before_death(individual_list))
print(birth_before_marriage(individual_list, family_list))
