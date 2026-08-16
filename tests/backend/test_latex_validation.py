from src.backend.latex_validation import has_latex_package

def test_mkdir_creates_output_and_history():

    assert has_latex_package('amsmath'), "No 'amsmath' LaTeX-package found."
    assert not has_latex_package('amsmat'),  "LaTeX-package 'amsmat' not supposed to exist."
