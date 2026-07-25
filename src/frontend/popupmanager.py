import tkinter as tk
import customtkinter
from tkinter import messagebox
from typing import Literal

class PopUpManagerMixin:
    """
    Mixin class to MathVecApp
    Manages pop ups

    ...

    See Also
    --------
    For more information, see main class MathVecApp
    """

    def popup_latex_issue(self, msg: str):
        messagebox.showwarning("LaTeX issue", f'{msg} Some functionality may be compromised.')

    def popup_button_unavailable(self, button_label: str):
        messagebox.showerror("Unavailable", f'{button_label} is unavailable since LaTeX issues were found.')

    def popup_figure_saved(self, path: str):
        messagebox.showinfo("Saved", f'figure saved in\n{path}')

    def popup_path_adjusted(self, path: str):
        messagebox.showinfo("Directory set", f'Directory changed to\n{path}')

    def popup_empty_field(self, field: Literal['Expression','Name'], func: Literal['VIEW','SAVE']):
        messagebox.showwarning("Empty field", f"Empty '{field}' field: could not {func}.")

    def pop_empty_expression_name(self, func: str):
        messagebox.showwarning("Empty field", f"Empty 'Name' field: could not {func}.")