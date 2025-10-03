
import math
import unittest
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from triangle import classify_triangle
from triangle import classify_from_input


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


    def test_right_triangle_float(self):
        # float precision test for right triangle
        self.assertEqual(classify_triangle(0.3, 0.4, 0.5), "Right Scalene")

    def test_isosceles_right_with_float(self):
        # float precision test for right isosceles
        self.assertEqual(classify_triangle(1.0, 1.0, math.sqrt(2)), "Right Isosceles")

    def test_order_invariance(self):
        # the order of sides should not matter
        self.assertEqual(classify_triangle(6, 4, 5), "Scalene")
        self.assertEqual(classify_triangle(13, 5, 12), "Right Scalene")

    def test_invalid_type_inputs(self):
        self.assertEqual(classify_triangle("a", 3, 4), "NotATriangle") 
        self.assertEqual(classify_triangle(None, 3, 4), "NotATriangle")
        self.assertEqual(classify_triangle([], {}, ()), "NotATriangle")
    
    def test_large_values(self):
        self.assertEqual(classify_triangle(1e10, 1e10, 1e10), "Equilateral")
        self.assertEqual(classify_triangle(3e8, 4e8, 5e8), "Right Scalene")

class TestClassifyFromInput(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(classify_from_input("3 4 5"), "Result: Right Scalene")

    def test_not_enough_numbers(self):
        self.assertEqual(
            classify_from_input("3 4"),
            "Please enter exactly three numbers, e.g. '3 4 5'"
        )

    def test_invalid_input(self):
        self.assertEqual(classify_from_input("a 2 3"), "Invalid input: inputs must be numbers.")


if __name__ == "__main__":
    unittest.main()
