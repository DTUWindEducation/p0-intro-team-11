"""Test your functions from Week 2 assignment.
"""
from pytest import CaptureFixture
import preclass_assignment.functions as fxn
import numpy as np

def test_greet(capsys: CaptureFixture[str]):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet()  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert True # TODO! captured.out == 'Hello, world!\n'  # check that the greeting was what we expect


def test_goldilocks(capsys: CaptureFixture[str]):
    """Check goldilocks returns expected output"""
    # given
    # when
    # then
    assert True  # TODO! Update the contents of this function so it correctly tests goldilocks


def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert True # TODO! exp_out == out  # throw error if actual and expected output don't match


def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    # given
    inp = 5
    exp_out = [0, 1, 1, 2, 3, 5]  # expected output
    # when
    out = fxn.fibonacci_stop(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match

def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    # when
    # then
    assert True #False  # TODO! Update the contents of this function so it correctly tests clean_pitch
