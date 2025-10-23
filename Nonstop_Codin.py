attribute_Students = ["MSSV", "Hovaten", "Email", "Phone_no", "Address"]
attribute_Courses = ["Course_ID", "Course_Name", "Description", "Credit"]
attribute_Enroll = ["Regis_ID", "MSSV", "Course_Name", "Regis_date"]

def Inserts_Temple_4(text1):
    n = int(input("Nhap so luong doi tuong muon nhap: "))
    x = []
    for i in range(n):
        x.append(tuple((input(f"Nhap thong tin co cach dau phay cho {text1}: ").split(', '))))

    if "Courses" in text1: test = attribute_Courses
    if "Enroll" in text1: test = attribute_Enroll

    out1 = (f"INSERT INTO {text1}"
        f"({test[0]}, {test[1]}, {test[2]}, {test[3]}) "
        "VALUES (%s, %s, %s, %s)"
    )
    out2 = x

    return out1, out2

x, y = Inserts_Temple_4("Courses")
print(x)
print(y)
