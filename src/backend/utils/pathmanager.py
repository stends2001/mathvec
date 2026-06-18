from pathlib import Path

class PathManager:
    def __init__(self):
        self.project_dir = Path(__file__).parent.parent.parent
        self.output  = self.project_dir / 'output'
        self.src     = self.project_dir / 'src'

