import shutil
import subprocess

class LaTeXNotFoundError(Exception):
    """raised when no latex found on system"""
    def __init__(self):
        super().__init__('No LaTeX found on this system. Please install LaTeX through https://miktex.org/ (Windows)')

class LaTeXPackageNotFoundError(Exception):
    """raised when a specific package is not found"""
    def __init__(self, package: str):
        super().__init__(f'LaTeX package `{package}` not found. Please install.')

def is_latex_found():
    """Check whether a LaTeX distribution is installed and on PATH."""
    return not shutil.which("latex") is None 

def require_latex_package(package: str) -> None:
    check = f"\\documentclass{{article}}\\usepackage{{{package}}}\\begin{{document}}\\end{{document}}"
    try:
        subprocess.run(["latex", "-halt-on-error"], input=check, text=True,
                        capture_output=True, timeout=10, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired) as e:
        raise LaTeXPackageNotFoundError(package) from e

if __name__ == '__main__':
    require_latex_package('amsmath')
