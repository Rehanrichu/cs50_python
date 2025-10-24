from um import count
import pytest

def test_single_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1

def test_multiple_um():
    assert count("Um, thanks, um...") == 2
    assert count("um um um") == 3

def test_no_um():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("album") == 0

def test_case_insensitive():
    assert count("UM um Um uM") == 4

def test_with_punctuation():
    assert count("um!") == 1
    assert count("Um.") == 1
    assert count("um, um.") == 2
