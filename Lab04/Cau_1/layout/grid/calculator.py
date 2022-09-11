from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style


class Example(Frame):
    def __init__(self, parent: Tk):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Calculator")
        # Quy định kiểu phông chữ thông qua tham số font và khoảng cách của frame với cửa sổ thông qua tham số padding
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        # region Hai phương thức columnconfigure() và rowconfigure() quy định khoảng các giữa các widget
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        # endregion

        # region Tạo một Entry để hiển thị số cũng như kết quả tính toán
        # Tham số sticky quy định cách thức co dãn theo kích thước của cửa sổ. W+E tức là co dãn từ trái sang phải (West to East)  
        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=W+E)
        # endregion

        # region 4 nút được đặt ở hàng 1 
        clear = Button(self, text="CLS")
        clear.grid(row=1, column=0)
        bck = Button(self, text="BACK")
        bck.grid(row=1, column=1)
        lbl = Button(self)
        lbl.grid(row=1, column=2)
        close = Button(self, text='CLOSE')
        close.grid(row=1, column=3)
        # endregion

        # region 4 nút được đặt ở hàng 2
        sev = Button(self, text='7')
        sev.grid(row=2, column=0)
        eig = Button(self, text='8')
        eig.grid(row=2, column=1)
        nin = Button(self, text='9')
        nin.grid(row=2, column=2)
        div = Button(self, text='/')
        div.grid(row=2, column=3)
        # endregion

        # region 4 nút được đặt ở hàng 3
        fou = Button(self, text='4')
        fou.grid(row=3, column=0)
        fiv = Button(self, text='5')
        fiv.grid(row=3, column=1)
        six = Button(self, text='6')
        six.grid(row=3, column=2)
        mul = Button(self, text='*')
        mul.grid(row=3, column=3)
        # endregion

        # region 4 nút được đặt ở hàng 4
        one = Button(self, text='1')
        one.grid(row=4, column=0)
        two = Button(self, text='2')
        two.grid(row=4, column=1)
        thr = Button(self, text='3')
        thr.grid(row=4, column=2)
        sub = Button(self, text='-')
        sub.grid(row=4, column=3)
        # endregion

        # region 4 nút được đặt ở hàng 5
        zer = Button(self, text='0')
        zer.grid(row=5, column=0)
        poi = Button(self, text='.')
        poi.grid(row=5, column=1)
        equ = Button(self, text='=')
        equ.grid(row=5, column=2)
        plu = Button(self, text='+')
        plu.grid(row=5, column=3)
        # endregion

        # Phương thức pack() hiển thị các widget lên màn hình và khởi tạo kích thước cho chúng.
        # Nếu pack() được gọi ra mà không có tham số nào thì kích thước của các widget luôn là kích thước vừa đủ để bao bọc đoạn text bên trong
        # Ngoài ra, nếu không có tham số truyền vào thì phương thức sẽ đặt layout ở vị trí trên cùng của frame.
        self.pack()


root = Tk()
app = Example(root)
root.mainloop()
