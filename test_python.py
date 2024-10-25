import pytest, math

"""
В модуле написать тесты для встроенных функций filter, map, sorted, а также для функций из
библиотеки math: pi, sqrt, pow, hypot. Чем больше тестов на каждую функцию - тем лучше
"""


# Тестирование функции map()
@pytest.mark.parametrize("iter_obj, result", [([1, 2, 3], [2, 4, 6]),
                                              ([-1, -2.5, -3], [-2, -5, -6]),
                                              (['X', 'Y', 'Z'], ['XX', 'YY', 'ZZ'])])
def test_map_list(iter_obj, result):
    result = list(map(lambda x: x * 2, iter_obj))
    assert result == result


def test_map_with_none():
    result = list(map(lambda x: x is None, [None, 1, 2]))
    assert result == [True, False, False]


def test_map_string_lenght():
    result = list(map(len, ['Max', 'Leo', 'Bob']))
    assert result == [3, 3, 3]


def test_map_string_empty():
    result = list(map(lambda x: x * 2, []))
    assert result == []


def test_map_TypeError():
    with pytest.raises(TypeError):
        list(map(None, [1, 2]))


# Тестирование функции filter()
def test_filter_even_numbers():
    result = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
    assert result == [2, 4]


def test_filter_strings():
    result = list(filter(lambda x: isinstance(x, str), [1, 'hello', 2, 'world']))
    assert result == ['hello', 'world']


def test_filter_empty():
    result = list(filter(lambda x: x > 0, []))
    assert result == []


def test_filter_none():
    result = list(filter(lambda x: x is not None, [None, 1, 2]))
    assert result == [1, 2]


def test_filter_type_error():
    with pytest.raises(TypeError):
        list(filter(float, [None, 1, 2]))


# Тестирование функции sorted()
@pytest.mark.parametrize("iter_obj, effect", [([5, 2, 9, 1, 5, 6], [1, 2, 5, 5, 6, 9]),
                                              (['banana', 'apple', 'cherry'], ['apple', 'banana', 'cherry'])])
def test_sorted_num_str(iter_obj, effect):
    result = sorted(iter_obj)
    assert result == effect


def test_sorted_reverse():
    result = sorted([5, 2, 9, 1, 5, 6], reverse=True)
    assert result == [9, 6, 5, 5, 2, 1]


def test_sorted_with_key():
    result = sorted(['Mersedes', 'Ford', 'Skoda'], key=len)
    assert result == ['Ford', 'Skoda', 'Mersedes']


def test_sorted_empty():
    result = sorted([])
    assert result == []


def test_sorted_TypeError():
    with pytest.raises(TypeError):
        sorted([1, 'Max', 3])


# Тестирование функции math.pi
def test_math_pi_type():
    assert isinstance(math.pi, float) == True


def test_math_pi_value():
    assert math.pi == 3.141592653589793


def test_math_pi_compare():
    assert (3.14 < math.pi < 3.15) == True


# Тестирование функции math.sqrt

@pytest.mark.parametrize("num, res_", [(2, 4),
                                       (3, 9),
                                       (4, 16),
                                       (0.5, 0.25)])
def test_math_sqrt(num, res_):
    assert math.sqrt() == res_


def test_sqrt_ValueError():
    with pytest.raises(ValueError):
        math.sqrt(-2)


def test_sqrt_large_num():
    assert math.sqrt(1_000_000) == 1000


# Тестирование функции math.pow

@pytest.mark.parametrize("num, pow, res", [(1, 2, 1),
                                           (2, 3, 8),
                                           (3, 2, 9),
                                           (-2, 3, -8),
                                           (-2, 2, 4),
                                           (2, 0, 1),
                                           (0, 0, 1),
                                           (0.5, 2, 0.25)])
def test_math_pow(num, pow, res):
    assert math.pow(num, pow) == res

