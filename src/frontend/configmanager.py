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
    config:         dict[str, Any] | None

    def set_config(self):

        if self.config is None:
            self.config             = self._load_config()

        self.title              = self.config['title']

        self.window_height      = self.config['window_height']     
        self.window_width       = self.config['window_width']      
        self.right_panel_width  = self.config['right_panel_width'] 

        self.textbox_width      = self.config['textbox_width']     
        self.textbox_height     = self.config['textbox_height']            

        self.canvas_width       = self.config['canvas_width']      
        self.canvas_height      = self.config['canvas_height']     
        self.canvas_textsize_min= self.config['canvas_textsize_min']   
        self.canvas_textsize_max= self.config['canvas_textsize_max']           

        self.figure_height      = self.config['figure_height']     
        self.figure_width       = self.config['figure_width']      
        self.figure_dpi         = self.config['figure_dpi']              
        self.figure_textsize    = self.config['figure_textsize']   

        self.theme              = self.config['theme']

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