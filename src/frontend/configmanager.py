import tkinter as tk

class ConfigManagerMixin:

    root: tk.Tk

    def _set_cfg(self):
        self.title          = 'MATHVEC'

        self.window_height  = 400
        self.window_width   = 1000
        self.window_y_offset= 300
        self.right_panel_width = 100

    def manage_cfg(self):
        self._set_cfg()
        self.root.title(self.title)
        screen_width    = self.root.winfo_screenwidth()
        screen_height   = self.root.winfo_screenheight()        

        center_x = int(screen_width / 2 - self.window_width /2)
        center_y = int(screen_height/2 - self.window_height / 2 - self.window_y_offset)

        # set the position of the window to the center of the screen
        self.root.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')    

        self.root.resizable(False, False)         