import unittest
from triangle import area, perimeter


class TestTriangleFunctions(unittest.TestCase):
    def test_area(self):
        side_a = 3
        side_b = 4
        side_c = 5
        expected_area = (side_a + side_b + side_c) / 2
        result = area(side_a, side_b, side_c)
        self.assertEqual(result, expected_area)

    def test_perimeter(self):
        side_a = 3
        side_b = 4
        side_c = 5
        expected_perimeter = side_a + side_b + side_c
        result = perimeter(side_a, side_b, side_c)
        self.assertEqual(result, expected_perimeter)


if __name__ == '__main__':
    unittest.main()
