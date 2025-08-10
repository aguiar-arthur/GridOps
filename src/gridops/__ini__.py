"""
GridOps - A Python library for grid operations.

This package provides utilities and tools for working with grid-based operations.
"""

__version__ = "0.1.0"
__author__ = "Arthur Aguiar"

# Import the main function from core module
from gridops.core import get_one

# Make the main function available at package level
__all__ = [
    "get_one",
    "__version__",
    "__author__",
]
