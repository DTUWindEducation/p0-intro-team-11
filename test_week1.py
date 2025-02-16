"""Check whether the files for Week 1 are present.

We will cover the anatomy of a test (given/when/then) in Week 2.
"""
from pathlib import Path


def test_gitanswers_exists():
    """Verify that the file 'GitAnswers.md' exists"""
    # given
    filename = 'GitAnswers.md'  # the file must have this name
    # when
    p = Path(filename)  # create a pathlib.Path object, which has useful methods
    is_file = p.is_file()  # get True or False depending on if file exists
    # then
    assert is_file  # throw an error if the file doesn't exist


def test_gitanswers_notempty():
    """Verify that the file 'GitAnswers.md' is not empty"""
    # given
    filename = 'GitAnswers.md'  # the file must have this name
    # when
    p = Path(filename)  # create a pathlib.Path object, which has useful methods
    file_size = p.stat().st_size  # get size of file
    # then
    assert file_size > 0  # throw an error if file size is 0


def test_preclass_exists():
    """Verify that folder preclass_assignment exists."""
    # given
    foldername = 'preclass_assignment'  # name of folder
    # when
    p = Path(foldername)  # create a pathlib.Path object, which has useful methods
    is_dir = p.is_dir()  # get True or False depending on if folder exists
    # then
    assert is_dir  # throw an error if the folder doesn't exist


def test_preclass_notempty():
    """Verify that folder preclass_assignment is non-empty."""
    # given
    foldername = 'preclass_assignment'  # name of folder
    # when
    p = Path(foldername)  # create a pathlib.Path object, which has useful methods
    contents = list(p.glob('*.py'))  # get list of all py files
    # then
    assert len(contents) > 0  # throw error if list is empty (length 0)
