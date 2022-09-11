from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

# Tạo ra 2 frame:
# Frame đầu tiên (frame Example) là layout chình dùng để chứa toàn bộ widget
class Example(Frame):
    def __init__(self, parent:Tk):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Button")
        self.style = Style()
        self.style.theme_use("default")

        # region Tạo ra frame thứ 2, chiếm phần lớn diện tích frame chính.
        # Tham số relief mô phỏng hiệu ứng hiển thị 3D của frame
        # Tham số borderwidth hiển thị đường viền của frame, mặc định là 0
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        # endregion

        self.pack(fill=BOTH, expand=True)

        # region Tạo button Close và tham chiếu đến đối tượng closeButton
        # Phương thức pack quyiđịnh cách hinệ thị của button trên cửa sổ
        # Tham số side=RIGHT sẽ đưa button vào vị trí bên phải, padx và pady quy định khoảng cách giữa button và các widget khác và đường viền của cửa sổ chính. (Trường hợp trong ví dụ là 5 px)
        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        # endregion

        # region Button OK cũng được tạo tương tụ như Button Close
        # Button OK sẽ được đưa sang phía bên phải và sát cạnh bên Button Close với khoảng cách 5 pixel
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)
        # endregion
        
root=Tk()
root.geometry("300x200+300+300")
app=Example(root)
root.mainloop()