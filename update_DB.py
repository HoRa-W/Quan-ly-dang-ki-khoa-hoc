"""
Giải thích sơ bộ cấu trúc của UPDATE

UPDATE Customers -> Thay đổi thuộc tính
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt' -> Các phân bên trong thuộc tính đó sẽ thay đổi thành gì
WHERE CustomerID = 1; -> điều kiện khi thay đổi

UPDATE Customers & SET ContactName = 'Alfred Schmidt', City= 'Frankfurt' & WHERE CustomerID = 1;

=> Cần 1 mảng có thể phân loại ra cần sửa bao nhiêu cái và sửa cái nào trong thuộc tính đó
"""

attribute_Students = ["MSSV", "Hovaten", "Email", "Phone_no", "Address"]
attribute_Courses = ["Course_ID", "Course_Name", "Description", "Credit"]
attribute_Enroll = ["Regis_ID", "MSSV", "Course_Name", "Regis_date"]

def update(text1): #Thuoc tinh can update
    #Build structure
    Change = []
    num_change = input("Nhap so luong phan tu can thay doi: ")
    out = f"UPDATE {text1}"\
          f"SET "\
          f"WHERE "

