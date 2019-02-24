"""
Project 03: Parsing, Retrieving Data and printing in pretty table.

Author: Aditya R Munot
"""
# Importing file
from prettytable import PrettyTable
from datetime import date, datetime


def familyList():  # Initialising a empty list for family
	familylist = ["NA" for i in range(6)]
	familylist[5] = []
	return familylist


def individualList():  # Initialising a empty list for family
	return ["NA" for i in range(7)]


def Getname(individualList, IDnumber):  # Name of Individual
	for i in individualList:
		if(i[0] == IDnumber):
			return i[1]


def calculate_age(dob, dod):  # Calculate Age using Date of birth & Death
	birth_time = datetime.strptime(dob, "%Y %b %d")
	dod = str(dod)
	if dod == "NA":
		today = date.today()
		return today.year - birth_time.year - ((today.month, today.day) < (birth_time.month, birth_time.day))
	else:
		death_time = datetime.strptime(dod, "%Y %b %d")
		return death_time.year - birth_time.year - ((death_time.month, death_time.day) < (birth_time.month, birth_time.day))


def checkAlive(dod):
	if dod == "NA":
		return True
	else:
		return False


def Gedreader(path):  # parsing the gedcom file
	try:
		fp = open(path)
	except FileNotFoundError:
		raise FloatingPointError(" Can't open:", path)
	else:
		indiValue = 0
		famValue = 0
		individual_list = []
		family_list = []
		indiData = individualList()
		famData = familyList()
		for line in fp:
			s = line.split()
			if(s != []):
				if(s[0] == '0'):
					if(indiValue == 1):
						individual_list.append(indiData)
						indiData = individualList()
						indiValue = 0
					elif(famValue == 1):
						family_list.append(famData)
						famData = familyList()
						famValue = 0
					if(s[1] in ['NOTE', 'HEAD', 'TRLR']):
						pass
					else:
						if(s[2] == 'INDI'):
							indiValue = 1
							indiData[0] = (s[1])
						elif(s[2] == 'FAM'):
							famValue = 1
							famData[0] = (s[1])

				elif(s[0] == '1'):
					if(s[1] == 'NAME'):
						s[3] = s[3].replace("/", "")
						indiData[1] = s[2] + " " + s[3]
					elif(s[1] == 'SEX'):
						indiData[2] = s[2]
					elif(s[1] == 'BIRT'):
						dateID = 'BIRT'
					elif(s[1] == 'DEAT'):
						dateID = 'DEAT'
					elif(s[1] == 'MARR'):
						dateID = 'MARR'
					elif(s[1] == 'DIV'):
						dateID = 'DIV'
					elif(s[1] == 'FAMS'):
						indiData[5] = s[2]
					elif(s[1] == 'FAMC'):
						indiData[6] = s[2]
					elif(s[1] == 'HUSB'):
						famData[1] = s[2]
					elif(s[1] == 'WIFE'):
						famData[2] = s[2]
					elif(s[1] == 'CHIL'):
						famData[5].append(s[2])

				if(s[0] == '2'):
					if(s[1] == 'DATE'):
						date = s[4] + " " + s[3] + " " + s[2]
						if(dateID == 'BIRT'):
							indiData[3] = date
						elif(dateID == 'DEAT'):
							indiData[4] = date
						elif(dateID == 'MARR'):
							famData[3] = date
						elif(dateID == 'DIV'):
							famData[4] = date
					elif(s[1] == '_MARNM'):
						newname = indiData[1].split()
						indiData[1] = newname[0] + " " + s[2]
		return individual_list, family_list


def birth_before_death(id, birth, death):
	"""Check if death before birth"""
	if birth < death:  # if real person
		return death
	else:  # if not a real person put death = NA and add the error
		print("Error: User", id, "was dead before birth")
		return "NA"


def marraige_before_birth(id, marriage, husbandid, wifeid):
	"""Check if married before birth"""
	for i in individual_list:
		if husbandid in i:
			husbandbirth = i[5]
		if wifeid in i:
			wifebirth = i[5]
	# compare the deaths
	if husbandbirth < marriage and wifebirth < marriage:
		# if real family
		return marriage
	else:
		# if not a real family, return marriage as NA
		print("Error: Family", id, " member was married before being born")
		return "NA"


def marriage_before_death(id, marriage, husbandid, wifeid):
	"""Check if death before marriage"""
	# find husband death & wife death
	for i in individual_list:
		if husbandid in i:
			husbanddeath = i[4]
		if wifeid in i:
			wifedeath = i[4]
	# compare the deaths
	if marriage < husbanddeath and marriage < wifedeath:
		# if real family
		return marriage
	else:
		# if not a real family, return marriage as NA
		print("Error: Family", id, "was dead before marriage")
		return "NA"


# Function calling
individual_list, family_list = Gedreader(input("Enter GedCom File Location: "))

# printing the output about individuals
print("Individuals")
table = PrettyTable(["ID", "Name", "Gender", "Birthday",
					"Age", "Alive", "Death", "Child", "Spouse"])
for i in individual_list:
	table.add_row([i[0], i[1], i[2], i[3], calculate_age(i[3], i[4]), checkAlive(i[4]), birth_before_death(i[0], i[3], i[4]), i[6], i[5]])
print(table)

# Printing Husband's and wife's details
print("Families")
table = PrettyTable(["ID", "Married", "Divorced", "Husband ID",
					"Husband Name", "Wife ID", "Wife Name", "Child"])
for i in family_list:
	table.add_row([i[0], marriage_before_death(i[0], i[3], i[1], i[2]), i[4], i[1], Getname(individual_list, i[1]), i[2], Getname(individual_list, i[2]), i[5]])
print(table)



def marriage_before_death(family_list, individual_list): #user story 05_srikanth

	flag=0
	for i in individual_list:
		if i[5] is not "NA" and i[4] is not "NA":
			for j in family_list:
				if i[5]== j[0] and i[0] == j[1]:
					if j[3] > i[4]:
						print("marriage date greater than death death")
						flag = 1
	return flag

def fewer_than_15_siblings(family_list): #user story 15_srikanth

	flag = 0
	for i in family_list:
		if len(i[5]) > 15:
			flag+= 1
	return(flag)


# Error list for the Weird Values

birth_before_death("@I8@", "1956 FEB 11", "1906 AUG 15")
marriage_before_death("@F2@", "2010 APR 7", "@I4@", "@I5@")
