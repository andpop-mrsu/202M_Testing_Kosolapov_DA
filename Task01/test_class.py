import pytest
from triangle_class import Triangle, IncorrectTriangleSides

# --- Позитивные тесты ---

def test_equilateral_triangle():
    """Проверка равностороннего треугольника."""
    t = Triangle(5, 5, 5)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 15

def test_isosceles_triangle():
    """Проверка равнобедренного треугольника и его периметра."""
    # Варианты комбинаций равных сторон
    t1 = Triangle(7, 7, 10)
    assert t1.triangle_type() == "isosceles"
    assert t1.perimeter() == 24

    t2 = Triangle(10, 7, 7)
    assert t2.triangle_type() == "isosceles"
    assert t2.perimeter() == 24

    t3 = Triangle(7, 10, 7)
    assert t3.triangle_type() == "isosceles"
    assert t3.perimeter() == 24

def test_nonequilateral_triangle():
    """Проверка разностороннего треугольника."""
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 12

def test_float_sides():
    """Проверка работы с числами с плавающей точкой."""
    t = Triangle(10.5, 10.5, 10.5)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 31.5

# --- Негативные тесты ---

def test_invalid_triangle_inequality():
    """Проверка нарушения неравенства треугольника (сумма двух сторон не больше третьей)."""
    with pytest.raises(IncorrectTriangleSides) as excinfo:
        Triangle(1, 2, 3)
    assert str(excinfo.value) == "Сумма двух сторон должна быть больше третьей стороны."

    with pytest.raises(IncorrectTriangleSides):
        Triangle(10, 2, 1)

def test_zero_sides():
    """Проверка случая, когда сторона равна нулю."""
    with pytest.raises(IncorrectTriangleSides) as excinfo:
        Triangle(0, 5, 5)
    assert str(excinfo.value) == "Стороны должны быть положительными числами."

def test_negative_sides():
    """Проверка случая с отрицательными сторонами."""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-2, 4, 4)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(5, -5, 5)

def test_all_zeros():
    """Проверка случая, когда все стороны равны нулю."""
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 0, 0)