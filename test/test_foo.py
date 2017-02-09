from src import foo


def test_bar():
    assert foo.bar(0) == 0
    assert foo.bar(1) == 2
