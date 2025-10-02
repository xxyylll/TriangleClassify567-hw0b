# triangles.py

import math

# Floating point tolerance to avoid errors with values like 3, 4, 5
EPS = 1e-9

def classify_triangle(a, b, c):

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
        else:
            return "Right Scalene"

    if abs(a - b) <= EPS or abs(b - c) <= EPS or abs(a - c) <= EPS:
        return "Isosceles"

    return "Scalene"


if __name__ == "__main__":
    raw = input("Enter three side lengths: ").strip().split()
    if len(raw) != 3:
        print("Please enter exactly three numbers, e.g. '3 4 5'")
    else:
        try:
            a = float(raw[0])
            b = float(raw[1])
            c = float(raw[2])
            print("Result:", classify_triangle(a, b, c))
        except Exception as e:
            print("Error:", e)
