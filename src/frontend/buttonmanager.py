import tkinter as tk

class ButtonManagerMixin:

    panel_right: tk.Frame

    def manage_buttons(self):

        # button1: clear
        btn1 = tk.Button(
            self.panel_right,
            text    = 'CLEAR',
            command = lambda: print('input to be cleared'),
        )        

        # button2: rename equation
        btn2 = tk.Button(
            self.panel_right,
            text    = 'rename',
            command = lambda: print('equation to be renamed'),
        )

        # button3: save equation
        btn3 = tk.Button(
            self.panel_right,
            text    = 'save',
            command = lambda: print('output to be saved'),
        )    

        for row, btn in enumerate([btn1, btn2, btn3]):
      
            btn.grid(
                    row=row,
                    column = 0,
                    sticky="nsew",
                    padx=2,
                    pady=2
                )
