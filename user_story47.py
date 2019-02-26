from datetime import date, datetime

# User Story 4
def Marriage_befor_divorce(family_list):
    error = 0
    for i in family_list:
        if i[2] == "DIV":
            dateD = datetime.strptime(i[3], "%Y %b %d")
        if i[2] == "MARR":
            dateM = datetime.strptime(i[3], "%Y %b %d")
        if dateD < dateM:
            error += 1

    return error

# User Story 7

def Less_then_150_years_old(family_list): 
    today = datetime.today()
    error = 0
    for i in family_list:
        if i[2] == "BIRT":
            dateD = datetime.strptime(i[3], "%Y %b %d")
            if (dateD - today).year > 150:
                error += 1
    return error
