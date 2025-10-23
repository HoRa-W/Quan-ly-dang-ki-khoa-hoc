import mysql.connector
from mysql.connector import errorcode

config = {
    'user' : 'root',
    'password': '123456789',
    'host': 'localhost'
}

#Ý tưởng tại đây chính là sử dụng với 1 Query nhưng có thể truy xuất ra 
#dữ liệu tiện hơn và gọn hơn so với việc tạo ra Students_Query,...
#Tại đây có các thuộc tính của từng biến
#Có thể áp dụng cho các function khác
attribute_Students = ["MSSV", "Hovaten", "Email", "Phone_no", "Address"]
attribute_Courses = ["Course_ID", "Course_Name", "Description", "Credit"]
attribute_Enroll = ["Regis_ID", "MSSV", "Course_Name", "Regis_date"]

#Plan
"""
Khi hoan thanh cac chuc nhu insert ta can build 1 cai goc tuc
khi insert chi can truyen tham so vao con lai ham ben nay tu dong cap nhat

Vì database là nơi lữu trữ chính nên ta chỉ cần phương thức để truy cập
"""

#Kiem tra connect voi MySQL
try:
    # conn: connection
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connect MySQL Server successfully")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Connect error, please check user and password again")
    else:
        print(err)



#Tạo một database và kiểm tra đã tồn tại hay chưa
def dataBase_conn(input):

    try:
        cursor.execute(f"CREATE DATABASE {input}")

    except mysql.connector.Error as err:
        if (err.errno == errorcode.ER_DB_CREATE_EXISTS) :
            print("Database already created")
        else:
            print(err)


dataBase_conn("Course_Registration")

#Ket noi su dung database Course_Registration
def checkConn():

    try:
        conn.database = config['database']
        print("Connect DB successfully")

    except mysql.connector.Error as err:
        print("Cannot connect DB")
        print(err)


def checkTable(input):

    try:
        cursor.execute(input)
        print(f"Create table successfully")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("The table is existing")
        else:
            print(err)


def InsertData(input):

    # In this input will be InsertBook1 ()
    """
    InsertBook1 = ("INSERT INTO Books"
               "(title, author, published_date) "
               "VALUES ('Programming Python', 'Raymond', '2023-01-01')"
               )
    """

    try:
        cursor.execute(input)
        conn.commit()
        print("Insert data successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback() #Đưa database về lại trạng thái trước khi thực thi lệnh


def InsertDatas(input1, input2):

    #Obligated that input1 must be an string, input2 is list
    #In this input1 is sql_add_book () and input2 is book_data [()]
    """
    sql_add_book = ("INSERT INTO Books "
                  "(title, author, published_date) "
                   "VALUES (%s, %s, %s)")
    book_data = [
        ('Learning Python', 'Mark Lutz', '2019-06-10'),
        ('Python Crash Course', 'Eric Matthes', '2022-05-12'),
        ('Effective Modern C++', 'Scott Meyers', '2023-12-24'),
        ('The C++ Programming Language', 'Bjarne Strourstrup', '2016-05-20')
    ]
    """
    if (isinstance(input1, str)):
        return f"{input1} Khong phai la string"
    elif (isinstance(input2, list)):
        return f"{input2} Khong phai la list"
    else:
        try:
            cursor.executemany(input1, input2)
            conn.commit()
            print("Insert records successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            conn.rollback #Đưa database về lại trạng thái trước khi thực thi lệnh


def checkUpdate(input1, input2):

    try:
        cursor.execute(input1, input2)
        conn.commit()
        print("Update data successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback() #Đưa database về lại trạng thái trước khi thực thi lệnh


def Query(input):

    #In here input will be select_query
    """
    select_query = "SELECT * FROM Books"

    #Excute Select
    try:
        cursor.execute(select_query)
        results = cursor.fetchall()
        for row in results:
            print(f"ID: {row[0]}, Author: {row[1]}, Title: {row[2]}, Published date: {row[3]}")
    
    Catch error if it happen
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    """

    #Tại đây là phân lọc ra những trường hợp 
    if "Students" in input: test = attribute_Students
    if "Courses" in input: test = attribute_Courses
    if "Enroll" in input: test = attribute_Enroll

    #Bắt đầu chạy code query kiểm và xuất ra
    try:
        cursor.execute(input)
        results = cursor.fetchall()
        if (test == attribute_Students):
            for row in results:
                print(f"{test[0]}: {row[0]}, {test[1]}: {row[1]}, {test[2]}: {row[2]}\
                        {test[3]}: {row[3]}, {test[4]}: {row[4]}.")
        else:
            for row in results:
                print(f"{test[0]}: {row[0]}, {test[1]}: {row[1]}, {test[2]}: {row[2]}\
                        {test[3]}: {row[3]}.")
                
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def Delete_Data():

    pass


def Turnoff():
    cursor.close()
    conn.close()

def Data_Important():
    #------------------------Information--------------------------
    config['database'] = 'Course_Registration'
    checkConn()

    sql_Students = (
        "CREATE TABLE Students ("
        " MSSV VARCHAR(255) primary key,"
        " Hovaten VARCHAR(255),"
        " Email VARCHAR(255),"
        " Phone_no VARCHAR(10),"
        " Address VARCHAR(255)"
        ");"
    )

    checkTable(sql_Students)

    #-----------------------------------------------------------------

    config['database'] = 'Course_Registration'
    checkConn()

    sql_Courses = (
        "CREATE TABLE Courses ("
        " Course_ID VARCHAR(10) PRIMARY KEY," 
        " Course_Name VARCHAR(255)," 
        " Description VARCHAR(255),"
        " Credit INT" 
        ");"
    )

    checkTable(sql_Courses)

    #-----------------------------------------------------------------

    config['database'] = 'Course_Registration'
    checkConn()

    sql_Enroll = (
        "CREATE TABLE Enroll(" 
        " Regis_ID INT," 
        " MSSV VARCHAR(255)," 
        " Course_Name VARCHAR(255)," 
        " Regis_date DATE" 
        ")"
    )
    checkTable(sql_Enroll)

if __name__ == "__main__":
    Turnoff()