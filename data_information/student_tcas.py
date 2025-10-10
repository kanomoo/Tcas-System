from wcwidth import wcswidth
import datetime
from .course_info import data_dic_info

def pad_text(text, width = 0): # padding text เติมช่องว่าง ควรใช้เฉพาะภาษาไทย
    text = str(text)
    real_width = wcswidth(text)                         # คำนวณความกว้างจริงของข้อความในเทอมินอล (นับช่องว่างที่ข้อความใช้)
    if width == 0:
        return text 
    elif real_width < width:                            # ถ้าความกว้างจริงของข้อความน้อยกว่าความกว้างที่ต้องการ
        return text + " " * (width - real_width)        # เติมช่องว่างให้ครบตามความกว้างที่กำหนด เพื่อจัดข้อความให้อยู่ในตำแหน่ง len จริงๆ
    return text   

def student_menu():
    while True:
        print()
        head = f"|{"Student Menu":^25}|"
        line = f"+{"=" * (len(head) - 2)}+"
        choice = input(f"{line}\n{head}\n{line}\n|{"1. Student Register":25}|\n|{"2. Student Register Exam":25}|\n|{"3. Student data setting":25}|\n|{"4. Exit Program":25}|\n{line}\nSelect option : ")
        match choice:
            case "1":
                student_register()
            case "2":
                student_register_exam()
            case "3":
                sudent_data_setting()
            case "4":
                break


def student_register():
    with open(r"data_information/datas/data_student.txt","w",encoding = "utf-8") as fin:
        # iden_code = input("Enter Identification code : ")
        # name = input("Enter Name-Surname : ")
        # email = input("Enter Emaill : ")
        # phon = input("Enter Phone Number : ")
        

        data_list = [
        ["1199901140886", "นายปภาวิน ธิติชุณหกุล", "few717254@gmail.com", "0806525546"],
        ["1199901140999", "นางสาวสมหญิง ตัวอย่าง", "example@gmail.com", "0912345678"],
        ["1199901140887", "นายสมชาย ใจดี", "somchai@example.com", "0801234567"],
        ["1199901140888", "นางสาวสมศรี ขยัน", "somsri@example.com", "0812345678"],
        ["1199901140889", "นายดำรงค์ ศรีสุข", "damrong@example.com", "0823456789"],
        ["1199901140890", "นางสาวสุนิสา ยิ้มแย้ม", "sunisa@example.com", "0898765432"],
        ["1199901140891", "นายปรเมศวร์ ดีใจ", "promet@example.com", "0865432198"],
        ["1199901140892", "นางสาวมุกดา สวยสดงดงาม", "mukda@example.com", "0843219876"],
        ["1199901140893", "นายสหัส ว่องไว", "sahat@example.com", "0832198765"],
        ["1199901140894", "นางสาวกิตติมา มีน้ำใจ", "kittima@example.com", "0821987654"]
        ]
        
        for i in data_list:
            fin.write("|".join(i)+"\n")

        iden_code = "1199901140886"
        name = "นายปภาวิน ธิติชุณหกุล"
        email = "few717254@gmail.com"
        phone = "0806525546"
    

        print(f"Enter Identification code : {iden_code}")
        print("Enter Emaill : ")
        print("Enter Phone Number : ")
        print(f"Enter Name-Surname : {name}")

        head = f"|{'Register':^98}|"
        line = "-" * len(head)
        result = f"{line}\n{head}\n{line}\n"
        datas = {"identification code":iden_code,"emaill":email,"phone":phone,"name":name}
        for title, data in datas.items():
            result += (f"| {title:25} | {pad_text(data,68)} |\n")
        result += line 
        print(result)

        confirm = input("Confirm Information (y/n) : ").lower()
        match confirm:
            case "y":
                fin.writelines("|".join((iden_code,name,email,phone))+"\n")
            case "n":
                pass
            case _:
                print("Invalid input. Please try again.")        

def sudent_data_setting():
    datas = data_student()
    data_re = data_register()
    # iden_code = input("Enter Identification code :")
    
    iden_code = "1199901140887"
    print(f"Enter Identification code : {iden_code}")
    
    # for index ,data in enumerate(datas):
        # if iden_code in data and len(data) > 4:
    for index ,data in enumerate(data_re):
        if iden_code in data and len(data) > 4:
            iden_code = data[0]
            name = data[1]
            email = data[2]
            phone = data[3]

            time = data[4]
            univ = data[5]
            fac = data[6]
            program = data[7]
            catg = data[8]
            campus = data[9]
            expenses = data[10]


            head = f"|{'Register':^98}|"
            line = "-" * len(head)
            result = f"{line}\n{head}\n{line}\n"
            data_students = {}

            data_students["iden_code"] = iden_code
            data_students["name"] = name
            data_students["email"] = email
            data_students["phone"] = phone

            data_students["time"] = time
            data_students["university "] = univ
            data_students["faculty"] = fac
            data_students["program"] = program
            data_students["category"] = catg
            data_students["campus"] = campus
            data_students["expenses"] = expenses

            for title, student in data_students.items():
                result += (f"| {title:25} | {pad_text(student,68)} |\n")
                if title == "phone":
                    result += line + "\n"
                    result += (f"| {data[len(data) - 1]:^96} |\n")
                    result += line + "\n"
            result += line
            print(result)

            choice = input("1. Edit\n2. Delete\n3. Save & Exit\nselect : ")
            match choice:
                case "1":
                    # e_data = input("Enter the field name to edit : ")

                    e_data = "phone"
                    print(f"Enter The Field Name to Edit : {e_data}")

                    print(f"{e_data} : {data_students[e_data]}")
            
                    # n_data = input("Enter data to edit : ")

                    n_data = "12"
                    print(f"Enter Data to Edit : {n_data}")

                    data_students[e_data] = n_data
                    confirm = input("Confirm Change Data (y/n) : ").lower()
                    match confirm:
                        case "y":
                            # with open(r"data_information/datas/data_student.txt","w",encoding = "utf-8") as fin:
                            #     fin.writelines("|".join(([data for key, data in data_students.items()]))+"\n")
                            # print(True)
                            datas[index] = [sub_data for key, sub_data in data_students.items()]
                            with open(r"data_information/datas/data_student.txt","w",encoding="utf-8") as fin:
                                for i in datas:
                                    fin.writelines("|".join(i)+"\n")
                            print("Data saved.")

                        case "n":
                            print("Data not save")
                        case _:
                            print("Invalid input. Please try again.")
                case "2":
                    del datas[index]
                    with open(r"data_information/datas/data_student.txt","w",encoding="utf-8") as fin:
                        for i in datas:
                            fin.writelines("|".join(i)+"\n")
                    print("Data deleted.")
            break
    else:
        for index ,data in enumerate(datas):

            if iden_code in data and len(data) <= 4:
                iden_code = data[0]
                name = data[1]
                email = data[2]
                phone = data[3]



                head = f"|{'Register':^98}|"
                line = "-" * len(head)
                result = f"{line}\n{head}\n{line}\n"
                data_students = {}
                    
                data_students["iden_code"] = iden_code
                data_students["name"] = name
                data_students["email"] = email
                data_students["phone"] = phone

                for title, student in data_students.items():
                    result += (f"| {title:25} | {pad_text(student,68)} |\n")
                result += line + "\n"
                result += (f"| {"No data exam":^96} |\n")
                result += line
                print(result)

                choice = input("1. Edit\n2. Delete\n3. Save & Exit\nselect : ")
                match choice:
                    case "1":
                        # e_data = input("Enter the field name to edit : ")

                        e_data = "phone"
                        print(f"Enter The Field Name to Edit : {e_data}")

                        print(f"{e_data} : {data_students[e_data]}")
                
                        # n_data = input("Enter data to edit : ")

                        n_data = "12"
                        print(f"Enter Data to Edit : {n_data}")

                        data_students[e_data] = n_data
                        confirm = input("Confirm Change Data (y/n) : ").lower()
                        match confirm:
                            case "y":
                                # with open(r"data_information/datas/data_student.txt","w",encoding = "utf-8") as fin:
                                #     fin.writelines("|".join(([data for key, data in data_students.items()]))+"\n")
                                # print(True)
                                datas[index] = [sub_data for key, sub_data in data_students.items()]
                                with open(r"data_information/datas/data_student.txt","w",encoding="utf-8") as fin:
                                    for i in datas:
                                        fin.writelines("|".join(i)+"\n")
                                print("Data saved.")
                            case "n":
                                print("Data not save")
                            case _:
                                print("Invalid input. Please try again.")
                    case "2":
                        del datas[index]
                        with open(r"data_information/datas/data_student.txt","w",encoding="utf-8") as fin:
                            for i in datas:
                                fin.writelines("|".join(i)+"\n")
                        print("Data deleted.")
                break
            
            else:
                print("No sutdent data")

def data_student():
    data = []
    with open(r"data_information/datas/data_student.txt","r",encoding="utf-8") as fout:
        for i in fout: 
            data.append(i.strip("\n").split("|"))
    return data

def data_register():
    data = []
    with open(r"data_information/datas/data_register.txt","r",encoding="utf-8") as fout:
        for i in fout:
            data.append(i.strip("\n").split("|"))
    return data

def student_register_exam():
    univ, id1 = search_university()
    if univ is None:
        print("Invalid university selection.")
        return None
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
        choice = input("selcet : ")
        id = ""
        id += choice if choice != "00" and choice in check_id else ""
        if choice in search_univ and choice != "00": return(search_univ[choice]) ,id 
        elif choice == "00": break

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
        id += choice if choice != "00" and choice in check_id else ""
        if choice in search_fac and choice != "00": return(search_fac[choice]) ,id
        elif choice == "00": break
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
        choice = input("selcet : ")
        id += choice if choice != "00" and choice in check_id else ""
        if choice in search_program and choice != "00": return(search_program[choice]) , id
        elif choice == "00": search_faculty(id,univ)
        print()
    
def search_title(id,univ = "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ",fac = "คณะเทคโนโลยีและการจัดการอุตสาหกรรม",program = "วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี"):
    while True:
        print()
        data = data_dic_info()
        result = ""
        head = f"|{'Couse_Information':^98}|"
        line = "-" * len(head)
        result += f"{line}\n{head}\n{line}\n"
        check_id = []  
        exam = []
        time = (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
        uni_list = []
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
            uni_list.extend((univ,fac,program))
            # search_title = {}
            titles = []
            for key_title, title in university[univ][fac][program].items():
                # n += 1
                # col_key_c_type = pad_text(title,len(head)-9)
                # search_title[f"{n:0>2}"] = key_title
                # สร้าง key ตาม number format n_f จะเป็น key automatic
                # result += (f"| {n:0>2} | {key_title} | {title} |\n")
                col_title = pad_text(title,68)
                result += (f"| {key_title:25} | {col_title} |\n")
                titles.append(title)

            tcass = {"01":"TCAS1 Portfolio","02":"TCAS2 Quota","03":"TCAS1 Admission","04":"TCAS4 Direct Admission"}
            result += f"{line}\n|{'Round TCAS':^98}|\n{line}\n"
            for key, n_tcas in tcass.items():
                result += (f"| {key:0>2} | {n_tcas:{len(head)-9}} |\n")
                check_id.append(key)

        print(result+line)   

        choice = input("Enter Round Tcas : ")
        tcas = tcass[choice] ## 
        id += choice if choice != "00" and choice in check_id else ""
        main_id = 1
        with open(r"data_information/datas/data_register.txt","r",encoding="utf-8") as fin :
            for i in fin:
                i = i.strip("\n").split("|")
                if i[4][:8] == id:
                    main_id += 1
        id += format(main_id,"0>4")
        exam.append(id)
        exam.append(tcas)
        exam.append(time)
        exam.extend(uni_list)
        exam.extend(titles)
        exam.append("300")
        print(id)
        choice = input(f"1. register for study\n2. Back to main\nselect : ")
        match choice:
            case "1":
                datas = data_student()

                iden_code = input("Enter Identification code :")

                # iden_code = "1199901140886"
                # print(f"Enter Identification code : {iden_code}")

                for index ,data in enumerate(datas):
                    if iden_code in data and len(data) <= 4:
                        with open(r"data_information/datas/data_register.txt","a",encoding="utf-8") as fin:
                            data.extend(exam)
                            fin.writelines("|".join(data)+"\n")

                            # # datas[index].extend(exam)
                            # for i in data:
                            #     fin.writelines("|".join(i)+"\n")
                        print("Data saved.")
                        break
                    elif len(data) >= 5:
                        print("This Data already exists. You cannot add it again.")
                    else:
                        print("No sutdent data")
                break
            case "2":
                break

        # choice = input("Enter Identification code")


        # choice = input("selcet : ")
        # if choice in search_title: return(search_title[choice])