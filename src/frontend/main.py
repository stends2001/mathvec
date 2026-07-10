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
from .popupmanager import PopUpManagerMixin

from ..backend import PathManager, is_latex_found, require_latex_package

class MathVecApp(
    ConfigManagerMixin,
    WindowManagerMixin,
    ButtonManagerMixin,
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
    _figure: Optional[Figure]

    def __init__(self):
        self.latex_supported = is_latex_found()

        if self.latex_supported:
            require_latex_package('amsmath')
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

        def _on_change():
            self._figure = None   # invalidate cached VIEW/SAVE figure
            self._update_canvas()

        self.entry.bind("<KeyRelease>", lambda e: _on_change())
        self.naming.bind("<KeyRelease>", lambda e: _on_change())  # name changes affect save filename too           

    def run_app(self):
        """main function to run the app"""
        self.root.mainloop()

    def quit_app(self):
        self.root.destroy()          # or self.root.destroy()

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
            self.button_unavailable('VIEW')
            return None

        self.figure
        plt.show()        

    def save(self, extension: Literal['svg','png']) -> None:
        """save expression"""
        if not self.latex_supported:
            self.button_unavailable('SAVE')
            return None
                
        path = self._savefig(extension)
        self.figure_saved(str(path))    

    def set_output_dir(self):
        """interactively adjust output_dir"""
        self.output_dir = Path(filedialog.askdirectory())
        self.path_adjusted(str(self.output_dir))              

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