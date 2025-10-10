#เจิม
from wcwidth import wcswidth

def pad_text(text, width = 0): # padding text เติมช่องว่าง ควรใช้เฉพาะภาษาไทย
    text = str(text)
    real_width = wcswidth(text)                         # คำนวณความกว้างจริงของข้อความในเทอมินอล (นับช่องว่างที่ข้อความใช้)
    if width == 0:
        return text 
    elif real_width < width:                            # ถ้าความกว้างจริงของข้อความน้อยกว่าความกว้างที่ต้องการ
        return text + " " * (width - real_width)        # เติมช่องว่างให้ครบตามความกว้างที่กำหนด เพื่อจัดข้อความให้อยู่ในตำแหน่ง len จริงๆ
    return text   

file_register = r"data_information/datas/data_register.txt"


def report_idcard(): #ข้อ D แบบรายบุคคล
    id_card = input("Enter Identification Code : ").strip() #รับค่าใช้ ID นักเรียนเด้อ
    with open(file_register,"r",encoding="UTF-8") as FileIn :
        for Data in FileIn:
            Data = Data.strip().split("|")
            if Data[0] == id_card:
                header = f"{"REPORT ID CARD":^90}"
                line = "="*(len(header))
                print(f"{line}\n{header}\n{line}")
                detail = f"| {pad_text("TCAS", 15)} | {pad_text(Data[4], 68)} |\n"
                detail += f"| {pad_text("ID", 15)} | {pad_text(Data[0], 68)} |\n"
                detail += f"| {pad_text("NAME", 15)} | {pad_text(Data[1], 68)} |\n"
                detail += f"| {pad_text("UNIVERSITY", 15)} | {pad_text(Data[7], 68)} |\n"
                detail += f"| {pad_text("FACULTY", 15)} | {pad_text(Data[8], 68)} |\n"
                detail += f"| {pad_text("DEPARTMENT", 15)} | {pad_text(Data[9], 68)} |\n"
                detail += f"| {pad_text("CAMPUS", 15)} | {pad_text(Data[10], 68)} |\n"
                detail += f"| {pad_text("DATE", 15)} | {pad_text(Data[6], 68)} |\n"
                # detail += f"| {pad_text("EXPENSES", 15)} | {pad_text(Data[13], 68)} |\n"
                # detail += f"| {"ID CARD":<15} | {Data[0]:<68} |\n"
                # detail += f"| {"NAME":<15} | {Data[1]:<68} | \n"
                # detail += f"| {"UNIVERSITY":<15} | {Data[7]:<68} |\n"
                # detail += f"| {"FACULTY":<15} | {Data[8]:<68} |\n"
                # detail += f"| {"DEPARTMENT":<15} | {Data[9]:<68} |\n"
                # detail += f"| {"CAMPUS":<15} | {Data[10]:<68} |\n"
                # detail += f"| {"DATE":<15} | {Data[6]:<68} |\n"
                # detail += f"| {"EXPENSES":<15} | {Data[13]:<68} |\n"
                print(f"{detail}{line}")

def report_idcard_All(): #ข้อ D แบบทั้งหมด
    with open(file_register,"r",encoding="UTF-8") as FileIn :
        num = 1
        for Data in FileIn:
            Data = Data.strip().split("|")
            header = f"{"REPORT ID CARD":^90}#{num:<2}"
            line = "="*(len(header))
            print(f"{line}\n{header}\n{line}")
            detail = f"| {pad_text("TCAS", 15)} | {pad_text(Data[4], 71)} |\n"
            detail += f"| {pad_text("ID", 15)} | {pad_text(Data[0], 71)} |\n"
            detail += f"| {pad_text("NAME", 15)} | {pad_text(Data[1], 71)} |\n"
            detail += f"| {pad_text("UNIVERSITY", 15)} | {pad_text(Data[7], 71)} |\n"
            detail += f"| {pad_text("FACULTY", 15)} | {pad_text(Data[8], 71)} |\n"
            detail += f"| {pad_text("DEPARTMENT", 15)} | {pad_text(Data[9], 71)} |\n"
            detail += f"| {pad_text("CAMPUS", 15)} | {pad_text(Data[10], 71)} |\n"
            detail += f"| {pad_text("DATE", 15)} | {pad_text(Data[6], 71)} |\n"
            detail += f"| {pad_text("EXPENSES", 15)} | {pad_text(Data[13], 71)} |\n"
            print(f"{detail}{line}")
            num += 1

def report_exp_id_card(): #ข้อ E
    id_card = input("Enter Identification Code : ").strip() #รับค่าใช้ ID นักเรียนเด้อ
    with open(file_register,"r",encoding="UTF-8") as FileIn :
        for Data in FileIn:
            Data = Data.strip().split("|")
            if Data[0] == id_card:
                header = f"{"REPORT ID CARD":^90}"
                line = "="*(len(header))
                print(f"{line}\n{header}\n{line}")
                detail = f"| {pad_text("TCAS", 15)} | {pad_text(Data[4], 68)} |\n"
                detail += f"| {pad_text("ID", 15)} | {pad_text(Data[0], 68)} |\n"
                detail += f"| {pad_text("NAME", 15)} | {pad_text(Data[1], 68)} |\n"
                detail += f"| {pad_text("UNIVERSITY", 15)} | {pad_text(Data[7],68)} |\n"
                detail += f"| {pad_text("FACULTY", 15)} | {pad_text(Data[8], 68)} |\n"
                detail += f"| {pad_text("DEPARTMENT", 15)} | {pad_text(Data[9], 68)} |\n"
                detail += f"| {pad_text("CAMPUS", 15)} | {pad_text(Data[10], 68)} |\n"
                detail += f"| {pad_text("DATE", 15)} | {pad_text(Data[6], 68)} |\n"
                expenses = f"| {pad_text("EXPENSES", 15)} | {pad_text(Data[13], 68)} |\n"
                print(f"{detail}{line}\n{expenses}{line}")

def report_course(): #ข้อ F
    with open(file_register,"r",encoding="UTF-8") as FileIn :
        report_count = {} #ผมสร้างเอาไว้เก็บค่า
        for Data in FileIn:
            Data = Data.strip().split("|")
            university = Data[7]
            department = Data[9]
            tcas = Data[4]
            primary = (tcas,university, department)
            # print(primary)
            if primary in report_count: #ผมใช้ifนับว่าถ้าหลักสูตรนี้มีคนให้ +1 แต่ถ้าไม่มีให้สร้างใหม่ ค่าเริ่ม 1
                report_count[primary] += 1
            else:
                report_count[primary] = 1
        # print(report_count)
        header = f"{"REPORT COURSE TOTAL":^113}"
        line = "="*(len(header))
        print(f"{line}\n{header}\n{line}")
        print(f"| {pad_text("UNIVERSITY - มหาวิทยาลัย", 35)} | {pad_text("COURSE - หลักสูตร", 30)} | {pad_text("TCAS - รอบสมัคร", 15)} | {pad_text("NUMBER - จำนวน", 20)} |")
        print(line)
        total_people = 0
        for key, value in report_count.items():
            tcas = key[0]
            university = key[1]
            department = key[2]
            count = value
            total_people += count
            print(f"| {pad_text(university, 35)} | {pad_text(department, 30)} | {pad_text(tcas, 15)} | {pad_text(f'{count} คน', 20)} |")
        print(line)
        print(f"| {pad_text("จำนวนทั้งหมด", 86)} | {pad_text(f'{total_people} คน', 20)} |")
        print(line)


# report_idcard()
report_idcard_All()
# report_exp_id_card()
# report_course()