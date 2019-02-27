from HW3AdityaMunot import *
# User Story 1


def CheckDates(Tlist):  # Check dates in gedcom file are before current date
    today = datetime.today()
    for i in Tlist:
        if i[3] != "NA":
            tdate = datetime.strptime(i[3], "%Y %b %d")
            if tdate > today:
                i[3] = "NA"
                print(f"Error: US1- {i[0]} date {i[3]} is after current Date {today} ")
        if i[4] != "NA":
            tdate = datetime.strptime(i[4], "%Y %b %d") 
            if tdate > today:
                i[4] = "NA"
                print(f"Error: US1- {i[0]} date {i[4]} is after current Date {today} ")
    return Tlist

# User Story 6


def Divorce_before_death(family_list):  # Check Divorce before death
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

# User Story 4


def Marriage_before_divorce(family_list):
    for i in family_list:
        if i[4] != "NA":
            Mdate = datetime.strptime(i[3], "%Y %b %d")
            Ddate = datetime.strptime(i[4], "%Y %b %d")
            if Mdate > Ddate:
                i[4] = "NA"
                print(f"Error: US4- Family {i[0]} is Divorce date {i[4]} is before Marriage ")
    return family_list

# User Story 7


def lessthen150(individual_list):
    for i in individual_list:
        age = calculate_age(i[3], i[4])
        if age > 150:
            i[4] == "NA"
            print(f"Error: US7- Individual {i[0]} age is greater than 150 years ")
    return individual_list

def marriage_before_death(family_list, individual_list): #user story 05

    l=list()
    for i in individual_list:
        if i[5] is not "NA" and i[4] is not "NA":
            for j in family_list:
                if i[5]== j[0] and i[0] == j[1]:
                    if j[3] > i[4]:
                        l.append(j[0])
    return l, " list of families who do not have marriage date before death date of one of the members"

def fewer_than_15_siblings(family_list): #user story 15
    
    l=list()
    for i in family_list:
        if len(i[5]) > 15:
            l.append(i[0])
    return l, " list of families have more than 15 siblings"

# Running User Stories

individual_list = CheckDates(individual_list)  # Running User Story 1
family_list = CheckDates(family_list)  # Running User Story 1
family_list = Divorce_before_death(family_list)  # Running User Story 6
family_list = Marriage_before_divorce(family_list)  # Running User Story 4       
individual_list = lessthen150(individual_list)  # Running User Story 7
