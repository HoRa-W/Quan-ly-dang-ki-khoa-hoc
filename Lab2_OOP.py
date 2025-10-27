from DBLab21 import *
from Insert_Func import *
from Select_Query import *
from update_DB import *
from Delete_DB import *
import os
import time
"""
Xây dựng 1 cái menu gồm có nhưng chức năng như
+ Thêm (Insert)
+ Xóa (drop || delete)
+ Sửa (Update)
+ Tìm kiếm (Query)

Cần áp dụng 1 tính năng có chức năng nhập dữ liệu không cần phải\
create table hay insert into...
"""

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("Dang nhap vao database")
    user_in = input("Ten tai khoan: ")
    password_in = input("Mat khau: ")
    db = Database(user_in, password_in)
    test = db.Secure()
    if test != 0:
        print("WELCOME")
        db.Connect()
        db.checkConn()
        db.Data_Important()
        time.sleep(2)
    else:
        print("Nhap sai roi")
        return 0

    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ ĐĂNG KÝ KHÓA HỌC ===")
        print("1. Thêm sinh viên")
        print("2. Sửa thông tin sinh viên")
        print("3. Tìm kiếm sinh viên")
        print("4. Hiển thị danh sách sinh viên")
        print("5. Thêm khóa học")
        print("6. Sửa thông tin khóa học")
        print("7. Tìm kiếm khóa học")
        print("8. Hiển thị khóa học")
        print("9. Đăng ký khóa học")
        print("10. Tìm kiếm thông tin đăng ký theo MSSV và khóa học")
        print("11. Xoa bo thong tin")
        print("12. Thoát")

        choice = input("Chọn chức năng: ")
		# SV thêm code chạy được các chức năng của chương trình
        if choice == "1":
            #Them sinh vien
            num = int(input("Ban muon them bao nhieu sinh vien: "))
            if num == 1:
                db.InsertData(Insert_Temple5("Students"))
            elif num > 1:
                x, y = Inserts_Temple_5("Students", num)
                db.InsertDatas(x, y)
            else:
                print("Nhap lai")

        elif choice == "2":
            # Sua thong tin sinh vien (Update)
            db.Update_Data(update("Students"))

        elif choice == "3":
            #Tim kiem sinh vien
            db.Query(Select("Students"))

        elif choice == "4":
           #Hien thi danh sach sinh vien
           db.Query(Select_All("Students"))
		
		# tương tự như phần sinh viên ở trên
        elif choice == "5":
            #Them khoa hoc
            num = int(input("Ban muon them bao nhieu khoa hoc: "))
            if num == 1:
                db.InsertData(Insert_Temple4("Courses"))
            elif num > 1:
                x, y = Inserts_Temple_4("Courses", num)
                db.InsertDatas(x, y)
            else:
                print("Nhap lai")

        elif choice == "6":
            #Sua thong tin khoa hoc
            db.Update_Data(update("Courses"))

        elif choice == "7":
            #Tim kiem khoa hoc
            db.Query(Select("Courses"))

        elif choice == "8":
            #Hien thi khoa hoc
            db.Query(Select_All("Courses"))

        elif choice == "9":
            #Dang ki khoa hoc
            db.InsertData(Insert_Temple4("Enroll"))

        elif choice == "10":
            #Tìm kiếm thông tin đăng ký theo MSSV và khóa học
            db.Query(Select_LotsCondition("Enroll"))
            
        elif choice == "11":
            print("Ban muon xoa bo thong tin thuoc tinh gi: ")
            delete = input()
            db.Delete_Data(Delete_in4(delete))

        elif choice == "12":
            print("Thoát chương trình.")
            db.Turnoff()
            break
        else:
            print("Input Wrong")

if __name__ == "__main__":
    main()

    