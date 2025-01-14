import json

from course_list_imports_buggy import *
from utils_buggy import *

# CS BS courses ##################################################################################################

possible_courses["cs2312"] = getFullNameFromNum(all_courses, ["CSCI 2312"])
possible_courses["cs2501"] = getFullNameFromNum(all_courses, ["CSCI 2501"])
possible_courses["cs2541W"] = getFullNameFromNum(all_courses, ["CSCI 2541W"])
possible_courses["cs3212"] = getFullNameFromNum(all_courses, ["CSCI 3212"])
possible_courses["cs3313"] = getFullNameFromNum(all_courses, ["CSCI 3313"])
possible_courses["cs3410"] = getFullNameFromNum(all_courses, ["CSCI 3410"])
possible_courses["cs3411"] = getFullNameFromNum(all_courses, ["CSCI 3411"])
possible_courses["cs4243W"] = getFullNameFromNum(all_courses, ["CSCI 4243W"])
possible_courses["cs4244"] = getFullNameFromNum(all_courses, ["CSCI 4244"])

# TODO: do we need to include the grad versions of all these courses for 5-year masters students?
possible_courses["cs_tech_track_2113_1"] = getFullNameFromNum(all_courses, cs_tt_2113_prereq)
possible_courses["cs_tech_track_2113_2"] = possible_courses["cs_tech_track_2113_1"]
possible_courses["cs_tech_track_core_1"] = getFullNameFromNum(all_courses, ["CSCI 6411", "CSCI 6421", "CSCI 4431", "CSCI 6431", "CSCI 4331", "CSCI 6331", "CSCI 4364", "CSCI 6364", "CSCS 8331", "CSCI 4366", "CSCI 4341", "CSCI 4527", "CSCI 6527", "CSCI 6351", "EMSE 6575", "CSCI 4554", "CSCI 4237", "CSCI 4533", "CSCI 4331", "CSCI 6331", "CSCI 8331"])
possible_courses["cs_tech_track_core_2"] = possible_courses["cs_tech_track_core_1"]

# math courses ##################################################################################################

possible_courses["stats"] = getFullNameFromNum(all_courses, ["APSC 3115", "CSCI 3362", "CSCI 6362", "CSCI 4341", "STAT 4157"]) # why was "STAT 3157" in here by Kinga?
possible_courses["linear_alg"] = getFullNameFromNum(all_courses, ["MATH 2184", "CSCI 4342", "EMSE 2705"])

# university requirements ##################################################################################################

possible_courses["gened_ss_1"] = getFullNameFromNum(all_courses, all_GPAC_courses['Critical Thinking, Quantitative Reasoning or Scientific Reasoning in the Social Sciences'])
possible_courses["gened_ss_2"] = getFullNameFromNum(all_courses, all_GPAC_courses['Critical Thinking, Quantitative Reasoning or Scientific Reasoning in the Social Sciences'])
possible_courses["gened_hum"] = getFullNameFromNum(all_courses, all_GPAC_courses['Critical Thinking in the Humanities'])

# other requirements ##################################################################################################
possible_courses["sci_seq_1"] = getFullNameFromNum(all_courses, ["BISC 1111", "CHEM 1111", "PHYS 1021"])
possible_courses["sci_seq_2"] = getFullNameFromNum(all_courses, ["BISC 1112", "CHEM 1112", "PHYS 1022"])
possible_courses["sci_3"] = list(set(possible_courses["sci_seq_1"] + possible_courses["sci_seq_2"]))

# the courses below were manually collected from this pdf: https://engineering.gwu.edu/sites/g/files/zaxdzs5436/files/downloads/SEAS%20Non-Technical%20Course%20List_0.pdf
manual_seas = ["AMST 1050", "AMST 1160", "AMST 1200", "AMST 2010", "AMST 2011", "AMST 2020", "AMST 2020W", "AMST 2120W ", "PSC 2120W", "AMST 2210", "AMST 2320", "AMST 2350", "AMST 2380", "AMST 2410", "AMST 2440", "AMST 2520", "AMST 2521", "AMST 2530", "AMST 2710", "AMST 2730", "AMST 2730W", "AMST 2750W", "AMST 3352", "AMST 3352W", "ANTH 2750", "ANTH 2750W", "AH *", "ARAB *", "CLAS *", "GREK *", "LATN *", "HEBR *", "PERS *", "TURK *", "YDSH *", "CHIN *", "KOR *", "JAPN *", "EALL 3811", "EALL 3814", "EALL 3814W", "EALL 3821", "EALL 3831", "EALL 3832", "ENGL *", "HIST *", "HONR 1016", "HONR 2016", "HONR 2053", "HONR 2053W", "HONR 2054", "SMPA 2110W", "SMPA 3230", "SMPA 3236W", "SMPA 3241W", "SMPA 3243W", "SMPA 3245", "SMPA 3246", "MUS 1103", "MUS 1104", "MUS 1107", "MUS 1108", "MUS 2101", "MUS 2102", "MUS 2109", "MUS 2110", "MUS 2111", "MUS 2121", "NSC 2126", "NSC 2180", "PSTD 1010", "NSC 4176", "PHIL *", "PSC 2120W", "SPAN *", "ITAL *", "FREN *", "PORT *", "GER *", "SLAV *", "REL *", "SLHS 1072", "SLHS 1081", "SLHS 1082", "TRDA 1015", "TRDA 1020", "TRDA 1025", "TRDA 3245", "TRDA 3246", "TRDA 2191", "WGSS 2380", "WGSS 3352", "WGSS 3353", "WGSS 3981", "WLP 1020", "AMST 2490", "AMST 2532", "AMST 3324", "AMST 3350", "ANTH 1002", "ANTH 1002W", "ANTH 1003", "ANTH 1004", "ANTH 2008", "ANTH 2008W", "ANTH 2502", "ANTH 2506", "ANTH 3501", "ANTH 3502", "ANTH 3503", "ANTH 3504", "ANTH 3505", "ANTH 3506", "ANTH 3507", "ANTH 3508", "ANTH 3509", "ANTH 3513", "ANTH 3522", "ANTH 3601", "ANTH 3602", "ANTH 3603", "ANTH 3701", "ANTH 3702", "ANTH 3703", "ANTH 3704", "ANTH 3705", "ANTH 3707", "ANTH 3708", "ANTH 3709", "ANTH 3801", "ANTH 3802", "ANTH 3803", "ANTH 3804", "ANTH 3806", "ANTH 3813", "ANTH 3814", "ANTH 3838", "ANTH 3838W", "COMM 1025", "COMM 1040", "COMM 1041", "ECON *", "GEOG 1001", "GEOG 1002", "GEOG 1003", "GEOG 2110", "GEOG 2127", "GEOG 2133", "GEOG 2134", "GEOG 2141", "GEOG 2144", "GEOG 2145", "GEOG 2146", "GEOG 3120", "GEOG 2120", "GEOG 3143", "GEOG 3154", "GEOG 3161", "GEOG 3164", "HSCI 2101", "HSCI 2103", "HLWL 1109", "HONR 2043", "HONR 2044", "HONR 2047", "HONR 2047W", "HONR 2048", "HMSR 2171", "HMSR 2172", "HMSR 2177", "IAFF 2090", "IAFF 2091", "IAFF 2092", "IAFF 2093", "MAE 2170", "SMPA 1050", "SMPA 2101", "SMPA 2102", "SMPA 2173", "SMPA 2177", "SMPA 3428", "SMPA 3470", "SMPA 3471", "SMPA 3472", "SMPA 3474", "SMPA 3476", "NSC 1051", "NSC 2160", "NSC 2175", "PSC *", "PSYC *", "SOC *", "SLHS 1071", "SLHS 1071W", "SLHS 1084", "SUST 1001", "TSTD 3001", "WGSS 1020", "WGSS 2120", "WGSS 2125"]
cleaned_manual_seas = getFullNameFromNum(all_courses, manual_seas)

possible_courses["seas_hss_1"] = cleaned_manual_seas
possible_courses["seas_hss_2"] = cleaned_manual_seas
possible_courses["seas_hss_3"] = cleaned_manual_seas

possible_courses["ntt_1"] = ntt
possible_courses["ntt_2"] = ntt
possible_courses["ntt_3"] = ntt

possible_courses["elective_1"] = electives
possible_courses["elective_2"] = electives
possible_courses["elective_3"] = electives
possible_courses["elective_4"] = electives


result = {"requirements": possible_courses}
with open("possible_courses_BS_2019.json", "w") as fp: 
	json.dump(result , fp) 


big_dict = reformatForFrontEnd(possible_courses)
big_dict["degree"] = "BS 2019-2020"
semesters = [
        ["cs1010", "cs1111", "calc_1", "seas1001", "uw1020", "gened_ss_1"],
        ["cs1112", "cs1311", "calc_2", "sci_seq_1", "gened_ss_2"],
        ["cs2113", "cs2312", "cs_architecture", "sci_seq_2", "gened_hum"],
        ["cs2501", "cs2541W", "cs3313", "cs3410","stats", "sci_3"],
        ["cs3212", "cs3411", "cs_tech_track_2113_1", "seas_hss_1"],
        ["cs_tech_track_2113_2","elective_1", "linear_alg", "elective_2", "seas_hss_2"],
        ["cs4243W", "cs_tech_track_core_1", "elective_3", "elective_4", "seas_hss_3"],
        ["cs4244","cs_tech_track_core_2", "ntt_1", "ntt_2", "ntt_3"]
    ]
big_dict["semesters"] = semesters
with open("BS_2019-2020.json", "w") as fp: 
	json.dump(big_dict , fp) 

print(possible_courses["elective_1"].count("CSCI 2501#Ethical Issues in Computing"))
