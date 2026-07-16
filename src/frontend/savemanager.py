from typing import Literal, assert_never
from matplotlib.figure import Figure
from pathlib import Path

from ..exceptions import EmtpyExpressionName, EmptyExpressionError

class SaveManagerMixin:
    """
    Mixin class to MathVecApp
    Manages saving of figures

    The necessary properties that live on the main class need
    to be defined here by stubs.

    Methods
    -------
    - `_savefig()`
    - `_resolve_filename()`

    See Also
    --------
    For more information, see main class MathVecApp
    """
    output_dir: Path

    @property
    def figure(self) -> Figure:
        """stub. actually defined on ViewerManagerMixin class"""
        raise NotImplementedError
    
    @property 
    def expression_input(self) -> str:
        """stub. actually defined on main class"""
        raise NotImplementedError
    
    @property 
    def expression_name(self) -> str:
        """stub. actually defined on main class"""        
        raise NotImplementedError
    
    def _savefig(self, extension: Literal['svg','png']) -> Path:
        """saves figure under resolved filename with inputted extension. Returns path"""
        if self.expression_input == '':
            raise EmptyExpressionError('SAVE')
        
        if self.expression_name == '':
            raise EmtpyExpressionName()

        filename = f"{self.expression_name}.{extension}"
        path     = self.output_dir / filename
        path     = self._resolve_filename(path)

        fig = self.figure

        match extension:
            case 'svg':
                fig.savefig(
                    path, format='svg', 
                    dpi=self.figure.dpi,
                    transparent=True,
                    bbox_inches='tight', 
                    pad_inches=0.05,
                )

            case 'png':
                fig.savefig(
                    path, 
                    dpi=self.figure.dpi,
                    bbox_inches='tight', 
                    pad_inches=0.05,
                )

            case _:
                assert_never(extension)

        return path    

    def _resolve_filename(self, path: Path) -> Path:
        """
        if filename already exists, gets the first integer in filename as "(idx)" that doesn't exist
        otherwise, it's returned unchanged
        """
        if not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
        
        ext         = path.suffix
        filename_cp = path.stem
        idx         = 0

        path_cp     = path.parent / f'{filename_cp}{ext}'
        
        while path_cp.exists():
            idx += 1
            path_cp     = path.parent / f'{filename_cp}({idx}){ext}'

        return path_cp