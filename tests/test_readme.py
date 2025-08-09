import subprocess
from pathlib import Path


def test_readme_has_no_spelling_errors():
    readme = Path(__file__).resolve().parents[1] / 'README.md'
    result = subprocess.run(
        ['codespell', str(readme)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    assert result.returncode == 0, result.stdout
