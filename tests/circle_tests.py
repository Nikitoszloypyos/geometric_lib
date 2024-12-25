import math
import unittest

from circle import area, perimeter


class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        # Arrange
        radius = 5
        expected_area = math.pi * radius * radius
        result = area(radius)
        self.assertAlmostEqual(result, expected_area, places=7)

    def test_perimeter(self):
        radius = 5
        expected_perimeter = 2 * math.pi * radius
        result = perimeter(radius)
        self.assertAlmostEqual(result, expected_perimeter, places=7)


if __name__ == '__main__':
    unittest.main()
