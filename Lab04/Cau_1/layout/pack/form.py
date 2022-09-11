from tkinter import Tk, Text, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry


class Example(Frame):
    def __init__(self, parent: Tk):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Review")

        # Tạo frame chính đẻ chứa các widget còn lại 
        self.pack(fill=BOTH, expand=True)

        # region Tạo frame 1 và đặt 2 widget vào đó: Label và Entry
        # Label: Widget dùng để hiển thị text, có độ dài cố định
        # Entry: Widget dùng để nhập text, có độ dài biến động theo kích thức cửa sổ nhờ 2 tham số fill và expand.
        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Title", width=6)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)
        # endregion

        # region Tạo frame 2 tương tự frame 1
        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Author", width=6)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)
        # endregion

        # region Trong frame thứ 3, đặt 1 Label và 1 Text. 
        # Label được đặt về phía trên của Frame3,
        # Text tự động co dãn theo kích thước cửa sổ
        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text="Review", width=6)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt = Text(frame3)
        txt.pack(fill=X, padx=5, pady=5, expand=True)
        # endregion


root = Tk()
root.geometry("300x300+300+300")
app = Example(root)
root.mainloop()
