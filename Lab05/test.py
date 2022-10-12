from mysql.connector import MySQLConnection, Error


def connect():
    db_config = {
        'host': 'localhost',
        'database': 'QLSinhVien',
        'user': 'root',
        'password': 'DoMinhDang2002'
    }

    conn = None
    try:
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            return conn
    except Error as error:
        print(error)
    return conn


def close(conn):
    if conn:
        conn.close()


def insert_class(tenLop):
    try:
        connection = connect()
        cursor = connection.cursor()

        query = f"insert into Lop(TenLop) values ('{tenLop}');"

        cursor.execute(query)

        connection.commit()
        print('Đã thêm thành công')
        close(connection)
    except Error as error:
        print(error)


def get_all_class():
    try:
        connection = connect()
        cursor = connection.cursor()

        select_query = "select * from Lop"
        cursor.execute(select_query)
        records = cursor.fetchall()

        print("Danh sách các lớp là:")
        for row in records:
            print("*"*50)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])

        close(connection)
    except Error as error:
        print("Đã có lỗi xảy ra khi thực thi! Thông tin lỗi:", error)

insert_class('CTK46')
get_all_class()
