import tkinter as tk
import customtkinter
from typing import Literal, Protocol
from .colorpalette import ColorPalette

class _ButtonProtocol(Protocol):
    """
    Protocol that lists methods in MathVecApp, 
    as fallback for ButtonManagerMixin
    """
    panel_right_top:    customtkinter.CTkFrame
    root:               customtkinter.CTk

    latex_supported:    bool
    latex_supported:    bool

    color_palette: ColorPalette
    right_panel_width:  int

    def reset(self) -> None:
        ...
    
    def view(self) -> None:
        ...
    
    def save(self, extension: Literal['png','svg']) -> None:
        ...
    
    def set_output_dir(self) -> None:
        ...   
    
    def quit_app(self) -> None:
        ...                
    
    def clear_history(self) -> None:
        ...           

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
    def manage_buttons(self: _ButtonProtocol):

        # BUTTONS - INDEPENDENT ON LATEX

        # button1: clear
        btn1 = customtkinter.CTkButton(self.panel_right_top, 
                                       text="CLEAR", 
                                       width = int(0.975 * self.right_panel_width),
                                       command=self.reset, 
                                       fg_color = self.color_palette.button, 
                                       hover_color= self.color_palette.button_hover)

        # button5: set directory
        btn5 = customtkinter.CTkButton(self.panel_right_top, 
                                       text="SET dir", 
                                       command=self.set_output_dir, 
                                       fg_color = self.color_palette.button, 
                                       hover_color= self.color_palette.button_hover)

        btn7 = customtkinter.CTkButton(self.panel_right_top, 
                                       text="EXIT", 
                                       command=self.quit_app, 
                                       fg_color = self.color_palette.button, 
                                       hover_color= self.color_palette.button_hover)      
        
        btn6 = customtkinter.CTkButton(self.panel_right_top, 
                                       text="CLEAR HISTORY", 
                                       command=self.clear_history, 
                                       fg_color = self.color_palette.button, 
                                       hover_color= self.color_palette.button_hover)      
        
                                    

        # button2: view expression
        btn2 = customtkinter.CTkButton(self.panel_right_top, 
                         text='VIEW' if self.latex_supported else '❌VIEW', 
                         command=self.view, 
                         fg_color = self.color_palette.button if self.latex_supported else self.color_palette.button_unavail,
                         hover_color= self.color_palette.button if self.latex_supported else self.color_palette.button_unavail,
                         text_color = 'white' if self.latex_supported else 'black'
                         )  
        
        btn3 = customtkinter.CTkButton(self.panel_right_top, 
                         text='SAVE .svg' if self.latex_supported else '❌SAVE .svg', 
                         command= lambda ext = 'svg': self.save(ext), 
                         fg_color = self.color_palette.button if self.latex_supported else self.color_palette.button_unavail,
                         hover_color= self.color_palette.button if self.latex_supported else self.color_palette.button_unavail,
                         text_color = 'white' if self.latex_supported else 'black'
                         )   

        btn4 = customtkinter.CTkButton(self.panel_right_top, 
                         text='SAVE .png' if self.latex_supported else '❌SAVE .png', 
                         command= lambda ext = 'png': self.save(ext), 
                         fg_color = self.color_palette.button if self.latex_supported else self.color_palette.button_unavail,
                         hover_color= self.color_palette.button if self.latex_supported else self.color_palette.button_unavail,
                         text_color = 'white' if self.latex_supported else 'black'
                         )              

        for row, btn in enumerate([btn1, btn2, btn3, btn4, btn5, btn6, btn7]):
      
            btn.grid(
                    row=row,
                    column = 0,
                    sticky="nsew",
                    padx=2,
                    pady=2
                )

