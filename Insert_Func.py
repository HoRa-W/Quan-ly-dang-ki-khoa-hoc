attribute_Students = ["MSSV", "Hovaten", "Email", "Phone_no", "Address"]
attribute_Courses = ["Course_ID", "Course_Name", "Description", "Credit"]
attribute_Enroll = ["Regis_ID", "MSSV", "Course_Name", "Regis_date"]

"""
InsertBook1 = ("INSERT INTO Books"
             "(title, author, published_date) "
             "VALUES ('Programming Python', 'Raymond', '2023-01-01')"
             )
"""
def Insert_Temple4(text1):

    if "Courses" in text1: test = attribute_Courses
    if "Enroll" in text1: test = attribute_Enroll

    x = []
    for i in range(4):
        x.append(input(f"Nhap thong tin {test[i]}: "))
    out1 = f"INSERT INTO {text1} "\
           f"({test[0]}, {test[1]}, {test[2]}, {test[3]}) "\
           f"VALUES (`{x[0]}`, `{x[1]}`, `{x[2]}`, `{x[3]}`)"

    return out1


def Insert_Temple5(text1):
    test = attribute_Students

    x = []
    for i in range(5):
        x.append(input(f"Nhap thong tin {test[i]}: "))

    out1 = (
        f"INSERT INTO {text1} "
        f"({test[0]}, {test[1]}, {test[2]}, {test[3]}, {test[4]}) "
        f"VALUES (`{x[0]}`, `{x[1]}`, `{x[2]}`, `{x[3]}`, `{x[4]}`);"
    )

    return out1


def Inserts_Temple_4(text1, num):

    if "Courses" in text1: test = attribute_Courses
    if "Enroll" in text1: test = attribute_Enroll
    n = num
    out2 = []
    for i in range(n):
        out2.append(tuple((input(f"Nhap thong tin co cach dau phay cho {text1}: ").split(', '))))

    out1 = (f"INSERT INTO {text1} "
        f"({test[0]}, {test[1]}, {test[2]}, {test[3]}) "
        "VALUES (%s, %s, %s, %s)"
    )

    return out1, out2


def Inserts_Temple_5(text1, num):

    n = num
    out2 = []
    for i in range(n):
        out2.append(tuple((input(f"Nhap thong tin co cach dau phay cho {text1}: ").split(', '))))

    test = attribute_Students

    out1 = (f"INSERT INTO {text1} "
        f"({test[0]}, {test[1]}, {test[2]}, {test[3]}, {test[4]}) "
        "VALUES (%s, %s, %s, %s, %s)"
    )

    return out1, out2


