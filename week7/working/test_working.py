from working import convert
import pytest

def test_regular_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_midnight_and_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_with_minutes():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert convert("5:15 AM to 9:45 PM") == "05:15 to 21:45"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
