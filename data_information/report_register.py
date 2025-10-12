#เจิม
from wcwidth import wcswidth
import datetime
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
            expenses = f"| {pad_text("EXPENSES", 15)} | {pad_text(Data[13], 71)} |\n"
            print(f"{detail}{line}\n{expenses}{line}")
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
    time = (datetime.datetime.now().strftime("%d/%m/%Y"))
    with open(file_register,"r",encoding="UTF-8") as FileIn :
        report_count = {} #ผมสร้างเอาไว้เก็บค่า
        for Data in FileIn:
            Data = Data.strip().split("|")
            university = Data[7]
            department = Data[9]
            tcas = Data[4]
            primary = (tcas,university,department)
            # print(primary)
            if primary in report_count: #ผมใช้ifนับว่าถ้าหลักสูตรนี้มีคนให้ +1 แต่ถ้าไม่มีให้สร้างใหม่ ค่าเริ่ม 1
                report_count[primary] += 1
            else:
                report_count[primary] = 1
        # print(report_count)
        header = f"{"REPORT COURSE TOTAL":^123}"
        line = "="*(len(header))
        print(f"{line}\n{header}\n{line}")
        print(f"| {pad_text("UNIVERSITY - มหาวิทยาลัย", 35)} | {pad_text("COURSE - หลักสูตร", 30)} | {pad_text("TCAS - รอบสมัคร", 25)} | {pad_text("NUMBER - จำนวน", 20)} |")
        print(line)
        total_people = 0
        for key, value in report_count.items():
            tcas = key[0]
            university = key[1]
            department = key[2]
            count = value
            total_people += count
            print(f"| {pad_text(university, 35)} | {pad_text(department, 30)} | {pad_text(tcas, 25)} | {pad_text(f"{count} คน", 20)} |")
        print(line)
        print(f"| {pad_text("จำนวนทั้งหมด", 96)} | {pad_text(f"{total_people} คน", 20)} |")
        print(line)
        print(f"| {pad_text("", 96)} | {pad_text(f"{"ข้อมูลวันที่":<14} {time}")} |")
        print(line)

def report_paymentAll(): #ข้อ G
    time = (datetime.datetime.now().strftime("%d/%m/%Y"))
    with open(file_register,"r",encoding="UTF-8") as FileIn :
        report_count = {} #ผมสร้างเอาไว้เก็บค่า
        for Data in FileIn:
            Data = Data.strip().split("|")
            university = Data[7]
            department = Data[9]
            tcas = Data[4]
            expenses = Data[13]
            primary = (tcas,university,department,expenses)
            if primary in report_count: #ผมใช้ifนับว่าถ้าหลักสูตรนี้มีคนให้ +1 แต่ถ้าไม่มีให้สร้างใหม่ ค่าเริ่ม 1
                report_count[primary] += 1
            else:
                report_count[primary] = 1
        header = f"|{"REPORT COURSE TOTAL":^130}|"
        line = "="*(len(header))
        print(f"{line}\n{header}\n{line}")
        print(f"| {pad_text("TCAS - รอบสมัคร", 25)} | {pad_text("UNIVERSITY - มหาวิทยาลัย", 35)} | {pad_text("COURSE - หลักสูตร", 20)} | {pad_text("NUMBER - จำนวน", 16)} | {pad_text("MONEY - จำนวนเงิน", 20)} |")
        # print(line)
        total_people = 0
        total_expenses = 0
        n_tcas = None
        for key, value in sorted(report_count.items()):
            tcas = key[0]
            university = key[1]
            department = key[2]
            expenses = key[3]
            count = value
            total_people += count
            total_exp_people = int(expenses)*count
            total_expenses += total_exp_people
            if tcas != n_tcas:
                tcas_display = tcas
                n_tcas = tcas
                print(line)
            else:
                tcas_display = ""
            print(f"| {pad_text(tcas_display, 25)} | {pad_text(university, 35)} | {pad_text(department, 20)} | {pad_text(f"{count} คน", 16)} | {pad_text(f"{total_exp_people:>16,.2f} บาท")} |")
        print(line)
        print(f"| {pad_text("จำนวนคนสมัครทั้งหมด - TOTAL NUMBER OF REGISTER", 105)} | {pad_text(f"{total_people:>17} คน")} |")
        print(line)
        print(f"| {pad_text("ยอดเงินทั้งหมด - TOTAL AMOUNT", 105)} | {pad_text(f"{total_expenses:>16,.2f} บาท")} |")
        print(line)
        print(f"| {pad_text("", 105)} | {pad_text(f"{"ข้อมูลวันที่":<14} {time}")} |")
        print(line)

#report_idcard()
# report_idcard_All()
# report_exp_id_card()
report_course()
# report_paymentAll()

#----------------------------------------------------------------------------------------------------------------------------------
# วิสา G

# file_register = r"data_information/datas/data_register.txt" #อ่านของเจิม  #ขอคอมเม้นไว้ เพราะเจิมเรียกมาแล้ว

def read_register(filename):
    
    file = open(filename, 'r' , encoding='utf-8') 
    lines = file.readlines()
    file.close()

    data = []
    for line in lines:
        Table = line.strip().split('|') #ลบช่องว่าง \n แล้วแยกข้อมูลด้วย |
        data.append(Table) #เก็บข้อมูลแต่ละบรรทัดลงใน list
    return data #ส่งข้อมูลออกไปใช้งาน

def display_report(data): #พารามิเตอร์ จากการส่งค่าข้อมูลที่อ่านมา
    print("\n")
    Top = (f'{pad_text("TCAS Applicant and Fee Statistics Report".center(151))}\n') # ไปนับมาจาก col_width มาใส่
    Top += (f'{pad_text("รายงานสถิติจำนวนผู้สมัครและค่าสมัคร TCAS 69".center(158))}')
    print(Top)

    #กำหนดหัวตาราง
    headers = ["|Admission", "University", "Faculty", "Program","Type", "Units(คน)", "Total Price(บาท)|"]
  
    col_widths = [18, 39, 28, 25, 18, 12, 16] 

    table_width = sum(col_widths) # รวมค่าความกว้างทั้งหมดจาก list col_widths ที่กำหนดด้านบน

    print("-" * table_width)

    #สร้างหัวตารางด้วย for loop
    for i in range(len(headers)): # h คือชื่อหัวคอลัมน์ เช่น "Admission"
        h = headers[i]
        print(pad_text(h,col_widths[i]), end="") # col_widths[i] คือ i จะวนไปหาความกว้างที่กำหนดใน list
        #จัดข้อความ h  ภายในความกว้างกำหนดใน col_widths[]
        # end = "" ไม่ขึ้นบรรทัดใหม่ทันที แต่พิพพ์ต่อกันเป็นแถวเดียว
    print() #ขึ้นบรรทัดใหม่ หลังจากพิมพ์หัวตารางครบทุกคอลัมน์

    Total_applicants = 0 #ใช้เก็บข้อมูลจำนวนผู้สมัครทั้งหมด 
    Total_fee = 0 # ยอดเงินรวมทัังหมด
 
    
    rounds = {}
    for row in data: # data คือ รายการข้อมูลที่อ่านมาจาก ระบบลงทะเบียนของเจิม
        round_name = "|" + row[4].split()[0] +" " +row[4].split()[1]#หยิบเอาคำแค่ TCAS หรือรอบการสมัครนั้นๆ มา เว้นช่องด้วย ""
    
        if round_name not in rounds: #ตรวจสอบว่าใน rounds ยังไม่มีคีย์ชื่อ round_name หรือไม่
            rounds[round_name] = [] # ถ้าไม่มี ให้สร้างคีย์นั้น พร้อมกำหนดเป็นค่า list ว่าง
        rounds[round_name].append(row)

        #for loop วนแสดงผลรายงานทีละรอบ TCAS 
        round_names = sorted(rounds) #เปลี่ยนจาก litsที่ตอนแรกเราใส่ เป็น sorted เท่านี้ก็จบแล้ว

    for round_name in round_names:
        print("-" * table_width)

        for count in range(len(rounds[round_name])):
            row = rounds[round_name][count]
            if count == 0 :
                Admission = round_name  # ถ้าเป็นบรรทัดแรกของรอบ ให้ใส่ชื่อรอบ TCAS นั้นๆ
            else:
                Admission = "|" # ถ้าไม่มี ให้เป็น |
            
            University = row[7]             #ชื่อมหาลัย
            Faculty = row[8]                #ชื่อคณะ
            Program = row[9]                #ชื่อสาขา
            Prog_type = row[10]             #ชื่อประเภทการเรียน
            Units = 1                       #จำนวนนักเรียนสมัคร
            Fee = int(row[13])              #ค่าสมัครสอบ

            Total_applicants += 1           #ยอดสมัคร
            Total_fee += Fee                #ค่าใช้จ่ายในการสอบทั้งหมดของทุกคน


            cols = [Admission , University, Faculty, Program, Prog_type, str(Units), str(Fee)] #lits ใน col ที่เก็บค่าของ index ที่รันมา


            for i in range(len(cols)):
                c = cols[i]
                print(pad_text(c,col_widths[i]),end="") 
            print("|")

    print("-" * table_width)
    print("|",end="")
    summary_1 = f"{pad_text('ผู้สมัครทั้งหมดจำนวน')} {Total_applicants} คน"
    summary_2 = f"{pad_text('จำนวนเงินทั้งหมด')} {Total_fee:,.2f} บาท"
    print(summary_1.rjust(130),end=""+" | ")
    print(summary_2.rjust(20)+" |") 
    print("-" * table_width)
    Time = (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
    print(f'{pad_text("ข้อมูลล่าสุด ณ วันที่ ").rjust(147)}{Time}')


# def main(): #เรียกใช้งาน
#     # file_register = r"data_information/datas/data_register.txt"
#     data = read_register(file_register) #อ่านไฟล์เจิม

#     display_report(data)


# if __name__ == "__main__":
#     main()