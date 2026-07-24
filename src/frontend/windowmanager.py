import tkinter as tk
import customtkinter
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from ..backend import PathManager

from .colorpalette import ColorPalette

class WindowManagerMixin:
    """
    Mixin class to MathVecApp
    Manages the window and the division into planes.

    See Also
    --------
    For more information, see main class MathVecApp
    For a visual aid, see mathvec > docs > window-doc.svg
    """
    root:               customtkinter.CTk
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

    color_palette:      ColorPalette

    def _setup_windows(self):
        """initial window setup"""
        self.root.title(self.title)
        screen_width    = self.root.winfo_screenwidth()
        screen_height   = self.root.winfo_screenheight()        

        center_x = int(screen_width / 2 - self.window_width /2)
        center_y = int(screen_height/2 - self.window_height / 2 - self.window_y_offset)

        # set the position of the window to the center of the screen
        self.root.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')    
        self.root.resizable(True, True)         
        self.root.iconbitmap(self.pathmanager.assets / 'logo.ico') # type: ignore

    def configure_panels(self):
        """window division into planes"""
        self._setup_windows()
        
        # two columns: a large one with input and latex preview, and one on the right for buttons
        self.root.grid_columnconfigure(0, weight = 1) # grows
        self.root.grid_columnconfigure(1, weight = 0) # fixed
        self.root.grid_rowconfigure(0, weight=1)

        # first division: 
        # left: input panel & canvas panel
        # right: button panel & history panel

        self.panel_left  = customtkinter.CTkFrame(self.root, fg_color = self.color_palette.frame, border_color= self.color_palette.frame_edge)
        self.panel_right = customtkinter.CTkFrame(self.root, fg_color = self.color_palette.frame, border_color= self.color_palette.frame_edge)
        
        self.panel_left.grid(row = 0,  column = 0, sticky = 'nsew')
        self.panel_right.grid(row = 0, column = 1, sticky = 'ns')

        # right panel is divided into right_top and right_bottom
        # right_top: button panel
        # right_bottom: history panel
        self.panel_right.grid_rowconfigure(0, weight=1)
        self.panel_right.grid_rowconfigure(1, weight=6)
        self.panel_right.grid_columnconfigure(0, weight=1)
        self.panel_right.grid_propagate(False)

        # right_top: button panel
        self.panel_right_top = customtkinter.CTkFrame(self.panel_right, fg_color=self.color_palette.frame, border_color= 'red') # border color doesn't show
        self.panel_right_top.grid(row=0, column=0, sticky="nsew")

        # right_bottom: history panel
        self.panel_right_bottom = customtkinter.CTkFrame(self.panel_right, fg_color=self.color_palette.frame, border_color = 'red') # border color doesn't show
        self.panel_right_bottom.grid(row=1, column=0, sticky="nsew")

        # left panel is divided into left_top and left_bottom
        # left_top: input_panel
        # left_bottom: canvas panel
        self.panel_left.grid_rowconfigure(0, weight=1)
        self.panel_left.grid_rowconfigure(1, weight=1)
        self.panel_left.grid_columnconfigure(0, weight=1)
        self.panel_right.grid_propagate(True)

        # left_top: input panel
        self.panel_left_top = customtkinter.CTkFrame(self.panel_left, fg_color=self.color_palette.frame, border_color= 'red') # border color doesn't show
        self.panel_left_top.grid(row=0, column=0, sticky="nsew")

        # left_bottom: canvas panel
        self.panel_left_bottom = customtkinter.CTkFrame(self.panel_left, fg_color=self.color_palette.frame, border_color = 'red') # border color doesn't show
        self.panel_left_bottom.grid(row=1, column=0, sticky="nsew")        

        row1 = customtkinter.CTkFrame(self.panel_left_top, fg_color = self.color_palette.frame, border_color= self.color_palette.input_edge)
        row1.pack(fill="x", padx=2, pady=10)
        customtkinter.CTkLabel(row1, text="Name:        ",  fg_color=self.color_palette.frame, text_color=self.color_palette.text).pack(side="left", padx=(0, 5))


        self.naming = customtkinter.CTkEntry(row1, width=50, fg_color = self.color_palette.frame, border_color= self.color_palette.input_edge, text_color= self.color_palette.text)
        self.naming.insert(0, self.default_name)
        self.naming.pack(side="left", fill="x", expand=True)

        # Input 2 row
        row2 = customtkinter.CTkFrame(self.panel_left_top, fg_color = self.color_palette.frame)
        row2.pack(fill="x", padx=2, pady=10)
        customtkinter.CTkLabel(row2, text="Expression:", fg_color=self.color_palette.frame, text_color=self.color_palette.text).pack(side="left", padx=(0, 5))

        self.entry = customtkinter.CTkTextbox(row2, width=self.textbox_width, height=self.textbox_height,
                                    fg_color = self.color_palette.frame,
                                    border_color = self.color_palette.input_edge,
                                    border_width = 2,
                                    text_color = self.color_palette.text)
        self.entry.insert('1.0', self.default_input)
        self.entry.pack(side="left", fill="x", expand=True)

        self.canvas_plane = customtkinter.CTkCanvas(self.panel_left_bottom, 
                                                    # width=self.canvas_width, 
                                                    # height=self.canvas_height, 
                                                    bg=self.color_palette.frame,
                                                    highlightthickness=1,
                                                    highlightbackground=self.color_palette.frame,
                                                    highlightcolor=self.color_palette.frame_edge                                                    
                                                    )
        self.canvas_plane.pack(fill="both", expand=True)        

        self.root.grid_rowconfigure(0, weight = 1)