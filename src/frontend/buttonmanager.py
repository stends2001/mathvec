import tkinter as tk
from typing import Literal 

class ButtonManagerMixin:
    """
    Mixin class to MathVecApp
    Manages buttons

    As the source code lives in other mixins, or on the main class,
    the buttons here call to stubs. The method with proper 
    functionality live on the main class.

    See Also
    --------
    For more information, see main class MathVecApp
    """
    panel_right: tk.Frame

    def manage_buttons(self):

        # button1: clear
        btn1 = tk.Button(self.panel_right, text = 'CLEAR', 
                         command = lambda: self.reset())        

        # button2: rename equation
        btn2 = tk.Button(self.panel_right, text = 'VIEW', 
                         command = lambda: self.view())

        # button3: save equation as svg
        btn3 = tk.Button(self.panel_right, text = 'SAVE .svg', 
                         command = lambda extension = 'svg': self.save(extension))    
        
        # button4: save equation as png
        btn4 = tk.Button(self.panel_right, text = 'SAVE .png', 
                         command = lambda extension = 'png': self.save(extension))    

        # button5: set directory
        btn5 = tk.Button(self.panel_right, text = 'SET dir', 
                         command = lambda: self.set_output_dir())                             

        for row, btn in enumerate([btn1, btn2, btn3, btn4, btn5]):
      
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
    
    def save(self, extension: Literal['png','svg']):
        raise NotImplementedError('this is supposed to be a stub for `save()`')     
    
    def set_output_dir(self):
        raise NotImplementedError('this is supposed to be a stub for `set_output_dir()`')           
    