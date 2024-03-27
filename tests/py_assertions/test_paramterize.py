import pytest

@pytest.mark.parametrize("my_input", [94,52,35,67])
def test_param01(my_input):
    assert my_input > 50