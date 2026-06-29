import tkinter as tk

class ButtonManagerMixin:

    panel_right: tk.Frame

    def manage_buttons(self):

        # button1: clear
        btn1 = tk.Button(
            self.panel_right,
            text    = 'CLEAR',
            command = lambda: self.reset(),
        )        

        # button2: rename equation
        btn2 = tk.Button(
            self.panel_right,
            text    = 'view',
            command = lambda: self.view(),
        )

        # button3: save equation
        btn3 = tk.Button(
            self.panel_right,
            text    = 'save',
            command = lambda: self.save(),
        )    

        for row, btn in enumerate([btn1, btn2, btn3]):
      
            btn.grid(
                    row=row,
                    column = 0,
                    sticky="nsew",
                    padx=2,
                    pady=2
                )

    def reset(self):
        raise NotImplementedError('this is supposed to be a stub for `reset()`')
    
    def view(self):
        raise NotImplementedError('this is supposed to be a stub for `view()`')
    
    def save(self):
        raise NotImplementedError('this is supposed to be a stub for `save()`')     