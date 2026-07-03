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
    root: tk.Tk

    latex_supported:    bool

    def manage_buttons(self):

        # BUTTONS - INDEPENDENT ON LATEX

        # button1: clear
        btn1 = tk.Button(self.panel_right, text = 'CLEAR', 
                         command = lambda: self.reset())        

        # button5: set directory
        btn5 = tk.Button(self.panel_right, text = 'SET dir', 
                         command = lambda: self.set_output_dir())         
                
        btn6 = tk.Button(self.panel_right, text="EXIT",
            command=self.quit_app)        
        
        # button2: view expression
        btn2 = tk.Button(self.panel_right, 
                         text='VIEW' if self.latex_supported else '❌VIEW', 
                         command=self.view, 
                         bg = None if self.latex_supported else '#F7A8A8'   # type: ignore
                         )  
        
        btn3 = tk.Button(self.panel_right, 
                         text='SAVE .svg' if self.latex_supported else '❌SAVE .svg', 
                         command= lambda ext = 'svg': self.save(ext), 
                         bg = None if self.latex_supported else '#F7A8A8'   # type: ignore
                         )   

        btn4 = tk.Button(self.panel_right, 
                         text='SAVE .png' if self.latex_supported else '❌SAVE .png', 
                         command= lambda ext = 'png': self.save(ext), 
                         bg = None if self.latex_supported else '#F7A8A8'   # type: ignore
                         )              

        for row, btn in enumerate([btn1, btn2, btn3, btn4, btn5, btn6]):
      
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
    
    def quit_app(self):
        raise NotImplementedError('this is supposed to be a stub for `quit_app()`')                   
