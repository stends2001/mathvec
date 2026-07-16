import tkinter as tk
import customtkinter
from typing import Literal, Dict

class HistoryManagerMixin:
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
    panel_right_bottom: customtkinter.CTkFrame
    root: customtkinter.CTk

    latex_supported:    bool

    theme_main:         str 
    theme_text:         str
    theme_frame:        str

    _history: Dict[str,str]

    def manage_history(self):
        row1 = customtkinter.CTkFrame(self.panel_right_bottom, fg_color = self.theme_frame)
        row1.pack(fill="x", padx=2, pady=10)
        customtkinter.CTkLabel(
            row1,
            text="HISTORY",
            fg_color=self.theme_frame,
            text_color=self.theme_text,
            font=customtkinter.CTkFont(size=20, weight="bold")
        ).pack(pady=10)         

    def _save_to_history(self, name: str, expression: str):
        self._history[name] = expression

        print(f'history: {self._history}')

    def _save_history(self):
        pass