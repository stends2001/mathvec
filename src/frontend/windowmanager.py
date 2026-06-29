import tkinter as tk

class WindowManagerMixin:

    root: tk.Tk
    right_panel_width: int
    default_name: str
    default_input: str

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

        self.entry = tk.Entry(row2, width=50)
        self.entry.insert(0, self.default_input)
        self.entry.pack(side="left", fill="x", expand=True)

        self.canvas = tk.Canvas(self.panel_left, width=500, height=150, bg="white")
        self.canvas.pack(fill="both", expand=True)        

        self.root.grid_rowconfigure(0, weight = 1)