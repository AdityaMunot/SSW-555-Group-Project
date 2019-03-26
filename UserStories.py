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
    return l


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
            fam_id = i[5]
            for j in family_list:
                if (i[0] == j[1] or i[0] == j[2]) and j[3] != "NA":
                    marriage = datetime.strptime(j[3], "%Y %b %d")
                    if birth > marriage:
                        val = ("Error: User", fam_id,
                               "was born before marraige")
                        l.append(val)
    return l


def marriage_under_age_14():
    l = []
    for k in family_list:
        id = k[0]
        marriage = k[3]
        husbandid = k[1]
        wifeid = k[2]
        for i in individual_list:
            if husbandid in i and husbandid != "NA":
                husbandbirth = i[3][:4]
                try:
                    legal_husband_age = int(husbandbirth)+14
                except ValueError:
                    continue
            if wifeid in i:
                wifebirth = i[3][:4]
                try:
                    legal_wife_age = int(wifebirth)+14
                except ValueError:
                    continue
        for i in family_list:
            try:
                if legal_husband_age > int(marriage[:4]) or legal_wife_age > int(marriage[:4]):
                    l.append(("Error,", id, "married when less than 14"))
            except ValueError:
                continue
    return (dict.fromkeys(l))


def parents_birth_before_death():  # birth before death of parents
    l = []
    for i in family_list:
        children = i[5]
        children_dob = []
        if len(children) > 0:
            dad_id = i[1]
            mom_id = i[2]
            for j in individual_list:
                if j[0] in children:
                    if j[3] != "NA":
                        children_dob.append(
                            datetime.strptime(j[3], "%Y %b %d"))
                if j[0] == mom_id:
                    if j[4] != "NA":
                        dom = datetime.strptime(j[4], "%Y %b %d")
                elif j[0] == dad_id:
                    if j[4] != "NA":
                        dodd = datetime.strptime(j[4], "%Y %b %d")
            for f in children_dob:
                try:
                    if f > dom and f > dodd:
                        l.append(
                            ("Error", f, "children born after parents death"))
                except UnboundLocalError:
                    continue
    return l


def no_bigamy(family_list, individual_list):  # user story 11
    error = 0
    for i in family_list:
        fam = i[0]
        spouse1 = i[1]
        spouse2 = i[2]
        div = i[4]
        for j in family_list:
            if j[0] != fam:
                if j[1] == spouse1:
                    if div == "NA":
                        for k in individual_list:
                            if k[0] == spouse2 and k[4] != "NA" and k[4] > j[3]:
                                    print(f"Error: US 11 - family {fam} and family {j[0]} marriage is bigamy")
                    elif div < j[3]:
                        print(f"Error: US 11 - family {fam} and family {j[0]} marriage is bigamy")
                elif j[2] == spouse2:
                    if div == "NA":
                        for k in individual_list:
                            if k[0] == spouse1 and k[4] != "NA" and k[4] > j[3]:
                                    print(f"Error: US 11 - family {fam} and family {j[0]} marriage is bigamy")
                    elif div < j[3]:
                        print(f"Error: US 11 - family {fam} and family {j[0]} marriage is bigamy")
    if error == 0:
        print("US 11: There is no bigamy in the Family")
    return error


def get_age_with_id(id, individual_list):  # created for User Stories 12
    if id != "NA":
        for i in individual_list:
            if i[0] == id:
                return calculate_age(i[3], i[4])
    else:
        return 'NA'


def parents_not_too_old(family_list, individual_list):  # User Story 12
    error = 0
    for i in family_list:
        if len(i[5]) != 0:
            husband_age = get_age_with_id(i[1], individual_list)
            wife_age = get_age_with_id(i[2], individual_list)
            child_age = get_age_with_id(i[5][-1], individual_list)
            if husband_age == "NA"or wife_age == "NA"or child_age == "NA":
                print(f"Error: US 12 - {i[0]} family is missing date")
                error += 1
                continue
            elif (husband_age-child_age) > 80 or (wife_age-child_age) > 60:
                print(f"Error: US 12 - {i[0]} family is parents are too old for kids")
                error += 1
    if error == 0:
        print("US 12: all parents are in appropriate age for children")
    return error


def correct_gender_for_role(family_list, individual_list):  # user story 21
    for i in family_list:
        for j in individual_list:
            if i[1] == j[0]:
                if j[2] !="M":
                    return("invalid gender in family ", i[1])
            if i[2] == j[0]:
                if j[2] != "F":
                    return("invalid gender in family ", i[1])
    return "all gender roles in the families are correct" 


def unique_ids(family_list, individual_list):  # user story 22
    uid = list()
    fid = list()

    for i in family_list:
        if i[0] not in fid:
            fid.append(i[0])
        else:
            return i[0], " not unique in family list"

    for i in individual_list:
        if i[0] not in uid:
            uid.append(i[0])
        else:
            return i[0], " not unique in individual list"

    return "all IDs unique in Family and Individual list" 





checked_no_bigamy = no_bigamy(family_list, individual_list)  # Running User Story 11
checked_parents_not_too_old = parents_not_too_old(family_list, individual_list)  # Running User Story 12


# Running User Stories
print(birth_before_death(individual_list))
print(birth_before_marriage(individual_list, family_list))
print(list(marriage_under_age_14()))
print(list(parents_birth_before_death()))
print(correct_gender_for_role(family_list, individual_list))
print(unique_ids(family_list,individual_list))


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
