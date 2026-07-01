import tkinter as tk
from typing import Optional, Literal
from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.figure import Figure
from pathlib import Path

from .configmanager import ConfigManagerMixin
from .buttonmanager import ButtonManagerMixin
from .windowmanager import WindowManagerMixin
from .figuremanager import FigureManager
from .savemanager import SaveManagerMixin

from ..backend import PathManager

class MathVecApp(
    ConfigManagerMixin,
    WindowManagerMixin,
    ButtonManagerMixin,
    FigureManager,
    SaveManagerMixin,
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
    _figure: Optional[Figure]

    def __init__(self):
        self._toggle_usetex('on')
        mpl.rcParams["text.latex.preamble"] = r"\usepackage{amsmath}"

        self.root       = tk.Tk()
        self.pathmanager= PathManager()

        self.default_input= ''
        self.default_name = 'equation_1'
        self.output_dir   = self.pathmanager.output

        self.set_config()               
        self.configure_window()   
        self.manage_buttons()     
        self.reset()

    def run_app(self):
        """main function to run the app"""
        self.root.mainloop()

    def reset(self):
        """reset everything, with the exceptino of the output directory"""
        self._figure = None 
        self._canvas = None 
        self._update_canvas()   

        self.entry.bind("<KeyRelease>", lambda e: self._update_canvas())        

    def view(self):
        """preview expression in separate window"""
        self.figure
        plt.show()        

    def save(self, extension: Literal['svg','png']) -> None:
        """save expression"""
        self._savefig(extension)

    def set_output_dir(self):
        """interactively adjust output_dir"""
        self.output_dir = Path(filedialog.askdirectory())

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