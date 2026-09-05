import tkinter as tk
import customtkinter
from typing import Literal, Dict, List, Protocol
import pandas as pd

from .colorpalette import ColorPalette
from ..backend import PathManager

class _HistoryProtocol(Protocol):
    """
    Protocol that lists methods in ``MathVecApp``
    as fallback for ``HistoryManagerMixin``.
    """     
    history_list : customtkinter.CTkScrollableFrame
    root : customtkinter.CTk

    latex_supported : bool
    pathmanager : PathManager

    color_palette : ColorPalette
    history_buttons : List[customtkinter.CTkFrame]
    max_history_entries : int

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
    Mixin class to ``MathVecApp`` that manages history.

    Methods
    ------
    ``manage_history()``
        Initiate history: load from file, and update the panel.
    ``_save_to_history()``
        Save an expression to the history.
    ``_save_history()``
        Save history to file.
    ``_load_history()``
        Load history from file.
    ``_clear_history()``
        Clear history.
    ``_update_history_panel()``
        Update history panel below the buttons.
        
    See Also
    --------
    For more information, see main class MathVecApp
    """

    def manage_history(self: _HistoryProtocol):   
        """Initiate history: load from file, and update the panel."""
        self._history = self._load_history()
        self._update_history_panel()

    def _save_to_history(self: _HistoryProtocol, name: str, expression: str):
        """Save an expression to the history."""
        # if name is already present, remove
        if name in self._history['name'].unique():
            self._remove_from_history(name)

        self._history.loc[len(self._history)] =  {"name": name, "expression": expression}
        self._update_history_panel()

    def _save_history(self: _HistoryProtocol) -> None:
        """Save history to file. File is taken from ``PathManager``."""        
        filepath = self.pathmanager.history

        self._history.reset_index(drop = True).to_csv(filepath, sep = "\t", index = False)

    def _load_history(self: _HistoryProtocol) -> pd.DataFrame:
        """Load history from file. File is taken from ``PathManager``."""      
        filepath = self.pathmanager.history
        if filepath.exists():
           return pd.read_csv(filepath, delimiter="\t")
        else:
            return pd.DataFrame(columns=["name", "expression"])
        
    def _clear_history(self: _HistoryProtocol) -> None:
        """Clear history: remove existent file and attached data frame."""
        self._history = pd.DataFrame(columns=["name", "expression"])
        filepath = self.pathmanager.history
        if filepath.exists():
            filepath.unlink()

    def _update_history_panel(self: _HistoryProtocol) -> None:
        """Update history panel based on history data frame."""
        num_expressions = len(self._history)

        # Remove old rows
        for row in self.history_buttons:
            row.destroy()

        self.history_buttons.clear()

        # Create new buttons
        for n in range(min(num_expressions, self.max_history_entries)):

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
            max_button_textsize     = 21

            if len(button_text) > max_button_textsize:
                button_text = button_text[:max_button_textsize-3]+"..."

            # Main history button
            btn = customtkinter.CTkButton(
                row,
                text=button_text,
                command=lambda nm=expression_name, expr=expression: self.insert_from_history(nm, expr),
                fg_color=self.color_palette.frame,
                hover_color=self.color_palette.history_entry_hover,
                text_color = self.color_palette.history_text,
                anchor="w"
            )

            # Delete button
            delete_btn = customtkinter.CTkButton(
                row,
                text="X",
                width=25,
                command=lambda nm=expression_name: self._remove_from_history(nm),
                fg_color=self.color_palette.frame,
                hover_color=self.color_palette.history_entry_remove,
                text_color = self.color_palette.history_text,                
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

        if num_expressions > 6:
            self.history_list._scrollbar.configure(
                button_color= self.color_palette.scrollbar,
                button_hover_color=self.color_palette.scrollbar
            )
        else:
            self.history_list._scrollbar.configure(
                button_color=self.color_palette.frame,                  # matches bg, "invisible"
                button_hover_color=self.color_palette.frame,
            )