# Tkinter là một package trong Python chứa module Tk hỗ trợ lập trình giao diện (GUI)
# Tk ban đầu được viết cho ngôn ngữ Tcl, sau đó được viết ra để sử dụng Tk bằng trình thông dịch Tcl trên nền Python
# Một số công cụ tạo GUI khác hỗ trợ Python: wxPython, PyQt, PyGTK

# Import lớp Tk từ gói Tkinker
# Tk được dùng để tạo cửa sổ
from tkinter import Tk, BOTH

# Một số widget trong Tkintẻ được hỗ trợ màu sắc khác nhau, thuật ngữ gọi là theme
# Module ttk hỗ trợ sử dụng theme trong Python
from tkinter.ttk import Frame, Button, Style


# Định nghĩa lớp Example kế thừa lớp Frame.
# Frame là một widget đùng để quản lý các widget khác
# Các widget tương tự được gọi chung là container hoặc layout
# Trong phương thức khởi tạo (Constructor), gọi Constructor của Frame và đưa tham số màu nền là màu trắng
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        # Dùng thuộc tính parent để lưu lại đối tượng root
        self.parent = parent

        # Phương thức initUI() dùng để tạo các widget trên cửa sổ
        self.initUI()

    def initUI(self):

        # Phương thức title() dùng để thay đổi tiêu đề cửa sổ
        self.parent.title("Simple")

        # Để quy định kiểu theme thì khởi tạo đối tượng Style() và gọi tới phương thức theme_use().
        # Một số kiểu theme mặc định: clam, default, alt, classic
        self.style = Style()
        self.style.theme_use("default")

        # Phương thức pack() sắp xếp vị trí các widget trước khi gắn chúng lên cửa sổ chính.
        # Tham số fill=BOTH dãn widget ra theo chièu ngang và chiều rộng ==> widget đó chiếmm toàn bộ cửa sổ
        self.pack(fill=BOTH, expand=1)

        # Tạo một đội tượng widget là button.
        # Tham số đầu tiên là đối tượng container của nó
        # Tham số thứ 2 là đoạn text sẽ hiển thị trên nút
        # Tham số thứ 3 là lệnh được thực thi khi nút được bấm
        quitButton = Button(self, text="Quit", command=self.quit)

        # Phương thức place() quy định vị trí của nút bấm trên cửa sổ
        quitButton.place(x=50, y=50)


# Tạo một cửa sổ và gắn vào biến root để quản lý.
# Cửa sổ luôn phải được tạo trước khi tạo các widget
root = Tk()

# Phương thức geomertry() quy định kích thước cửa sổ và vị trí hiển thị trên màn hình
# 2 tham số đầu tiên là kích thước cửa sổ, 2 phương thức sau là vị trí của cửa sổ trên màn hình
root.geometry("250x150+300+300")

# Tạo một Frame và gắn nó vào cửa sổ chính
app = Example(root)

# gọi mainloop() để cửa sổ hiện lên màn hình và nhận các event để xử lý
root.mainloop()
