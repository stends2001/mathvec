import tkinter as tk
import customtkinter
from typing import Optional, Literal, assert_never, Protocol
from io import BytesIO
from matplotlib.mathtext import MathTextParser
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.axes import Axes
import matplotlib.pyplot as plt

from ..exceptions import EmptyExpressionError
from .colorpalette import ColorPalette

class _FigureProtocol(Protocol):
    canvas_plane:   customtkinter.CTkCanvas

    figure_height:  int 
    figure_width:   int 
    figure_dpi:     int
    figure_textsize:int

    canvas_width:   int 
    canvas_height:  int
    canvas_textsize:int

    _figure:        Optional[Figure]
    _canvas:        Optional[ImageTk.PhotoImage]
    
    color_palette: ColorPalette    

    @property 
    def expression_input(self) -> str:
        ...
    
    @property 
    def expression_name(self) -> str:
        ...

    def _toggle_usetex(self, mode: Literal['on','off']) -> None:
        ...

    def _draw_figure(self) -> Figure:        
        ...

    def _draw_canvas(self) ->  ImageTk.PhotoImage:        
        ...

    def _update_canvas(self) -> None:
        ...

class FigureManager:
    """
    Mixin class to MathVecApp
    Manages figures

    The necessary properties that live on the main class need
    to be defined here by stubs.

    Methods
    -------
    - `_toggle_usetex()`
    - `_draw_figure()`
    - `_draw_canvas()`
    - `_update_canvas()`

    See Also
    --------
    For more information, see main class MathVecApp
    """

    @property
    def figure(self: _FigureProtocol) -> Figure:
        """return figure"""        
        if self._figure is None:
            return self._draw_figure()
        return self._figure

    def _toggle_usetex(self: _FigureProtocol, mode: Literal['on','off']) -> None:
        """turn or or off the usetex matplotlib mode"""
        match mode:
            case 'on':
                plt.rcParams["text.usetex"] = True

            case 'off':
                plt.rcParams["text.usetex"] = False          

            case _:
                assert_never(mode)      

    def _draw_figure(self: _FigureProtocol) -> Figure:
        """
        Draw figure: that is, an image of proper latex code. 
        To be viewed or saved. Both returned, and stored in `self._figure`
        """
        if self.expression_input == '':
            raise EmptyExpressionError('VIEW')

        self._toggle_usetex('on')        

        fig, ax = plt.subplots(figsize=(self.figure_width, self.figure_height))

        input_text          = self.expression_input
        expression_latex    = " ".join(input_text.splitlines())   # Remove literal newlines

        ax.text(
            0.5, 0.5,
            f"${expression_latex}$",
            fontsize=self.figure_textsize,
            ha="center",
            va="center",
        )

        ax.axis("off")
        plt.tight_layout()

        fig.canvas.manager.set_window_title(self.expression_name) # type: ignore

        self._figure = fig
        return fig

    def _draw_canvas(self: _FigureProtocol) ->  ImageTk.PhotoImage:
        """
        Draw canvas: that is, an image of previewing matplotlib math.
        """
        input_text = self.expression_input
        
        fig     = Figure(figsize=(self.figure_width, self.figure_height), 
                         dpi=self.figure_dpi,
                        facecolor=self.color_palette.canvas_bg)
        
        ax: Axes= fig.add_axes([0, 0, 1, 1]) # type: ignore
        ax.axis("off")
        ax.set_facecolor(self.color_palette.canvas_bg)

        parser = MathTextParser("agg")

        try:
            parser.parse(f"${input_text}$")
            text = f"${input_text}$"
        except ValueError:
            text = input_text

        ax.text(
            0.05,
            0.5,
            text,
            fontsize=self.canvas_textsize,
            va="center",
            color=self.color_palette.text
        )


        buf = BytesIO()
        FigureCanvasAgg(fig).print_png(buf)

        buf.seek(0)
        img = Image.open(buf)

        return ImageTk.PhotoImage(img)

    def _update_canvas(self: _FigureProtocol) -> None:
        """update canvas plane with a canvas"""
        
        self._toggle_usetex('off')
        self._canvas_image = self._draw_canvas()

        self.canvas_plane.delete("all")
        self.canvas_plane.create_image(
            0, 0,
            anchor="nw",
            image=self._canvas_image
        )

        self._toggle_usetex('on')