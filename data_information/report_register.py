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
    id_card = input("\nEnter Identification Code : ").strip() #รับค่าใช้ ID นักเรียนเด้อ
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
                break
        else: print("Data not found")

def report_idcard_All(): #ข้อ D แบบทั้งหมด
    print()
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
    id_card = input("\nEnter Identification Code : ").strip() #รับค่าใช้ ID นักเรียนเด้อ
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
                break
        else: print("Data not found")

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

# report_idcard()
# report_idcard_All()
# report_exp_id_card()
# report_course()
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

def display_report(data = file_register): #พารามิเตอร์ จากการส่งค่าข้อมูลที่อ่านมา
    data = read_register(file_register) 
    print("\n")
    Top = (f'{("TCAS Applicant and Fee Statistics Report".center(151))}\n') # ไปนับมาจาก col_width มาใส่
    Top += (f'{("รายงานสถิติจำนวนผู้สมัครและค่าสมัคร TCAS 69".center(158))}')
    print(Top)

    #กำหนดหัวตาราง
    headers = ["|Admission", "University", "Faculty", "Program","Type", "Units(คน)", "Total Price(บาท)|"]

  
    col_widths = [18, 39, 28, 25, 18, 12, 16] 

    table_width = sum(col_widths)+1 # รวมค่าความกว้างทั้งหมดจาก list col_widths ที่กำหนดด้านบน

    print("=" * table_width)
    


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
    for row in data:
        round_name = "|" + row[4].split()[0] +" "+row[4].split()[1] #เอารอบ TCAS ไปเก็บไว้ที่ round_name ก่อน

        if round_name not in rounds: #ส่วนสำคัญ ในการจัดกลุ่มข้อมูลตามรอบ TCAS
            rounds[round_name] = [] #สรา้ง list ว่างก่อน เพราะยังไม่มี key นี้ใน dictionary
            #ถ้าไม่ทำ rounds[round_name] = [] จะทำให้เกิด KeyError ได้
        rounds[round_name].append(row)

    # วนลูปแสดงผลทีละรอบ
    round_names = sorted(rounds)
    for round_name in round_names:
        print("-" * table_width)

        # เก็บกลุ่มย่อย (มหาวิทยาลัย, คณะ, สาขา, ประเภท)
        groups = {}
        for row in rounds[round_name]:
            key = (row[7], row[8], row[9], row[10]) #สร้าง tuple เป็น key ไปเลย 

            #ถ้าไม่ซํ้ากัน ทำ if นี้
            if key not in groups:
                groups[key] = [0, 0] # [จำนวคนสมัคร(ซ้ำ), total_fee] เอาง่ายๆคือvalue เริ่มใหม่ ซ้ำกันก็ไม่แสดงชื่อซ้ำ
                # print(groups[key]) อันนี้ดูเฉยๆว่ามันถูกไหม

            groups[key][0] += 1 # ถ้ามันซ้ำให้ +1 จาก key = (row[7], row[8], row[9], row[10]) เอาง่ายๆถ้ามันซ้ำกันก็บวกตามที่ซ้ำกันนั่นแหละ
            groups[key][1] += int(row[13]) # total_fee ตรงกับช่องจำนวนเงิน เอาง่ายๆถ้ามันซ้ำกันก็บวกตามที่ซ้ำกันนั่นแหละ

            # print(groups[key][0], groups[key][1]) เช็ค

            # groups {
            # groups element = 1 (row[7], row[8], row[9], row[10]) , [2, fee+fee = 600]
            # }

        Tcas = 0 #ตัวนับลำดับรายการแรก พิมพ์ TCAS แค่บรรทัดแรกของรอบนั้น

        # แสดงผลเฉพาะค่าที่รวมแล้ว
        for (university, faculty, program, prog_type), (units, fee) in groups.items():
            # for loop ทำงานตามคู่ element หรือ จำนวนบรรทัดที่มีข้อมูล

            #วงเล็บแรก: แตก key ซึ่งเป็น tuple 4 ค่า ออกเป็นตัวแปร university, faculty, program, prog_type
            #วงเล็บสอง: แตก value ซึ่งเป็น list 2 ค่า ออกเป็นตัวแปร units, fee
            
            if Tcas == 0:
                admission = round_name # row[4] ตรงกับคำว่า Tcas รอบนั้นๆ
            else:
                admission = "|"

            cols = [admission, university, faculty, program, prog_type, format(units).rjust(8), format(fee, ",.2f").rjust(15)]

            for i in range(len(cols)):
                print(pad_text(cols[i], col_widths[i]), end="")
                # if i == 6 :
                #     print(str(fee).rjust())
            print("|")

            Total_applicants += units
            Total_fee += fee
            Tcas += 1

    print("=" * table_width)
    print("|",end="")
    summary_1 = f"{('ผู้สมัครทั้งหมดจำนวน')} {Total_applicants} คน"
    summary_2 = f"{('จำนวนเงินทั้งหมด')} {Total_fee:,.2f} บาท"
    print(summary_1.rjust(130),end=""+" | ")
    print(summary_2.rjust(20)+" |") 
    print("-" * table_width)
    Time = (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
    print(f'{("|")+("| ข้อมูลล่าสุด ณ วันที่ ").rjust(145)}{Time} |')
    print(f"{("=" * table_width)}")