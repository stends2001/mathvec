import tkinter as tk
import customtkinter
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
    panel_right_top: customtkinter.CTkFrame
    root: customtkinter.CTk

    latex_supported:    bool

    theme_button:       str 
    theme_button_hover: str
    theme_button_unavail:str
    right_panel_width:  int

    def manage_buttons(self):

        # BUTTONS - INDEPENDENT ON LATEX

        # button1: clear
        btn1 = customtkinter.CTkButton(self.panel_right_top, 
                                       text="CLEAR", 
                                       width = int(0.975 * self.right_panel_width),
                                       command=self.reset, 
                                       fg_color = self.theme_button, 
                                       hover_color= self.theme_button_hover)

        # button5: set directory
        btn5 = customtkinter.CTkButton(self.panel_right_top, 
                                       text="SET dir", 
                                       command=self.set_output_dir,
                                       fg_color = self.theme_button, 
                                       hover_color= self.theme_button_hover)     

        btn6 = customtkinter.CTkButton(self.panel_right_top, 
                                       text="EXIT", 
                                       command=self.quit_app,
                                       fg_color = self.theme_button, 
                                       hover_color= self.theme_button_hover)       
        
                                    

        # button2: view expression
        btn2 = customtkinter.CTkButton(self.panel_right_top, 
                         text='VIEW' if self.latex_supported else '❌VIEW', 
                         command=self.view, 
                         fg_color = self.theme_button if self.latex_supported else self.theme_button_unavail,
                         hover_color= self.theme_button_hover if self.latex_supported else self.theme_button_unavail
                         )  
        
        btn3 = customtkinter.CTkButton(self.panel_right_top, 
                         text='SAVE .svg' if self.latex_supported else '❌SAVE .svg', 
                         command= lambda ext = 'svg': self.save(ext), 
                         fg_color = self.theme_button if self.latex_supported else self.theme_button_unavail,
                         hover_color= self.theme_button_hover if self.latex_supported else self.theme_button_unavail
                         )   

        btn4 = customtkinter.CTkButton(self.panel_right_top, 
                         text='SAVE .png' if self.latex_supported else '❌SAVE .png', 
                         command= lambda ext = 'png': self.save(ext), 
                         fg_color = self.theme_button if self.latex_supported else self.theme_button_unavail,
                         hover_color= self.theme_button_hover if self.latex_supported else self.theme_button_unavail
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