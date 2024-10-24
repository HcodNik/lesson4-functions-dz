
"""
В модуле написать тесты для встроенных функций filter, map, sorted, а также для функций из
библиотеки math: pi, sqrt, pow, hypot. Чем больше тестов на каждую функцию - тем лучше
"""

# Тестирование функции map()
def test_map_func():
    assert list(map(lambda x: x * 2, [1, 2])) == [2, 4]
    assert list(map(lambda x: x * 2, ['Max', 'Leo'])) == ['MaxMax', 'LeoLeo']



