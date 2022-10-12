from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


class ToDo(Frame):
    counter = 1

    def __init__(self, parent: Tk):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):

        task_list = []

        def inputError():
            if entryTask.get() == "":
                messagebox.showerror("Input Error")
                return 0
            return 1

        def clear_taskNumberField():
            txtTaskNumber.delete(0.0, END)

        def clear_taskField():
            entryTask.delete(0, END)

        def insertTask():
            value = inputError()
            if value == 0:
                return

            content = entryTask.get()+"\n"

            task_list.append(content)

            txtTaskArea.insert(
                'end -1 chars', "["+str(self.counter)+"]"+content)
            self.counter += 1
            clear_taskField()

        def delete():
            if len(task_list) == 0:
                messagebox.showerror("No task")
                return

            number = txtTaskNumber.get(1.0, END)

            if number == "\n":
                messagebox.showerror("input error")
                return
            else:
                task_no = int(number)

            clear_taskNumberField()
            task_list.pop(task_no-1)
            self.counter -= 1
            txtTaskArea.delete(1.0, END)
            for i in range(len(task_list)):
                txtTaskArea.insert(
                    "end -1 chars", "[{0}] {1}".format(str(i+1), task_list[i]))

        self.parent.title("Task To Do")

        lbEnter = Label(self, text="Enter your task", foreground="blue")
        entryTask = Entry(self)
        btnSubmit = Button(self, text="Submit", command=insertTask)
        txtTaskArea = Text(self, height=5, width=25, font="lucida 13")
        btnDelete = Button(self, text="Delete", command=delete)
        lbTaskNumber = Label(
            self, text="Delete Task Number", foreground="blue")
        txtTaskNumber = Text(self, height=1, width=2, font="lucida 13")
        btnExit = Button(self, text="Exit", command=exit)

        lbEnter.grid(row=0, column=2)
        entryTask.grid(row=1, column=2, ipadx=50)
        btnSubmit.grid(row=2, column=2)
        txtTaskArea.grid(row=3, column=2)
        lbTaskNumber.grid(row=4, column=2)
        txtTaskNumber.grid(row=5, column=2)
        btnDelete.grid(row=6, column=2)
        btnExit.grid(row=7, column=2)
        self.pack()


if __name__ == "__main__":
    root = Tk()
    root.geometry("250x300")
    app = ToDo(root)
    root.mainloop()
