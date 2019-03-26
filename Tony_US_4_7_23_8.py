import unittest
#User Story 4
def Divorce_before_mariage(family_list):
	for i in family_list:
		if i[4] != 'NA':
			if i[4] < i[3]:
				print(f"Error: {i[0]} Divorce date {i[4]} is Before marriage {i[3]} ")

#User Story 7
def Less_then_150_years_old(individual_list):
	for i in individual_list:
		if i[4] != "NA":
			if calculate_age(i[3], i[4]) > 150:
				print(f"Error: individual {i[0]}, {calculate_age(i[3], i[4])} is more than 150")

#User Story 23
def Unique_name_and_birthday(individual_list):
	str = ''
	for i in individual_list:
		for j in individual_list:
			if i[0] != j[0]:
				if i[1]== j[1] and i[3]== j[3]:
					str = f"Error: {i[1]} Birth at {i[3]} have been duplicated "
					print(str)
	return str

#User Story 8
def Birth_before_mariage_of_parents(individual_list, family_list):
	str = ''
	for family in family_list:
		for child in family[5]:
			for i in individual_list:
				if child == i[0]:
					if i[3] < family[3]:
						str = f"Error: {i[1]} Birth at {i[3]} have been duplicated "
						print(str)
	return str
