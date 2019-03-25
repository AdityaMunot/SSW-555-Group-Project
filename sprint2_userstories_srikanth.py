'''user stories of sprint 2 
    author: srikanth'''

from gedcom_parser import *


def correct_gender_for_role(family_list, individual_list): #user story 21
    for i in family_list:
        for j in individual_list:
            if i[1] == j[0]:
                if j[2] !="M":
                    return("invalid gender in family ", i[1])
            if i[2] == j[0]:
                if j[2] != "F":
                    return("invalid gender in family ", i[1])
    return "all gender roles in the families are correct" 



def unique_ids(family_list, individual_list): #user story 22
    uid=list()
    fid=list()

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



print(correct_gender_for_role(family_list, individual_list))
print(unique_ids(family_list,individual_list))