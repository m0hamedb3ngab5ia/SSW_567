"""Triangle classification module for HW03c assignment."""


def classify_triangle(a, b, c):
    """
    Classify a triangle based on side lengths.

    Args:
        a (int or float): length of side a
        b (int or float): length of side b
        c (int or float): length of side c

    Returns:
        str: The type of triangle:
            - "Equilateral" if all sides equal
            - "Isosceles" if two sides equal
            - "Scalene" if all sides different
            - "Right" appended if Pythagorean theorem holds
            - "Not a triangle" if triangle inequality fails
    """

    # Check for invalid sides (zero or negative)
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle"

    # Check triangle inequality
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Not a triangle"

    # Check right triangle using Pythagoras
    sides = sorted([a, b, c])
    right = sides[0]**2 + sides[1]**2 == sides[2]**2

    if a == b and b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles and Right" if right else "Isosceles"
    if right:
        return "Scalene and Right"
    return "Scalene"
