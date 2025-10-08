# def data_course_info(): # เก็บข้อมูลจากไฟล์
#     data = []
#     with open(r"data_information/course_info.txt","r",encoding="utf-8") as fout:
#         for i in fout: 
#             data.append(i.strip("\n").split("|"))
#     return(sorted(data))

# def data_dic_info(): # test chat 
#     data = data_course_info()
#     data_dic = {"Institution": {}}
#     for course in data:
#         institution = course[0]
#         faculty = course[1]
#         program = course[2]
#         program_name_en = course[3]
#         program_type = course[4]
#         campus = course[5]
#         tuition = course[6]
#         employment = course[7]
#         median_salary = course[8]
        
#         if institution not in data_dic["Institution"]:
#             data_dic["Institution"][institution] = {}
#         if faculty not in data_dic["Institution"][institution]:
#             data_dic["Institution"][institution][faculty] = {}
#         if program not in data_dic["Institution"][institution][faculty]:
#             data_dic["Institution"][institution][faculty][program] = {}

#         data_dic["Institution"][institution][faculty][program] = {
#             "Program Name in English": program_name_en,
#             "Program Type": program_type,
#             "Campus": campus,
#             "Tuition Fee per Semester": tuition,
#             "Employment Rate": employment,
#             "Median Salary": median_salary
#         }

#     return data_dic

# def search_course_info():
#     # ใช้ data ที่ เป็น dic
#     data = data_dic_info()
#     result = ""
#     head = f"|{'Search Course Information':^50}|"
#     line = "-" * len(head)
#     result += f"{line}\n{head}\n{line}\n"
    

# def main():
#     data_dic_info()

# if __name__ == "__main__":
#     main()

test = "|1|1+1.1+|1"
tests = ((test.split("|")))
data = []
for i in tests:
    data.append(i.split("+"))
print(data)