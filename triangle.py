def area(a, b, c):
    """Находит площадь треугольника.

    Параметры:
        a (float): сторона треугольника.
        b (float): сторона треугольника.
        c (float): сторона треугольника.

    Возвращаемые значения:
        float: площадь треугольника.
    """
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def perimeter(a, b, c):
    """Находит периметр треугольника.

    Параметры:
        a (float): первая сторона.
        b (float): вторая сторона.
        c (float): третья сторона.

    Возвращаемые значения:
        float: длина периметра треугольника.
    """
    return a + b + c
