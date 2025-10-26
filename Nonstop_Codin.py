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


def Insert_Temple5(text1):
    test = attribute_Students

    x = []
    for i in range(5):
        x.append(input(f"Nhap thong tin {test[i]}: "))

    out1 = (
        f"INSERT INTO {text1} "
        f"({test[0]}, {test[1]}, {test[2]}, {test[3]}, {test[4]}) "
        f"VALUES ('{x[0]}', '{x[1]}', '{x[2]}', '{x[3]}', '{x[4]}');"
    )

    return out1

print(Insert_Temple5("Students"))