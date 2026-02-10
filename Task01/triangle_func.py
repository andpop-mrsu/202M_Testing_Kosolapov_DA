class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(a, b, c):
    """
    >>> get_triangle_type(5, 5, 5)
    'equilateral'
    >>> get_triangle_type(7, 7, 10)
    'isosceles'
    >>> get_triangle_type(7, 10, 7)
    'isosceles'
    >>> get_triangle_type(10, 7, 7)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(10.5, 10.5, 10.5)
    'equilateral'
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Сумма двух сторон должна быть больше третьей стороны.
    >>> get_triangle_type(0, 5, 5)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Стороны должны быть больше нуля.
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Стороны должны быть больше нуля.")
    
    if not (a + b > c and a + c > b and b + c > a):
        raise IncorrectTriangleSides("Сумма двух сторон должна быть больше третьей стороны.")
    
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"