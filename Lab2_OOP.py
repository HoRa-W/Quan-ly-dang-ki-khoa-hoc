import DBLab21
import datetime

"""
Xây dựng 1 cái menu gồm có nhưng chức năng như
+ Thêm (Insert)
+ Xóa (drop || delete)
+ Sửa (Update)
+ Tìm kiếm (Query)

Cần áp dụng 1 tính năng có chức năng nhập dữ liệu không cần phải\
create table hay insert into...
"""

class menu:
    def __init__(self, user, password, host):
        self__user = user
        self__password = password
        self__host = host
    
    