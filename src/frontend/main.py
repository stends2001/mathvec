import tkinter as tk
from typing import Optional, Literal, Dict, List
from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.figure import Figure
from pathlib import Path
import pandas as pd
import customtkinter
from PIL import ImageTk

from .configmanager import ConfigManagerMixin
from .buttonmanager import ButtonManagerMixin
from .historymanager import HistoryManagerMixin
from .windowmanager import WindowManagerMixin
from .figuremanager import FigureManager
from .savemanager import SaveManagerMixin
from .popupmanager import PopUpManagerMixin
from .colorpalette import ColorPalette

from ..backend import PathManager, has_latex, has_latex_package
from ..exceptions import EmptyExpressionError, EmtpyExpressionName

class MathVecApp(
    ConfigManagerMixin,
    WindowManagerMixin,
    ButtonManagerMixin,
    HistoryManagerMixin,
    FigureManager,
    SaveManagerMixin,
    PopUpManagerMixin
    ):
    
    """
    Main backend class that orchestrates the running of the app by using Mixin classes

    Parameters
    ----------
    None

    Methods 
    -------
    - `run_app()`
    - `reset()`
    - `save()`
    - `set_output_dir()`
    - `expression_input`
    - `expression_name`

    Mixins
    ------
    - ConfigManagerMixin
    - WindowManagerMixin
    - ButtonManagerMixin
    - FigureManager
    - SaveManagerMixin
    """
    _figure:        Figure | None
    _canvas:        ImageTk.PhotoImage | None
    _history:       pd.DataFrame

    color_palette:  ColorPalette
    latex_supported: bool
    
    def __init__(self):

        self.pathmanager= PathManager()
        self._validate_latex()
        self.set_config()     

        self.root       = customtkinter.CTk(fg_color=self.color_palette.frame)
        
        self.default_input: str = ''
        self.default_name:  str = 'equation_1'
        self.output_dir:    Path= self.pathmanager.output

        self.history_buttons: List[customtkinter.CTkButton] = []
                  
        self.configure_panels()   
        self.manage_buttons()     
        self.manage_history()
        self.reset()

        def _on_change():
            self._figure = None
            self._update_canvas()

            print(f'Text now is: {len(self.expression_input)} chars long over {len(self.expression_input.splitlines())} lines.')

        self.entry.bind("<KeyRelease>",  lambda e: _on_change())
        self.naming.bind("<KeyRelease>", lambda e: _on_change())  # name changes affect save filename too           

    def _validate_latex(self):

        latex_packages          = ['amsmath']
        latex_on_path           = has_latex()

        self.latex_supported    = False

        # if latex found, test whether required packages are supported
        if latex_on_path:
            for pkg in latex_packages:
                if not has_latex_package(pkg):
                    self.popup_latex_issue(f'Package {pkg} not found.')
                    break

                self.latex_supported = True
                self._toggle_usetex('on')
                mpl.rcParams["text.latex.preamble"] = fr"\usepackage{{{pkg}}}"

        # if no latex found, popup saying not all funcationality available
        else:
            self.popup_latex_issue('LaTeX installation was not found.')

    def run_app(self):
        """main function to run the app"""
        self.root.mainloop()

    def quit_app(self):
        self._save_history()
        self.root.destroy()

    def change_theme(self):
        print('To be implemented')

    def reset(self):
        """reset everything, with the exception of the output directory"""
        self._figure = None
        self._canvas = None
        self.entry.delete("1.0", "end")
        self.entry.insert("1.0", self.default_input)

        self.naming.delete(0, "end")
        self.naming.insert(0, self.default_name)

        self._update_canvas()           

    def view(self) -> None:
        """preview expression in separate window"""
        if not self.latex_supported:
            self.popup_button_unavailable('VIEW')
            return None
        
        try:
            self._save_to_history(self.expression_name, self.expression_input)
            self.figure
            plt.show()      
            print(f'saving {self.expression_name, self.expression_input}')
            
        
        except EmptyExpressionError as e:
            print(e)

    def clear_history(self):
        self._clear_history()
        self._update_history_panel()

    def insert_from_history(self, name: str, expression_name: str):
        self.reset()
        self.entry.delete("1.0", "end")
        self.entry.insert("1.0", expression_name)

        self.naming.delete(0, "end")
        self.naming.insert(0, name)
        self._update_history_panel()

    def save(self, extension: Literal['svg','png']) -> None:
        """save expression"""
        if not self.latex_supported:
            self.popup_button_unavailable('SAVE')
            return None
        try:         
            path = self._savefig(extension)
            self.popup_figure_saved(str(path))  
            self._save_to_history(self.expression_name, self.expression_input)
        
        except (EmptyExpressionError,  EmtpyExpressionName) as e:
            print(e)

    def set_output_dir(self):
        """interactively adjust output_dir"""
        output_dir = Path(filedialog.askdirectory())

        # if not filled in, will be default
        if output_dir == "":
            output_dir = self.pathmanager.output
        
        self.output_dir = output_dir
        self.popup_path_adjusted(str(self.output_dir))              

    @property 
    def expression_input(self) -> str:
        """entire input expression"""
        return self.entry.get("1.0", "end-1c")
    
    @property 
    def expression_name(self) -> str:
        """cleaned name"""
        return self.naming.get().replace(" ","_")

    def __repr__(self) -> str:
        representation = f"<{self.__class__.__name__}({self.expression_name}: {self.expression_input})>"

        return representation