import tkinter as tk

class WindowManagerMixin:

    root: tk.Tk
    right_panel_width: int

    # WINDOW - MANAGER - MIXIN
    def configure_window(self):
        
        # two columns: a large one with input and latex preview, and one on the right for buttons
        self.root.grid_columnconfigure(0, weight = 1) # grows
        self.root.grid_columnconfigure(1, weight = 0) # fixed

        self.panel_left = tk.Frame(self.root)
        self.panel_left.grid(row = 0, column = 0, sticky = 'nsew')

        self.panel_right = tk.Frame(self.root, width = self.right_panel_width, bg = 'lightgray')
        self.panel_right.grid(row = 0, column = 1, sticky = 'ns')
        self.panel_right.grid_columnconfigure(0, weight=1)        
        self.panel_right.grid_propagate(False)

        self.root.grid_rowconfigure(0, weight = 1)