# MATHVEC

This little project is there to make .svgs out of math text.
You can run it by running `runapp.py` in the project root.

## TODO
- tests
- BUG: history keeps duplicating. In addition, the same name appearing newly should remove old entries with that name in history.
- BUG: edge-frame color is not being used
- IMPLEMENT: scroll bar over history
- IMPLEMENT: vertically-extending input frame

## Requirements
Python 3.10+, tkinter (usually a standard library), and a LaTeX distribution (e.g. TeX Live or MiKTeX) available on your PATH. Also note, specifically the following LaTeX packages are used:
- asmath

## User Interface
In the main plane, we have two text fields. The first is **Name** for the name of the expression, by default `equation_1`. The second is the actual **Expression**, which can be any LaTeX math. Comparing to actual LaTeX code, options are fairly limited (only core math and matrices, no equations, etc.) but I aim to extend on that soon. Below that input box, there's the **Canvas**, which shows a preview of the input text (not fully LaTeX but rather matplotlib math style).

On the right plane, there are 5 buttons:
- `CLEAR`: resets the app. everything is removed from memory, except the path. So, if it has been adjusted with the button `SET dir` before, you will still be in that directory.
- `VIEW`: creates a **Figure** in a separate window, that shows proper LaTeX output.
- `SAVE .svg`: saves a figure equivalent to the one seen when pressing `VIEW` in the directory output_path under the name **Name** in `svg` format.
- `SAVE .png`: saves a figure equivalent to the one seen when pressing `VIEW` in the directory output_path under the name **Name** in `png` format.
- `SET dir`: adjusts output_dir.

## Source code

### Backend
My backend only contains a global pathmanager. It is solely used to extracts paths from.

### Frontend
The main class that brings everything together, is found in `src/frontend/main.py`. This class has some mixin classes, which are found in the other `.py` files. 