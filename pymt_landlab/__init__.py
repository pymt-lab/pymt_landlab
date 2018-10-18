#! /usr/bin/env python

from .bmi import OverlandFlow, Flexure

__all__ = ["OverlandFlow", "Flexure"]

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
