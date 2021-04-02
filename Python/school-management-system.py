import csv

def write_csv(list):
    with open('data.csv', 'a', newline = '') as csv_file:
        write = csv.writer(csv_file)

        if (csv_file.tell() == 0):
            write.writerow(["Name", "Age", "Contact No.", "Email ID"])

        write.writerow(list)

if __name__ == "__main__":

    condition = True
    st_num = 1

    print("")
    print("------------------------------------- WELCOME TO SCHOOL MANAGEMENT SYSTEM -------------------------------------")
    print("")
    while (condition == 1):
        st_info = input("Enter student information for student #{} in following format - (Name Age Contact No. Email ID): ".format(st_num))
        st_info_list = st_info.split(' ')

        print("\nThe entered information -->\nName: {}\nAge: {}\nContact No.: {}\nEmal ID: {}".format(st_info_list[0], st_info_list[1], st_info_list[2], st_info_list[3]))
        print("")
        choice = input("Is the entered information correct (yes/no) : ")

        if (choice == "yes"):
            write_csv(st_info_list)

            condition_check = input("Want to continue adding another student's information (yes/no) : ")
            print("")
            if (condition_check == "yes"):
                condition = True
                st_num += 1
            elif (condition_check == "no"):
                condition = False
        elif (choice == "no"):
            print("\nPlease continue adding another student's information.")
            print("")
