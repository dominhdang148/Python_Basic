
# Để khởi tạo đối tượng hình ảnh, sử dụng thư viện Pillow trong Python 
# # Mặc định thì label trong Tkinter cũng có các module có thể hiển thị ảnh nhưng hạn chế
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Label


class Example(Frame):
    def __init__(self, parent: Tk):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('Label')

        self.img = Image.open("image.jpg")
        rotunda = ImageTk.PhotoImage(self.img)

        # Gán tham số image khi khởi tạo để gán ảnh vào label
        label = Label(self, image=rotunda)

        # Tạo một biến để giữ lại tham chiếu đến ảnh
        # Nếu không tạo, bộ thu dọn tài nguyên của Python sẽ xóa mất ảnh
        label.image = rotunda

        label.pack()
        self.pack()


        # Hàm tạo kích thước cửa sổ bằng đúng với kích thước ảnh
    def setGeometry(self):
        w, h = self.img.size
        self.parent.geometry(("%dx%d+300+300") % (w, h))


root = Tk()
ex = Example(root)
ex.setGeometry()
root.mainloop()
