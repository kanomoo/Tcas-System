from data_information.course_info import *
from data_information.student import *

def main(): # report main menu
    print()
    head = f"|{"TCAS System":^25}|"
    line = f"+{"=" * (len(head) - 2)}+"
    choice = input(f"{line}\n{head}\n{line}\n|{"1. Student Register":25}|\n|{"2. Course information":25}|\n|{"2. Exit Program":25}|\n{line}\nSelect option : ")
    match choice:
        case "1":
            student_register()
        case "2":
            course_info()
        case "3":
            exit()

if __name__ == "__main__":
    main()