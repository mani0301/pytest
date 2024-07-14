from Calculator import *
import pytest


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(3, 2) == 1


def test_multi():
    assert multi(2, 3) == 6


def test_div():
    assert div(6, 3) == 2
