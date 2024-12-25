import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):

    def test_area(self):
        side_length = 4
        expected_area = side_length * side_length
        result = area(side_length)
        self.assertEqual(result, expected_area)

    def test_perimeter(self):
        side_length = 4
        expected_perimeter = side_length * 4
        result = perimeter(side_length)
        self.assertEqual(result, expected_perimeter)


if __name__ == '__main__':
    unittest.main()
