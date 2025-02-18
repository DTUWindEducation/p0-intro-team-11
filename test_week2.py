"""Test your functions from Week 2 assignment.
"""
import functions_Tudor as fxn


def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect



def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    # given
    length = 145  # test input to function
    # when
    fxn.goldilocks(length)  # call the function
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Just right!\n'  # check that the output was what we expect

    # Test for too small
    length = 135
    fxn.goldilocks(length)
    captured = capsys.readouterr()
    assert captured.out == 'Too small!\n'

    # Test for too large
    length = 155
    fxn.goldilocks(length)
    captured = capsys.readouterr()
    assert captured.out == 'Too large!\n'


def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    # Test for max_value less than 1
    max_value = 0
    assert fxn.fibonacci_stop(max_value) == []

    # Test for max_value equal to 1
    max_value = 1
    assert fxn.fibonacci_stop(max_value) == [1, 1]

    # Test for max_value equal to 2
    max_value = 2
    assert fxn.fibonacci_stop(max_value) == [1, 1, 2]

    # Test for max_value equal to 10
    max_value = 10
    assert fxn.fibonacci_stop(max_value) == [1, 1, 2, 3, 5, 8]

    # Test for max_value equal to 21
    max_value = 21
    assert fxn.fibonacci_stop(max_value) == [1, 1, 2, 3, 5, 8, 13, 21]


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # Test case 1: All values within range and status is normal
    x = [10, 20, 30, 40]
    status = [0, 0, 0, 0]
    expected = [10, 20, 30, 40]
    assert fxn.clean_pitch(x, status) == expected

    # Test case 2: Some values out of range and status is malfunctioning
    x = [10, 100, 30, -10]
    status = [0, 1, 0, 1]
    expected = [10, -999, 30, -999]
    assert fxn.clean_pitch(x, status) == expected

    # Test case 3: All values out of range but status is normal
    x = [100, 110, -10, -20]
    status = [0, 0, 0, 0]
    expected = [100, 110, -10, -20]
    assert fxn.clean_pitch(x, status) == expected

    # Test case 4: Mixed values and statuses
    x = [10, 20, 150, 200]
    status = [0, 1, 1, 1]
    expected = [10, 20, -999, -999]
    assert fxn.clean_pitch(x, status) == expected

    # Test case 5: Empty lists
    x = []
    status = []
    expected = []
    assert fxn.clean_pitch(x, status) == expected
