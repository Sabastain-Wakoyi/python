from CS50Name import hello


def test_default():
    assert hello("David") == "hello, David"


def test_argument():
    assert hello() == "hello, David"
