import csv

# ---------------------- จัดการข้อมูลหลักสูตร ----------------------

def add_course(course_id, name, type, seats, fee):
    with open('courses.csv', 'a', newline='', encoding='utf-8') as file:
        w = csv.writer(file)
        w.writerow([course_id, name, type, seats, fee])

def list_courses():
    with open('courses.csv', encoding='utf-8') as file:
        r = csv.reader(file)
        print("CourseID, Name, Type, Seats, Fee")
        for row in r:
            print(', '.join(row))

# ---------------------- จัดการข้อมูลนักเรียน ----------------------

def add_student(student_id, id_number, name, birthdate, phone, email, address):
    with open('students.csv', 'a', newline='', encoding='utf-8') as file:
        w = csv.writer(file)
        w.writerow([student_id, id_number, name, birthdate, phone, email, address])

def list_students():
    with open('students.csv', encoding='utf-8') as file:
        r = csv.reader(file)
        print("StudentID, ID_Number, Name, Birthdate, Phone, Email, Address")
        for row in r:
            print(', '.join(row))

# ---------------------- สมัครสอบ ----------------------

def register_exam(reg_id, student_id, course_id, date, payment_status, receipt_no):
    with open('registrations.csv', 'a', newline='', encoding='utf-8') as file:
        w = csv.writer(file)
        w.writerow([reg_id, student_id, course_id, date, payment_status, receipt_no])

def list_registrations():
    with open('registrations.csv', encoding='utf-8') as file:
        r = csv.reader(file)
        print("RegID, StudentID, CourseID, Date, PaymentStatus, ReceiptNo")
        for row in r:
            print(', '.join(row))

# ---------------------- ตัวอย่างเมนู ----------------------

def main_menu():
    while True:
        print("\n1. เพิ่มหลักสูตร\n2. ดูหลักสูตร\n3. สมัครนักเรียนใหม่\n4. ดูนักเรียน\n5. สมัครสอบ\n6. ดูการสมัคร\n0. จบโปรแกรม")
        choice = input("เลือกเมนู: ")
        if choice == '1':
            add_course(input("Course ID: "), input("Name: "), input("Type: "), input("Seats: "), input("Fee: "))
        elif choice == '2':
            list_courses()
        elif choice == '3':
            add_student(input("Student ID: "), input("ID Number: "), input("Name: "), input("Birthday: "), input("Phone: "), input("Email: "), input("Address: "))
        elif choice == '4':
            list_students()
        elif choice == '5':
            register_exam(input("RegID: "), input("StudentID: "), input("CourseID: "), input("Date: "), input("Payment (Y/N): "), input("Receipt No: "))
        elif choice == '6':
            list_registrations()
        elif choice == '0':
            break
        else:
            print("เลือกเมนูผิด!")

if __name__ == "__main__":
    main_menu()
