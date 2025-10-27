attribute_Students = ["MSSV", "Hovaten", "Email", "Phone_no", "Address"]
attribute_Courses = ["Course_ID", "Course_Name", "Description", "Credit"]
attribute_Enroll = ["Regis_ID", "MSSV", "Course_Name", "Regis_date"]

def Inserts_Temple_5(text1, num):

    n = num
    out2 = []
    for i in range(n):
        out2.append(tuple((input(f"Nhap thong tin co cach dau phay cho {text1}: ").split(', '))))

    test = attribute_Students

    out1 = (f"INSERT INTO {text1} "
        f"({test[0]}, {test[1]}, {test[2]}, {test[3]}, {test[4]}) "
        "VALUES "
    )
    
    return out1, out2

x, y = Inserts_Temple_5("Students", 5)

print(tuple(y))