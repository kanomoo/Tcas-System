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





# test = "|1|1+1.1+|1"
# tests = ((test.split("|")))
# data = []
# for i in tests:
#     data.append(i.split("+"))
# print(data)


def add_course_info():
    with open(r"data_information/course_info.txt","w",encoding="utf-8") as fin:
        # universityal =  input("กรุณากรอกชื่อสถานบัน")
        # faculty = input("กรุณากรอกชื่อคณะ")
        # program = input("กรุณากรอกหลักสูตร : ")
        # eng_program = input("กรุณากรอกชื่อหลักสูตรภาษาอังกฤษ : ")
        # c_type = input("กรุณากรอกประเภทหลักสูตร : ")
        # campus = input("กรุณากรอกวิทยาเขต : ")
        # expenses = input("กรุณากรอกค่าใช้จ่ายต่อภาคเรียน : ")
        # employment_rate = input("กรุณากรอกอัตราการได้งานทำ : ")
        # median_salary = input("กรุณากรอกค่ามัธยฐานเงินเดือน : ")
      

        #  ==================== True Use
        universityal =  "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ"
        faculty = "คณะเทคโนโลยีและการจัดการอุตสาหกรรม"
        program = "วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี"
        eng_program = "Bachelor of Science Program in Information Technology"
        c_type = "ภาษาไทย ปกติ"
        campus = "ปราจีนบุรี"
        expenses = "19,000"

        fin.writelines(("|".join((universityal,faculty,program,eng_program,c_type,campus,expenses)))+"\n")

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

def data_course_info(): # เก็บข้อมูลจากไฟล์
    data = []
    with open(r"data_information/course_info.txt","r",encoding="utf-8") as fout:
        for i in fout: 
            data.append(i.strip("\n").split("|"))
    return(sorted(data))