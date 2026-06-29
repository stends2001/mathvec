import tkinter as tk
from io import BytesIO

from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

import matplotlib.pyplot as plt
import time

class PreviewerManagerMixin:

    entry: tk.Entry
    canvas: tk.Canvas
    name: tk.Entry

    def render_preview(self):
        expr = self.entry.get()
        plt.rcParams["text.usetex"] = False

        fig = Figure(figsize=(5, 1.5), dpi=100)
        ax = fig.add_axes([0, 0, 1, 1]) # type: ignore
        ax.axis("off")

        if len(expr)>0:

            ax.text(
                0.05,
                0.5,
                rf'${self.entry.get()}$',
                fontsize=24,
                va="center",
            )

        buf = BytesIO()
        FigureCanvasAgg(fig).print_png(buf)

        buf.seek(0)
        img = Image.open(buf)

        self._photo = ImageTk.PhotoImage(img)

        self.canvas.delete("all")
        self.canvas.create_image(
            0, 0,
            anchor="nw",
            image=self._photo
        )
