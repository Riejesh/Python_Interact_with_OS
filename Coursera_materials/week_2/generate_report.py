"""A dialect is essentially a set of rules that describe the format of a CSV file. Different CSV files can use different delimiters (like commas, semicolons, or tabs), different quoting characters, or different ways of handling spaces. By defining a dialect, you tell the csv module how to correctly parse or write a CSV file that adheres to those specific rules."""
"""The primary advantage of csv.DictReader is that it reads each row as a dictionary, where the keys are taken from the header row of the CSV file. This makes accessing data by column name (e.g., employee_data['Department']) highly readable, intuitive, and less error-prone. You don't have to remember the numeric index of each column. """
#!/usr/bin/env python3
import csv
def read_employees(csv_file_location):
        csv.register_dialect('empDialect',skipinitialspace=True,strict=True)                
        employee_file = csv.DictReader(open(csv_file_location),dialect ='empDialect')        # strict=True -This parameter dictates how "bad" quoting is handled.
        employee_list = []
        for data in employee_file:
                employee_list.append(data)
        return employee_list

def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                #print (employee_data)
                department_list.append(employee_data['Department'])
        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(department_name)
        return department_data

def write_report(dictionary, report_file):
        with open(report_file, "w+") as f:            #It ensures that resources, like open files, are properly managed. Specifically, it guarantees that the file will be automatically closed after the block of code inside the with statement is executed, even if errors occur. 
                for k in sorted(dictionary):          #"w+" opens a file for both writing and reading. "r+" Read and Write mode, "a" Append mode
                        f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()                                 #  Python's context manager protocol (which with utilizes) handles the closing of the file. This is redundant.



employee_list = read_employees('/home/student-01-1add08146376/data/employees.csv')
#print(employee_list)
dictionary = process_data(employee_list)
#print(dictionary)
write_report(dictionary, '/home/student-01-1add08146376/test_report.txt')
