
import math
import unittest
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from triangle import classify_triangle


class TestTriangles(unittest.TestCase):
    # classification tests
    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")
        self.assertEqual(classify_triangle(1.0, 1.0, 1.0 + 1e-10), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")
        self.assertEqual(classify_triangle(8, 5, 5), "Isosceles")
        self.assertEqual(classify_triangle(2.0, 2.0, 3.0), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_right_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Right Scalene")
        self.assertEqual(classify_triangle(5, 12, 13), "Right Scalene")
        self.assertEqual(classify_triangle(5, 3, 4), "Right Scalene")

    def test_right_isosceles(self):
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), "Right Isosceles")

    # boundary and special cases
    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "NotATriangle")  # 边界：1+2==3
        self.assertEqual(classify_triangle(2, 3, 6), "NotATriangle")
        self.assertEqual(classify_triangle(0, 4, 5), "NotATriangle")
        self.assertEqual(classify_triangle(-1, 2, 2), "NotATriangle")
        self.assertEqual(classify_triangle(float("inf"), 2, 2), "NotATriangle")
        self.assertEqual(classify_triangle(float("nan"), 2, 2), "NotATriangle")

    def test_equilateral_never_right(self):
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")


if __name__ == "__main__":
    unittest.main(verbosity=2)
