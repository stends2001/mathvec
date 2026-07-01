from pathlib import Path

class PathNotFound(Exception):

    def __init__(self, pathname: str, path: Path):
        msg = f'path {pathname} not found at {path}'
        super().__init__(msg)

class PathManager:
    def __init__(self):
        self.project = Path(__file__).parents[2]
        self.src     = self.project / 'src'
        self.assets  = self.project / 'assets'
        self.output  = self.project / 'output'        

        self._assert_path_integrity()

    def _assert_path_integrity(self):
        path: Path 
        for pathname, path in vars(self).items():
            if not path.exists():
                raise PathNotFound(pathname, path)
