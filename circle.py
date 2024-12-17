import math

def area(r):
    """Находит площадь окружности.

    Параметры:
        r (float): радиус окружности.

    Возвращаемые значения:
        float: площадь окружности.
    """
    return math.pi * r * r

def perimeter(r):
    """Находит периметр окружности.

    Параметры:
        r (float): радиус окружности.

    Возвращаемые значения:
        float: периметр окружности.
    """
    return 2 * math.pi * r
