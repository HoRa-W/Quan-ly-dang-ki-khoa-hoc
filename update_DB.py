"""
Giải thích sơ bộ cấu trúc của UPDATE

UPDATE Customers -> Thay đổi thuộc tính
SET ContactName = 'Alfred Schmidt', City = 'Frankfurt' -> Các phân bên trong thuộc tính đó sẽ thay đổi thành gì
WHERE CustomerID = 1; -> điều kiện khi thay đổi

UPDATE Customers & SET ContactName = 'Alfred Schmidt', City= 'Frankfurt' & WHERE CustomerID = 1;

=> Cần 1 mảng có thể phân loại ra cần sửa bao nhiêu cái và sửa cái nào trong thuộc tính đó
"""

attribute_Students = ["MSSV", "Hovaten", "Email", "Phone_no", "Address"]
attribute_Courses = ["Course_ID", "Course_Name", "Description", "Credit"]
attribute_Enroll = ["Regis_ID", "MSSV", "Course_Name", "Regis_date"]

def update(text1): #Thuoc tinh can update

    if "Courses" in text1: test = attribute_Courses
    if "Enroll" in text1: test = attribute_Enroll
    if "Students" in text1: test = attribute_Students

    #Build structure
    Attri_Change = []
    Change_Into = []
    num_change = int(input("Nhap so luong phan tu can thay doi: "))
    for i in range(num_change):
        for j in range(len(test)):
            print(test[j], sep = ' - ')
        Attri_Change.append(input("SET: "))
        Change_Into.append(input(" -> "))

    result = ", ".join([f"{Attri_Change[i]} = '{Change_Into[i]}'" for i in range(num_change)])

    in_where = input(f"WHERE {test[0]} = ")

    out = f"UPDATE {text1} "\
          f"SET {result} "\
          f"WHERE {test[0]} = {in_where};"
    
    return out
