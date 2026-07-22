import tkinter as tk
import customtkinter
from typing import Literal, Dict, List, Protocol
import pandas as pd

from .colorpalette import ColorPalette
from ..backend import PathManager

class _HistoryProtocol(Protocol):
    panel_right_bottom: customtkinter.CTkFrame
    root:               customtkinter.CTk

    latex_supported:    bool
    pathmanager:        PathManager

    panel_right_bottom: customtkinter.CTkFrame

    color_palette: ColorPalette
    history_buttons: List[customtkinter.CTkButton]

    _history: pd.DataFrame

    def insert_from_history(self, name: str, expression_name: str) -> None:
        ...

    def manage_history(self) -> None:
        ...

    def _save_to_history(self) -> None:
        ...

    def _save_history(self) -> None:
        ...

    def _load_history(self) -> pd.DataFrame:
        ...

    def _clear_history(self) -> None:
        ... 

    def _update_history_panel(self) -> None:
        ...

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

    def manage_history(self: _HistoryProtocol):
        row1 = customtkinter.CTkFrame(self.panel_right_bottom, fg_color = self.color_palette.frame)
        row1.pack(fill="x", padx=2, pady=10)
        customtkinter.CTkLabel(
            row1,
            text="HISTORY",
            fg_color=self.color_palette.frame,
            text_color=self.color_palette.text,
            font=customtkinter.CTkFont(size=20, weight="bold")
        ).pack(pady=10)         

        self._history = self._load_history()

    def _save_to_history(self: _HistoryProtocol, name: str, expression: str):
        self._history.loc[len(self._history)] =  {"name": name, "expression": expression}
        self._update_history_panel()

    def _save_history(self: _HistoryProtocol):
        filepath = self.pathmanager.history

        self._history.reset_index(drop = True).to_csv(filepath, sep = "\t", index = False)

    def _load_history(self: _HistoryProtocol) -> pd.DataFrame:
        filepath = self.pathmanager.history
        if filepath.exists():
           return pd.read_csv(filepath, delimiter="\t")
        else:
            return pd.DataFrame(columns=["name", "expression"])
        
    def _clear_history(self: _HistoryProtocol) -> None:
        self._history = pd.DataFrame(columns=["name", "expression"])
        filepath = self.pathmanager.history
        if filepath.exists():
            filepath.unlink()

    def _update_history_panel(self: _HistoryProtocol) -> None:
        num_expressions = len(self._history)
        buttons = []

        # Remove old buttons
        for btn in self.history_buttons:
            btn.destroy()

        self.history_buttons.clear()

        # Create new buttons
        for n in range(min(num_expressions, 9)):

            idx = n + 1

            expression_name = str(self._history.loc[n, "name"])
            expression      = str(self._history.loc[n, "expression"])

            btn_n = customtkinter.CTkButton(
                self.panel_right_bottom,
                text=f"{idx}. {expression_name}",
                command=lambda nm=expression_name, expr=expression: self.insert_from_history(nm, expr),
                fg_color=self.color_palette.frame,
                hover_color=self.color_palette.frame_edge
            )

            self.history_buttons.append(btn_n)

        # Pack buttons
        for btn in self.history_buttons:
            btn.pack(
                fill="y",
                padx=2,
                pady=2
            )
