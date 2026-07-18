import tkinter as tk
import customtkinter
import yaml
from typing import Dict, Any, TYPE_CHECKING
from .colorpalette import ColorPalette

if TYPE_CHECKING:
    from ..backend import PathManager

class ConfigManagerMixin:
    """
    Mixin class to MathVecApp
    Manages config

    Sets attributes from .yaml file, path to which 
    is extracted from self.pathmanager.config

    See Also
    --------
    For more information, see main class MathVecApp
    """
    root:           customtkinter.CTk
    pathmanager:    'PathManager'

    def set_config(self):
        config                  = self._load_config()

        self.title              = config['title']

        self.window_height      = config['window_height']     
        self.window_width       = config['window_width']      
        self.window_y_offset    = config['window_y_offset']   
        self.right_panel_width  = config['right_panel_width'] 

        self.textbox_width      = config['textbox_width']     
        self.textbox_height     = config['textbox_height']            

        self.canvas_width       = config['canvas_width']      
        self.canvas_height      = config['canvas_height']     
        self.canvas_textsize    = config['canvas_textsize']   

        self.figure_height      = config['figure_height']     
        self.figure_width       = config['figure_width']      
        self.figure_dpi         = config['figure_dpi']              
        self.figure_textsize    = config['figure_textsize']   

        self.theme              = config['theme']

        theme_vars              = self._load_theme_colors()
        self.color_palette      = ColorPalette(**theme_vars[self.theme])

    def _load_config(self) -> Dict[str, Any]:
        """loads config.yaml"""
        filepath = self.pathmanager.config

        with open(filepath, "r") as f:
            return yaml.safe_load(f)       
        
    def _load_theme_colors(self) -> Dict[str, Any]:
        filepath = self.pathmanager.assets / 'themes.yaml'

        with open(filepath, "r") as f:
            return yaml.safe_load(f)            