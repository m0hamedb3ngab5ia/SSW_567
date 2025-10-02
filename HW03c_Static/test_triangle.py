# test_classify_triangle.py
import unittest
from triangle import classify_triangle

class TestTriangles(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_right_triangle(self):
        result = classify_triangle(3, 4, 5)
        print(f"Result: '{result}'")
        self.assertEqual(result.strip(), "Scalene and Right")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle")

    def test_equilateral_not_right(self):
        result = classify_triangle(1, 1, 1)
        self.assertEqual(result, "Equilateral")

    def test_another_right_triangle(self):
        result = classify_triangle(5, 12, 13)
        self.assertEqual(result, "Scalene and Right")


if __name__ == "__main__":
    unittest.main()


#Citations: Github Copilot helped debug my code in classify_triangle.py