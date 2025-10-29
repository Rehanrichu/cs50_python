from datetime import date, timedelta
from seasons import minutes_to_words


def test_one_year():
    birth = date.today() - timedelta(days=365)
    result = minutes_to_words(birth)
    assert "five hundred twenty-five thousand, six hundred minutes" in result.lower()


def test_leap_year():
    birth = date.today() - timedelta(days=366)
    result = minutes_to_words(birth).lower()
    assert (
        "five hundred twenty-seven thousand forty minutes" in result
        or "five hundred twenty-seven thousand, forty minutes" in result
    )



def test_multiple_years():
    birth = date.today() - timedelta(days=730)
    result = minutes_to_words(birth)
    assert "one million, fifty-one thousand, two hundred minutes" in result.lower()


def test_future_date():
    # Future date should result in negative days, handle gracefully
    birth = date.today() + timedelta(days=10)
    result = minutes_to_words(birth)
    assert "minutes" in result.lower()
