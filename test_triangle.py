import unittest
from triangle import is_valid_triangle, triangle_perimeter, triangle_area, triangle_type

class TestTriangleFunctions(unittest.TestCase):
    def test_is_valid_triangle(self):
        self.assertTrue(is_valid_triangle(3, 4, 5))
        self.assertTrue(is_valid_triangle(5, 5, 5))
        self.assertFalse(is_valid_triangle(1, 2, 3))
        self.assertFalse(is_valid_triangle(10, 1, 1))

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(triangle_perimeter(5, 5, 5), 15)

    def test_triangle_area(self):
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6.0)
        self.assertAlmostEqual(triangle_area(5, 5, 5), 10.825317547305486)

    def test_triangle_type(self):
        self.assertEqual(triangle_type(3, 3, 3), "równoboczny")
        self.assertEqual(triangle_type(5, 5, 3), "równoramienny")
        self.assertEqual(triangle_type(3, 4, 5), "różnoboczny")

if __name__ == "__main__":
    unittest.main()
