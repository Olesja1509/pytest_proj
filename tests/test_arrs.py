from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, False) == 2
    assert arrs.get([], -2, False) == False
    assert arrs.get([1, 2, 3], 5, False) == False


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -2) == [2, 3]

