import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # change the icon
        self.iconbitmap('calc.ico')
        self.title("Calculator")

        # Colors (HEX)
        self.app_bg = "#0e1a40"
        self.entry_bg = "#5d5d5d"
        self.entry_fg = "#FFFFFF"
        self.btn_bg = "#222f5b"
        self.btn_fg = "#FFFFFF"
        self.clear_bg = "#5d5d5d"
        self.del_bg = "#5d5d5d"
        self.action_fg = "#FFFFFF"
        self.operator_bg = "#946b2d"
        self.operator_fg = "#000000"

        # Background
        self.configure(bg=self.app_bg)

        # create the input field
        self.input_text = tk.StringVar()
        self.input_field = tk.Entry(self, textvariable=self.input_text, justify='right', width=30,
                                    font=("Arial", 12, "bold"), bg=self.entry_bg, fg=self.entry_fg, insertbackground=self.entry_fg)
        self.input_field.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # create the buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '(', ')',
        ]

        # create the buttons and add them to the grid
        row = 1
        col = 0
        for button in buttons:
            button_action = lambda x=button: self.button_click(x)

            if button in "+-*/":
                bg = self.operator_bg
                fg = self.operator_fg
            else:
                bg = self.btn_bg
                fg = self.btn_fg

            tk.Button(self, text=button, width=5, command=button_action, bg=bg, fg=fg, font=("Arial", 12),
                      activebackground=bg, activeforeground=fg).grid(row=row, column=col, padx=5, pady=5),
            col += 1
            if col > 3:
                col = 0
                row += 1

        # add clear and delete buttons
        clear_button = tk.Button(
            self, text="C", width=5, command=self.clear_input,
            bg=self.clear_bg, fg=self.action_fg, font=("Arial", 11),
            activebackground=self.clear_bg, activeforeground=self.action_fg
        )
        clear_button.grid(row=5, column=2, padx=5, pady=5)

        delete_button = tk.Button(
            self, text="DEL", width=5, command=self.delete_char,
            bg=self.del_bg, fg=self.action_fg, font=("Arial", 11),
            activebackground=self.del_bg, activeforeground=self.action_fg
        )
        delete_button.grid(row=5, column=3, padx=5, pady=5)

        # bind the keyboard events to the calculator window
        self.bind('<Key>', self.keyboard_input)

    def button_click(self, button):
        # handle button clicks
        if button == '=':
            try:
                result = eval(self.input_text.get())
                self.input_text.set(result)
            except:
                self.input_text.set('ERROR')

        elif button == 'C':
            self.clear_input()
        elif button == 'DEL':
            self.delete_char()
        else:
            current_text = self.input_text.get()
            if self._should_insert_mul(current_text, button):
                current_text += '*'

            new_text = current_text + button
            self.input_text.set(new_text)

    def clear_input(self):
        # clear the input field
        self.input_text.set('')

    def delete_char(self):
        # delete the last character from the input field
        current_text = self.input_text.get()
        new_text = current_text[:-1]
        self.input_text.set(new_text)

    def _should_insert_mul(self, current, next_char):
        if not current:
            return False
        prev = current[-1]
        return (next_char == '(' and (prev.isdigit() or prev == '.' or prev == ')')) or (
                    next_char.isdigit() and prev == ')')

    def keyboard_input(self, event):
        # handle keyboard input
        if event.char in '0123456789+-*/.()':
            self.button_click(event.char)
        elif event.keysym == 'Return':
            self.button_click('=')
        elif event.keysym == 'BackSpace':
            self.delete_char()


if __name__ == '__main__':
    calc = Calculator()
    calc.mainloop()







