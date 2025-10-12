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
        break
    

        

def add_course_info():
    univ, n_data1 = add_university()
    fac, n_data2 = add_faculty(n_data1,univ)
    program, n_data3 = add_program(n_data2,univ,fac)
    add_title(n_data3,univ,fac,program)

    # with open(r"data_information/datas/data_course_info.txt","a",encoding="utf-8") as fin:
    #     universityal =  input("Enter University Name :")
    #     faculty = input("Enter Faculty : ")
    #     program = input("Enter Program : ")
    #     catg_program = input("Enter Category of Program : ")
    #     campus = input("Enter Campus : ")
    #     expenses = input("Enter Expenses : ")

    #     #  ==================== True Use
    #     # universityal =  "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ"
    #     # faculty = "คณะเทคโนโลยีและการจัดการอุตสาหกรรม"
    #     # program = "วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี"
    #     # catg_program = "ภาษาไทย ปกติ"
    #     # campus = "ปราจีนบุรี"
    #     # expenses = "19,000"



    #     # print(f"Enter University Name : {universityal}")
    #     # print(f"Enter Faculty : {faculty}")
    #     # print(f"Enter Program : {program}")
    #     # print(f"Enter Category of Program : {catg_program}")
    #     # print(f"Enter Campus : {campus}")
    #     # print(f"Enter Expenses : {expenses}")

    #     head = f"|{'Couse_Information':^98}|"
    #     line = "-" * len(head)
    #     result = f"{line}\n{head}\n{line}\n"
    #     title = ["University","Faculty","Program","Category of Program","Campus","Expenses"]
    #     datas = [universityal,faculty,program,catg_program,campus,expenses]
    #     for i in range(len(title)):
    #         result += (f"| {title[i]:25} | {pad_text(datas[i],68)} |\n")
    #     result += line 

       
    #     print(result)
    #     check = input("Confirm Information (y/n) : ").lower()
    #     if check == "y":
    #         fin.writelines(("|".join((universityal,faculty,program,catg_program,campus,expenses)))+"\n")
    #     else :
    #         pass
        
        # ==========================

        # data_universities = [
        # # มหาวิทยาลัย 1
        # ["มหาวิทยาลัยจุฬาลงกรณ์", "คณะวิทยาศาสตร์", "วิทยาการคอมพิวเตอร์", "ภาษาไทย ปกติ", "ปทุมวัน", "22000"],
        # ["มหาวิทยาลัยจุฬาลงกรณ์", "คณะวิทยาศาสตร์", "คณิตศาสตร์ประยุกต์", "ภาษาไทย ปกติ", "ปทุมวัน", "22000"],
        # ["มหาวิทยาลัยจุฬาลงกรณ์", "คณะวิศวกรรมศาสตร์", "วิศวกรรมไฟฟ้า", "ภาษาไทย ปกติ", "ปทุมวัน", "25000"],
        # ["มหาวิทยาลัยจุฬาลงกรณ์", "คณะวิศวกรรมศาสตร์", "วิศวกรรมโยธา", "ภาษาไทย ปกติ", "ปทุมวัน", "25000"],

        # # มหาวิทยาลัย 2
        # ["มหาวิทยาลัยธรรมศาสตร์", "คณะวิทยาศาสตร์", "วิทยาการคอมพิวเตอร์", "ภาษาไทย ปกติ", "ท่าพระจันทร์", "20000"],
        # ["มหาวิทยาลัยธรรมศาสตร์", "คณะวิทยาศาสตร์", "เคมีประยุกต์", "ภาษาไทย ปกติ", "ท่าพระจันทร์", "20000"],
        # ["มหาวิทยาลัยธรรมศาสตร์", "คณะนิติศาสตร์", "กฎหมายแพ่ง", "ภาษาไทย ปกติ", "รังสิต", "22000"],
        # ["มหาวิทยาลัยธรรมศาสตร์", "คณะนิติศาสตร์", "กฎหมายอาญา", "ภาษาไทย ปกติ", "รังสิต", "22000"],

        # # มหาวิทยาลัย 3
        # ["มหาวิทยาลัยเกษตรศาสตร์", "คณะวิทยาศาสตร์", "เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "บางเขน", "18500"],
        # ["มหาวิทยาลัยเกษตรศาสตร์", "คณะวิทยาศาสตร์", "ฟิสิกส์", "ภาษาไทย ปกติ", "บางเขน", "18500"],
        # ["มหาวิทยาลัยเกษตรศาสตร์", "คณะวิศวกรรมศาสตร์", "วิศวกรรมโยธา", "ภาษาไทย ปกติ", "บางเขน", "19000"],
        # ["มหาวิทยาลัยเกษตรศาสตร์", "คณะวิศวกรรมศาสตร์", "วิศวกรรมเครื่องกล", "ภาษาไทย ปกติ", "บางเขน", "19000"],

        # # มหาวิทยาลัย 4
        # ["มหาวิทยาลัยเชียงใหม่", "คณะวิทยาศาสตร์", "เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "เชียงใหม่", "18900"],
        # ["มหาวิทยาลัยเชียงใหม่", "คณะวิทยาศาสตร์", "เคมี", "ภาษาไทย ปกติ", "เชียงใหม่", "18900"],
        # ["มหาวิทยาลัยเชียงใหม่", "คณะวิศวกรรมศาสตร์", "วิศวกรรมเครื่องกล", "ภาษาไทย ปกติ", "เชียงใหม่", "20000"],
        # ["มหาวิทยาลัยเชียงใหม่", "คณะวิศวกรรมศาสตร์", "วิศวกรรมไฟฟ้า", "ภาษาไทย ปกติ", "เชียงใหม่", "20000"],

        # # มหาวิทยาลัย 5
        # ["มหาวิทยาลัยขอนแก่น", "คณะวิทยาศาสตร์", "เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "ขอนแก่น", "16800"],
        # ["มหาวิทยาลัยขอนแก่น", "คณะวิทยาศาสตร์", "ชีววิทยา", "ภาษาไทย ปกติ", "ขอนแก่น", "16800"],
        # ["มหาวิทยาลัยขอนแก่น", "คณะวิศวกรรมศาสตร์", "วิศวกรรมคอมพิวเตอร์", "ภาษาไทย ปกติ", "ขอนแก่น", "17500"],
        # ["มหาวิทยาลัยขอนแก่น", "คณะวิศวกรรมศาสตร์", "วิศวกรรมโยธา", "ภาษาไทย ปกติ", "ขอนแก่น", "17500"],

        # # มหาวิทยาลัย 6
        # ["มหาวิทยาลัยสงขลานครินทร์", "คณะวิทยาศาสตร์", "เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "หาดใหญ่", "17500"],
        # ["มหาวิทยาลัยสงขลานครินทร์", "คณะวิทยาศาสตร์", "จุลชีววิทยา", "ภาษาไทย ปกติ", "หาดใหญ่", "17500"],
        # ["มหาวิทยาลัยสงขลานครินทร์", "คณะวิศวกรรมศาสตร์", "วิศวกรรมไฟฟ้า", "ภาษาไทย ปกติ", "หาดใหญ่", "18000"],
        # ["มหาวิทยาลัยสงขลานครินทร์", "คณะวิศวกรรมศาสตร์", "วิศวกรรมโยธา", "ภาษาไทย ปกติ", "หาดใหญ่", "18000"],

        # # มหาวิทยาลัย 7
        # ["มหาวิทยาลัยมหิดล", "คณะวิทยาศาสตร์", "วิทยาการคอมพิวเตอร์", "ภาษาไทย ปกติ", "พญาไท", "21800"],
        # ["มหาวิทยาลัยมหิดล", "คณะวิทยาศาสตร์", "เคมี", "ภาษาไทย ปกติ", "พญาไท", "21800"],
        # ["มหาวิทยาลัยมหิดล", "คณะวิศวกรรมศาสตร์", "วิศวกรรมไฟฟ้า", "ภาษาไทย ปกติ", "พญาไท", "24000"],
        # ["มหาวิทยาลัยมหิดล", "คณะวิศวกรรมศาสตร์", "วิศวกรรมสิ่งแวดล้อม", "ภาษาไทย ปกติ", "พญาไท", "24000"],

        # # มหาวิทยาลัย 8
        # ["มหาวิทยาลัยบูรพา", "คณะวิทยาศาสตร์", "เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "ชลบุรี", "18000"],
        # ["มหาวิทยาลัยบูรพา", "คณะวิทยาศาสตร์", "คณิตศาสตร์ประยุกต์", "ภาษาไทย ปกติ", "ชลบุรี", "18000"],
        # ["มหาวิทยาลัยบูรพา", "คณะวิศวกรรมศาสตร์", "วิศวกรรมโยธา", "ภาษาไทย ปกติ", "ชลบุรี", "18500"],
        # ["มหาวิทยาลัยบูรพา", "คณะวิศวกรรมศาสตร์", "วิศวกรรมเครื่องกล", "ภาษาไทย ปกติ", "ชลบุรี", "18500"],

        # # มหาวิทยาลัย 9
        # ["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี", "คณะเทคโนโลยีสารสนเทศ", "เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "บางมด", "20500"],
        # ["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี", "คณะเทคโนโลยีสารสนเทศ", "วิทยาการคอมพิวเตอร์", "ภาษาไทย ปกติ", "บางมด", "20500"],
        # ["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี", "คณะวิทยาศาสตร์", "ฟิสิกส์", "ภาษาไทย ปกติ", "บางมด", "21000"],
        # ["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี", "คณะวิทยาศาสตร์", "เคมี", "ภาษาไทย ปกติ", "บางมด", "21000"],

        # # มหาวิทยาลัย 10
        # ["มหาวิทยาลัยศรีนครินทรวิโรฒ", "คณะวิทยาศาสตร์", "คณิตศาสตร์", "ภาษาไทย ปกติ", "ประสานมิตร", "19300"],
        # ["มหาวิทยาลัยศรีนครินทรวิโรฒ", "คณะวิทยาศาสตร์", "ชีววิทยา", "ภาษาไทย ปกติ", "ประสานมิตร", "19300"],
        # ["มหาวิทยาลัยศรีนครินทรวิโรฒ", "คณะนิติศาสตร์", "กฎหมายแพ่ง", "ภาษาไทย ปกติ", "ประสานมิตร", "20000"],
        # ["มหาวิทยาลัยศรีนครินทรวิโรฒ", "คณะนิติศาสตร์", "กฎหมายอาญา", "ภาษาไทย ปกติ", "ประสานมิตร", "20000"],

        # # มหาวิทยาลัย 11
        # ["มหาวิทยาลัยนเรศวร", "คณะวิทยาศาสตร์", "เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "พิษณุโลก", "15900"],
        # ["มหาวิทยาลัยนเรศวร", "คณะวิทยาศาสตร์", "ฟิสิกส์", "ภาษาไทย ปกติ", "พิษณุโลก", "15900"],
        # ["มหาวิทยาลัยนเรศวร", "คณะวิศวกรรมศาสตร์", "วิศวกรรมโยธา", "ภาษาไทย ปกติ", "พิษณุโลก", "16500"],
        # ["มหาวิทยาลัยนเรศวร", "คณะวิศวกรรมศาสตร์", "วิศวกรรมเครื่องกล", "ภาษาไทย ปกติ", "พิษณุโลก", "16500"],

        # # มหาวิทยาลัย 12
        # ["มหาวิทยาลัยเชียงใหม่", "คณะวิทยาศาสตร์", "วิทยาการคอมพิวเตอร์", "ภาษาไทย ปกติ", "เชียงใหม่", "18900"],
        # ["มหาวิทยาลัยเชียงใหม่", "คณะวิทยาศาสตร์", "เคมี", "ภาษาไทย ปกติ", "เชียงใหม่", "18900"],
        # ["มหาวิทยาลัยเชียงใหม่", "คณะวิศวกรรมศาสตร์", "วิศวกรรมไฟฟ้า", "ภาษาไทย ปกติ", "เชียงใหม่", "19500"],
        # ["มหาวิทยาลัยเชียงใหม่", "คณะวิศวกรรมศาสตร์", "วิศวกรรมโยธา", "ภาษาไทย ปกติ", "เชียงใหม่", "19500"],
        # ]


        # for course in data_universities:
        #     course = "|".join(course)
        #     fin.write(course+"\n")
    print()

def add_university():
    state = 0
    data = data_dic_info()
    while True:
        # ใช้ data ที่ เป็น dic
        print()
        result = ""
        head = f"|{'Search Course Information':^98}|"
        line = "-" * len(head)
        result += f"{line}\n{head}\n{line}\n"
        check_id = []
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
                check_id.append(f"{n:0>2}")
            result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
            result += line
        print(result)
        choice = input("selcet number data or name new data : ")
        id = ""
        id += choice if choice != "00" and choice in check_id else ""
        if choice in search_univ and choice != "00": return(search_univ[choice]) , data 
        elif choice == "00": report_course_info()
        elif not choice.isdigit() : 
            if state == 0:
                print(f"New course information : {choice}")
                confirm = input("Confirm Information (y/n) : ").lower()
                match confirm:
                    case "y":
                        if choice not in data["university"]:
                            data["university"][choice] = {}
                            state = 1
                    case "n":
                        pass
                    case _:
                        print("Invalid input Please try again")
                none_data = choice
            else: print(f"Please add data {none_data} to finishd")
        else: print("Invalid input Please try again")

            


def add_faculty(n_data,univ):
    state = 0
    while True:
        print()
        # data = data_dic_info()
        result = ""
        head = f"|{'Faculty':^98}|"
        line = "-" * len(head)
        result += f"{line}\n{head}\n{line}\n"
        check_id = []
        for key,university in n_data.items():
            n = 0
            search_fac = {}
            col_univ = pad_text(univ,68)
            result += (f"| {"University":25} | {col_univ} |\n{line}\n")

            for key_fac, faculty in university[univ].items():
                n += 1
                col_key_fac = pad_text(key_fac,len(head)-9)
                search_fac[f"{n:0>2}"] = key_fac
                # สร้าง key ตาม number format n_f จะเป็น key automatic
                result += (f"| {n:0>2} | {col_key_fac} |\n")
                check_id.append(f"{n:0>2}")
            result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
            result += line
        print(result)        
        choice = input("selcet : ")
        # id += choice if choice != "00" and choice in check_id else ""
        if choice in search_fac and choice != "00": return(search_fac[choice]) ,n_data
        elif choice == "00": search_university() 
        elif not choice.isdigit() : 
            if state == 0 :
                print(f"New course information : {choice}")
                confirm = input("Confirm Information (y/n) : ").lower()
                match confirm:
                    case "y":
                        if choice not in n_data["university"][univ]:
                            n_data["university"][univ][choice] = {}
                            state = 1
                    case "n":
                        pass
                    case _:
                        print("Invalid input Please try again")
                none_data = choice
            else: print(f"Please add data {none_data} to finishd")
        else: print("Invalid input Please try again")
        print()

def add_program(n_data,univ,fac):
    state = 0
    while True:
        print()
        # data = data_dic_info()
        result = ""
        head = f"|{'Couse_Name':^98}|"
        line = "-" * len(head)
        result += f"{line}\n{head}\n{line}\n"
        check_id = []
        for key,university in n_data.items():
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
                check_id.append(f"{n:0>2}")
            result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
            result += line
        print(result)        
        choice = input("selcet : ")
        # id += choice if choice != "00" and choice in check_id else ""
        if choice in search_program and choice != "00": return(search_program[choice]) , n_data
        elif choice == "00": search_faculty(id,univ)
        elif not choice.isdigit() : 
            print(f"New course information : {choice}")
            confirm = input("Confirm Information (y/n) : ").lower()
            match confirm:
                case "y":
                    if state == 0:
                        if choice not in n_data["university"][univ][fac]:
                            n_data["university"][univ][fac][choice] = {}

                            n_data["university"][univ][fac][choice] = {
                                "Category of Program": "Please add data",
                                "Campus": "Please add data",
                                "Expenses": "Please add data",
                            }
                            print(n_data)
                            state = 1
                    else: print("Please add data to finishd")
                case "n":
                    pass
                case _:
                    print("Invalid input Please try again")
        else: print("Invalid input Please try again")
        print()

    
def add_title(n_data,univ = "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ",fac = "คณะเทคโนโลยีและการจัดการอุตสาหกรรม",program = "วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี"):
    print()
    state = 0
    while True:
        # data = data_dic_info()
        result = ""
        head = f"|{'Couse_Information':^98}|"
        line = "-" * len(head)
        result += f"{line}\n{head}\n{line}\n"

        
        for key,university in n_data.items():

            # n = 0
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
        if state == 0 and title == "Please add data":
            catg = input("Enter Category of Program : ")
            campus = input("Enter Campus : ")
            expenses = input("Enter Expenses : ")
            confirm = input("Confirm Information (y/n) : ").lower()
            match confirm:
                case "y":
                    n_data["university"][univ][fac][program] = {
                        "Category of Program": catg,
                        "Campus": campus,
                        "Expenses": expenses,
                    }
                    state = 1
                case "n":
                    pass
                case _:
                    print("Invalid input Please try again")

        choice = input(f"1. Change data\n2. Delect data\n3. Save data\nselect : ")
        match choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                # with open(r"data_information/datas/data_course_info.txt","w",encoding="utf-8") as fin:
                #     fin.write("|".joine(n_data+"\n"))
                pass
            case _:
                pass
        

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
                course_info()
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
    result += (f"{line}\n{head}\n{line}")
    print(result)

    n = 0
    for course in datas:
        n += 1
        if n == 1: print(f"|{f" Course {n} ":^90}|\n{line}")
        else: print(f"\n{line}\n|{f" Course {n} ":^90}|\n{line}")
        for i in range(len(title)):
            # result += f"คอร์สที่ {n} {course[i]}\n"
            col_data = pad_text(course[i], 90 - 29)  # ลบ len tile กับช่องว่างก่อน col_data
            print(f"| {title[i]:25}| {col_data} |")
            # result += (f"| {title[i]:25}| {col_data} |\n")
        print(line)
        # result += line + f"{n}\n"
    print()

def setting_course_info():
    univ, id1 = search_university()
    fac, id2 = search_faculty(id1,univ)
    program, id3 = search_program(id2,univ,fac)
    search_title(id3,univ,fac,program)

def search_university():
    while True:
        # ใช้ data ที่ เป็น dic
        print()
        data = data_dic_info()
        result = ""
        head = f"|{'Search Course Information':^98}|"
        line = "-" * len(head)
        result += f"{line}\n{head}\n{line}\n"
        check_id = []
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
                check_id.append(f"{n:0>2}")
            result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
            result += line
        print(result)
        choice = input("selcet number data or name new data : ")
        id = ""
        id += choice if choice != "00" and choice in check_id else ""
        if choice in search_univ and choice != "00": return(search_univ[choice]) ,id 
        elif choice == "00": report_course_info()
        else: print("Invalid input Please try again")



def search_faculty(id,univ):
    while True:
        print()
        data = data_dic_info()
        result = ""
        head = f"|{'Faculty':^98}|"
        line = "-" * len(head)
        result += f"{line}\n{head}\n{line}\n"
        check_id = []
        for key,university in data.items():
            n = 0
            search_fac = {}
            col_univ = pad_text(univ,68)
            result += (f"| {"University":25} | {col_univ} |\n{line}\n")

            for key_fac, faculty in university[univ].items():
                n += 1
                col_key_fac = pad_text(key_fac,len(head)-9)
                search_fac[f"{n:0>2}"] = key_fac
                # สร้าง key ตาม number format n_f จะเป็น key automatic
                result += (f"| {n:0>2} | {col_key_fac} |\n")
                check_id.append(f"{n:0>2}")
            result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
            result += line
        print(result)        
        choice = input("selcet number data or name new data : ")
        id += choice if choice != "00" and choice in check_id else ""
        if choice in search_fac and choice != "00": return(search_fac[choice]) ,id
        elif choice == "00": search_university()
        else: print("Invalid input Please try again")
        print()

def search_program(id,univ,fac):
    while True:
        print()
        data = data_dic_info()
        result = ""
        head = f"|{'Couse_Name':^98}|"
        line = "-" * len(head)
        result += f"{line}\n{head}\n{line}\n"
        check_id = []
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
                check_id.append(f"{n:0>2}")
            result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
            result += line
        print(result)        
        choice = input("selcet number data or name new data : ")
        id += choice if choice != "00" and choice in check_id else ""
        if choice in search_program and choice != "00": return(search_program[choice]) , id
        elif choice == "00": search_faculty(id,univ)
        else: print("Invalid input Please try again")

        print()
    

    
def search_title(id,univ = "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ",fac = "คณะเทคโนโลยีและการจัดการอุตสาหกรรม",program = "วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี"):
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