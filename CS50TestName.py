from CS50Name import hello


def test_hello():
    assert hello("David") == "hello, David"
    assert hello() == "hello, David"
