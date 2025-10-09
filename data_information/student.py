from course_info import pad_text

def student_register():
    with open(r"data_information/datas/data_student.txt","w",encoding = "utf-8") as fin:
        # iden_code = input("Enter Identification code : ")
        # n_s = input("Enter Name-Surname : ")
        
        iden_code = "1199901140886"
        name = "นายปภาวิน ธิติชุณหกุล"



        print(f"Enter Identification code : {iden_code}")
        print(f"Enter Name-Surname : {name}")

        head = f"|{'Register':^98}|"
        line = "-" * len(head)
        result = f"{line}\n{head}\n{line}\n"
        datas = {"identification code":iden_code,"name":name}
        for title, data in datas.items():
            result += (f"| {title:25} | {pad_text(data,68)} |\n")
        result += line 
        print(result)

        confirm = input("Confirm Information (y/n) : ").lower()
        match confirm:
            case "y":
                fin.writelines("|".join((iden_code,name))+"\n")
            case "n":
                1.
        

def data_studten():
    data = []
    with open(r"data_information/datas/data_student.txt","r",encoding="utf-8") as fout:
        for i in fout: 
            data.append(i.strip("\n").split("|"))
    print(data)
    return data