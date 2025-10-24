from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_invalid_numbers():
    assert validate("275.3.6.28") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False

def test_invalid_format():
    assert validate("cat") == False
    assert validate("192.168.001.1") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
