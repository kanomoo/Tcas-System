from wcwidth import wcswidth
# คำนวณความกว้างของการแสดงผล

def pad_text(text, width = 0): # padding text เติมช่องว่าง ควรใช้เฉพาะภาษาไทย
    text = str(text)
    real_width = wcswidth(text)                         # คำนวณความกว้างจริงของข้อความในเทอมินอล (นับช่องว่างที่ข้อความใช้)
    if width == 0:
        return text 
    elif real_width < width:                            # ถ้าความกว้างจริงของข้อความน้อยกว่าความกว้างที่ต้องการ
        return text + " " * (width - real_width)        # เติมช่องว่างให้ครบตามความกว้างที่กำหนด เพื่อจัดข้อความให้อยู่ในตำแหน่ง len จริงๆ
    return text                                         # ถ้าความกว้างของข้อความมากกว่าหรือเท่ากับที่ต้องการ return เหมือนเดิม ใช้ format string จัดการต่อเอา

def data_studten():
    data = []
    with open(r"data_information/student.txt","r",encoding="utf-8") as fout:
        for i in fout: 
            data.append(i.strip("\n").split("|"))
    print(data)
    return data

def menu_main(): # report main menu
    head = f"|{"TCAS System":^25}|"
    line = f"+{"=" * (len(head) - 2)}+"
    choice = input(f"{line}\n{head}\n{line}\n|{"1. Course information":25}|\n|{"2. Exit Program":25}|\n{line}\nSelect option : ")
    match choice:
        case "1":
            course_info()
        case "2":
            exit()
    print()

def data_course_info(): # เก็บข้อมูลจากไฟล์
    data = []
    with open(r"data_information/course_info.txt","r",encoding="utf-8") as fout:
        for i in fout: 
            data.append(i.strip("\n").split("|"))
    return(sorted(data))

# def data_dic():
#     data = data_course_info()
#     # data_dic = {}
#     data_dic = {"university": {}}

#     for course in data:
#         # ต้องตั้งชื่อ key ดีๆ ก่อน
#         # data_dic[course[0]] = {course[1]: {course[2]}}

#         data_dic["university"][course[0]] = {"คณะ": course[1]}
        

#         # for course in data:
#         #     university = course[0]
#         #     data_dic["university"][university] = {
#         #         "คณะ": course[1],
#         #         "สาขา": course[2],
#         #         "โปรแกรม": course[3],
#         #         # เพิ่ม key: value ตามข้อมูลที่มี
#         #     }


#     print(data_dic)


def data_dic_info(): # test chat 
    data = data_course_info()
    data_dic = {"university": {}}
    for course in data:
        university = course[0]
        faculty = course[1]
        program = course[2]

        catg_program = course[3]
        campus = course[4]
        expenses  = course[5]

        r1_tcase = course[6]
        r1_cc = course[7]
        r1_ic = course[8]
        r1_vc = course[9]
        r1_nfe = course[10]
        r1_ged = course[11]
        r1_grade = course[12]
        
        r2_tcase = course[13]
        r2_cc = course[14]
        r2_ic = course[15]
        r2_vc = course[16]
        r2_nfe = course[17]
        r2_ged = course[18]
        r2_grade = course[19]

        r3_tcase = course[20]
        r3_cc = course[21]
        r3_ic = course[22]
        r3_vc = course[23]
        r3_nfe = course[24]
        r3_ged = course[25]
        r3_grade = course[26]

        r4_tcase = course[27]
        r4_cc = course[28]
        r4_ic = course[29]
        r4_vc = course[30]
        r4_nfe = course[31]
        r4_ged = course[32]
        r4_grade = course[33]



#         employment = course[7]
#         median_salary = course[8]
        
        if university not in data_dic["university"]:
            data_dic["university"][university] = {}
        if faculty not in data_dic["university"][university]:
            data_dic["university"][university][faculty] = {}
        if program not in data_dic["university"][university][faculty]:
            data_dic["university"][university][faculty][program] = {}
            # data_dic["university"][university][faculty][program] = [program_name_en,program_type,campus,tuition]

        # data_dic["university"][university][faculty][program] = {
        #     [program_name_en,program_type,campus,tuition]
        # }

        data_dic["university"][university][faculty][program] = {
            "Category of Program": catg_program,
            "Campus": campus,
            "Expenses": expenses,
            "TCAS 1": [r1_tcase,r1_cc,r1_ic,r1_vc,r1_nfe,r1_ged,r1_grade],
            "TCAS 2": [r2_tcase,r2_cc,r2_ic,r2_vc,r2_nfe,r2_ged,r2_grade],
            "TCAS 3": [r3_tcase,r3_cc,r3_ic,r3_vc,r3_nfe,r3_ged,r3_grade],
            "TCAS 4": [r4_tcase,r4_cc,r4_ic,r4_vc,r4_nfe,r4_ged,r4_grade],

        }

    return data_dic

    # # print (data_dic)
    # for i in data_dic["university"]["จุฬาลงกรณ์มหาวิทยาลัย"]:
    #     print(i)

    # print()

    # for i in data_dic["university"]["จุฬาลงกรณ์มหาวิทยาลัย"]["คณะวิทยาศาสตร์"]["วท.บ.เทคโนโลยีสารสนเทศ"]:
    #     print(i)

    # print()

    # print(data_dic["university"]["จุฬาลงกรณ์มหาวิทยาลัย"]["คณะวิทยาศาสตร์"]["วท.บ.เทคโนโลยีสารสนเทศ"]["Program Name in English"])

    # # print (data_dic["university"]["จุฬาลงกรณ์มหาวิทยาลัย"])



def course_info(): # menu input course_info
    while True:
        print()
        head = f"|{"Course information":^30}|"
        line = f"+{"-" * (len(head) - 2)}+"
        choice = input(f"{line}\n{head}\n{line}\n|{"1. Add Course Information":{len(head)-2}}|\n|{"2. Report Course Information":{len(head)-2}}|\n|{"3. Back to main":{len(head)-2}}|\n{line}\nSelect option : ")
        match choice:
            case "1":
                add_course_info()
            case "2": 
                report_course_info()
            case "3":
                back_to_main()
            case "4":
                break
        

def add_course_info():
    with open(r"data_information/course_info.txt","w",encoding="utf-8") as fin:
        # universityal =  input("กรุณากรอกชื่อสถานบัน : ")
        # faculty = input("กรุณากรอกชื่อคณะ : ")
        # program = input("กรุณากรอกหลักสูตร : ")
        # c_type = input("กรุณากรอกประเภทหลักสูตร : ")
        # campus = input("กรุณากรอกวิทยาเขต : ")
        # expenses = input("กรุณากรอกค่าใช้จ่ายต่อภาคเรียน : ")
        # employment_rate = input("กรุณากรอกอัตราการได้งานทำ : ")
        # median_salary = input("กรุณากรอกค่ามัธยฐานเงินเดือน : ")
      

        #  ==================== True Use
        # universityal =  "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ"
        # faculty = "คณะเทคโนโลยีและการจัดการอุตสาหกรรม"
        # program = "วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี"
        # catg_program = "ภาษาไทย ปกติ"
        # campus = "ปราจีนบุรี"
        # expenses = "19,000"


        # # ================ test
        # print(f"Enter University Name : {universityal}")
        # print(f"Enter Faculty : {faculty}")
        # print(f"Enter Program : {program}")
        # print(f"Enter Category of Program : {catg_program}")
        # print(f"Enter Campus : {campus}")
        # print(f"Enter Expenses : {expenses}")
        # # ================

        # head = f"|{'Couse_Information':^98}|"
        # line = "-" * len(head)
        # result = f"{line}\n{head}\n{line}\n"
        # title = ["University","Faculty","Program","Category of Program","Campus","Expenses"]
        # datas = [universityal,faculty,program,catg_program,campus,expenses]
        # for i in range(len(title)):
        #     result += (f"| {title[i]:25} | {pad_text(datas[i],68)} |\n")
        # result += line 

        # head2 = f"\n|{'TCAS Rounds':^98}|"
        # title2 = f"| {"Rouds":^25} |{"Central":^10}| International |{"Vocational":10}|{"Non-Formal":10}|{"GED":^10}|{"Grade":^10}|"
        # line2 = "-" * len(head2)
        # result += f"{head2}\n{line2}\n{title2}\n{line2}\n"

        # tcas1 = input("Apply to TCAS Round 1 Portfolio (y/n) : ").lower()
        # result += f"| TCAS 1 | {"Portfolio":16} |"
        # match tcas1:
        #     case "y": 
        #         check_cc = input("Accepted Central Curriculum (y/n) : ").lower()
        #         # check_cc = "y"
        #         if check_cc == "y": cc = "Accepted"
        #         else: cc = "Declined"
        #         check_ic = input("Accepted International Curriculum (y/n) : ").lower()
        #         # check_ic = "y"
        #         if check_ic == "y": ic = "Accepted"
        #         else: ic = "Declined"
        #         check_vc = input("Accepted Vocational Curriculum (y/n) : ").lower()
        #         # check_vc = "y"
        #         if check_vc == "y": vc += "Accepted"
        #         else: vc = "Declined"
        #         check_nfe = input("Accepted Non Formal Education (y/n) : ").lower()
        #         # check_nfe = "y"
        #         if check_nfe == "y": nfe = "Accepted"
        #         else: nfe = "Declined"
        #         check_ged = input("Accepted GED Curriculum (y/n) : ").lower()
        #         # check_ged = "y"
        #         if check_ged == "y": ged += "Accepted"
        #         else: ged = "Declined"
        #         while True:
        #             try:
        #                 mini_gpa = int(input("Enter minimum required GPA : "))
        #                 if mini_gpa >= 0 and mini_gpa <= 4: 
        #                     break
        #             except ValueError: print("Please Enter a numberic minimum required GPA ")
        #         result += f"{cc:^10}|{ic:^15}|{vc:^10}|{nfe:^10}|{ged:^10}|{mini_gpa:^10}|\n"
        #         # d_t1 = (tcas1,check_cc,check_ic,check_vc,check_nfe,check_ged)
        #         d_t1 = ("Portfolio",cc,ic,vc,nfe,ged,mini_gpa)

        #     case _:
        #         cc = "Declined"
        #         ic = "Declined"
        #         vc = "Declined"
        #         nfe = "Declined"
        #         ged = "Declined"
        #         mini_gpa = "Declined"
        #         result += f"{cc:^10}|{ic:^15}|{vc:^10}|{nfe:^10}|{ged:^10}|{mini_gpa:^10}|\n"
        #         d_t1 = ("Portfolio",cc,ic,vc,nfe,ged,mini_gpa)

                


        # tcas2 = input("Apply to TCAS Round 2 Quota (y/n) : ").lower()
        # result += f"| TCAS 2 | {"Quota":16} |"
        # match tcas2:
        #     case "y": 
        #         check_cc = input("Accepted Central Curriculum (y/n) : ").lower()
        #         # check_cc = "y"
        #         if check_cc == "y": cc = "Accepted"
        #         else: cc = "Declined"
        #         check_ic = input("Accepted International Curriculum (y/n) : ").lower()
        #         # check_ic = "y"
        #         if check_ic == "y": ic = "Accepted"
        #         else: ic = "Declined"
        #         check_vc = input("Accepted Vocational Curriculum (y/n) : ").lower()
        #         # check_vc = "y"
        #         if check_vc == "y": vc += "Accepted"
        #         else: vc = "Declined"
        #         check_nfe = input("Accepted Non Formal Education (y/n) : ").lower()
        #         # check_nfe = "y"
        #         if check_nfe == "y": nfe = "Accepted"
        #         else: nfe = "Declined"
        #         check_ged = input("Accepted GED Curriculum (y/n) : ").lower()
        #         # check_ged = "y"
        #         if check_ged == "y": ged += "Accepted"
        #         else: ged = "Declined"
        #         while True:
        #             try:
        #                 mini_gpa = int(input("Enter minimum requi'red GPA : "))
        #                 if mini_gpa >= 0 and mini_gpa <= 4: 
        #                     break
        #             except ValueError: print("Please Enter a numberic minimum required GPA ")
        #         result += f"{cc:^10}|{ic:^15}|{vc:^10}|{nfe:^10}|{ged:^10}|{mini_gpa:^10}|\n"
        #         # d_t2 = (tcas1,check_cc,check_ic,check_vc,check_nfe,check_ged)
        #         d_t2 = ("Quota",cc,ic,vc,nfe,ged,mini_gpa)

        #     case _:
        #         cc = "Declined"
        #         ic = "Declined"
        #         vc = "Declined"
        #         nfe = "Declined"
        #         ged = "Declined"
        #         mini_gpa = "Declined"
        #         result += f"{cc:^10}|{ic:^15}|{vc:^10}|{nfe:^10}|{ged:^10}|{mini_gpa:^10}|\n"
        #         # d_t2 = (tcas2,"n","n","n","n","n")
        #         d_t2 = ("Quota",cc,ic,vc,nfe,ged,mini_gpa)


        # tcas3 = input("Apply to TCAS Round 3 Admission (y/n) : ").lower()
        # result += f"| TCAS 3 | {"Admission":16} |"
        # match tcas1:
        #     case "y": 
        #         check_cc = input("Accepted Central Curriculum (y/n) : ").lower()
        #         # check_cc = "y"
        #         if check_cc == "y": cc = "Accepted"
        #         else: cc = "Declined"
        #         check_ic = input("Accepted International Curriculum (y/n) : ").lower()
        #         # check_ic = "y"
        #         if check_ic == "y": ic = "Accepted"
        #         else: ic = "Declined"
        #         check_vc = input("Accepted Vocational Curriculum (y/n) : ").lower()
        #         # check_vc = "y"
        #         if check_vc == "y": vc += "Accepted"
        #         else: vc = "Declined"
        #         check_nfe = input("Accepted Non Formal Education (y/n) : ").lower()
        #         # check_nfe = "y"
        #         if check_nfe == "y": nfe = "Accepted"
        #         else: nfe = "Declined"
        #         check_ged = input("Accepted GED Curriculum (y/n) : ").lower()
        #         # check_ged = "y"
        #         if check_ged == "y": ged += "Accepted"
        #         else: ged = "Declined"
        #         while True:
        #             try:
        #                 mini_gpa = int(input("Enter minimum required GPA : "))
        #                 if mini_gpa >= 0 and mini_gpa <= 4: 
        #                     break
        #             except ValueError: print("Please Enter a numberic minimum required GPA ")
        #         result += f"{cc:^10}|{ic:^15}|{vc:^10}|{nfe:^10}|{ged:^10}|{mini_gpa:^10}|\n"
        #         # d_t3 = (tcas1,check_cc,check_ic,check_vc,check_nfe,check_ged)
        #         d_t3 = ("Admission",cc,ic,vc,nfe,ged,mini_gpa)

        #     case _:
        #         cc = "Declined"
        #         ic = "Declined"
        #         vc = "Declined"
        #         nfe = "Declined"
        #         ged = "Declined"
        #         mini_gpa = "Declined"
        #         result += f"{cc:^10}|{ic:^15}|{vc:^10}|{nfe:^10}|{ged:^10}|{mini_gpa:^10}|\n"
        #         # d_t3 = (tcas3,"n","n","n","n","n")
        #         d_t3 = ("Admission",cc,ic,vc,nfe,ged,mini_gpa)


        # tcas4 = input("Apply to TCAS Round 4 Direct Admission (y/n) : ").lower()
        # result += f"| TCAS 4 | {"Direct Admission":16} |"
        # match tcas4:
        #     case "y": 
        #         check_cc = input("Accepted Central Curriculum (y/n) : ").lower()
        #         # check_cc = "y"
        #         if check_cc == "y": cc = "Accepted"
        #         else: cc = "Declined"
        #         check_ic = input("Accepted International Curriculum (y/n) : ").lower()
        #         # check_ic = "y"
        #         if check_ic == "y": ic = "Accepted"
        #         else: ic = "Declined"
        #         check_vc = input("Accepted Vocational Curriculum (y/n) : ").lower()
        #         # check_vc = "y"
        #         if check_vc == "y": vc += "Accepted"
        #         else: vc = "Declined"
        #         check_nfe = input("Accepted Non Formal Education (y/n) : ").lower()
        #         # check_nfe = "y"
        #         if check_nfe == "y": nfe = "Accepted"
        #         else: nfe = "Declined"
        #         check_ged = input("Accepted GED Curriculum (y/n) : ").lower()
        #         # check_ged = "y"
        #         if check_ged == "y": ged += "Accepted"
        #         else: ged = "Declined"
        #         while True:
        #             try:
        #                 mini_gpa = int(input("Enter minimum required GPA : "))
        #                 if mini_gpa >= 0 and mini_gpa <= 4: 
        #                     break
        #             except ValueError: print("Please Enter a numberic minimum required GPA ")
        #         result += f"{cc:^10}|{ic:^15}|{vc:^10}|{nfe:^10}|{ged:^10}|{mini_gpa:^10}|\n"
        #         # d_t4 = (tcas1,check_cc,check_ic,check_vc,check_nfe,check_ged)
        #         d_t4 = ("Direct Admission",cc,ic,vc,nfe,ged,mini_gpa)

        #     case _:
        #         cc = "Declined"
        #         ic = "Declined"
        #         vc = "Declined"
        #         nfe = "Declined"
        #         ged = "Declined"
        #         mini_gpa = "Declined"
        #         result += f"{cc:^10}|{ic:^15}|{vc:^10}|{nfe:^10}|{ged:^10}|{mini_gpa:^10}|\n"
        #         # d_t4 = (tcas4,"n","n","n","n","n")
        #         d_t4 = ("Direct Admission",cc,ic,vc,nfe,ged,mini_gpa)


        # result += line

       
        # print(result)
        # check = input("Confirm Information (y/n) : ").lower()
        # if check == "y":
        #     fin.writelines(("|".join((universityal,faculty,program,catg_program,campus,expenses)))+"|"+"|".join(d_t1)+"|"+"|".join(d_t2)+"|"+"|".join(d_t3)+"|"+"|".join(d_t4)+"\n")
            
        # else :
        #     pass
        # ==========================

        data_universities = [
            ["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ", "คณะเทคโนโลยีและการจัดการอุตสาหกรรม", "วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี", "ภาษาไทย ปกติ", "ปราจีนบุรี", "19,000", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.00", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.75", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
            ["มหาวิทยาลัยธรรมศาสตร์", "คณะวิทยาศาสตร์และเทคโนโลยี", "วท.บ.วิทยาการคอมพิวเตอร์", "ภาษาไทย ปกติ", "รังสิต", "20,000", "Portfolio", "Accepted", "Accepted", "Declined", "Declined", "Declined", "2.50", "Quota", "Accepted", "Accepted", "Declined", "Declined", "Declined", "2.75", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
            ["จุฬาลงกรณ์มหาวิทยาลัย", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "ปทุมวัน", "22,000", "Portfolio", "Accepted", "Accepted", "Declined", "Declined", "Declined", "2.50", "Quota", "Accepted", "Accepted", "Declined", "Declined", "Declined", "2.75", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
            ["มหาวิทยาลัยเกษตรศาสตร์", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ วิทยาเขตบางเขน", "ภาษาไทย ปกติ", "บางเขน", "18,500", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.25", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.75", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
            ["มหาวิทยาลัยสงขลานครินทร์", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "หาดใหญ่", "17,500", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.25", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.70", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
            ["มหาวิทยาลัยขอนแก่น", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "เมืองขอนแก่น", "16,800", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.00", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.50", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
            ["มหาวิทยาลัยเชียงใหม่", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "เมืองเชียงใหม่", "18,900", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.30", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.70", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
            ["มหาวิทยาลัยมหิดล", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "พญาไท", "21,800", "Portfolio", "Accepted", "Accepted", "Declined", "Declined", "Declined", "2.50", "Quota", "Accepted", "Accepted", "Declined", "Declined", "Declined", "2.75", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
            ["มหาวิทยาลัยศรีนครินทรวิโรฒ", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "ประสานมิตร", "19,300", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.00", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.50", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
            ["มหาวิทยาลัยนเรศวร", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "เมืองพิษณุโลก", "15,900", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.00", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.50", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
            ["มหาวิทยาลัยบูรพา", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "เมืองชลบุรี", "18,000", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.10", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.60", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
            ["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี", "คณะเทคโนโลยีสารสนเทศ", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "บางมด", "20,500", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.00", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.75", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"]
            ]

        for course in data_universities:
            course = "|".join(course)
            fin.write(course+"\n")
    print()

def tcas_round():
    pass
       

        

def report_course_info(): # report 
    while True:
        print()
        head = f"|{"Report Course Infomation":^30}|"
        line = f"{"-" * len(head)}"
        choice = input(f"{line}\n{head}\n{line}\n|{"1. All Course Information":{len(head)-2}}|\n|{"2. Search Course Information":{len(head)-2}}|\n|{"3. Back to main":{len(head)-2}}|\n{line}\nSelect option : ")
        match choice:
            case "1":
                all_course_info()
            case "2": 
                search_course_info()
            case "3":
                back_to_main()
            case "4":
                break

def all_course_info():
    result = ""
    datas = data_course_info()
    head = f"|{'Report Course Infomation':^90}|"
    line = "-" * len(head)
    # title = ["สถานบัน","คณะ","หลักสูตร","ชื่อหลักสูตรภาษาอังกฤษ","ประเภทหลักสูตร","วิทยาเขต","ค่าใช้จ่ายต่อภาคเรียน"]
    title = ["University","Faculty","Program","Category of Program","Campus","Expenses"]
    result += (f"{line}\n{head}\n{line}\n")
    for course in datas:
        for i in range(len(title)):
            col_data = pad_text(course[i], 90 - 29)  # ลบ len tile กับช่องว่างก่อน col_data
            result += (f"| {title[i]:25}| {col_data} |\n")
        result += line+"\n"
    print(result)
    print()

def search_university():
    while True:
        # ใช้ data ที่ เป็น dic
        print()
        data = data_dic_info()
        result = ""
        head = f"|{'Search Course Information':^98}|"
        line = "-" * len(head)
        result += f"{line}\n{head}\n{line}\n"
        # ค้นหาข้อมูลผ่าน data dic ต้องใช้ items ช่วย ที่ใช้คือ value
        for key,university in data.items():
            n = 0
            search_univ = {}
            for key_univ,faculty in university.items():
                n += 1
                # แปลงเป็น string เติม 0 ด้านหน้า id จะกรอกง่าย
                col_key_univ = pad_text(key_univ,len(head)-9)
                # ทำให้เป็นค่าความกว้างจริง
                search_univ[f"{n:0>2}"] = key_univ
                # สร้าง key id และ value ชื่อ
                result += (f"| {n:0>2} | {col_key_univ} |\n")
            result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
            result += line
        print(result)
        choice = input("selcet : ")
        if choice in search_univ and choice != "00": return(search_univ[choice])
        elif choice == "00": break

def search_faculty(univ):
    while True:
        print()
        data = data_dic_info()
        result = ""
        head = f"|{'Faculty':^98}|"
        line = "-" * len(head)
        result += f"{line}\n{head}\n{line}\n"
        for key,university in data.items():
            n = 0        
            col_univ = pad_text(univ,68)
            result += (f"| {"University":25} | {col_univ} |\n{line}\n")

            search_fac = {}
            for key_fac,faculty in university[univ].items():
                n += 1
                col_key_fac = pad_text(key_fac,len(head)-9)
                search_fac[f"{n:0>2}"] = key_fac
                # สร้าง key ตาม number format n_f จะเป็น key automatic
                result += (f"| {n:0>2} | {col_key_fac} |\n")
            result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
            result += line
        print(result)        
        choice = input("selcet : ")
        if choice in search_fac and choice != "00": return(search_fac[choice])
        elif choice == "00": search_university() 
        print()

def search_program(univ,fac):
    while True:
        print()
        data = data_dic_info()
        result = ""
        head = f"|{'Couse_Name':^98}|"
        line = "-" * len(head)
        result += f"{line}\n{head}\n{line}\n"
        for key,university in data.items():
            n = 0
            col_univ = pad_text(univ,68)
            col_fac = pad_text(fac,68)

            result += (f"| {"University":25} | {col_univ} |\n")
            result += (f"| {"Faculty":25} | {col_fac} |\n{line}\n")

            search_program = {}
            for key_program, program in university[univ][fac].items():
                n += 1
                col_key_program = pad_text(key_program,len(head)-9)
                search_program[f"{n:0>2}"] = key_program
                # สร้าง key ตาม number format n_f จะเป็น key automatic
                result += (f"| {n:0>2} | {col_key_program} |\n")
            result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
            result += line
        print(result)        
        choice = input("selcet : ")
        if choice in search_program and choice != "00": return(search_program[choice])
        elif choice == "00": search_faculty(univ)
        print()
    
def search_title(univ = "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ",fac = "คณะเทคโนโลยีและการจัดการอุตสาหกรรม",program = "วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี"):
    print()
    data = data_dic_info()
    result = ""
    head = f"|{'Couse_Information':^98}|"
    line = "-" * len(head)
    result += f"{line}\n{head}\n{line}\n"
    for key,university in data.items():
        n = 0
        # university = course[0]
        # faculty = course[1]
        # program = course[2]

        col_univ = pad_text(univ,68)
        col_fac = pad_text(fac,68)
        col_program = pad_text(program,68)

        result += (f"| {"University":25} | {col_univ} |\n")
        result += (f"| {"Faculty":25} | {col_fac} |\n")
        result += (f"| {"Program":25} | {col_program} |\n")

        # search_title = {}
        for key_title, title in university[univ][fac][program].items():
            data_title = []
            # n += 1
            # col_key_c_type = pad_text(title,len(head)-9)
            # search_title[f"{n:0>2}"] = key_title
            # สร้าง key ตาม number format n_f จะเป็น key automatic
            # result += (f"| {n:0>2} | {key_title} | {title} |\n")
            if "TCAS" not in key_title:
                col_title = pad_text(title,68)
                result += (f"| {key_title:25} | {col_title} |\n")
                data_title.append(col_title)
            else:
                if key_title == "TCAS 1":
                    head2 = f"|{'TCAS Rounds':^98}|"
                    title2 = f"| {"Rouds":^25} |{"Central":^10}| International |{"Vocational":10}|{"Non-Formal":10}|{"GED":^10}|{"Grade":^10}|"
                    line2 = "-" * len(head2)
                    result += f"{line2}\n{head2}\n{line2}\n{title2}\n{line2}\n"
                    result += f"| {key_title} |"
                    result +=  f" {title[0]:16} |"
                    result += f"{title[1]:^10}|"    
                    result += f"{title[2]:^15}|"
                    result += f"{title[3]:^10}|"
                    result += f"{title[4]:^10}|"
                    result += f"{title[5]:^10}|"
                    result += f"{title[6]:^10}|\n"
                    # if key_title[0]: result +=  f"{key_title[0]:16} |"
                    # elif key_title[2]: result += f"{key_title[2]:^15}"
                    # else: result += f"{key_title:^10}"
                else: 
                    result += f"| {key_title} |"
                    result +=  f" {title[0]:16} |"
                    result += f"{title[1]:^10}|"    
                    result += f"{title[2]:^15}|"
                    result += f"{title[3]:^10}|"
                    result += f"{title[4]:^10}|"
                    result += f"{title[5]:^10}|"
                    result += f"{title[6]:^10}|\n"
                    # result += f"| {key_title} |"
                    # if key_title[0]: result +=  f"{key_title[0]:16} |"
                    # elif key_title[2]: result += f"{key_title[2]:^15}"
                    # else: result += f"{key_title:^10}"
    

    print(result+line)        
    choice = input(f"1. register for study\n2. Back to main\nselect : ")
    match choice:
        case "1":
            datas = data_studten()
            data1 = []
            # iden_code = input("Enter Identification code : ")
            iden_code = "1199901140886"
            print("Enter Identification code : ",iden_code)
            for data in datas:
                if iden_code in data:
                    data.extend((univ,fac,program))
                    
 

            print(data)


    # choice = input("Enter Identification code")


    # choice = input("selcet : ")
    # if choice in search_title: return(search_title[choice])

# test
def search_course_info():
    univ = search_university() 
    fac = search_faculty(univ)
    program = search_program(univ,fac)
    search_title(univ,fac,program)





    
    

def back_to_main():
    menu_main()

def main():
    # course_info()
    # report_course_info()

    # add_course_info()
    # data_course_info()

    # while True:
    #     menu_main()

    # search_course_info()
    search_title()

    # all_course_info()

    # data_dic()
    # print(data_dic_info())

    # data_studten()

if __name__ == "__main__":
    main()