
# User Story 4
def Divorce_before_marriage(family_list):  # Check Divorce before marriage
    for i in family_list:
        if i[4] != "NA":
            if i[4] < i[3]:
                print(f"Error: US6- Divorce date {i[4]} is Befor marriage {i[3]} ")
    return family_list

# User Story 7

def Less_then_150_years_old(family_list):  # Check Age more than 150
    for i in individual_list:
        calculate_age(i[3], i[4]) > 150:
            print(f"Error: {calculate_age(i[3], i[4])} is more than 150")
    return error
