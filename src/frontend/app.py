import tkinter as tk
from typing import Optional

import matplotlib.pyplot as plt

from .configmanager import ConfigManagerMixin
from .buttonmanager import ButtonManagerMixin
from .windowmanager import WindowManagerMixin
from .previewmanager import PreviewerManagerMixin

from ..pathmanager import PathManager

class App(ConfigManagerMixin,
          WindowManagerMixin,
          ButtonManagerMixin,
          PreviewerManagerMixin,
          ):

    def __init__(self):
        self.root   = tk.Tk()
        self.pathmanager= PathManager()
        self._photo: Optional[tk.PhotoImage] = None

        self.default_input= ''
        self.default_name = 'unnamed_equation'

        self.reset()

    def run_app(self):
        self.root.mainloop()

    def reset(self):
        self._photo = None 
        self.manage_cfg()
        self.configure_window()
        self.manage_buttons()        
        self.render_preview()   

        self.entry.bind("<KeyRelease>", lambda e: self.render_preview())        

    def view(self):
        fig, ax = plt.subplots(figsize=(3, 1))
        plt.rcParams["text.usetex"] = True
    
        fig.canvas.manager.set_window_title(f"{self.naming.get()}") # type: ignore

        ax.text(
            0.5, 0.5,
            rf'${self.entry.get()}$',
            fontsize=20,
            ha='center'
        )

        ax.axis('off')
        plt.tight_layout()

        plt.show()

    def save(self):
        fig, ax = plt.subplots(figsize=(3, 1))
        plt.rcParams["text.usetex"] = True

        dir = self.pathmanager.output
        title = self.naming.get().replace(" ","_")
        expr = self.entry.get()

        ax.text(
            0.5, 0.5,
            rf'${expr}$',
            fontsize=20,
            ha='center',
            va='center'
        )

        ax.axis('off')
        plt.tight_layout()

        filename = f"{title}.png"
        fig.savefig(dir / filename, dpi=300, bbox_inches='tight')

        plt.close(fig)  # important: frees memory