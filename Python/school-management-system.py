import csv

def write_csv(list):
    with open('data.csv', 'a', newline = '') as csv_file:
        write = csv.writer(csv_file)

        if (csv_file.tell() == 0):
            write.writerow(["Name", "Age", "Contact No.", "Email ID"])

        write.writerow(list)
