from datetime import date, datetime

# User Story 1


def CheckDates(Tlist):  # Check dates in gedcom file are before current date
    today = datetime.today()
    for i in Tlist:
        if i[3] != "NA":
            tdate = datetime.strptime(i[3], "%Y %b %d")
            if tdate > today:
                i[3] = "NA"
        if i[4] != "NA":
            tdate = datetime.strptime(i[4], "%Y %b %d") 
            if tdate > today:
                i[4] = "NA"
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
    return family_list
