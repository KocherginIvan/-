import math
def test_filters():
    assert list(filter(lambda s : s%2==0, [1, 2, 3, 4, 5])) == [2, 4]
    list_word = ['python', 'c#', 'java', 'c++']
    assert list(filter(lambda s : s in list_word, ['java', 'classic', 'falk', 'python'])) == ['java', 'python']
def test_filters2():
    list_word = ['python', 'c#', 'java', 'c++']
    assert list(filter(lambda s: s in list_word, ['java', 'classic', 'falk', 'python'])) == ['java', 'python']
def test_map():
    assert list(map(lambda s : s**2, [1, 2, 3, 4, 5])) == [1, 4, 9, 16, 25]
def test_map2():
    assert list(map(len, ['java', 'classic', 'falk', 'python'])) == [4, 7, 4, 6]
def test_sort():
    list_for_sort = [10, 4, 89, 16, 25]
    assert  sorted(list_for_sort) == [4, 10, 16, 25, 89]
    assert sorted(list_for_sort, reverse=True) == [89, 25, 16, 10, 4]
def test_sort_2():
    list_for_sort = ['python', 'c#', 'java', 'c++']
    assert  sorted(list_for_sort) == ['c#', 'c++', 'java', 'python']
    assert  sorted(list_for_sort, reverse=True) == ['python', 'java', 'c++', 'c#']
def test_pi():
    assert math.pi == 3.141592653589793
def test_sqrt():
    assert math.sqrt(4) == 2
def test_pow():
    assert math.pow(2, 3) == 8
def test_hypot():
    assert math.hypot(0, 2) == 2.0

