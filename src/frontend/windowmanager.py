import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..backend import PathManager

class WindowManagerMixin:
    """
    Mixin class to MathVecApp
    Manages the window and the division into planes.

    See Also
    --------
    For more information, see main class MathVecApp
    """
    root:               tk.Tk
    pathmanager:        'PathManager'
    right_panel_width:  int
    default_name:       str
    default_input:      str

    title:              str

    window_width:       int
    window_height:      int
    window_y_offset:    int

    textbox_width:      int 
    textbox_height:     int

    canvas_width:       int 
    canvas_height:      int

    def _setup_windows(self):
        """initial window setup"""
        self.root.title(self.title)
        screen_width    = self.root.winfo_screenwidth()
        screen_height   = self.root.winfo_screenheight()        

        center_x = int(screen_width / 2 - self.window_width /2)
        center_y = int(screen_height/2 - self.window_height / 2 - self.window_y_offset)

        # set the position of the window to the center of the screen
        self.root.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')    
        self.root.resizable(False, False)         
        self.root.iconbitmap(self.pathmanager.assets / 'logo.ico') # type: ignore

    def configure_window(self):
        """window division into planes"""
        self._setup_windows()
        
        # two columns: a large one with input and latex preview, and one on the right for buttons
        self.root.grid_columnconfigure(0, weight = 1) # grows
        self.root.grid_columnconfigure(1, weight = 0) # fixed

        self.panel_left = tk.Frame(self.root)
        self.panel_left.grid(row = 0, column = 0, sticky = 'nsew')

        self.panel_right = tk.Frame(self.root, width = self.right_panel_width, bg = 'lightgray')
        self.panel_right.grid(row = 0, column = 1, sticky = 'ns')
        self.panel_right.grid_columnconfigure(0, weight=1)        
        self.panel_right.grid_propagate(False)

        # Input 1 row
        row1 = tk.Frame(self.panel_left)
        row1.pack(fill="x", padx=2, pady=10)
        tk.Label(row1, text="Name:        ").pack(side="left", padx=(0, 5))

        self.naming = tk.Entry(row1, width=50)
        self.naming.insert(0, self.default_name)
        self.naming.pack(side="left", fill="x", expand=True)

        # Input 2 row
        row2 = tk.Frame(self.panel_left)
        row2.pack(fill="x", padx=2, pady=10)
        tk.Label(row2, text="Expression:").pack(side="left", padx=(0, 5))

        self.entry = tk.Text(row2, width=self.textbox_width, height = self.textbox_height)
        self.entry.insert('1.0', self.default_input)
        self.entry.pack(side="left", fill="x", expand=True)

        self.canvas_plane = tk.Canvas(self.panel_left, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas_plane.pack(fill="both", expand=True)        

        self.root.grid_rowconfigure(0, weight = 1)