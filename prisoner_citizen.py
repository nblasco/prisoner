from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely.geometry import LineString


def input_format(line):
    """ Converts a string into a list of vertices and a point

    Receive an entry with this format with 
    this format '1 1, 3 2, 1 4, 3 4 | 3 3 '
    Returns:
    list = [(1,1), (3,2), (1,4), (3,4)] and a point = (3,3)

    :param line: 
    :return: list, point
    """

    line_strip = line.rstrip('\n').split(' | ')
    point = line_strip[1].split(' ')
    coord = (float(point[0]), float(point[1]))
    vertices = []
    for vertex in line_strip[0].split(', '):
        vertices.append(
            (float(vertex.split(' ')[0]),
             float(vertex.split(' ')[1])))

    return vertices, coord


def read_file(file_name):
    """ Read a file and format the data

    Read a file, format the data in a vector of points for the 
    jail and the coordinate of the prisoner or citizen.
    :param file_name: name of file
    :return:  list of all test cases
    """

    with open(file_name, encoding='utf-8') as f:
        tests = []
        for line in f.readlines():
            vertices, point = input_format(line)
            tests.append([vertices, point])
    return tests


def point_in_polygon(vertices, point):
    """ Determines whether a point is inside or on the edge of the polygon

    Returns True if the point is inside the polygon
    Returns False if the point is outside the polygon

    :param vertices: 
    :param point: 
    :return: Boolean
    """

    point = Point(point)
    polygon = Polygon(vertices)
    line = LineString(vertices)

    inside_polygon = polygon.contains(point)
    line_polygon = line.contains(point)

    if inside_polygon or line_polygon:
        return True
    else:
        return False


def prisoner_or_citizen(data_list):
    """ Show if a person is a prisoner or citizen

    Find out where a person is—in jail or at large—depending on the 
    coordinates. If in jail, print Prisoner; otherwise, print Citizen.

    Check if the coordinates are inside the jail or on the edge of the jail.
    """

    for item in data_list:
        vertices = item[0]
        point = item[1]
        if point_in_polygon(vertices, point):
            print('Prisoner')
        else:
            print('Citizen')


if __name__ == '__main__':
    data = read_file('fixtures/data.txt')
    prisoner_or_citizen(data)