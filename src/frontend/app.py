import tkinter as tk

from .configmanager import ConfigManagerMixin
from .buttonmanager import ButtonManagerMixin
from .windowmanager import WindowManagerMixin

from ..backend import PathManager

class App(ConfigManagerMixin,
                     WindowManagerMixin,
                     ButtonManagerMixin):

    def __init__(self):
        self.root   = tk.Tk()
        self.pm     = PathManager()

        # FUNCS
        self.manage_cfg()
        self.configure_window()
        self.manage_buttons()

        # CONSTANTS
        self.name = 'equation X'

    def run_app(self):
        self.root.mainloop()