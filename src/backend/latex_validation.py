import shutil
import subprocess
import tempfile
from pathlib import Path

def has_latex() -> bool:
    """Return True if the 'latex' executable is available."""
    return shutil.which("latex") is not None


def has_latex_package(package: str) -> bool:
    """
    Return True if the given LaTeX package can be loaded.

    Returns False if LaTeX is not installed or if compilation fails.
    """
    if not has_latex():
        return False


    tex = rf"""\documentclass{{article}}
\usepackage{{{package}}}
\begin{{document}}
Test
\end{{document}}
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        texfile = Path(tmpdir) / "test.tex"
        texfile.write_text(tex, encoding="utf-8")

        result = subprocess.run(
            [
                "latex",
                "-halt-on-error",
                "-interaction=nonstopmode",
                texfile.name,
            ],
            cwd=tmpdir,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    return result.returncode == 0