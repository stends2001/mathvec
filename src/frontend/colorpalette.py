from dataclasses import dataclass

@dataclass 
class ColorPalette:
  frame:            str
  text:             str
  button_text:      str
  button_text_unvavail: str
  input_edge:       str
  
  button:           str
  button_hover:     str
  button_unavail:   str
  
  canvas_bg:        str
  scrollbar:        str

  history_text:   str
  history_entry_hover:  str   
  history_entry_remove:  str  