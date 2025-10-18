from data_information.course_info import *
from data_information.student_tcas import *
from data_information.report_register import *

def main(): # report main menu
    while True:
        print()
        head = f"|{"TCAS System":^50}|"
        line = f"+{"=" * (len(head) - 2)}+"
        choice = input(f"{line}\n{head}\n{line}\n|{"1. Student Menu":50}|\n|{"2. Course information":50}|\n|{"3. TCAS Applicant and Fee Statistics Report":50}|\n|{"4. Exit Program":50}|\n{line}\nSelect option : ")
        match choice:
            case "1":
                student_menu()
            case "2":
                course_info()
            case "3":
                display_report() 
            case "4":
                exit()

if __name__ == "__main__":
    main()