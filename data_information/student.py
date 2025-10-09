def student_login():
    with open(r"data_information/student.txt","w",encoding = "utf-8") as fin:
        # iden_code = input("Enter Identification code : ")
        # n_s = input("Enter Name-Surname : ")
        
        iden_code = "1199901140886"
        n_s = "นายปภาวิน ธิติชุณหกุล"
        fin.writelines("|".join((iden_code,n_s))+"\n")

student_login()