from pathlib import Path
import pytest

from src.backend.pathmanager import PathManager, PathNotFound

def make_project_skeleton(root: Path) -> None:
    """create the static dirs/files PathManager expects to already exist"""
    (root / 'src').mkdir()
    (root / 'config').mkdir()
    (root / 'config' / 'config.yaml').touch()
    (root / 'assets').mkdir()

def test_mkdir_creates_output_and_history(tmp_path: Path):
    make_project_skeleton(tmp_path)

    pathmanager = PathManager(project_root=tmp_path)

    assert pathmanager.output.is_dir(), "PathManager didn't create 'output'"
    assert pathmanager.history.parent.is_dir(), "PathManager didn't create 'history'"

def test_missing_src_raises(tmp_path: Path):
    # skeleton without 'src' dir
    (tmp_path / 'config').mkdir()
    (tmp_path / 'config' / 'config.yaml').touch()
    (tmp_path / 'assets').mkdir()

    with pytest.raises(PathNotFound):
        PathManager(project_root=tmp_path)