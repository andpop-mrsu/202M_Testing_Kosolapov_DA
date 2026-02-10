import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestTriangleType(unittest.TestCase): 
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(5, 5, 5), "equilateral")
        self.assertEqual(get_triangle_type(10.5, 10.5, 10.5), "equilateral")

    def test_isosceles(self):
        self.assertEqual(get_triangle_type(7, 7, 10), "isosceles")
        self.assertEqual(get_triangle_type(10, 7, 7), "isosceles")
        self.assertEqual(get_triangle_type(7, 10, 7), "isosceles")

    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")

    def test_invalid_sum_of_sides(self):
        with self.assertRaisesRegex(IncorrectTriangleSides, "Сумма двух сторон должна быть больше третьей стороны."):
            get_triangle_type(1, 2, 3)
        with self.assertRaisesRegex(IncorrectTriangleSides, "Сумма двух сторон должна быть больше третьей стороны."):
            get_triangle_type(10, 2, 1)

    def test_zero_or_negative_sides(self):
        with self.assertRaisesRegex(IncorrectTriangleSides, "Стороны должны быть больше нуля."):
            get_triangle_type(0, 5, 5)
        with self.assertRaisesRegex(IncorrectTriangleSides, "Стороны должны быть больше нуля."):
            get_triangle_type(-2, 4, 4)
        with self.assertRaisesRegex(IncorrectTriangleSides, "Стороны должны быть больше нуля."):
            get_triangle_type(5, -5, 5)


if __name__ == "__main__":
    import doctest
    print("Запуск doctest")
    doctest.testmod()
    print("Запуск unittest")
    unittest.main()