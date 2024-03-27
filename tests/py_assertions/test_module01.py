import pytest
pytestmark = [pytest.mark.mod1, pytest.mark.mod2]


@pytest.mark.pinia
def test_a1():
    assert 4 > 3


def test_a2():
    assert True  # passed
    print("Ala ma kota")
    assert 1  # passed
    assert 0  # failed
    assert False  # failed


@pytest.mark.pinia
@pytest.mark.stringtest
def test_a3():
    assert "abcde" == "abcde"


@pytest.mark.pinia
def test_a4():
    assert ((3-1)*4/2) == 4.0


def test_a5():
    assert 1 in divmod(9, 5)
    assert 'py' in 'python'
    assert 2 in [1, 2, 4]  # passed
    assert [1, 2] in [1, 2, 4]  # failed
    assert [1, 2] in [[1, 2], [4, 0]]  # passed (sublist in list of list)
