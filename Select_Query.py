import DBLab21

attribute_Students = ["MSSV", "Hovaten", "Email", "Phone_no", "Address"]
attribute_Courses = ["Course_ID", "Course_Name", "Description", "Credit"]
attribute_Enroll = ["Regis_ID", "MSSV", "Course_Name", "Regis_date"]

"""
SELECT *
FROM Students
WHERE MSSV = '098';
"""

def Select(text1):

    #Select (...) from text1 
    #where (MSSV,...) = ?
    if "Courses" in text1: test = attribute_Courses
    if "Enroll" in text1: test = attribute_Enroll
    if "Students" in text1: test = attribute_Students

    for i in range(len(text1)):
        print(f"{test[i]}", sep = " - ")

    while(True):
        print(f"Ban muon tim kiem thong tin gi: ")
        find_in4 = input()
        if (find_in4 in text1):
            break
        else:
            print("Vui long nhap lai")

    Data_Find = input(f"Tim kiem thong tin gi cua {find_in4}: ")

    out1 = f"SELECT * FROM {text1}"\
           f"WHERE {find_in4} = {Data_Find}"
    
    return out1

def Select_All(text1):
    
    out1 = f"SELECT * FROM {text1}"
    return out1