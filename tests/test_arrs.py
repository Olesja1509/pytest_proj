from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "Test") == 2
    assert arrs.get([], -2, "Test") == "Test"
    assert arrs.get([1, 2, 3], 5, "Test") == "Test"



def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -2) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3], -5) == [1, 2, 3]
