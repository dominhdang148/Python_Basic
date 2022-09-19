from tkinter import Tk, BOTH, IntVar, LEFT
from tkinter.ttk import Frame, Label, Scale, Style


class Example(Frame):
    def __init__(self, parent: Tk):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Scale")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)


        # Tạo một đối tượng Scale
        # Hai tham số from_ và to là phạm vi giá trị của scale.
        # Tham số command chỉ định phương thức sẽ được gọi khi di chuyển thanh cuộn
        scale = Scale(self, from_=0, to=100, command=self.onScale)
        scale.pack(side=LEFT, padx=15)


        # region Tạo label, một đối tượng IntVar và kết nối đối tượng đó với Label bằng tham số textvariable.
        # Giá trị của biến này sẽ được hiển thị trên label
        self.var = IntVar()
        self.label = Label(self, text=0, textvariable=self.var)
        # endregion
        self.label.pack(side=LEFT)

        # Khi di chuyển thanh cuộn, phương thức onScale() sẽ được gọi kèm theo giá trị hiện tại của Scale.
        # Thực hiện chuyển đổi kiểu dữ liệu của tham số này sang float rồi sang int sau đó đặt giá trị của đối tượng IntVar và đoạn text hiển thị trên label sẽ thay đổi theo.
    def onScale(self, val):
        v = int(float(val))
        self.var.set(v)


root = Tk()
ex=Example(root)
root.geometry("250x100+300+300")
root.mainloop()