from HW3AdityaMunot import Gedreader

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
