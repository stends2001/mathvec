from pathlib import Path

class PathNotFound(Exception):

    def __init__(self, pathname: str, path: Path):
        msg = f'Path {pathname} not found at {path}'
        super().__init__(msg)

class PathManager:
    """
    Path Manager class for the entire project

    Attributes
    ----------
    - `project`
    - `src`
    - `config`
    - `assets`
    - `output`
    """
    def __init__(self):
        self.project = Path(__file__).parents[2]
        self.src     = self.project / 'src'       
        self.config  = self.project / 'config'    
        self.assets  = self.project / 'assets'             
        self.output  = self.project / 'output'

        self._assert_path_existence()

    def _assert_path_existence(self):
        path: Path
        for pathname, path in vars(self).items():
            if not path.exists():
                raise PathNotFound(pathname, path)

