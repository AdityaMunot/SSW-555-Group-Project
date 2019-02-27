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


