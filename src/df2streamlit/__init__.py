from pathlib import Path

import pkg_resources
import toml

from .core import hmm


def get_version():
    try:
        return pkg_resources.get_distribution("wavyts").version
    except Exception:
        path = Path(__file__).resolve().parents[2] / "pyproject.toml"
        pyproject = toml.loads(open(str(path)).read())
        return pyproject["tool"]["poetry"]["version"]


__version__ = get_version()
