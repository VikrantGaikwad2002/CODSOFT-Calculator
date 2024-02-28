from tkinter import *
import tkinter as tk

class Calculator:
    def __init__(self, calc):
        self.calc = calc
        self.calc.title("Calculator")
        self.calc.iconbitmap('calculator-app-icon.ico')
        self.calc.configure(bg="aquamarine4")


        # input display entrybox
        self.entry = tk.Entry(calc, bg="white", fg="black", width=20, font=('Arial', 18), justify='right')
        self.entry.grid(row=0, column=0, columnspan=6, sticky='nsew', pady=5)

        # result display label
        self.result_lbl = tk.Label(calc, text="", font=('Arial', 18), anchor='e', bg='white', fg='black')
        self.result_lbl.grid(row=1, column=0, columnspan=6, sticky='nsew', pady=5)

        # Buttons 
        buttons = [
            'DEL', '←', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', 'Ans'
        ]
        row = 2
        col = 0
        button_bg_color = 'azure1'
        self.buttons = {}
        for button in buttons:
            fg_color = 'black'
            self.buttons[button] = tk.Button(calc, text=button, width=5, height=2,
                                             command=lambda b=button: self.on_button_click(b),
                                             bg=button_bg_color, fg=fg_color, font=('Arial', 18), bd=0, relief='flat')
            self.buttons[button].grid(row=row, column=col, padx=5, pady=5, sticky='nsew', ipadx=10, ipady=10, columnspan=1)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.calc.bind("<Key>", self.on_keyboard_input)
        self.calc.bind("<Return>", lambda event: self.on_button_click('='))
        self.calc.bind("<BackSpace>", lambda event: self.on_button_click('←'))

        # last answer for ans button
        self.last_answer = None

    def on_button_click(self, button):
        current_text = self.entry.get()
        if button == '=':
            try:
                result = eval(current_text)
                self.last_answer = result
                self.result_lbl.config(text=f"Result: {result}")
                self.entry.delete(0, tk.END)  
            except ZeroDivisionError:
                self.result_lbl.config(text="Result: Division by zero")
            except Exception as e:
                self.result_lbl.config(text="Result: Error")

        elif button == 'DEL':
            self.entry.delete(0, tk.END)
            self.result_lbl.config(text="")

        elif button == '←':
            current_text = current_text[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text)

        elif button == '%':
            try:
                result = eval(current_text) / 100
                self.result_lbl.config(text=f"Result: {result}")
                self.entry.delete(0, tk.END) 
            except Exception as e:
                self.result_lbl.config(text="Result: Error")

        elif button == 'Ans':
            self.entry.insert(tk.END, str(self.last_answer))

        else:
            self.entry.insert(tk.END, button)
# for keybord input 
    def on_keyboard_input(self, event):
        key = event.char
        if key in self.buttons:
            self.on_button_click(key)

def main():
    calc = Tk()
    c = Calculator(calc)
    calc.mainloop()

if __name__ == "__main__":
    main()
