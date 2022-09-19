from tkinter import Tk, Frame, Checkbutton
from tkinter import BooleanVar, BOTH


class Example(Frame):
    def __init__(self, parent: Tk):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("CheckButton")
        self.pack(fill=BOTH, expand=True)

        # Tạo một đối tượng BoolearnVar kết nối với checkbutton, mỗi khi trạng thái check thay đổi thì giá trị var cũng sẽ thay đổi
        self.var = BooleanVar()

        # Tạo một đối tượng Checkbutton, kết nối biến var thông qua tham số variable. 
        # Tham số command chỉ định phương thức nào sẽ được gọi khi check. (Trong trường hợp này là phương thức onClick())
        cb = Checkbutton(self, text="Show Title",
                         variable=self.var, command=self.onClick)
        
        # Sử dụng phương thức select() để thiết lập trạng thái cho check cho button
        cb.select()
        cb.place(x=50, y=50)

    # region Cho hiện/ẩn tiêu đề cửa sổ thông qua phương thức master.title()
    # Kiểm tra check button có được check hay thông thông qua thuộc tính self.var
    def onClick(self):
        if self.var.get()==True:
            self.master.title("CheckButton")
        else:
            self.master.title("")
    # endregion

root=Tk()
root.geometry("250x150+300+300")
app=Example(root)
root.mainloop()