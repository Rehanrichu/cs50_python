from plates import is_valid

# Valid cases
def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("GO") == True  # shortest valid

# Too short or long
def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

# Beginning with non-letters (this is what check50 looks for!)
def test_starts_with_nonletters():
    assert is_valid("50CS") == False
    assert is_valid("1CS50") == False
    assert is_valid("5CS50") == False
    assert is_valid("123ABC") == False

# Number placement rules
def test_number_rules():
    assert is_valid("CS05") == False   # leading zero
    assert is_valid("CS50P") == False  # letter after number
    assert is_valid("CS500") == True   # valid all digits at end

# Invalid characters
def test_invalid_chars():
    assert is_valid("CS 50") == False
    assert is_valid("CS.50") == False
    assert is_valid("CS@50") == False

