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

def data_course_info(): # เก็บข้อมูลจากไฟล์
    data = []
    with open(r"data_information/datas/data_course_info.txt","r",encoding="utf-8") as fout:
        for i in fout: 
            data.append(i.strip("\n").split("|"))
    return(sorted(data))

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
        
        if university not in data_dic["university"]:
            data_dic["university"][university] = {}
        if faculty not in data_dic["university"][university]:
            data_dic["university"][university][faculty] = {}
        if program not in data_dic["university"][university][faculty]:
            data_dic["university"][university][faculty][program] = {}

        data_dic["university"][university][faculty][program] = {
            "Category of Program": catg_program,
            "Campus": campus,
            "Expenses": expenses,
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
                break

        

def add_course_info():
    with open(r"data_information/datas/data_course_info.txt","w",encoding="utf-8") as fin:
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



        # print(f"Enter University Name : {universityal}")
        # print(f"Enter Faculty : {faculty}")
        # print(f"Enter Program : {program}")
        # print(f"Enter Category of Program : {catg_program}")
        # print(f"Enter Campus : {campus}")
        # print(f"Enter Expenses : {expenses}")


        # head = f"|{'Couse_Information':^98}|"
        # line = "-" * len(head)
        # result = f"{line}\n{head}\n{line}\n"
        # title = ["University","Faculty","Program","Category of Program","Campus","Expenses"]
        # datas = [universityal,faculty,program,catg_program,campus,expenses]
        # for i in range(len(title)):
        #     result += (f"| {title[i]:25} | {pad_text(datas[i],68)} |\n")
        # result += line 

       
        # print(result)
        # check = input("Confirm Information (y/n) : ").lower()
        # if check == "y":
        #     fin.writelines(("|".join((universityal,faculty,program,catg_program,campus,expenses)))+"\n")
        # else :
        #     pass
        
        # ==========================

        data_universities = [
        # มหาวิทยาลัย 1
        ["มหาวิทยาลัยจุฬาลงกรณ์", "คณะวิทยาศาสตร์", "วิทยาการคอมพิวเตอร์", "ภาษาไทย ปกติ", "ปทุมวัน", "22000"],
        ["มหาวิทยาลัยจุฬาลงกรณ์", "คณะวิทยาศาสตร์", "คณิตศาสตร์ประยุกต์", "ภาษาไทย ปกติ", "ปทุมวัน", "22000"],
        ["มหาวิทยาลัยจุฬาลงกรณ์", "คณะวิศวกรรมศาสตร์", "วิศวกรรมไฟฟ้า", "ภาษาไทย ปกติ", "ปทุมวัน", "25000"],
        ["มหาวิทยาลัยจุฬาลงกรณ์", "คณะวิศวกรรมศาสตร์", "วิศวกรรมโยธา", "ภาษาไทย ปกติ", "ปทุมวัน", "25000"],

        # มหาวิทยาลัย 2
        ["มหาวิทยาลัยธรรมศาสตร์", "คณะวิทยาศาสตร์", "วิทยาการคอมพิวเตอร์", "ภาษาไทย ปกติ", "ท่าพระจันทร์", "20000"],
        ["มหาวิทยาลัยธรรมศาสตร์", "คณะวิทยาศาสตร์", "เคมีประยุกต์", "ภาษาไทย ปกติ", "ท่าพระจันทร์", "20000"],
        ["มหาวิทยาลัยธรรมศาสตร์", "คณะนิติศาสตร์", "กฎหมายแพ่ง", "ภาษาไทย ปกติ", "รังสิต", "22000"],
        ["มหาวิทยาลัยธรรมศาสตร์", "คณะนิติศาสตร์", "กฎหมายอาญา", "ภาษาไทย ปกติ", "รังสิต", "22000"],

        # มหาวิทยาลัย 3
        ["มหาวิทยาลัยเกษตรศาสตร์", "คณะวิทยาศาสตร์", "เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "บางเขน", "18500"],
        ["มหาวิทยาลัยเกษตรศาสตร์", "คณะวิทยาศาสตร์", "ฟิสิกส์", "ภาษาไทย ปกติ", "บางเขน", "18500"],
        ["มหาวิทยาลัยเกษตรศาสตร์", "คณะวิศวกรรมศาสตร์", "วิศวกรรมโยธา", "ภาษาไทย ปกติ", "บางเขน", "19000"],
        ["มหาวิทยาลัยเกษตรศาสตร์", "คณะวิศวกรรมศาสตร์", "วิศวกรรมเครื่องกล", "ภาษาไทย ปกติ", "บางเขน", "19000"],

        # มหาวิทยาลัย 4
        ["มหาวิทยาลัยเชียงใหม่", "คณะวิทยาศาสตร์", "เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "เชียงใหม่", "18900"],
        ["มหาวิทยาลัยเชียงใหม่", "คณะวิทยาศาสตร์", "เคมี", "ภาษาไทย ปกติ", "เชียงใหม่", "18900"],
        ["มหาวิทยาลัยเชียงใหม่", "คณะวิศวกรรมศาสตร์", "วิศวกรรมเครื่องกล", "ภาษาไทย ปกติ", "เชียงใหม่", "20000"],
        ["มหาวิทยาลัยเชียงใหม่", "คณะวิศวกรรมศาสตร์", "วิศวกรรมไฟฟ้า", "ภาษาไทย ปกติ", "เชียงใหม่", "20000"],

        # มหาวิทยาลัย 5
        ["มหาวิทยาลัยขอนแก่น", "คณะวิทยาศาสตร์", "เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "ขอนแก่น", "16800"],
        ["มหาวิทยาลัยขอนแก่น", "คณะวิทยาศาสตร์", "ชีววิทยา", "ภาษาไทย ปกติ", "ขอนแก่น", "16800"],
        ["มหาวิทยาลัยขอนแก่น", "คณะวิศวกรรมศาสตร์", "วิศวกรรมคอมพิวเตอร์", "ภาษาไทย ปกติ", "ขอนแก่น", "17500"],
        ["มหาวิทยาลัยขอนแก่น", "คณะวิศวกรรมศาสตร์", "วิศวกรรมโยธา", "ภาษาไทย ปกติ", "ขอนแก่น", "17500"],

        # มหาวิทยาลัย 6
        ["มหาวิทยาลัยสงขลานครินทร์", "คณะวิทยาศาสตร์", "เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "หาดใหญ่", "17500"],
        ["มหาวิทยาลัยสงขลานครินทร์", "คณะวิทยาศาสตร์", "จุลชีววิทยา", "ภาษาไทย ปกติ", "หาดใหญ่", "17500"],
        ["มหาวิทยาลัยสงขลานครินทร์", "คณะวิศวกรรมศาสตร์", "วิศวกรรมไฟฟ้า", "ภาษาไทย ปกติ", "หาดใหญ่", "18000"],
        ["มหาวิทยาลัยสงขลานครินทร์", "คณะวิศวกรรมศาสตร์", "วิศวกรรมโยธา", "ภาษาไทย ปกติ", "หาดใหญ่", "18000"],

        # มหาวิทยาลัย 7
        ["มหาวิทยาลัยมหิดล", "คณะวิทยาศาสตร์", "วิทยาการคอมพิวเตอร์", "ภาษาไทย ปกติ", "พญาไท", "21800"],
        ["มหาวิทยาลัยมหิดล", "คณะวิทยาศาสตร์", "เคมี", "ภาษาไทย ปกติ", "พญาไท", "21800"],
        ["มหาวิทยาลัยมหิดล", "คณะวิศวกรรมศาสตร์", "วิศวกรรมไฟฟ้า", "ภาษาไทย ปกติ", "พญาไท", "24000"],
        ["มหาวิทยาลัยมหิดล", "คณะวิศวกรรมศาสตร์", "วิศวกรรมสิ่งแวดล้อม", "ภาษาไทย ปกติ", "พญาไท", "24000"],

        # มหาวิทยาลัย 8
        ["มหาวิทยาลัยบูรพา", "คณะวิทยาศาสตร์", "เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "ชลบุรี", "18000"],
        ["มหาวิทยาลัยบูรพา", "คณะวิทยาศาสตร์", "คณิตศาสตร์ประยุกต์", "ภาษาไทย ปกติ", "ชลบุรี", "18000"],
        ["มหาวิทยาลัยบูรพา", "คณะวิศวกรรมศาสตร์", "วิศวกรรมโยธา", "ภาษาไทย ปกติ", "ชลบุรี", "18500"],
        ["มหาวิทยาลัยบูรพา", "คณะวิศวกรรมศาสตร์", "วิศวกรรมเครื่องกล", "ภาษาไทย ปกติ", "ชลบุรี", "18500"],

        # มหาวิทยาลัย 9
        ["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี", "คณะเทคโนโลยีสารสนเทศ", "เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "บางมด", "20500"],
        ["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี", "คณะเทคโนโลยีสารสนเทศ", "วิทยาการคอมพิวเตอร์", "ภาษาไทย ปกติ", "บางมด", "20500"],
        ["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี", "คณะวิทยาศาสตร์", "ฟิสิกส์", "ภาษาไทย ปกติ", "บางมด", "21000"],
        ["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี", "คณะวิทยาศาสตร์", "เคมี", "ภาษาไทย ปกติ", "บางมด", "21000"],

        # มหาวิทยาลัย 10
        ["มหาวิทยาลัยศรีนครินทรวิโรฒ", "คณะวิทยาศาสตร์", "คณิตศาสตร์", "ภาษาไทย ปกติ", "ประสานมิตร", "19300"],
        ["มหาวิทยาลัยศรีนครินทรวิโรฒ", "คณะวิทยาศาสตร์", "ชีววิทยา", "ภาษาไทย ปกติ", "ประสานมิตร", "19300"],
        ["มหาวิทยาลัยศรีนครินทรวิโรฒ", "คณะนิติศาสตร์", "กฎหมายแพ่ง", "ภาษาไทย ปกติ", "ประสานมิตร", "20000"],
        ["มหาวิทยาลัยศรีนครินทรวิโรฒ", "คณะนิติศาสตร์", "กฎหมายอาญา", "ภาษาไทย ปกติ", "ประสานมิตร", "20000"],

        # มหาวิทยาลัย 11
        ["มหาวิทยาลัยนเรศวร", "คณะวิทยาศาสตร์", "เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "พิษณุโลก", "15900"],
        ["มหาวิทยาลัยนเรศวร", "คณะวิทยาศาสตร์", "ฟิสิกส์", "ภาษาไทย ปกติ", "พิษณุโลก", "15900"],
        ["มหาวิทยาลัยนเรศวร", "คณะวิศวกรรมศาสตร์", "วิศวกรรมโยธา", "ภาษาไทย ปกติ", "พิษณุโลก", "16500"],
        ["มหาวิทยาลัยนเรศวร", "คณะวิศวกรรมศาสตร์", "วิศวกรรมเครื่องกล", "ภาษาไทย ปกติ", "พิษณุโลก", "16500"],

        # มหาวิทยาลัย 12
        ["มหาวิทยาลัยเชียงใหม่", "คณะวิทยาศาสตร์", "วิทยาการคอมพิวเตอร์", "ภาษาไทย ปกติ", "เชียงใหม่", "18900"],
        ["มหาวิทยาลัยเชียงใหม่", "คณะวิทยาศาสตร์", "เคมี", "ภาษาไทย ปกติ", "เชียงใหม่", "18900"],
        ["มหาวิทยาลัยเชียงใหม่", "คณะวิศวกรรมศาสตร์", "วิศวกรรมไฟฟ้า", "ภาษาไทย ปกติ", "เชียงใหม่", "19500"],
        ["มหาวิทยาลัยเชียงใหม่", "คณะวิศวกรรมศาสตร์", "วิศวกรรมโยธา", "ภาษาไทย ปกติ", "เชียงใหม่", "19500"],
        ]


        for course in data_universities:
            course = "|".join(course)
            fin.write(course+"\n")
    print()

def report_course_info(): # report 
    while True:
        print()
        head = f"|{"Report Course Infomation":^30}|"
        line = f"{"-" * len(head)}"
        choice = input(f"{line}\n{head}\n{line}\n|{"1. All Course Information":{len(head)-2}}|\n|{"2. Setting Course Information":{len(head)-2}}|\n|{"3. Back to main":{len(head)-2}}|\n{line}\nSelect option : ")
        match choice:
            case "1":
                all_course_info()
            case "2": 
                setting_course_info()
            case "3":
                break
            case "4":
                break

def all_course_info():
    print()
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
        result += line + "\n"
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
            search_fac = {}
            for key_fac, faculty in university[univ].items():
                n += 1
                col_key_fac = pad_text(key_fac,len(head)-9)
                search_fac[f"{n:0>2}"] = key_fac
                # สร้าง key ตาม number format n_f จะเป็น key automatic
                result += (f"| {n:0>2} | {col_key_fac} |\n")
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
            col_title = pad_text(title,68)
            result += (f"| {key_title:25} | {col_title} |\n")
            data_title.append(col_title)
    

    print(result+line)        
    choice = input(f"1. Change data\n2. Delect data\nselect : ")
    


    # choice = input("Enter Identification code")


    # choice = input("selcet : ")
    # if choice in search_title: return(search_title[choice])

# test
def setting_course_info():
    univ = search_university()
    if univ is None:
        print("Invalid university selection.")
        return None
    fac = search_faculty(univ)
    program = search_program(univ,fac)
    search_title(univ,fac,program)


def main():
    # course_info()
    # report_course_info()

    # data_course_info()

    # while True:
    #     menu_main()

    # setting_course_info()
    # search_title()

    # all_course_info()
    # data_dic()
    # print(data_dic_info())

    # data_studten()
    # add_course_info()
    pass

if __name__ == "__main__":
    main()