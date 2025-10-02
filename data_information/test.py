def input_data():
    head, result = "| System Tcas |", ""
    line = "=" * len(head)
    
    #ต้องสร้าง def data
    while True:
        choice = input(f"{line}\n{head}\n{line}\n1. Input School Name\n2. Output Data\nEnter choice : ")
        if choice == "1": 
            with open(r"Tcas/data_information/test.txt","r",encoding="utf-8") as fin: 
                data = []
                for i in fin.readlines():
                    data.append(i.strip("\n"))
                    # data.append(i.strip("\n").split("\n"))
                for n in range(len(data)):
                    data = (sorted(data))
                    print(f"{n+1} {data[n]}")
            school = input("Please input school name : ")
            if school.isdigit: school = data[int(school)-1]
            if school not in data: 
                with open(r"Tcas/data_information/test.txt","a",encoding="utf-8") as fout: fout.write(school+"\n")
            else: print("school in data")
            print(school)
        elif choice == "2": 
            for n in range(len(data)): 
                print(f"{n+1} {data[n]}")

def main():
    input_data()

if __name__ == "__main__":
    main()
