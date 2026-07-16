import tkinter as tk
import customtkinter
from typing import Literal, Dict
import pandas as pd

from ..backend import PathManager

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
    root:               customtkinter.CTk

    latex_supported:    bool
    pathmanager:        PathManager

    theme_main:         str 
    theme_text:         str
    theme_frame:        str

    theme_button:       str 
    theme_button_hover: str
    theme_button_unavail:str
    right_panel_width:  int


    panel_right_bottom: customtkinter.CTkFrame

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

        self._history = self._load_history()

    def _save_to_history(self, name: str, expression: str):
        self._history.loc[len(self._history)] =  {"name": name, "expression": expression}
        self._update_history_panel()

    def _save_history(self):
        filepath = self.pathmanager.history

        self._history.reset_index(drop = True).to_csv(filepath, sep = "\t", index = False)

    def _load_history(self) -> pd.DataFrame:
        filepath = self.pathmanager.history
        if filepath.exists():
           return pd.read_csv(filepath, delimiter="\t")
        else:
            return pd.DataFrame(columns=["name", "expression"])
        
    def _clear_history(self) -> None:
        self._history = pd.DataFrame(columns=["name", "expression"])
        filepath = self.pathmanager.history
        if filepath.exists():
            filepath.unlink()


    def _update_history_panel(self) -> None:
        num_expressions = len(self._history)
        buttons = []

        print('history:')
        print(self._history)

        for n in range(min(num_expressions,9)):

            idx   = n + 1

            expression_name = self._history.loc[n, "name"]
            expression      = self._history.loc[n, "expression"]

            btn_n = customtkinter.CTkButton(self.panel_right_bottom, 
                                            text        = f"{idx}. {expression_name}", 
                                            command= lambda nm = expression_name, expr = expression : self.insert_from_history(nm, expr), 
                                            fg_color    = self.theme_button, 
                                            hover_color = self.theme_button_hover)    
            buttons.append(btn_n)   

        for row, btn in enumerate(buttons):

            btn.pack(
                fill="y",
                padx=2,
                pady=2
            )

    def insert_from_history(self, name: str, expression_name: str):
        raise NotImplementedError('this is supposed to be a stub for `insert_from_history()`') 