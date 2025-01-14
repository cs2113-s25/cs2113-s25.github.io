import json



from utils_buggy import *



# get the latest courses lists generated via bulletin_scraper.py

json_file = open("./all_courses.json") 

all_courses = set(json.loads(json_file.read()))

json_file.close()

all_courses = list(set(all_courses))



json_file = open("./all_GPAC_courses.json") 

all_GPAC_courses = json.loads(json_file.read())

dedup_dict(all_GPAC_courses)

json_file.close()



json_file = open("./exceptions.json") 

exceptions = set(json.loads(json_file.read()))

json_file.close()

exceptions = list(set(exceptions))



json_file = open("./cs_offerings.json") 

cs_offerings = set(json.loads(json_file.read()))

json_file.close()

cs_offerings = list(set(cs_offerings))



electives = setRemove(all_courses, exceptions) # remove PCSC and PSIS courses from electives



bulletin_exceptions = ["BADM 2301", "EMSE 4197", "ISTM 3119", "ISTM 4120", "ISTM 4121", "ISTM 4123", "STAT 1051", "STAT 1053", "STAT 1129"]

electives = setRemove(electives, bulletin_exceptions)



manually_chosen_exceptions = ["BME 2820", "BME 2825", "DNSC 4211", "ECE 1120", "EMSE 4571", "EMSE 4574", "GEOG 4308", "INFR 4103", "ISTM 3119"]

electives = setRemove(electives, manually_chosen_exceptions)



other_exceptions = ["ECON 1001"] # "UW 1099" 

electives = setRemove(electives, other_exceptions)



# electives are similar in requirements to NTT, but they do allow you to take additional CS courses (with some restrictions)

electives, cs_tech_courses = beautifyElectives(all_courses, electives)



ntt = list(set(electives) - set(cs_tech_courses)) # remove CS courses from electives



possible_courses = {}

possible_courses["seas1001"] = getFullNameFromNum(all_courses, ["SEAS 1001"])

possible_courses["cs1010"] = getFullNameFromNum(all_courses, ["CSCI 1010"])



possible_courses["cs1111"] = getFullNameFromNum(all_courses, ["CSCI 1111"])

possible_courses["cs1112"] = getFullNameFromNum(all_courses, ["CSCI 1112"])

possible_courses["cs2113"] = getFullNameFromNum(all_courses, ["CSCI 2113"])

possible_courses["cs_architecture"] = getFullNameFromNum(all_courses, ["CSCI 3401", "CSCI 2461"])

possible_courses["cs1311"] = getFullNameFromNum(all_courses, ["CSCI 1311"])



cs_tt_2113_prereq = ["CSCI 3462", "CSCI 4223", "CSCI 4235",  "CSCI 4431", "CSCI 4237", "CSCI 4331", "CSCI 4341", "CSCI 4342", "CSCI 4345", "CSCI 4364", "CSCI 4366", "CSCI 4415", "CSCI 4431", "CSCI 4431W", "CSCI 4454", "CSCI 4455", "CSCI 4511", "CSCI 4527", "CSCI 4531", "CSCI 4533", "CSCI 4541", "CSCI 4554", "CSCI 4561", "CSCI 4572", "CSCI 4577"]



possible_courses["calc_1"] = getFullNameFromNum(all_courses, ["MATH 1231", "MATH 1221"])

possible_courses["calc_2"] = getFullNameFromNum(all_courses, ["MATH 1232"])



possible_courses["uw1020"] = getFullNameFromNum(all_courses, ["UW 1020", "HONR 1015"])







