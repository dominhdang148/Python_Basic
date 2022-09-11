from tkinter import Tk, Label, BOTH
from tkinter.ttk import Frame, Style

# Để hiển thị ảnh, có thể dùng module PhotoImage trong package Tkinter
# Tuy nhiên, module này không phổ biến, Module Image và ImageTK trong thư viện Pillow phổ biến hơn.
from PIL import Image, ImageTk


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        # Tô màu nền cửa sổ là màu xám đen (HEX=#333333)
        Style().configure("TFrame", background="#333")

        # region Tạo các đối tượng ảnh vào tải chúng vào chương trình
        bard = Image.open("cute.jpg")
        bard = bard.resize((100, 100), Image.Resampling.LANCZOS)
        # endregion

        cute = ImageTk.PhotoImage(bard)

        # Tạo đối tượng Label, dùng để hiển thị chữ và ảnh
        label1 = Label(self, image=cute)

        # Phải lưu lại tham chiếu trên ảnh, nếu không sẽ bị xóa
        label1.image = cute

        # Đặt ảnh tại vị trí x=20 và y=20
        label1.place(x=20, y=20)

        rot = Image.open("depress.jpg")
        rot = rot.resize((100, 100), Image.Resampling.LANCZOS)
        depress = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=depress)
        label2.image = depress
        label2.place(x=40, y=160)

        minc = Image.open("sad.jpg")
        minc = minc.resize((100, 100), Image.Resampling.LANCZOS)
        sad = ImageTk.PhotoImage(minc)
        label3 = Label(self, image=sad)
        label3.image = sad
        label3.place(x=170, y=50)


root = Tk()
root.geometry("300x280+300+300")
app = Example(root)
root.mainloop()
