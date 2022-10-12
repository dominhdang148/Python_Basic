from tkinter import *
from openpyxl import *

wb = load_workbook('data.xlsx')
sheet = wb.active

if __name__ == '__main__':
    root = Tk()
    root.title("Đăng ký học phần")
    root.configure(background="light green")
    root.geometry("1000x600")

    # region Frame
    headingFrame=Frame(root)
    id_Frame=Frame(root)
    # endregion
    # region Label
    heading = Label(headingFrame, text='THÔNG TIN ĐĂNG KÝ HỌC PHẦN',
                    bg='light green', fg='red',font='Nunito 20')
    student_ID = Label(root, text='Mã số sinh viên', bg='light green')
    dateOfBirth = Label(root, text='Ngày sinh', bg='light green')
    email = Label(root, text='Email', bg='light green')
    phoneNumb = Label(root, text='Số Điện Thoại', bg='light green')
    sem = Label(root, text='Học kỳ', bg='light green')
    year = Label(root, text='Năm học', bg='light green')
    subjects = Label(root, text='Chọn môn học', bg='light green')
    # endregion

    # region Packing
    heading.pack(side=LEFT)
    student_ID.pack(side=LEFT)
    dateOfBirth.pack(side=LEFT)
    email.pack(side=LEFT)
    phoneNumb.pack(side=LEFT)
    sem.pack(side=LEFT)
    year.pack(side=LEFT)
    subjects.pack(side=LEFT)
    # endregion
    root.mainloop()
