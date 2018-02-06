import unittest

from prisoner_citizen import input_format
from prisoner_citizen import read_file
from prisoner_citizen import point_in_polygon


class InputFormatTest(unittest.TestCase):
    """ Test input format """

    def test_input_format(self):
        """ Test if the entry generates a list and a point"""

        test1 = '1 1, 1 4, 3 4, 3 2 | 2 3'
        vertices, point = input_format(test1)
        # Vertices
        self.assertEqual(vertices, [(1,1),(1,4),(3,4),(3,2)])
        # Point
        self.assertTrue(point==(2,3))


class ReadFileTest(unittest.TestCase):
    """ Test the file reading"""

    def test_read_file(self):
        """ Read from the file and return a list of vertices and points """

        data_list = read_file('fixtures/data.txt')
        self.assertEqual(len(data_list), 9)


class PointInPolygonTest(unittest.TestCase):
    """ Test to Point in Polygon """

    def test_point_in_polygon(self):
        """ Test if point is or isn't inside polygon """

        # Case Prisoner
        test1 = '1 1, 1 4, 3 4, 3 2 | 2 3'
        vertices, point = input_format(test1)
        self.assertTrue(point_in_polygon(vertices, point))

        # Case Citizen
        test2 = '1 1, 3 2, 1 4, 3 4 | 3 3'
        vertices, point = input_format(test2)
        self.assertEqual(point_in_polygon(vertices, point), False)


if __name__ == '__main__':
    unittest.main()