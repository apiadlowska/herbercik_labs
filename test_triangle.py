import unittest
from triangle import _is_valid_triangle, _triangle_perimeter, _triangle_area, _triangle_type

class TestTriangleFunctions(unittest.TestCase):
    def test_is_valid_triangle(self):
        self.assertTrue(_is_valid_triangle(3, 4, 5))
        self.assertTrue(_is_valid_triangle(5, 5, 5))
        self.assertFalse(_is_valid_triangle(1, 2, 3))
        self.assertFalse(_is_valid_triangle(10, 1, 1))

    def test_triangle_perimeter(self):
        self.assertEqual(_triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(_triangle_perimeter(5, 5, 5), 15)

    def test_triangle_area(self):
        self.assertAlmostEqual(_triangle_area(3, 4, 5), 6.0)
        self.assertAlmostEqual(_triangle_area(5, 6, 5), 12.0)

    def test_triangle_type(self):
        self.assertEqual(_triangle_type(3, 4, 5), "prostokątny")  # 3^2+4^2=5^2
        self.assertEqual(_triangle_type(2, 2, 3), "rozwartokątny")   # 2^2+2^2 < 3^2
        self.assertEqual(_triangle_type(2, 3, 4), "rozwartokątny") # 2^2+3^2 < 4^2
        self.assertEqual(_triangle_type(5, 5, 5), "ostrokątny")   # All sides equal, always acute

if __name__ == "__main__":
    unittest.main()
