from HW3AdityaMunot import *
from datetime import timedelta


def CheckDates(Tlist):  # Check dates in gedcom file are before current date
	today = datetime.today()
	for i in Tlist:
		if i[3] != "NA":
			tdate = datetime.strptime(i[3], "%Y %b %d")
			if tdate > today:
				i[3] = "NA"
				print(
					f"Error: US1- {i[0]} date {i[3]} is after current Date {today} ")
		else:
			print(f"Error: US1- {i[0]} date is not mentioned")
		if i[4] != "NA":
			tdate = datetime.strptime(i[4], "%Y %b %d")
			if tdate > today:
				i[4] = "NA"
				print(
					f"Error: US1- {i[0]} date {i[4]} is after current Date {today} ")
	return Tlist


def Divorce_before_death(Tfamily_list):  # User Story 6
	# Check Divorce before death
	for i in Tfamily_list:
		if i[4] != "NA":
			for j in individual_list:
				if i[1] in j[0]:
					hdeath = j[4]
				if i[1] in j[0]:
					wdeath = j[4]
			if i[4] > hdeath and i[4] > wdeath:
				print(f"Error: US6- Divorce date {i[4]} is After Death ")
				i[4] = "NA"
	return Tfamily_list


def Marriage_before_divorce(Tfamily_list):  # User Story 4
	for i in Tfamily_list:
		if i[4] != "NA":
			Mdate = datetime.strptime(i[3], "%Y %b %d")
			Ddate = datetime.strptime(i[4], "%Y %b %d")
			if Mdate > Ddate:
				i[4] = "NA"
				print(
					f"Error: US4- Family {i[0]} is Divorce date {i[4]} is before Marriage ")
	return Tfamily_list


def lessthen150(Tindividual_list):  # User Story 7
	for i in Tindividual_list:
		age = calculate_age(i[3], i[4])
		if type(age) == int:
			if (age > 150):
				i[3] = "NA"
				print(
					f"Error: US7- Individual {i[0]} age is greater than 150 years ")
	return Tindividual_list


def marriage_before_death(family_list, individual_list):  # user story 05

	l = list()
	for i in individual_list:
		if i[5] is not "NA" and i[4] is not "NA":
			for j in family_list:
				if i[5] == j[0] and i[0] == j[1]:
					if j[3] > i[4]:
						print("Error: ", j[0],
							  "family has death before marriage")
						l.append(j[0])
	return l, " list of families who do not have marriage date before death date of one of the members"


def fewer_than_15_siblings(family_list):  # user story 15

	l = list()
	for i in family_list:
		if len(i[5]) > 14:
			print("Error: ", i[0],
				  "family has more than 15 or greater siblings")
			l.append(i[0])
	return l, " list of families have 15 or more siblings"


def birth_before_death(individual_list):
	"""Check if death before birth"""
	l = []
	for i in individual_list:
		id = i[0]
		if i[3] != "NA" and i[4] != "NA":
			birth = datetime.strptime(i[3], "%Y %b %d")
			death = datetime.strptime(i[4], "%Y %b %d")
			if birth > death:  # if real person
				val = ("Error: User", id, "was dead before birth")
				l.append(val)
	return l


def birth_before_marriage(individual_list, family_list):  # user story 03
	"""Check if married before birth"""
	l = []
	for i in individual_list:
		if i[3] != "NA":
			birth = datetime.strptime(i[3], "%Y %b %d")
			ind_id = i[0]
			fam_id = i[5]
			for j in family_list:
				if (i[0] == j[1] or i[0] == j[2]) and j[3] != "NA":
					marriage = datetime.strptime(j[3], "%Y %b %d")
					if birth > marriage:
						val = ("Error: User", fam_id,
							   "was born before marraige")
						l.append(val)
	return l


def marriage_under_age_14():
	l = []
	for k in family_list:
		id = k[0]
		marriage = k[3]
		husbandid = k[1]
		wifeid = k[2]
		for i in individual_list:
			if husbandid in i and husbandid != "NA":
				husbandbirth = i[3][:4]
				try:
					legal_husband_age = int(husbandbirth)+14
				except ValueError:
					continue
			if wifeid in i:
				wifebirth = i[3][:4]
				try:
					legal_wife_age = int(wifebirth)+14
				except ValueError:
					continue
		for i in family_list:
			try:
				if legal_husband_age > int(marriage[:4]) or legal_wife_age > int(marriage[:4]):
					l.append(("Error,", id, "married when less than 14"))
			except ValueError:
				continue
	return (dict.fromkeys(l))


def parents_birth_before_death():  # birth before death of parents
	l = []
	for i in family_list:
		children = i[5]
		children_dob = []
		if len(children) > 0:
			dad_id = i[1]
			mom_id = i[2]
			for j in individual_list:
				if j[0] in children:
					if j[3] != "NA":
						children_dob.append(
							datetime.strptime(j[3], "%Y %b %d"))
				if j[0] == mom_id:
					if j[4] != "NA":
						dom = datetime.strptime(j[4], "%Y %b %d")
				elif j[0] == dad_id:
					if j[4] != "NA":
						dodd = datetime.strptime(j[4], "%Y %b %d")
			for f in children_dob:
				try:
					if f > dom and f > dodd:
						l.append(
							("Error", i[0], "children born after parents death"))
				except UnboundLocalError:
					continue
	return l


def no_bigamy(family_list, individual_list):  # user story 11
	error = 0
	for i in family_list:
		fam = i[0]
		spouse1 = i[1]
		spouse2 = i[2]
		div = i[4]
		for j in family_list:
			if j[0] != fam:
				if j[1] == spouse1:
					if div == "NA":
						for k in individual_list:
							if k[0] == spouse2 and k[4] != "NA" and k[4] > j[3]:
									print(f"Error: US 11 - family {fam} and family {j[0]} marriage is bigamy")
									error += 1
					elif div < j[3]:
						print(f"Error: US 11 - family {fam} and family {j[0]} marriage is bigamy")
						error += 1
				elif j[2] == spouse2:
					if div == "NA":
						for k in individual_list:
							if k[0] == spouse1 and k[4] != "NA" and k[4] > j[3]:
									print(f"Error: US 11 - family {fam} and family {j[0]} marriage is bigamy")
									error += 1
					elif div < j[3]:
						print(f"Error: US 11 - family {fam} and family {j[0]} marriage is bigamy")
						error += 1
	if error == 0:
		print("US 11: There is no bigamy in the Family")
	return error


def get_age_with_id(id, individual_list):  # created for User Stories 12
	if id != "NA":
		for i in individual_list:
			if i[0] == id:
				return calculate_age(i[3], i[4])
	else:
		return 'NA'


def parents_not_too_old(family_list, individual_list):  # User Story 12
	error = 0
	for i in family_list:
		if len(i[5]) != 0:
			husband_age = get_age_with_id(i[1], individual_list)
			wife_age = get_age_with_id(i[2], individual_list)
			child_age = get_age_with_id(i[5][-1], individual_list)
			if husband_age == "NA"or wife_age == "NA"or child_age == "NA":
				print(f"Error: US 12 - {i[0]} family is missing date")
				error += 1
				continue
			elif (husband_age-child_age) > 80 or (wife_age-child_age) > 60:
				print(f"Error: US 12 - {i[0]} family is parents are too old for kids")
				error += 1
	if error == 0:
		print("US 12: all parents are in appropriate age for children")
	return error


def correct_gender_for_role(family_list, individual_list): #user story 21
	for i in family_list:
		hid=i[1]
		wid=i[2]

		for p in individual_list:
			if p[0]==hid:
				if p[2]=="F":
					return(f"error: US 21 gender role for", p[0],"not correct")
		for q in individual_list:
			if q[0]==wid:
				if q[2]=="M":
					return(f"error: US 21 gender role for", q[0], "not correct")
	return(f"error: US 21 gender role are correct")


def unique_ids(family_list, individual_list):  # user story 22
	uid = list()
	fid = list()

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

def sibling_should_not_mawrry():
	"""US 18 Siblings should not marry"""
	l = []
	for i in family_list:
		husband = i[1]
		wife = i[2]
		for j in family_list:
			if len(j[5]) > 1:
				if husband in j[5] and wife in j[5]:
					l.append(("Error both are sibblings but married", husband, wife))
	return l

def first_cousin_should_not_marry():
	"""First cousin should not marry US 19"""
	l = []
	hfather = None
	wfather = None
	hmother = None
	wmother = None
	for i in family_list:
		chhusband = i[1]
		chwife = i[2]
		if chwife != "NA" and chhusband != "NA":
			for j in family_list:
				if len(j[5])>1:
					if chhusband in j[5]:
						hfather = j[1]
						hmother = j[2]
					if chwife in j[5]:
						wfather = j[1]
						wmother = j[2]
		for k in family_list:
			if ((wfather and hmother) in k[5]) or ((hfather and wmother) in k[5]):
				l.append(("Error US 19 first cousins are getting married", k[0]))
	return l


#User Story 20
#Aunts and uncles shouldn't marry their nieces or nephews
def Aunts_and_uncles(individual_list, family_list):
	str = ''
	for grand_family in family_list:
		for individual_1 in grand_family[5]:
			for individual_2 in grand_family[5]:
				for family in family_list:
					if ((family[1] == individual_1 and family[2] == individual_2) or(family[2] == individual_1 and family[1] == individual_2)):
						str = f"Error: Aunts and uncles shouldn't marry their nieces or nephews {individual_1} and {individual_2} shouldn't been married "
						print(str)
	return str

#User Story 30
#List all living married people
def List_all_living_married_people(individual_list, family_list):
	str = ''
	married_people = []
	for i in individual_list:
		if checkAlive(i[4]):
			for family in family_list:
				if family[1] == i[0] or family[2] == i[0]:
					married_people.append(i)
	for people in married_people:
		print(people[0] + ' , name: ' + people[1])

def get_detail(id, individual_list):
	for i in individual_list:
		if i[0] == id:
			return i


#User Story 31
#List all living singles
def List_all_living_singles(individual_list, family_list):
	str = ''
	singles = []
	for i in individual_list:
		if checkAlive(i[4]):
			isSingle = False
			for family in family_list:
				if family[1] == i[0] or family[2] == i[0]:
					isSingle = True
			if isSingle:
				singles.append(i)
	for people in singles:
		print(people[0] + ' , name: ' + people[1])


#  User Story 13
def Siblings_spacing():
	error = 0
	for i in family_list:
		no_of_Child = len(i[5])
		if no_of_Child > 1:
			date = get_detail(i[5][0], individual_list)[3]
			if date != 'NA':
				prev = datetime.strptime(date, "%Y %b %d")
				for j in range(1, no_of_Child):
					date = get_detail(i[5][j], individual_list)[3]
					if date != "NA":
						curr = datetime.strptime(date, "%Y %b %d")
						datediff = prev - curr
						days = int(abs(datediff / timedelta(days=1)))
						if days > 2 and days < 240:
							print(f"Error: US13- Sibling Spacing Error in {i[5][j-1]} & {i[5][j]}")
							error += 1
						prev = curr
					else:
						print(f'Error: US13 - Date Error While Check US13')
			else:
				print(f'Error: US13 - Date Error While Check US13')
	return error


#  User Story 14
def Multiple_birth():
	error = 0
	for i in family_list:
		no_of_Child = len(i[5])
		if no_of_Child > 1:
			m = []
			count = 0
			date = get_detail(i[5][0], individual_list)[3]
			if date != 'NA':
				prev = datetime.strptime(date, "%Y %b %d")
				for j in range(1, no_of_Child):
					date = get_detail(i[5][j], individual_list)[3]
					if date != 'NA':
						curr = datetime.strptime(date, "%Y %b %d")
						if prev == curr:
							count = count + 1
							prev = curr
						else:
							count = 0
							prev = curr
						if count > 5:
							print(f"Error: US14 - Multiply birth detected in family {i[0]}")
							error += 1
					else:
						print(f'Error: US14 - Date Error While Check US14')
			else:
				print(f'Error: US14 - Date Error While Check US14')
	return error


def male_last_names(individual_list, family_list): #user story 16
	for i in family_list:
		father_name= Getname(individual_list, i[1]).split()
		father_last_name=father_name[-1]

		for j in individual_list:
			if j[0] in i[5]:
				if j[2]=="M":
					m_child_name=j[1].split()
					if m_child_name[-1]  != father_last_name:
						return ("error in family",i[0]," male child last name not the same as fathers last name" )

	return("all male child last names in the family are the same.")


def no_marriage_to_children(individual_list , family_list): #User story 17
	for i in family_list:
		for c in i[5]:
			for j in individual_list:
				if j[0]==c:
					if (j[5]== i[1] ) or ( j[5] == i[2]):
						return("ERROR in family ",i[0], " child is married to parent")

	return("No individuals in family are married to parents.")


def list_living_married(): # US 30
	"""list of married individuals who are living"""
	married_list = []
	for i in individual_list:
		if i[6] != "NA" and i[4] != "NA":
			married_list.append(i[0])
	return married_list


def unique_first_name(): #US 25
	"""list of people with unique names"""
	list_first_name = []
	for i in individual_list:
		fname = i[1].split()
		if fname not  in list_first_name:
			list_first_name.append(fname[0])
	return list_first_name

#Running User Stories
print(birth_before_death(individual_list))
print(birth_before_marriage(individual_list, family_list))
print(list(marriage_under_age_14()))
print(list(parents_birth_before_death()))
print(correct_gender_for_role(family_list, individual_list))
print(unique_ids(family_list,individual_list))
print(list(sibling_should_not_mawrry()))
print(list(first_cousin_should_not_marry()))
print("list of living married", list(list_living_married()))
print("list of people with unique name", list(unique_first_name()))


CheckedIndividuals = CheckDates(individual_list)  # Running User Story 1
CheckedFamilylist = CheckDates(family_list)  # Running User Story 1
Checked_Div_bef_dea = Divorce_before_death(family_list)  # Running User Story 6
Checked_Mar_bef_div = Marriage_before_divorce(
	family_list)  # Running User Story 4
checked_Les_Th_150 = lessthen150(individual_list)  # Running User Story 7
Checked_marriage_before_death = marriage_before_death(
	family_list, individual_list)  # Running User 05
Checked_fewer_than_15_siblings = fewer_than_15_siblings(
	family_list)  # Running User Story 15

checked_no_bigamy = no_bigamy(family_list, individual_list)  # Running User Story 11
checked_parents_not_too_old = parents_not_too_old(family_list, individual_list)  # Running User Story 12
checked_Sibling_spacing = Siblings_spacing() # running User Story 13
checked_Multiple_birth = Multiple_birth() # running User Story 14
print(male_last_names(individual_list,family_list)) #running user story 16
print(no_marriage_to_children(individual_list,family_list))# running user story 17
