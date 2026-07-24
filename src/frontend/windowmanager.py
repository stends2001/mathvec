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

    def _setup_window(self):
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

    def _configure_main(self):
        """divides window into two panels: left vs right"""

        # two columns: a large one with input and latex preview, and one on the right for buttons
        self.root.grid_columnconfigure(0, weight = 1) # grows
        self.root.grid_columnconfigure(1, weight = 0) # fixed
        self.root.grid_rowconfigure(0, weight=1)

        self.panel_left  = customtkinter.CTkFrame(self.root, fg_color = self.color_palette.frame, border_color= self.color_palette.frame_edge)
        self.panel_right = customtkinter.CTkFrame(self.root, fg_color = self.color_palette.frame, border_color= self.color_palette.frame_edge)
        
        self.panel_left.grid(row = 0,  column = 0, sticky = 'nsew')
        self.panel_right.grid(row = 0, column = 1, sticky = 'ns')        

    def _configure_sub(self):
        """divides left and right panels, each, into top and bottom"""        

        # ========= right main - panel ========== #
        self.panel_right.grid_rowconfigure(0, weight=0)
        self.panel_right.grid_rowconfigure(1, weight=1)
        self.panel_right.grid_columnconfigure(0, weight=1)
        self.panel_right.grid_propagate(True)

        # right_top: button panel
        self.panel_right_top = customtkinter.CTkFrame(self.panel_right, fg_color=self.color_palette.frame, border_color= 'white', border_width=2) # border color doesn't show
        self.panel_right_top.grid(row=0, column=0, sticky="nsew")

        # right_bottom: history panel
        self.panel_right_bottom = customtkinter.CTkFrame(self.panel_right, fg_color=self.color_palette.frame, border_color = 'white', border_width=2)
        self.panel_right_bottom.grid(row=1, column=0, sticky="nsew")

        # ========= left main - panel ========== #
        self.panel_left.grid_rowconfigure(0, weight=1)
        self.panel_left.grid_rowconfigure(1, weight=8)
        self.panel_left.grid_columnconfigure(0, weight=1)
        self.panel_right.grid_propagate(True)        

        self.panel_left_top = customtkinter.CTkFrame(self.panel_left, fg_color=self.color_palette.frame, border_color = 'white', border_width=2)
        self.panel_left_top.grid(row=0, column=0, sticky="nsew")
        self.panel_left_top.grid_rowconfigure(0, weight=0)  # name row
        self.panel_left_top.grid_rowconfigure(1, weight=1)  # expression row        

        # left_bottom: canvas panel
        self.panel_left_bottom = customtkinter.CTkFrame(self.panel_left, fg_color=self.color_palette.frame, border_color = 'white', border_width=2)
        self.panel_left_bottom.grid(row=1, column=0, sticky="nsew")      

    def _configure_subsub(self):
        """Divides left top panel into two rows: name and expression"""

        # Configure parent panel
        self.panel_left_top.grid_rowconfigure(0, weight=0)  # name row stays compact
        self.panel_left_top.grid_rowconfigure(1, weight=1)  # expression row expands
        self.panel_left_top.grid_columnconfigure(0, weight=1)
        self.panel_left_top.grid_propagate(True)

        # ======== panel expression name ========== #
        self.panel_expression_name = customtkinter.CTkFrame(
            self.panel_left_top,
            fg_color=self.color_palette.frame,
        )

        self.expression_name_lbl = customtkinter.CTkLabel(
            self.panel_expression_name,
            text="Name:",
            fg_color=self.color_palette.frame,
            text_color=self.color_palette.text
        )

        self.naming = customtkinter.CTkEntry(
            self.panel_expression_name,
            fg_color=self.color_palette.frame,
            border_color=self.color_palette.input_edge,
            text_color=self.color_palette.text
        )

        # Make entry column expand
        self.panel_expression_name.grid_columnconfigure(1, weight=1)

        # Place widgets
        self.expression_name_lbl.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.naming.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )

        self.naming.insert(0, self.default_name)

        # Place frame
        self.panel_expression_name.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="ew"
        )


        # ======== panel expression input ========= #
        self.panel_expression_input = customtkinter.CTkFrame(
            self.panel_left_top,
            fg_color=self.color_palette.frame,
        )

        self.expression_inp_lbl = customtkinter.CTkLabel(
            self.panel_expression_input,
            text="Expression:",
            fg_color=self.color_palette.frame,
            text_color=self.color_palette.text
        )

        self.entry = customtkinter.CTkTextbox(
            self.panel_expression_input,
            width=self.textbox_width,
            height=self.textbox_height,
            fg_color=self.color_palette.frame,
            border_color=self.color_palette.input_edge,
            border_width=2,
            text_color=self.color_palette.text
        )

        # Allow textbox area to expand
        self.panel_expression_input.grid_columnconfigure(1, weight=1)
        self.panel_expression_input.grid_rowconfigure(0, weight=1)

        # Place widgets
        self.expression_inp_lbl.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="nw"
        )

        self.entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky="nsew"
        )

        self.entry.insert("1.0", self.default_input)

        # Place frame
        self.panel_expression_input.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

    def _configure_canvas(self):
        self.canvas_plane = customtkinter.CTkCanvas(self.panel_left_bottom, 
                                                    # width=self.canvas_width, 
                                                    # height=self.canvas_height, 
                                                    bg=self.color_palette.frame,
                                                    # highlightthickness=1,
                                                    # highlightbackground="white",
                                                    # highlightcolor='white'                                                
                                                    )
        self.canvas_plane.pack(fill="both", expand=True)      

    def configure_panels(self):
        """window division into planes"""
        self._setup_window()

        # first division: 
        # left: input panel & canvas panel
        # right: button panel & history panel
        self._configure_main()
        
        # right panel is divided into right_top and right_bottom
        # right_top: button panel
        # right_bottom: history panel

        # left panel is divided into left_top and left_bottom
        # left_top: input_panel
        # left_bottom: canvas panel
        self._configure_sub()

        self._configure_subsub()
        self._configure_canvas()