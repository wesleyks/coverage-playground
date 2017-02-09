from src import foo


def test_bar():
    assert foo.bar(1) == 2


def test_bark():
    assert foo.bar(3) == 6
    assert foo.bar(4) == 8
    assert foo.bar(5) == 10
