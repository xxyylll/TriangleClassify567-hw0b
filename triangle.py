"""This module contains a function to classify triangles based on side lengths."""

import math

# Floating point tolerance to avoid errors with values like 3, 4, 5
EPS = 1e-9

def classify_triangle(a, b, c):
    """Classify a triangle given side lengths a, b, and c."""
    # Number needs to be numeric and positive
    for x in (a, b, c):
        if not isinstance(x, (int, float)):
            return "NotATriangle"
        if math.isinf(x) or math.isnan(x) or x <= 0:
            return "NotATriangle"

    # Triangle inequality (strictly greater than)
    if not (a + b > c and a + c > b and b + c > a):
        return "NotATriangle"

    # Equilateral triangle
    if abs(a - b) <= EPS and abs(b - c) <= EPS:
        return "Equilateral"

    # Right angle check
    sides = [float(a), float(b), float(c)]
    sides.sort()
    x = sides[0]
    y = sides[1]
    z = sides[2]

    if abs(x * x + y * y - z * z) <= EPS:
        if abs(a - b) <= EPS or abs(b - c) <= EPS or abs(a - c) <= EPS:
            return "Right Isosceles"
        return "Right Scalene"

    if abs(a - b) <= EPS or abs(b - c) <= EPS or abs(a - c) <= EPS:
        return "Isosceles"

    return "Scalene"

def classify_from_input(raw_input: str) -> str:
    """Classify triangle from raw input string like '3 4 5'."""
    raw = raw_input.strip().split()
    if len(raw) != 3:
        return "Please enter exactly three numbers, e.g. '3 4 5'"

    try:
        side1 = float(raw[0])
        side2 = float(raw[1])
        side3 = float(raw[2])
        return "Result: " + classify_triangle(side1, side2, side3)
    except ValueError:
        return "Invalid input: inputs must be numbers."


def main():
    """Read input from user and print classification."""
    user_input = input("Enter three side lengths: ")
    print(classify_from_input(user_input))

if __name__ == "__main__":
    main()

# End of triangle.py
