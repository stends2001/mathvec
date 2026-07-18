from dataclasses import dataclass

@dataclass 
class ColorPalette:
  frame:            str
  frame_edge:       str

  text:             str
  input_edge:       str
  
  button:           str
  button_hover:     str
  button_unavail:   str
  
  canvas_bg:        str