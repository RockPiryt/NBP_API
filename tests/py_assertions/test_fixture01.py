import pytest

@pytest.fixture
def setup_city_list():
    print("\n in fixtures \n")
    city = ["Warsaw", "Berlin", "Paris", "Dublin", "London"]
    return city

def test_getItem(setup_city_list):
    print(setup_city_list[0:2])
    assert setup_city_list[0] == "Warsaw"
    assert setup_city_list[::2] == ["Warsaw", "Paris", "London"]

def myReverse(c_list):
    c_list.reverse()
    return c_list

def test_reverselist(setup_city_list):
    assert setup_city_list[::-1] == myReverse(setup_city_list)