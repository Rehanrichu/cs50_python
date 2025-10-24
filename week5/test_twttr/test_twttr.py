from twttr import shorten

def test_lowercase():
    assert shorten("hello") == "hll"

def test_uppercase():
    assert shorten("HELLO") == "HLL"

def test_mixedcase():
    assert shorten("HeLLo WoRLd") == "HLL WRLd"

def test_numbers():
    assert shorten("CS50") == "CS50"

def test_punctuation():
    assert shorten("Hi!") == "H!"

def test_empty():
    assert shorten("") == ""
