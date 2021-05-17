import pytest
import builtins
from unittest import mock
import garden_simulator


def test_get_user_info():
    """Does get_user_info() return the user's name and age as a tuple?"""
    with mock.patch("builtins.input", side_effect=["Alice", "27"]):
        assert myproject.get_user_info() == ("Alice", 27)
