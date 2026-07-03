import tkinter as tk
from tkinter import messagebox

class PopUpManagerMixin:
    """
    Mixin class to MathVecApp
    Manages pop ups

    ...

    See Also
    --------
    For more information, see main class MathVecApp
    """
    panel_right: tk.Frame
    root: tk.Tk

    latex_supported:    bool

    def button_unavailable(self, button_label: str):
        messagebox.showerror("Unavailable", f'{button_label} is unavailable since LaTeX installation not found.')

    def figure_saved(self, path: str):
        messagebox.showinfo("Saved", f'figure saved in\n{path}')

    def path_adjusted(self, path: str):
        messagebox.showinfo("Directory set", f'Directory changed to\n{path}')        