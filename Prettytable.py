from UserStories import *

# printing the output about individuals
print("Individuals")
table = PrettyTable(["ID", "Name", "Gender", "Birthday",
                     "Age", "Alive", "Death", "Child", "Spouse"])
for i in individual_list:
    table.add_row([i[0], i[1], i[2], i[3], calculate_age(i[3], i[4]),
                   checkAlive(i[4]), birth_before_death(i[0], i[3], i[4]),
                   i[6], i[5]])
print(table)

# Printing Husband's and wife's details
print("Families")
table = PrettyTable(["ID", "Married", "Divorced", "Husband ID",
                     "Husband Name", "Wife ID", "Wife Name", "Child"])
for i in family_list:
    table.add_row([i[0], marriage_before_death(i[0], i[3], i[1], i[2]), i[4],
                   i[1], Getname(individual_list, i[1]), i[2],
                   Getname(individual_list, i[2]), i[5]])
print(table)
