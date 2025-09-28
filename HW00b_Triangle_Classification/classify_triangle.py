# classify_triangle.py

def classify_triangle(a, b, c):
    #sort sides to make it easier to check right triangle (largest side last)
    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]

    #check if it's a valid triangle
    if a + b <= c:
        return "Not a triangle"

    # determine type by sides
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Only mark as right if not equilateral or isosceles
    if a**2 + b**2 == c**2 and triangle_type == "Scalene":
        triangle_type += " and Right"

    return triangle_type
