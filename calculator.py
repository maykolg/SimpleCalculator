import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x600")
        self.master.resizable(0, 0)
        self.master.title("Calculator Minimalist")
        self.master.config(bg='black')

        self.string = tk.StringVar()
        self.entry = tk.Entry(self.master, textvariable=self.string, width=20, font=('poppins', 24), bd=5, insertwidth=4, bg='white', justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x = button: self.append_string(x)
            if button == "=":
                action = lambda: self.calculate()
            elif button == 'C':
                action = lambda: self.clear()

            tk.Button(self.master, text=button, width=10, height=3, command=action, bg='black', fg='white').grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        clear = tk.Button(self.master, text='C', width=10, height=3, command=lambda: self.clear(), bg='black', fg='white')
        clear.grid(row=row_val, column=col_val)

    def append_string(self, text):
        self.string.set(self.string.get() + str(text))

    def clear(self):
        self.string.set('')

    def calculate(self):
        try:
            result = eval(self.string.get())
            self.string.set(result)
        except Exception as e:
            messagebox.showerror('Error', 'Operación inválida')

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()