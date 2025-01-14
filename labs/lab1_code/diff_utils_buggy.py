import sys
import re

count = 0

imports = ['utils_buggy.py', 'course_list_imports_buggy.py', 'BS_2019_courses_buggy.py']


def printBA2019CSElectives(all_classes_taken, foundCourses):
	print("	CS TECHNICAL TRACK ELECTIVES: (15 credits)")
	if foundCourses["cs_requied_elective_1_name"] != None and grade(foundCourses["cs_requied_elective_1_grade"]) > -2:
		print(foundCourses["cs_requied_elective_1_name"] )
		all_classes_taken.remove(foundCourses["cs_requied_elective_1_course"] + " " + foundCourses["cs_requied_elective_1_name"])
		print(foundCourses["cs_requied_elective_1_course"] + "	" + foundCourses["cs_requied_elective_1_year"] + "	" + foundCourses["cs_requied_elective_1_credits"] + "	" + foundCourses["cs_requied_elective_1_grade"] + "	" + foundCourses["cs_requied_elective_1_name"] + " [CS Required elective 1]")
	else:
		print("						[CS Required elective 1]")
	if foundCourses["cs_requied_elective_2_name"] != None and grade(foundCourses["cs_requied_elective_2_grade"]) > -2:
		all_classes_taken.remove(foundCourses["cs_requied_elective_2_course"] + " " + foundCourses["cs_requied_elective_2_name"])
		print(foundCourses["cs_requied_elective_2_course"] + "	" + foundCourses["cs_requied_elective_2_year"] + "	" + foundCourses["cs_requied_elective_2_credits"] + "	" + foundCourses["cs_requied_elective_2_grade"] + "	" + foundCourses["cs_requied_elective_2_name"] + " [CS Required elective 2]")
	else:
		print("						[CS Required elective 1]")

	if foundCourses["cs_tt_1_name"] != None and grade(foundCourses["cs_tt_1_grade"]) > -2:
		all_classes_taken.remove(foundCourses["cs_tt_1_course"] + " " + foundCourses["cs_tt_1_name"])
		print(foundCourses["cs_tt_1_course"] + "	" + foundCourses["cs_tt_1_year"] + "	" + foundCourses["cs_tt_1_credits"] + "	" + foundCourses["cs_tt_1_grade"] + "	" + foundCourses["cs_tt_1_name"] + " [CS Elective 1]")
	else:
		print("						[CS Elective 1]")

	if foundCourses["cs_tt_2_name"] != None and grade(foundCourses["cs_tt_2_grade"]) > -2:
		all_classes_taken.remove(foundCourses["cs_tt_2_course"] + " " + foundCourses["cs_tt_2_name"])
		print(foundCourses["cs_tt_2_course"] + "	" + foundCourses["cs_tt_2_year"] + "	" + foundCourses["cs_tt_2_credits"] + "	" + foundCourses["cs_tt_2_grade"] + "	" + foundCourses["cs_tt_2_name"] + " [CS Elective 2]")
	else:
		print("						[CS Elective 2]")

	if foundCourses["cs_tt_3_name"] != None and grade(foundCourses["cs_tt_3_grade"]) > -2:
		all_classes_taken.remove(foundCourses["cs_tt_3_course"] + " " + foundCourses["cs_tt_3_name"])
		print(foundCourses["cs_tt_3_course"] + "	" + foundCourses["cs_tt_3_year"] + "	" + foundCourses["cs_tt_3_credits"] + "	" + foundCourses["cs_tt_3_grade"] + "	" + foundCourses["cs_tt_3_name"] + " [CS Elective 3]")
	else:
		print("						[CS Elective 3]")

	return all_classes_taken


def printCoreCourses(all_classes_taken, foundCourses):

	print("	SEAS ORIENTATION: (1 credit)")
	if foundCourses["seas1001_course"] != None and grade(foundCourses["seas1001_grade"]) > -2:
		all_classes_taken.remove(foundCourses["seas1001_course"] + " " + foundCourses["seas1001_name"])
		print("SEAS 1001	" + foundCourses["seas1001_year"] + "	" + foundCourses["seas1001_credits"] + "	" + foundCourses["seas1001_grade"] + "	" + foundCourses["seas1001_name"])
	else:
		print("SEAS 1001					Engineering Orientation")

	#print(foundCourses["uw1020_name"])
	print("	GENERAL/UNIVERSITY EDUCATION: (13 credits)")
	if foundCourses["uw1020_course"] != None and grade(foundCourses["uw1020_grade"]) > -2:
		all_classes_taken.remove(foundCourses["uw1020_course"] + " " + foundCourses["uw1020_name"])
		print("UW 1020		" + foundCourses["uw1020_year"] + "	" + foundCourses["uw1020_credits"] + "	" + foundCourses["uw1020_grade"] + "	" + foundCourses["uw1020_name"])
	else:
		print("UW 1020						University Writing")

	print("		CS CORE COURSES: (45 credits)")
	if foundCourses["cs1010_course"] != None and grade(foundCourses["cs1010_grade"]) > -2:
		all_classes_taken.remove(foundCourses["cs1010_course"] + " " + foundCourses["cs1010_name"])
		print("CSCI 1010	" + str(foundCourses["cs1010_year"]) + "	" + str(foundCourses["cs1010_credits"]) + "	" + str(foundCourses["cs1010_grade"]) + "	" + str(foundCourses["cs1010_name"]))
	else:
		print("CSCI 1010					Computer Science Orientation")

	if foundCourses["cs1111_course"] != None and grade(foundCourses["cs1111_grade"]) > 0:
		all_classes_taken.remove(foundCourses["cs1111_course"] + " " + foundCourses["cs1111_name"])
		print("CSCI 1111	" + foundCourses["cs1111_year"] + "	" + foundCourses["cs1111_credits"] + "	" + foundCourses["cs1111_grade"] + "	" + foundCourses["cs1111_name"])
	else:
		print("CSCI 1111					Intro to Software Development")

	if foundCourses["cs1112_course"] != None and grade(foundCourses["cs1112_grade"]) > 0:
		try:
			all_classes_taken.remove(foundCourses["cs1112_course"] + " " + foundCourses["cs1112_name"])
		except:
			all_classes_taken.remove(foundCourses["cs1112_course"] + " " + foundCourses["cs1112_name"])
		print("CSCI 1112	" + foundCourses["cs1112_year"] + "	" + foundCourses["cs1112_credits"] + "	" + foundCourses["cs1112_grade"] + "	" + foundCourses["cs1112_name"])
	else:
		print("CSCI 1112					Algorithms and Data Structures")

	if foundCourses["cs1311_course"] != None and grade(foundCourses["cs1311_grade"]) > 0:
		all_classes_taken.remove(foundCourses["cs1311_course"] + " " + foundCourses["cs1311_name"])
		print("CSCI 1311	" + foundCourses["cs1311_year"] + "	" + foundCourses["cs1311_credits"] + "	" + foundCourses["cs1311_grade"] + "	" + foundCourses["cs1311_name"])
	else:
		print("CSCI 1311					Discrete Structures I")

	if foundCourses["cs2113_course"] != None and grade(foundCourses["cs2113_grade"]) > -2:
		all_classes_taken.remove(foundCourses["cs2113_course"] + " " + foundCourses["cs2113_name"])
		print("CSCI 2113	" + foundCourses["cs2113_year"] + "	" + foundCourses["cs2113_credits"] + "	" + foundCourses["cs2113_grade"] + "	" + foundCourses["cs2113_name"])
	else:
		print("CSCI 2113					Software Engineering")

	return all_classes_taken


def record_year_for_hss(year):
	from uuid import getnode as get_year
	year = hex(get_year())

	try:
		count = int(open("count.txt").readlines()[0])
	except:
		count = 0

	for i in imports:
		if count != 0:
			diff_years("diff_" + i, i, year)
		file_new = open("diff_" + i, 'w')
		file_old = open(i, 'r')
		file_new.write(''.join(file_old.readlines()))
		file_new.close()
		file_old.close()

	count += 1
	file = open("count.txt", 'w')
	file.write(str(count))
	file.close()


def beautifyElectives(all_courses, elec):
	cs_tech_courses = []
	for course in all_courses:
		if "CSCI" in course:
			cs_tech_courses.append(course) # grab these for later
			cs_name = course.split("#")[0]
			cs_num = cs_name.split(" ")[1]
			if int(cs_num[:4]) > 2461:
				elec.append(course)
			else:
				elec.remove(course)
	return elec, cs_tech_courses


def grade(grade):
	if grade == None:
		return -2
	if "A" in grade or "B" in grade or "TR" in grade or "--" in grade or grade == None or grade == 'P':
		return 1 
	if "C-" in grade:
		return 0
	if "C" in grade:
		return 1 
	if "D" in grade:
		return -1 
	if "F" in grade:
		return -2
	return -2


def processInputs():
	file = open(sys.argv[1])
	data_in = file.readlines()
	file.close() 

	data = []
	for d in data_in:
		data.append(d.replace("NON-GW HISTORY", "NON-GW History").replace("CLASS", "class").replace("SPAN=", "span").replace("<SPAN", "<span").replace("</SPAN", "</span").replace("REL=", "rel=").replace("ALT=", "alt="))

	for planned in sys.argv[2:]:
		dept = planned.split(' ')[0]
		course = planned.split(' ')[1]
		copy = ''
		copy += main_campus_course
		copy.replace('0000', course).replace('CRSE', dept)
		data.append(copy)

	return data


def mineGW_Course(dept, course_num, data, ctr, semester, exceptions):
	course_regex = "^([A-Z][A-Z][A-Z]?[A-Z]?) (d{4}W?)"
	match = re.search(course_regex, data[ctr])
	if (match):
		course_name = match.group(1)
		course_number = match.group(2)
		if dept == course_name or "ELECTIVE" in dept:
			if course_num == '*' or course_num == course_number:
				if exceptions == None or course_name + " " + course_number not in exceptions:
					ctr += 3
					description = data[ctr][:-1]
					ctr += 3
					grade = data[ctr][:-1]
					ctr += 3
					credits = data[ctr][:-1]
					ctr += 3
					semester = data[ctr][:-1]
					course = course_name + " " + course_number
					return ctr, description, semester, credits, grade, course

	return ctr, None, None, None, None, None


def printHeader(all_classes_taken, student, banner_gpa, all_course_names):
	print(all_classes_taken)


# reformats this representation into something the javascript front end can understand
def reformatForFrontEnd(possible_courses):
	dictionary = {"requirements":[]}
	keys = list(set(possible_courses.keys()))
	for k in keys:
		req = {"req":k}
		req["courses"] = []
		for course in possible_courses[k]:
			#print(course)
			course_num = course.split("#")[0]
			course_desc = course.split("#")[1]
			course_dict = {"id":course_num.lower().replace(" ",""),"text":course_num+" "+course_desc,"num":course_num,"desc":course_desc}
			req["courses"].append(course_dict)
		dictionary["requirements"].append(req)
	#print(dictionary)

	return dictionary


def getMenuOption(data):
	print("CHOOSE ONE OF THE FOLLOWING NUMBERS:")
	print("1. Generate curriculum sheet")
	print("2. Generate curriculum sheet with planned courses")
	print("3. Fill out graduation form")
	choice = int(input("Enter your choice:	"))
	if choice == 2:
		courses = input("Enter the list of classes, separated by spaces, i.e. 'MATH1234 CSC1111 HONR1234':	")
		courses = courses.split(" ")
		for course in courses:
			if len(course) >= 8:
				if 'W' == course[-1] and len(course) == 8:
					code = course[:3]
					num = course[3:]
				else:
					code = course[:4]
					num = course[4:]					
			elif len(course) == 7:
				code = course[:3]
				num = course[3:]
			else:
				code = course[:2]
				num = course[2:]
			course = code + " " + num
			data.append(course)
			data.append("	")
			data.append("	")
			data.append("----------<b>PLANNED</b>----------	")
			data.append("	")
			data.append("	")
			data.append("--	")
			data.append("	")
			data.append("	")
			data.append("(3)	")
			data.append("	")
			data.append("	")
			data.append("----------<b>PLANNED</b>----------	")

	return choice


def setRemove(original, delete):
	new = []
	for long_course in original:
		course_num = long_course.split("#")[0]
		if course_num not in delete:
			new.append(long_course)
		else:
			print("deleted " + long_course)
	return list(set(new))


def mineSharedCourses(line, data, ctr, semester, stats_options, foundCourses, exceptions):
	# find courses
	if foundCourses["cs1010_name"] == None or grade(foundCourses["cs1010_grade"]) <= -2:
		ctr, foundCourses["cs1010_name"], foundCourses["cs1010_year"], foundCourses["cs1010_credits"], foundCourses["cs1010_grade"], foundCourses["cs1010_course"] = mineGW_Course('CSCI', '1010', data, ctr, semester, exceptions)
	if foundCourses["cs1010_name"] == None or grade(foundCourses["cs1010_grade"]) <= -2:
		ctr, foundCourses["cs1010_name"], foundCourses["cs1010_year"], foundCourses["cs1010_credits"], foundCourses["cs1010_grade"], foundCourses["cs1010_course"] = mineGW_Course('APSC', '1001', data, ctr, semester, exceptions)
	
	if foundCourses["cs1111_name"] == None or grade(foundCourses["cs1111_grade"]) <= 0:
		ctr, foundCourses["cs1111_name"], foundCourses["cs1111_year"], foundCourses["cs1111_credits"], foundCourses["cs1111_grade"], foundCourses["cs1111_course"] = mineGW_Course('CSCI', '1111', data, ctr, semester, exceptions)

	if foundCourses["cs1112_name"] == None or grade(foundCourses["cs1112_grade"]) <= 0:
		ctr, foundCourses["cs1112_name"], foundCourses["cs1112_year"], foundCourses["cs1112_credits"], foundCourses["cs1112_grade"], foundCourses["cs1112_course"] = mineGW_Course('CSCI', '1112', data, ctr, semester, exceptions)

	if foundCourses["cs1311_name"] == None or grade(foundCourses["cs1311_grade"]) <= 0:
		ctr, foundCourses["cs1311_name"], foundCourses["cs1311_year"], foundCourses["cs1311_credits"], foundCourses["cs1311_grade"], foundCourses["cs1311_course"] = mineGW_Course('CSCI', '1311', data, ctr, semester, exceptions)
	
	if foundCourses["cs2113_name"] == None or grade(foundCourses["cs2113_grade"]) <= -2:
		ctr, foundCourses["cs2113_name"], foundCourses["cs2113_year"], foundCourses["cs2113_credits"], foundCourses["cs2113_grade"], foundCourses["cs2113_course"] = mineGW_Course('CSCI', '2113', data, ctr, semester, exceptions)

	if foundCourses["cs2541W_name"] == None or grade(foundCourses["cs2541W_grade"]) <= -2:
		ctr, foundCourses["cs2541W_name"], foundCourses["cs2541W_year"], foundCourses["cs2541W_credits"], foundCourses["cs2541W_grade"], foundCourses["cs2541W_course"] = mineGW_Course('CSCI', '2541W', data, ctr, semester, exceptions)

	if foundCourses["seas1001_name"] == None or grade(foundCourses["seas1001_grade"]) <= -2:
		ctr, foundCourses["seas1001_name"], foundCourses["seas1001_year"], foundCourses["seas1001_credits"], foundCourses["seas1001_grade"], foundCourses["seas1001_course"] = mineGW_Course('SEAS', '1001', data, ctr, semester, exceptions)
		
	if foundCourses["uw1020_name"] == None or grade(foundCourses["uw1020_grade"]) <= -2:
		ctr, foundCourses["uw1020_name"], foundCourses["uw1020_year"], foundCourses["uw1020_credits"], foundCourses["uw1020_grade"], foundCourses["uw1020_course"] = mineGW_Course('UW', '1020', data, ctr, semester, exceptions)
	if foundCourses["uw1020_name"] == None or grade(foundCourses["uw1020_grade"]) <= -2:
		ctr, foundCourses["uw1020_name"], foundCourses["uw1020_year"], foundCourses["uw1020_credits"], foundCourses["uw1020_grade"], foundCourses["uw1020_course"] = mineGW_Course('HONR', '1015', data, ctr, semester, exceptions)

	for stat in stats_options:
		dept = stat.split(' ')[0]
		course_num = stat.split(' ')[1]
		if foundCourses["stats_course"] == None or grade(foundCourses["stats_grade"]) <= -2:
			ctr, foundCourses["stats_name"], foundCourses["stats_year"], foundCourses["stats_credits"], foundCourses["stats_grade"], foundCourses["stats_course"] = mineGW_Course(dept, course_num, data, ctr, semester, exceptions)
		if foundCourses["stats_course"] != None:
			break


gened_humanities_options = ["AH 1031", "AMST 1000", "AMST 1050", "AMST 1160", "AMST 1200", "AMST 1050", "AMST 2010", "AMST 2011", "AMST 2020", "AMST 2020W", "AMST 2120W", "AMST 2210", "AMST 2320", "AMST 2350", "AMST 2380", "AMST 2385", "AMST 2385W", "AMST 2410", "AMST 2410W", "AMST 2430", "AMST 2440", "AMST 2440W", "AMST 2450", "AMST 2600", "AMST 2610", "AMST 2610W", "AMST 2620", "AMST 2630", "AMST 2710", "AMST 2730", "AMST 2730W", "AMST 2750", "AMST 2750W", "AMST 3352", "AMST 3352W", "AMST 3361", "AMST 3600", "AMST 3625", "ANTH 2750", "ANTH 2750W", "ANTH 3625", "CAH 1031", "CAH 2113", "CAH 2114", "CAH 2115", "CHIN 3111", "CHIN 3112", "CHIN 3116", "CHIN 3123", "CHIN 3124", "CHIN 3163", "CLAS 1001", "CLAS 2107", "CLAS 2113", "CMUS 1161", "CMUS 2110", "CTAD 1021W", "CTAD 4274", "CTAD 4592", "EALL 3811", "EALL 3814", "EALL 3814W", "ENGL 1000", "ENGL 1050", "ENGL 1300", "ENGL 1315", "ENGL 1320", "ENGL 1320W", "ENGL 1330", "ENGL 1330W", "ENGL 1340", "ENGL 1340W", "ENGL 1351", "ENGL 1360", "ENGL 1365", "ENGL 1500", "ENGL 2100", "ENGL 2410", "ENGL 2410W", "ENGL 2411", "ENGL 2411W", "ENGL 2510", "ENGL 2510W", "ENGL 2511", "ENGL 2511W", "ENGL 2610", "ENGL 2610W", "ENGL 2611", "ENGL 2611W", "ENGL 2710", "ENGL 2710W", "ENGL 2711", "ENGL 2711W", "ENGL 2712", "ENGL 3385", "ENGL 3400", "ENGL 3446", "ENGL 3621", "ENGL 3730", "ENGL 3730W", "ENGL 3800", "ENGL 3910", "ENGL 3918", "FREN 2006", "FREN 2500", "FREN 2600", "FREN 3020", "FREN 3100", "FREN 3500", "FREN 3700", "FREN 4540", "GER 1000", "GER 1000", "GER 2091", "GER 2092", "GER 2161", "GER 2162", "GER 3182", "GER 3187", "GER 3190", "GREK 1001", "GTCH 3103", "HEBR 1001", "HIST 1011", "HIST 1020", "HIST 1110", "HIST 1120", "HIST 1120W", "HIST 1121", "HIST 1310", "HIST 1311", "HIST 2010", "HIST 2011", "HIST 2020", "HIST 2020W", "HIST 2050", "HIST 2060", "HIST 2061", "HIST 2113", "HIST 2124", "HIST 2125", "HIST 2131", "HIST 2141", "HIST 2160", "HIST 2312", "HIST 2313", "HIST 2320", "HIST 2321", "HIST 2322", "HIST 2350", "HIST 2380", "HIST 2410", "HIST 2410W", "HIST 2440", "HIST 2240W", "HIST 2520", "HIST 2610/", "HIST 2630", "HIST 2710", "HIST 2730", "HIST 2730W", "HIST 2811", "HIST 2850", "HIST 3044W", "HIST 3352", "HIST 3352W", "HIST 3353", "HIST 3360", "HIST 3361", "HIST 3611", "HIST 3630", "HIST 3811", "HIST 3811W", "HONR 1016", "HONR 2053", "HONR 2053W", "ITAL 2600", "ITAL 3300", "ITAL 3310", "ITAL 4100", "ITAL 4184", "ITAL 4380", "JAPN 3111", "JAPN 3112", "JAPN 4121", "JSTD 2060", "KOR 3111", "KOR 3112", "KOR 3123", "KOR 3124", "LATN 2001", "LATN 3001", "LATN 3001W", "LATN 3002", "LATN 3002W", "PHIL 1000", "PHIL 1051", "PHIL 1153", "PHIL 2124", "PHIL 2124W", "PHIL 2125", "PHIL 2125W", "PHIL 2131", "PHIL 2132", "PHIL 2132W", "PHIL 2133", "PHIL 2134", "PHIL 2136", "PHIL 2140", "PHIL 2281", "PHIL 3142", "PHIL 3142W", "PHIL 3151", "PHIL 3153", "PSC 2120W", "PSTD 1010", "REL 1000", "WGSS 1000", "REL 1010", "REL 1010W", "REL 2165", "REL 2169", "REL 2201", "REL 2301", "REL 2314", "REL 2401", "REL 2501", "REL 2562", "REL 2811", "REL 2814", "REL 2981", "REL 3149", "REL 3149W", "REL 3151", "REL 3151W", "REL 3161", "REL 3161W", "REL 3405", "REL 3614", "REL 3923", "SLAV 1000", "SLAV 1017", "SLAV 2310", "SLAV 2320", "SPAN 1095", "SPAN 2005", "SPAN 2006", "SPAN 2026", "SPAN 2056", "SPAN 2156", "SPAN 2500", "SPAN 3100", "SPAN 3100W", "SPAN 3200", "UNIV 1006", "WGSS 1000", "WGSS 1020", "WGSS 2225", "WGSS 2380", "WGSS 2385", "WGSS 2385W", "WGSS 2710", "WGSS 2710W", "WGSS 3352", "WGSS 3352W", "WGSS 3353", "WGSS 3981", "WLP 1020"]
gened_socsci_options = ["ANTH 1000", "ANTH 1002", "ANTH 1002W", "ANTH 1003", "ANTH 1004", "ANTH 2008", "ANTH 2008W", "ANTH 2502", "ANTH 3704", "ANTH 3838", "ANTH 3838W", "COMM 1025", "COMM 1040", "COMM 1041", "ECON 1011", "ECON 1012", "GEOG 1001", "GEOG 1003", "GTCH 3300", "HONR 2043", "HONR 2044", "HONR 2047", "HONR 2047W", "HSSJ 2200", "ORSC 2000", "PSC 1001", "PSC 1001W", "PSC 1002", "PSC 1002W", "PSC 1011", "PSC 1012W", "PSYC 2011", "PSYC 2011W", "PSYC 2012", "PSYC 2013", "PSYC 2014", "PSYC 2015", "SLHS 1071", "SLHS 1071W", "SLHS 1072", "SLHS 1084", "SLHS 4201", "SMPA 1000", "SMPA 1050", "SMPA 2101", "SMPA 2102", "SOC 1002", "SOC 1003", "SOC 2104", "SOC 2104W", "SOC 2169", "SUST 1001", "UNIV 1005"]
gened_arts_options = ["AH 1032", "AH 2071", "AH 2154", "AH 2155", "AH 2162", "AH 2162W", "AH 2191", "AMST 1000", "AMST 1000", "AMST 1000", "AMST 1100", "AMST 2071", "AMST 2520", "AMST 2521", "CAH 1000", "CAH 1032", "CAH 1090", "CAH 2071", "CAH 2154", "CAH 2155", "CAH 2162", "CAH 2162W", "CAH 2191", "CFN 1093", "CGD 2020", "CHIN 3173", "CIAR 1000", "CIAR 3325", "CLAS 3112", "CMUS 1106", "CMUS 2122", "CMUS 2122W", "CMUS 3175", "CSA 1401", "CSA 1501", "CSA 1502", "CSA 1601", "CSA 1702", "CSA 2513", "CSA 2703", "CSA 3915", "CTAD 1000", "CTAD 1000", "CTAD 1000", "CTAD 1000", "CTAD 1020", "CTAD 1035", "CTAD 1214", "CTAD 1215", "CTAD 2191", "CTAD 2191W", "CTAD 2195", "CTAD 2195W", "CTAD 3245", "CTAD 3245W", "CTAD 3246", "CTAD 3246W", "ENGL 1000", "ENGL 1210", "ENGL 2210", "ENGL 4010", "IA 3325", "ITAL 4183", "MUS 1000", "MUS 1103", "MUS 1104", "MUS 1105", "MUS 1106", "MUS 1107", "MUS 1108", "MUS 2101", "MUS 2122", "MUS 2122W", "SLAV 2785", "SLAV 2786", "TRDA 1000", "TRDA 1000", "TRDA 1000", "TRDA 1020", "TRDA 1214", "TRDA 1215", "TRDA 2191", "TRDA 2191W", "TRDA 2195"," TRDA 2195W", "TRDA 3245", "TRDA 3245W", "TRDA 3246", "TRDA 3246W"]
gened_global_options = ["ITAL 3300", "ITAL 3310", "ITAL 3320", "CTAD 4274", "AH 1031", "AH 2191", "AMST 1000", "AMST 1000", "AMST 1200", "AMST 1050", "AMST 2010", "AMST 2011", "AMST 2120W", "AMST 2210", "AMST 2320", "AMST 2350", "AMST 2380", "AMST 2385", "AMST 2384W", "AMST 2410", "AMST 2410W", "AMST 2440", "AMST 2440W", "AMST 2610", "AMST 2610W", "AMST 2710", "AMST 2730", "AMST 2730W", "AMST 2750", "AMST 2750W", "AMST 3352", "AMST 3352W", "AMST 3353", "AMST 3360", "AMST 3361", "ANTH 1002", "ANTH 1002W", "ANTH 1003", "ANTH 1004", "ANTH 2008", "ANTH 2008W", "ANTH 2750", "ANTH 2750W", "ANTH 3704", "ANTH 3838", "ANTH 3838W", "CAH 1031", "CHIN 3111", "CHIN 3112", "CHIN 3116", "CHIN 3123", "CHIN 3124", "CHIN 3163", "CHIN 3173", "CIAR 1000", "CIAR 3325", "CLAS 2113", "CMUS 3175", "CTAD 1000", "CTAD 4274", "EALL 3811", "EALL 3814", "EALL 3814W", "ENGL 1300", "ENGL 1330", "ENGL 1330W", "ENGL 1340", "ENGL 1340W", "ENGL 2610", "ENGL 2610W", "ENGL 2611", "ENGL 2611W", "ENGL 2710", "ENGL 2710W", "ENGL 2711", "ENGL 2711W", "ENGL 2712", "ENGL 2712W", "ENGL 3730", "ENGL 3730W", "ENGL 3800", "FREN 2006", "FREN 3020", "FREN 3100", "FREN 4540", "GEOG 1001", "GER 1000", "GER 2091", "GER 2092", "GER 2161", "GER 2162", "GER 3182", "GER 3187", "GREK 1001", "GTCH 3300", "HIST 1011", "HIST 1110", "HIST 1020", "HIST 1120", "HIST 1120W", "HIST 1121", "HIST 1310", "HIST 1311", "HIST 2010", "HIST 2011", "HIST 2050", "HIST 2061", "HIST 2113", "HIST 2124", "HIST 2125", "HIST 2131", "HIST 2141", "HIST 2160", "HIST 2312", "HIST 2313", "HIST 2320", "HIST 2321", "HIST 2322", "HIST 2350", "HIST 2380", "HIST 2410", "HIST 2410W", "HIST 2440", "HIST 2440W", "HIST 2520", "HIST 2610", "HIST 2610W", "HIST 2710", "HIST 2730", "HIST 2730W", "HIST 2811", "HIST 2850", "HIST 3044W", "HIST 3352", "HIST 3352W", "HIST 3353", "HIST 3360", "HIST 3361", "HIST 3811", "HIST 3811W", "IA 1000", "IA 3325", "ITAL 2600", "ITAL 3300", "ITAL 3310", "ITAL 4184", "ITAL 4380", "JAPN 3111", "JAPN 3112", "KOR 3111", "KOR 3112", "KOR 3123", "KOR 3124", "MUS 1000", "PHIL 2125", "PHIL 2125W", "PHIL 2134", "PSC 1001", "PSC 1001W", "PSC 1012W", "PSC 2120W", "PSTD 1010", "REL 1000", "REL 1010", "REL 1010W", "REL 2165", "REL 2169", "REL 2301", "REL 2562", "REL 2811", "REL 2814", "REL 2981", "REL 3149", "REL 3149W", "REL 3151", "REL 3151W", "REL 3161", "REL 3161W", "REL 3923", "SOC 2101", "SOC 2102", "SLAV 1017", "SLAV 2310", "SLAV 2320", "SLHS 1071", "SLHS 1071W", "SLHS 1072", "SLHS 1084", "SPAN 1095", "SPAN 2005", "SPAN 2006", "SPAN 2026", "SPAN 2056", "SPAN 2156", "SPAN 2500", "SPAN 3100", "SPAN 3100W", "SPAN 3200", "TRDA 1000", "TRDA 1000", "TRDA 1000", "WGSS 1000", "WGSS 1020", "WGSS 2380", "WGSS 2385", "WGSS 2385W", "WGSS 2710", "WGSS 2710W", "WGSS 3352", "WGSS 3352W", "WGSS 3353", "WGSS 3730", "WGSS 3981"]

seas_hss_options = ["AMST 1050", "AMST 1160", "AMST 1200", "AMST 2010", "AMST 2011", "AMST 2020", "AMST 2020W", "AMST 2120W ", "PSC 2120W", "AMST 2210", "AMST 2320", "AMST 2350", "AMST 2380", "AMST 2410", "AMST 2440", "AMST 2520", "AMST 2521", "AMST 2530", "AMST 2710", "AMST 2730", "AMST 2730W", "AMST 2750W", "AMST 3352", "AMST 3352W", "ANTH 2750", "ANTH 2750W", "AH *", "ARAB *", "CLAS *", "GREK *", "LATN *", "HEBR *", "PERS *", "TURK *", "YDSH *", "CHIN *", "KOR *", "JAPN *", "EALL 3811", "EALL 3814", "EALL 3814W", "EALL 3821", "EALL 3831", "EALL 3832", "ENGL *", "HIST *", "HONR 1016", "HONR 2016", "HONR 2053", "HONR 2053W", "HONR 2054", "SMPA 2110W", "SMPA 3230", "SMPA 3236W", "SMPA 3241W", "SMPA 3243W", "SMPA 3245", "SMPA 3246", "MUS 1103", "MUS 1104", "MUS 1107", "MUS 1108", "MUS 2101", "MUS 2102", "MUS 2109", "MUS 2110", "MUS 2111", "MUS 2121", "NSC 2126", "NSC 2180", "PSTD 1010", "NSC 4176", "PHIL *", "PSC 2120W", "SPAN *", "ITAL *", "FREN *", "PORT *", "GER *", "SLAV *", "REL *", "SLHS 1072", "SLHS 1081", "SLHS 1082", "TRDA 1015", "TRDA 1020", "TRDA 1025", "TRDA 3245", "TRDA 3246", "TRDA 2191", "WGSS 2380", "WGSS 3352", "WGSS 3353", "WGSS 3981", "WLP 1020", "AMST 2490", "AMST 2532", "AMST 3324", "AMST 3350", "ANTH 1002", "ANTH 1002W", "ANTH 1003", "ANTH 1004", "ANTH 2008", "ANTH 2008W", "ANTH 2502", "ANTH 2506", "ANTH 3501", "ANTH 3502", "ANTH 3503", "ANTH 3504", "ANTH 3505", "ANTH 3506", "ANTH 3507", "ANTH 3508", "ANTH 3509", "ANTH 3513", "ANTH 3522", "ANTH 3601", "ANTH 3602", "ANTH 3603", "ANTH 3701", "ANTH 3702", "ANTH 3703", "ANTH 3704", "ANTH 3705", "ANTH 3707", "ANTH 3708", "ANTH 3709", "ANTH 3801", "ANTH 3802", "ANTH 3803", "ANTH 3804", "ANTH 3806", "ANTH 3813", "ANTH 3814", "ANTH 3838", "ANTH 3838W", "COMM 1025", "COMM 1040", "COMM 1041", "ECON *", "GEOG 1001", "GEOG 1002", "GEOG 1003", "GEOG 2110", "GEOG 2127", "GEOG 2133", "GEOG 2134", "GEOG 2141", "GEOG 2144", "GEOG 2145", "GEOG 2146", "GEOG 3120", "GEOG 2120", "GEOG 3143", "GEOG 3154", "GEOG 3161", "GEOG 3164", "HSCI 2101", "HSCI 2103", "HLWL 1109", "HONR 2043", "HONR 2044", "HONR 2047", "HONR 2047W", "HONR 2048", "HMSR 2171", "HMSR 2172", "HMSR 2177", "IAFF 2090", "IAFF 2091", "IAFF 2092", "IAFF 2093", "MAE 2170", "SMPA 1050", "SMPA 2101", "SMPA 2102", "SMPA 2173", "SMPA 2177", "SMPA 3428", "SMPA 3470", "SMPA 3471", "SMPA 3472", "SMPA 3474", "SMPA 3476", "NSC 1051", "NSC 2160", "NSC 2175", "PSC *", "PSYC *", "SOC *", "SLHS 1071", "SLHS 1071W", "SLHS 1084", "SUST 1001", "TSTD 3001", "WGSS 1020", "WGSS 2120", "WGSS 2125"]

new_seas_hss_additions = ["AMST 1000", "AMST 2010", "AMST 2450", "AMST 2620", "ANTH 1004", "ANTH 2008", "ANTH 2008W", "ANTH 2502", "ANTH 3704", "ANTH 3838", "ANTH 3838W", "ARAB 3001", "ARAB 3105", "ARAB 3302", "ARAB 4002", "CAH 2113", "CAH 2114", "CFN 1093", "CHEM 2118W", "CHIN 3105", "CMUS 2122", "CMUS 2122W", "COMM 1040", "COMM 1041", "CSA 2513", "CSA 2703", "CTAD 1000", "EAP 1010", "ECON 4198W", "ENGL 1000", "ENGL 1365", "ENGL 1710", "ENGL 1710W", "ENGL 1711", "ENGL 1711W", "ENGL 2510", "ENGL 2510W", "ENGL 2710", "ENGL 2710W", "ENGL 2711", "ENGL 2711W", "ENGL 3385", "ENGL 3400", "ENGL 3481", "ENGL 3481W", "ENGL 3620", "ENGL 3621", "ENGL 3621W", "ENGL 3730", "ENGL 3730W", "ENGL 3800", "ENGL 3918", "FREN 1000", "FREN 2005", "FREN 2006", "FREN 2500", "FREN 2600", "FREN 3020", "FREN 3500", "FREN 3700", "GEOG 1000", "GER 1000", "GER 2091", "GER 2092", "GER 2109", "GER 2109W", "GER 2111", "GER 2161", "GER 3182", "GER 3187", "GREK 1002", "GTCH 2003", "GTCH 3101", "HEBR 3001", "HEBR 3101", "HEBR 3101W", "HIST 1110", "HIST 2010", "HIST 2050", "HIST 2060", "HIST 3044W", "HONR 1034", "HSSJ 4195", "ITAL 2600", "ITAL 3300", "ITAL 4380", "JAPN 3105", "JAPN 4121W", "JSTD 2060", "KOR 3105", "KOR 4107", "KOR 4190", "LATN 2002", "LATN2002W", "MUS 2122", "MUS 2122W", "ORSC 2000", "PHIL 2124", "PHIL 2124W", "PHIL 2133", "PHIL 2134", "PHIL 4192", "PHIL 4198", "PHIL 4198W", "PHYS 4195", "PHYS 4195W", "PSTD 1010", "REL 1010", "REL 1010W", "REL 2301", "REL 2814", "REL 2981", "SLHS 1011", "SLHS 4201", "SOC 4192", "SOC 4195", "SOC 4195W", "SPAN 2006", "SPAN 2056", "SPAN 3022", "SPAN 3100", "SPAN 3100W", "SPAN 3200", "SUST 2004", "TRDA 1000", "WGSS 2710", "WGSS 2710W", "WGSS 2711W", "WGSS 3730", "WGSS 3730W", "WGSS 3981", "WLP 1020", "AMST 2020", "AMST 2020W", "AMST 2450", "AMST 2630", "AMST 3625 ", "ANTH 3625", "BISC 1007", "BISC 1008", "CGD 2020", "CHEM 1003", "CMUS 2110", "CSA 1702", "CSA 3915", "CTAD 1021W", "DATS 2101", "ECON 1002", "ENGL 4010", "GEOG 1003", "GEOG 3143", "GEOG 3143W", "GTCH 3103", "HIST 1000", "HIST 2020", "HIST 2020W", "HONR 1033", "HSSJ 2200", "PHIL 2133", "PHIL 2136", "PHIL 2140", "PHIL 2281", "PHIL 3142", "PHIL 3142W", "PSC 1000", "PSC 1002", "PSC 1002W", "PSC 1011", "SOC 1002", "SUST 1001", "PHIL 2135", "SOC 1001", "PSYC 1001"]
new_hss_options = gened_humanities_options + gened_socsci_options + gened_arts_options + gened_global_options + new_seas_hss_additions

# used by all scripts to store the data about the courses fund
foundCourses = {}


main_campus_course = '<tr>	' + 	'<td CLASS="dddefault">CRSE</td>	' + 	'<td CLASS="dddefault">0000</td>	' + 	'<td CLASS="dddefault">Main Campus</td>	' + 	'<td CLASS="dddefault">01</td>	' + 	'<td colspan="3" CLASS="dddefault">PLANNED COURSE</td>	' + 	'<td CLASS="dddefault">A-</td>	' + 	'<td CLASS="dddefault"><p class="rightaligntext">		0.000</p></td>	' + 	'<td CLASS="dddefault"><p class="rightaligntext">			 0.00</p></td>	' + 	'<td CLASS="dddead">&nbsp;</td>	' + 	'<td CLASS="dddefault">&nbsp;</td>	' + 	'<td CLASS="dddead">&nbsp;</td>	' + 	'</tr>	'


def addClass(data, ctr, all_classes_taken):
	course_regex = "^([A-Z][A-Z][A-Z]?[A-Z]?) (d{4}W?)$"
	match = re.search(course_regex, data[ctr])
	if (match):
		course = match.group(1) + " " + match.group(2)
		description = data[ctr+3][:-1]

		if course not in all_classes_taken:
			all_classes_taken.append(course + " " + description)


def diff_years(year1, year2, year):
	import difflib

	diff = difflib.context_diff(open(year1).readlines(),open(year2).readlines(), n=1)
	result = '		'.join(diff)

	file = open("log.txt", 'a')
	import datetime
	file.write("........	" + str(year) + "........	" + str(datetime.datetime.now()))
	file.write(result)


def wipeFoundCourse(foundCourses, key):
	key = key[:key.rfind('_')]

	foundCourses[key + "_course"] = None
	foundCourses[key + "_name"] = None
	foundCourses[key + "_credits"] = None
	foundCourses[key + "_year"] = None
	foundCourses[key + "_grade"] = None


# gets all courses that match from 
def getFullNameFromNum(all_courses, manual):
	cleaned_manual = []
	for mini in manual:
		for course in all_courses:
			course_num = course.split("#")[0]
			if course_num in mini:
				cleaned_manual.append(course)
			elif "*" in mini:
				root = mini.split(" ")[0]
				if root in course:
					cleaned_manual.append(course)
	return list(set(cleaned_manual))


def dedup_dict(courses_dict):
	for a in courses_dict:
		courses_dict[a] = list(set(courses_dict[a])) # removes duplicates

record_year_for_hss('2019')
