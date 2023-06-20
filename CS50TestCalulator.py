# from CS50Calculator import square

# unit test are typically tests for functions that the programmer has written
# the simple test to use is pytest
# def main():
#     test_square()

# using assertion to test your code
# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")

# a kind of testing method for your code
# if square(2) != 4:
#     print("2 squared was not 4")
#
# if square(3) != 9:
#     print("3 squared was not 9")


# if __name__ == "_main_":
#     main()


from CS50Calculator import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0
