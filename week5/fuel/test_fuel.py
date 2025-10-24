from fuel import convert, gauge
import pytest

# --- Tests for convert() ---
def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_convert_invalid_value():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("3/2")  # X > Y not allowed

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

# --- Tests for gauge() ---
def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
