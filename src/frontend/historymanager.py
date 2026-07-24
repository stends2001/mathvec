import tkinter as tk
import customtkinter
from typing import Literal, Dict, List, Protocol
import pandas as pd

from .colorpalette import ColorPalette
from ..backend import PathManager

class _HistoryProtocol(Protocol):
    history_list: customtkinter.CTkFrame
    root:               customtkinter.CTk

    latex_supported:    bool
    pathmanager:        PathManager

    color_palette: ColorPalette
    history_buttons: List[customtkinter.CTkFrame]

    _history: pd.DataFrame

    def insert_from_history(self, name: str, expression_name: str) -> None:
        ...

    def manage_history(self) -> None:
        ...

    def _save_to_history(self, name: str, expression: str) -> None:
        ...

    def _save_history(self) -> None:
        ...

    def _load_history(self) -> pd.DataFrame:
        ...

    def _clear_history(self) -> None:
        ... 

    def _update_history_panel(self) -> None:
        ...

    def _remove_from_history(self, name: str) -> None:
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
        self._history = self._load_history()
        self._update_history_panel()

    def _save_to_history(self: _HistoryProtocol, name: str, expression: str):

        # if name is already present, remove
        if name in self._history['name'].unique():
            self._remove_from_history(name)

        self._history.loc[len(self._history)] =  {"name": name, "expression": expression}
        self._update_history_panel()

    def _save_history(self: _HistoryProtocol) -> None:
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

        # Remove old rows
        for row in self.history_buttons:
            row.destroy()

        self.history_buttons.clear()

        # Create new buttons
        for n in range(min(num_expressions, 9)):

            idx = n + 1

            expression_name = str(self._history.loc[n, "name"])
            expression      = str(self._history.loc[n, "expression"])

            # Row container
            row = customtkinter.CTkFrame(
                self.history_list,
                fg_color=self.color_palette.frame
            )

            row.grid_columnconfigure(0, weight=1)

            button_text             = f"{idx}. {expression_name}"
            max_button_textsize     = 23

            if len(button_text) > max_button_textsize:
                button_text = button_text[:max_button_textsize-3]+"..."

            # Main history button
            btn = customtkinter.CTkButton(
                row,
                text=button_text,
                command=lambda nm=expression_name, expr=expression: self.insert_from_history(nm, expr),
                fg_color=self.color_palette.frame,
                hover_color=self.color_palette.frame_edge,
                anchor="w"
            )

            # Delete button
            delete_btn = customtkinter.CTkButton(
                row,
                text="X",
                width=25,
                command=lambda nm=expression_name: self._remove_from_history(nm),
                fg_color=self.color_palette.frame,
                hover_color="red"
            )

            btn.grid(
                row=0,
                column=0,
                sticky="ew",
                padx=(2, 0),
                pady=2
            )

            delete_btn.grid(
                row=0,
                column=1,
                padx=(2, 2),
                pady=2
            )

            self.history_buttons.append(row)

        # Pack rows
        for row in self.history_buttons:
            row.pack(
                fill="x",
                padx=2,
                pady=2
            )
