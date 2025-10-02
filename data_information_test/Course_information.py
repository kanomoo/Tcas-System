def input_information():
    with open("Course_information.txt","w") as fout:
        # institutional =  input("กรุณากรอกชื่อสถานบัน")
        # c_name = input("กรุณากรอกหลักสูตร : ")
        # eng_c_name = input("กรุณากรอกชื่อหลักสูตรภาษาอังกฤษ : ")
        # c_type = input("กรุณากรอกประเภทหลักสูตร : ")
        # campus = input("กรุณากรอกวิทยาเขต : ")
        # expenses = input("กรุณากรอกค่าใช้จ่ายต่อภาคเรียน : ")
        # employment_rate = input("กรุณากรอกอัตราการได้งานทำ : ")
        # median_salary = input("กรุณากรอกค่ามัธยฐานเงินเดือน : ")

        institutional =  "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ"
        faculty = "คณะเทคโนโลยีและการจัดการอุตสาหกรรม"
        c_name = "วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี"
        eng_c_name = "Bachelor of Science Program in Information Technology"
        c_type = "ภาษาไทย ปกติ"
        campus = "ปราจีนบุรี"
        expenses = "19,000 ต่อภาคเรียน"
        employment_rate = "ร้อยละ 74.84 (ภาพรวมคณะ รุ่นปีการศึกษา 2565)"
        median_salary = "19,340 บาท (ภาพรวมคณะ รุ่นปีการศึกษา 2565)"

        fout.writelines("-".join((institutional,faculty,c_name,eng_c_name,c_type,campus,expenses,employment_rate,median_salary,"\n")))
        fout.writelines("-".join((institutional,"คณะครุศาสตร์อุตสาหกรรม","ค.อ.บ.เทคโนโลยีคอมพิวเตอร์ (ภาษาไทย ปกติ) วิทยาเขต กรุงเทพฯ",c_type,campus,expenses,employment_rate,median_salary,"\n")))


def data():
    with open("Course_information.txt","r") as fin:
        for i in fin:
            i = (i.strip("\n").strip("").split("-"))
            print(i)        

def report_information():
    details = ["ชื่อหลักสูตร","ชื่อหลักสูตรภาษาอังกฤษ","ประเภทหลักสูตร","วิทยาเขต","ค่าใช้จ่าย","อัตราการได้งานทำ","ค่ามัธยฐานเงินเดือน"]
    n = 0
    with open("Course_information.txt","r") as fin:
        for course in fin:
            n += 1
            print("========================================")
            course = course.split("-")
            print(course)
            for i in range(len(course)):
                print(f" : {course[i]}")
                if course[i] == "\n":
                    print(True)

            if n % 7 == 0:
                print("========================================")
                n = 0

input_information()
data()