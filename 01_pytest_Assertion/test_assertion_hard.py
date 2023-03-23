# content of test_assert1.py
a = 5
b = 10
c = 30


def f():
    return 3


def test_function_01():
    assert f() == 3
    print("success")
    assert a == 5
    print("success")
    assert b == 1
    print("success")


def test_function_02():
    assert f() == 4
    print("success")
    assert a == 5
    print("success")
    assert b == 1
    print("success")

# Hard assertion does not runs after assertion failed
# soft assertion runs after assertion failed or passed
