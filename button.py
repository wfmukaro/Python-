import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.add = tk.Button(self)
        self.add["text"] = "Addition\n"
        self.add["command"] = self.addnum
        self.add.pack(side="top")

        self.subtract = tk.Button(self)
        self.subtract["text"] = "Subtraction\n"
        self.subtract["command"] = self.subtractnum
        self.subtract.pack(side="top")

        self.multiply = tk.Button(self)
        self.multiply["text"] = "Multiplication\n"
        self.multiply["command"] = self.multiplynum
        self.multiply.pack(side="top")

        self.divide = tk.Button(self)
        self.divide["text"] = "Division\n"
        self.divide["command"] = self.dividenum
        self.divide.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def addnum(self):
        print("Add two numbers!")
        num1=float(input("Enter a number:"))
        num2=float(input("Enter another number:"))
        result=num1+num2
        print("The answer is",result)

    def subtractnum(self):
        print("subtract two numbers!")
        num1=float(input("Enter a number:"))
        num2=float(input("Enter another number:"))
        result=num1-num2
        print("The answer is",result)

    def multiplynum(self):
        print("multiply two numbers!")
        num1=float(input("Enter a number:"))
        num2=float(input("Enter another number:"))
        result=num1*num2
        print("The answer is",result)

    def dividenum(self):
        print("divide two numbers!")
        num1=float(input("Enter a number:"))
        num2=float(input("Enter another number:"))
        result=num1/num2
        print("The answer is",result)


root = tk.Tk()
app = Application(master=root)
app.mainloop()

