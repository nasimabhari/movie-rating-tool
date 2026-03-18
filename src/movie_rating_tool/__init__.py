"""
Movie Rating Tool package.
Demonstrates clean Python packaging + OOP.
"""

from .models import Movie, RatingsManager
from .cli import run_cli

__version__ = "0.5.0"
__all__ = ["Movie", "RatingsManager", "run_cli"]