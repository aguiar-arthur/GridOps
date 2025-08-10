"""
Tests for GridOps core functionality.
"""

from gridops.core import get_one
from gridops import get_one as imported_get_one


def test_get_one():
    """Test that get_one returns 1."""
    assert get_one() == 1


def test_get_one_from_package():
    """Test that get_one is available from the main package."""
    assert imported_get_one() == 1
