from wcwidth import wcswidth
from course_info import add_title
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


# def add_course_info():
    # with open(r"data_information/course_info.txt","w",encoding="utf-8") as fin:
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
#         universityal =  "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ"
#         faculty = "คณะเทคโนโลยีและการจัดการอุตสาหกรรม"
#         program = "วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี"
#         eng_program = "Bachelor of Science Program in Information Technology"
#         c_type = "ภาษาไทย ปกติ"
#         campus = "ปราจีนบุรี"
#         expenses = "19,000"

#         fin.writelines(("|".join((universityal,faculty,program,eng_program,c_type,campus,expenses)))+"\n")

#         # ==========================

#         data_universities = [
#             ["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ", "คณะเทคโนโลยีและการจัดการอุตสาหกรรม", "วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี", "ภาษาไทย ปกติ", "ปราจีนบุรี", "19,000", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.00", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.75", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
#             ["มหาวิทยาลัยธรรมศาสตร์", "คณะวิทยาศาสตร์และเทคโนโลยี", "วท.บ.วิทยาการคอมพิวเตอร์", "ภาษาไทย ปกติ", "รังสิต", "20,000", "Portfolio", "Accepted", "Accepted", "Declined", "Declined", "Declined", "2.50", "Quota", "Accepted", "Accepted", "Declined", "Declined", "Declined", "2.75", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
#             ["จุฬาลงกรณ์มหาวิทยาลัย", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "ปทุมวัน", "22,000", "Portfolio", "Accepted", "Accepted", "Declined", "Declined", "Declined", "2.50", "Quota", "Accepted", "Accepted", "Declined", "Declined", "Declined", "2.75", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
#             ["มหาวิทยาลัยเกษตรศาสตร์", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ วิทยาเขตบางเขน", "ภาษาไทย ปกติ", "บางเขน", "18,500", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.25", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.75", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
#             ["มหาวิทยาลัยสงขลานครินทร์", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "หาดใหญ่", "17,500", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.25", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.70", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
#             ["มหาวิทยาลัยขอนแก่น", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "เมืองขอนแก่น", "16,800", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.00", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.50", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
#             ["มหาวิทยาลัยเชียงใหม่", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "เมืองเชียงใหม่", "18,900", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.30", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.70", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
#             ["มหาวิทยาลัยมหิดล", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "พญาไท", "21,800", "Portfolio", "Accepted", "Accepted", "Declined", "Declined", "Declined", "2.50", "Quota", "Accepted", "Accepted", "Declined", "Declined", "Declined", "2.75", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
#             ["มหาวิทยาลัยศรีนครินทรวิโรฒ", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "ประสานมิตร", "19,300", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.00", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.50", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
#             ["มหาวิทยาลัยนเรศวร", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "เมืองพิษณุโลก", "15,900", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.00", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.50", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
#             ["มหาวิทยาลัยบูรพา", "คณะวิทยาศาสตร์", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "เมืองชลบุรี", "18,000", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.10", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.60", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"],
#             ["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี", "คณะเทคโนโลยีสารสนเทศ", "วท.บ.เทคโนโลยีสารสนเทศ", "ภาษาไทย ปกติ", "บางมด", "20,500", "Portfolio", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.00", "Quota", "Accepted", "Declined", "Declined", "Declined", "Declined", "2.75", "Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined", "Direct Admission", "Declined", "Declined", "Declined", "Declined", "Declined", "Declined"]
#             ]

#         for course in data_universities:
#             course = "|".join(course)
#             fin.write(course+"\n")

# def data_course_info(): # เก็บข้อมูลจากไฟล์
#     data = []
#     with open(r"data_information/course_info.txt","r",encoding="utf-8") as fout:
#         for i in fout: 
#             data.append(i.strip("\n").split("|"))
#     return(sorted(data))

# name = "าสว่ฟหกดา่ว่าสฟหกด"

# n = 0

# print(len(name))
# for i in name:
#     n += 1
# print(n)

# def pad_text(text, widht = 0):
#     result = ""
#     if len(text) != widht:
#         return text + " " * (widht - len(text))



# print(wcswidth(name))

# def pad_text(text, width = 0): # padding text เติมช่องว่าง ควรใช้เฉพาะภาษาไทย
#     text = str(text)
#     real_width = wcswidth(text)                         # คำนวณความกว้างจริงของข้อความในเทอมินอล (นับช่องว่างที่ข้อความใช้)
#     if width == 0:
#         return text 
#     elif real_width < width:                            # ถ้าความกว้างจริงของข้อความน้อยกว่าความกว้างที่ต้องการ
#         return text + " " * (width - real_width)        # เติมช่องว่างให้ครบตามความกว้างที่กำหนด เพื่อจัดข้อความให้อยู่ในตำแหน่ง len จริงๆ
#     return text   
# print(f"{"ปแอิ้ัราะีัๆไำๆ":58}|")
# print(f"{"ิแอือิืำพะไำพฟๆไพๆไะ":58}|")
# print(f"{"แอปิแไำะำไะไ-ำะๅ":58}|")
# print(f"{"าสว่ฟหกดา่ว่ำพภีะัพนุึคาสฟหกปแอือิด":58}|")



# ================================================== add couse
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
        

# ===================== check

    # # print (data_dic)
    # for i in data_dic["university"]["จุฬาลงกรณ์มหาวิทยาลัย"]:
    #     print(i)

    # print()

    # for i in data_dic["university"]["จุฬาลงกรณ์มหาวิทยาลัย"]["คณะวิทยาศาสตร์"]["วท.บ.เทคโนโลยีสารสนเทศ"]:
    #     print(i)

    # print()

    # print(data_dic["university"]["จุฬาลงกรณ์มหาวิทยาลัย"]["คณะวิทยาศาสตร์"]["วท.บ.เทคโนโลยีสารสนเทศ"]["Program Name in English"])

    # # print (data_dic["university"]["จุฬาลงกรณ์มหาวิทยาลัย"])


# ========================== add scourse infor

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


# =============================================== student_register
# data_list = [
    # ["1199901140886", "นายปภาวิน ธิติชุณหกุล", "few717254@gmail.com", "0806525546"],
    # ["1199901140999", "นางสาวสมหญิง ตัวอย่าง", "example@gmail.com", "0912345678"],
    # ["1199901140887", "นายสมชาย ใจดี", "somchai@example.com", "0801234567"],
    # ["1199901140888", "นางสาวสมศรี ขยัน", "somsri@example.com", "0812345678"],
    # ["1199901140889", "นายดำรงค์ ศรีสุข", "damrong@example.com", "0823456789"],
    # ["1199901140890", "นางสาวสุนิสา ยิ้มแย้ม", "sunisa@example.com", "0898765432"],
    # ["1199901140891", "นายปรเมศวร์ ดีใจ", "promet@example.com", "0865432198"],
    # ["1199901140892", "นางสาวมุกดา สวยสดงดงาม", "mukda@example.com", "0843219876"],
    # ["1199901140893", "นายสหัส ว่องไว", "sahat@example.com", "0832198765"],
    # ["1199901140894", "นางสาวกิตติมา มีน้ำใจ", "kittima@example.com", "0821987654"]
    # ]
    
# for i in data_list:
#     fin.write("|".join(i)+"\n")

# iden_code = "1199901140886"
# name = "นายปภาวิน ธิติชุณหกุล"
# email = "few717254@gmail.com"
# phone = "0806525546"


# print(f"Enter Identification code : {iden_code}")
# print("Enter Emaill : ")
# print("Enter Phone Number : ")
# print(f"Enter Name-Surname : {name}")

# ============================================ old code course_info

# def report_course_info(): # report 
#     while True:
#         print()
#         head = f"|{"Report Course Infomation":^30}|"
#         line = f"{"-" * len(head)}"
#         choice = input(f"{line}\n{head}\n{line}\n|{"1. All Course Information":{len(head)-2}}|\n|{"2. Setting Course Information":{len(head)-2}}|\n|{"3. Back to main":{len(head)-2}}|\n{line}\nSelect option : ")
#         match choice:
#             case "1":
#                 all_course_info()
#             case "2": 
#                 setting_course_info()
#             case "3":
#                 course_info()
#             case "4":
#                 break
#         break



# def setting_course_info():
#     univ, id1 = search_university()
#     fac, id2 = search_faculty(id1,univ)
#     program, id3 = search_program(id2,univ,fac)
#     search_title(id3,univ,fac,program)
# 
# def search_university():
#     while True:
#         # ใช้ data ที่ เป็น dic
#         print()
#         data = data_dic_info()
#         result = ""
#         head = f"|{'Search Course Information':^98}|"
#         line = "-" * len(head)
#         result += f"{line}\n{head}\n{line}\n"
#         check_id = []
#         # ค้นหาข้อมูลผ่าน data dic ต้องใช้ items ช่วย ที่ใช้คือ value
#         for key,university in data.items():
#             n = 0
#             search_univ = {}
#             for key_univ,faculty in university.items():
#                 n += 1
#                 # แปลงเป็น string เติม 0 ด้านหน้า id จะกรอกง่าย
#                 col_key_univ = pad_text(key_univ,len(head)-9)
#                 # ทำให้เป็นค่าความกว้างจริง
#                 search_univ[f"{n:0>2}"] = key_univ
#                 # สร้าง key id และ value ชื่อ
#                 result += (f"| {n:0>2} | {col_key_univ} |\n")
#                 check_id.append(f"{n:0>2}")
#             result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
#             result += line
#         print(result)
#         choice = input("selcet number data or name new data : ")
#         id = ""
#         id += choice if choice != "00" and choice in check_id else ""
#         if choice in search_univ and choice != "00": return(search_univ[choice]) ,id 
#         elif choice == "00": report_course_info()
#         else: print("Invalid input Please try again")

# def search_faculty(id,univ):
#     while True:
#         print()
#         data = data_dic_info()
#         result = ""
#         head = f"|{'Faculty':^98}|"
#         line = "-" * len(head)
#         result += f"{line}\n{head}\n{line}\n"
#         check_id = []
#         for key,university in data.items():
#             n = 0
#             search_fac = {}
#             col_univ = pad_text(univ,68)
#             result += (f"| {"University":25} | {col_univ} |\n{line}\n")

#             for key_fac, faculty in university[univ].items():
#                 n += 1
#                 col_key_fac = pad_text(key_fac,len(head)-9)
#                 search_fac[f"{n:0>2}"] = key_fac
#                 # สร้าง key ตาม number format n_f จะเป็น key automatic
#                 result += (f"| {n:0>2} | {col_key_fac} |\n")
#                 check_id.append(f"{n:0>2}")
#             result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
#             result += line
#         print(result)        
#         choice = input("selcet number data or name new data : ")
#         id += choice if choice != "00" and choice in check_id else ""
#         if choice in search_fac and choice != "00": return(search_fac[choice]) ,id
#         elif choice == "00": search_university()
#         else: print("Invalid input Please try again")
#         print()

# def search_program(id,univ,fac):
#     while True:
#         print()
#         data = data_dic_info()
#         result = ""
#         head = f"|{'Couse_Name':^98}|"
#         line = "-" * len(head)
#         result += f"{line}\n{head}\n{line}\n"
#         check_id = []
#         for key,university in data.items():
#             n = 0
#             col_univ = pad_text(univ,68)
#             col_fac = pad_text(fac,68)

#             result += (f"| {"University":25} | {col_univ} |\n")
#             result += (f"| {"Faculty":25} | {col_fac} |\n{line}\n")

#             search_program = {}
#             for key_program, program in university[univ][fac].items():
#                 n += 1
#                 col_key_program = pad_text(key_program,len(head)-9)
#                 search_program[f"{n:0>2}"] = key_program
#                 # สร้าง key ตาม number format n_f จะเป็น key automatic
#                 result += (f"| {n:0>2} | {col_key_program} |\n")
#                 check_id.append(f"{n:0>2}")
#             result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
#             result += line
#         print(result)        
#         choice = input("selcet number data or name new data : ")
#         id += choice if choice != "00" and choice in check_id else ""
#         if choice in search_program and choice != "00": return(search_program[choice]) , id
#         elif choice == "00": search_faculty(id,univ)
#         else: print("Invalid input Please try again")

#         print()
    
# def search_title(id,univ = "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ",fac = "คณะเทคโนโลยีและการจัดการอุตสาหกรรม",program = "วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี"):
#     print()
#     data = data_dic_info()
#     result = ""
#     head = f"|{'Couse_Information':^98}|"
#     line = "-" * len(head)
#     result += f"{line}\n{head}\n{line}\n"

#     for key,university in data.items():

#         col_univ = pad_text(univ,68)
#         col_fac = pad_text(fac,68)
#         col_program = pad_text(program,68)

#         result += (f"| {"University":25} | {col_univ} |\n")
#         result += (f"| {"Faculty":25} | {col_fac} |\n")
#         result += (f"| {"Program":25} | {col_program} |\n")

#         for key_title, title in university[univ][fac][program].items():
#             data_title = []
#             col_title = pad_text(title,68)
#             result += (f"| {key_title:25} | {col_title} |\n")
#             data_title.append(col_title)
    

#     print(result+line)        
#     choice = input(f"1. Change data\n2. Delect data\nselect : ")
    
# test data
# def test_data():
#     data = data_course_info()
#     data_dic = {"university": {}}
#     for course in data:
#         university = course[0]
#         faculty = course[1]
#         program = course[2]

#         catg_program = course[3]
#         campus = course[4]
#         expenses  = course[5]
        
#         if university not in data_dic["university"]:
#             data_dic["university"][university] = {}
#         if faculty not in data_dic["university"][university]:
#             data_dic["university"][university][faculty] = {}
#         if program not in data_dic["university"][university][faculty]:
#             data_dic["university"][university][faculty][program] = {}

#         data_dic["university"][university][faculty][program] = {
#             "Category of Program": catg_program,
#             "Campus": campus,
#             "Expenses": expenses,
#         }

#     data_dic["university"]["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ"] = {}
#     data_dic["university"]["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ"]["คณะเทคโนโลยีและการจัดการอุตสาหกรรม"] = {}
#     data_dic["university"]["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ"]["คณะเทคโนโลยีและการจัดการอุตสาหกรรม"]["วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี"] = {}


#     data_dic["university"]["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ"]["คณะเทคโนโลยีและการจัดการอุตสาหกรรม"]["วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี"] = {
#             "Category of Program": "test",
#             "Campus": "test",
#             "Expenses": "test",
#         }
    
#     return data_dic




# ================
# select = input(f"\n{"-" * 22}\n|{"1. Edit":20}|\n|{"2. Delete":20}|\n|{"3. Go Back":20}|\n{"-" * 22}\nselect : ")

# choice = input(f"1. Edit data\n2. Save data\n3. Deleate data\n4. Go Back\nselect : ")
# match choice:
#     case "1":
#         data, univ, fac, program, catg , campus , expenses  = edit_add_data(search_univ[choice], univ, fac, program, catg , campus , expenses) 
#         print("Data Edit")
#     case "2":
#         save_data(data)
#         print("Data Save")
#     case "3":
#         confirm = input("Confirm Information (y/n) : ").lower()
#         match confirm:
#             case "y":
#                 del data["university"][univ]
#                 del_data(data)
#                 return True
#             case "n":
#                 pass
#             case _:
#                 print("Invalid input Please try again")
#         print("Data Delete")
#     case "4":
#         break
#     case _:
#         pass