import tkinter as tk
import customtkinter
from typing import Literal, Protocol,TypedDict

from .colorpalette import ColorPalette

class ButtonStyleKwargs(TypedDict):
    """Simple TypedDict for Button - arguments"""
    text: str
    width: int
    fg_color: str
    hover_color: str
    text_color: str


def get_buttonstyle(latex_status : bool | None, 
                    text : str, 
                    colorpalette : ColorPalette, 
                    width : int) -> ButtonStyleKwargs:
    """
    Get an instance of ``buttonstyle`` depending on configuration.

    Parameters
    ----------
    latex_status : bool | None
        Whether ``latex_supported`` is True or False. When this is not applicable to the button,
        use None.
    text : str
        Button label.
    colorpalette : ColorPalette
        The theme of the application.
    width : int
        The width of buttons in the application.

    Returns
    -------
    ``ButtonStyleKwargs``
        Simple TypedDict for Button - arguments        
    """
    if latex_status is False:
        text        = f"❌ {text}"
        fg_color    = colorpalette.button_unavail
        hover_color = colorpalette.button_unavail
        text_color  = colorpalette.button_text_unvavail

    else:
        text        = text 
        fg_color    = colorpalette.button 
        hover_color = colorpalette.button_hover
        text_color  = colorpalette.button_text        

    return { 
        "text"          : text,
        "width"         : width,
        "fg_color"      : fg_color,
        "hover_color"   : hover_color,
        "text_color"    : text_color
    }

class _ButtonProtocol(Protocol):
    """
    Protocol that lists methods in ``MathVecApp``
    as fallback for ButtonManagerMixin
    """
    latex_supported : bool

    root : customtkinter.CTk
    panel_right_top : customtkinter.CTkFrame
    right_panel_width : int   
    color_palette : ColorPalette

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

    def change_theme(self) -> None:
        ...

class ButtonManagerMixin:
    """
    Mixin class to ``MathVecApp`` that manages buttons.

    See Also
    --------
    For more information, see main class ``MathVecApp``.
    """
    def manage_buttons(self: _ButtonProtocol):
        """
        Main function to ``ButtonManagerMixin. Sets the button grid.
        Note that the buttons are linked to ``self.right_panel_top``, 
        which is linked in the declaration of each button.
        """

        # ===== BUTTONS - INDEPENDENT OF LATEX STATUS ===== #

        button_width = int(0.975 * self.right_panel_width)

        # button1: clear
        btn1 = customtkinter.CTkButton(self.panel_right_top, 
                                       command=self.reset, 
                                       **get_buttonstyle(None, 'CLEAR', self.color_palette, button_width)
                                       )

        # button5: set directory
        btn5 = customtkinter.CTkButton(self.panel_right_top, 
                                       command=self.set_output_dir, 
                                       **get_buttonstyle(None, 'SET DIR', self.color_palette, button_width)
                                       )

        btn6 = customtkinter.CTkButton(self.panel_right_top, 
                                       command=self.clear_history, 
                                       **get_buttonstyle(None, 'CLEAR HISTORY', self.color_palette, button_width)
                                       )     

        btn7 = customtkinter.CTkButton(self.panel_right_top, 
                                       command=self.change_theme, 
                                       **get_buttonstyle(None, 'SWITCH THEME', self.color_palette, button_width)
                                       )  

        btn8 = customtkinter.CTkButton(self.panel_right_top,
                                       command=self.quit_app, 
                                       **get_buttonstyle(None, 'EXIT', self.color_palette, button_width)
                                       )      
        
     
        # button2: view expression
        btn2 = customtkinter.CTkButton(self.panel_right_top, 
                                       command=self.view, 
                                       **get_buttonstyle(self.latex_supported, 'VIEW', self.color_palette, button_width)
                                       )  
          
        btn3 = customtkinter.CTkButton(self.panel_right_top, 
                                       command= lambda ext = 'svg': self.save(ext), 
                                       **get_buttonstyle(self.latex_supported, 'SAVE .svg', self.color_palette, button_width)
                                       )  
            
        btn4 = customtkinter.CTkButton(self.panel_right_top, 
                                       command= lambda ext = 'png': self.save(ext), 
                                       **get_buttonstyle(self.latex_supported, 'SAVE .png', self.color_palette, button_width)
                                       )  

        buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8]

        for row, btn in enumerate(buttons):
      
            btn.grid(
                    row=row,
                    column = 0,
                    sticky="nsew",
                    padx=2,
                    pady=2
                )

