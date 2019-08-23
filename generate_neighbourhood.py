from read_pink_cells import read_pink_cells
import numpy as np
from math import sqrt

filename_mean = 'pinkcells_stats/pinkcells_Track_Position.csv'
filename_start = 'pinkcells_stats/pinkcells_Track_Position_Start.csv'

data = read_pink_cells(filename_mean, filename_start)

data_mock = np.array([[0.0, 0.0, 100, 100, 0], [0.0, 0.0, 200, 200, 0]])

vector = np.array([9, 10, 353, 484, 22, 1])

size_x = 0.999
size_z = 2.26
size_y = 0.976


def generate_neighbourhood(vector, data, size):

    """Returns the closest cells to a given vector. 

    Parameters:
    vector (array): vector of interest
    data (list): List of arrays containing cell coordinates
    size (int): number of closest cells to be returned

    Returns:
    list: list of arrays with data from the closest cells

   """

    if (vector == [] or data == []):
        return []
    else:
        if len(data) <= size:
            return data
        distances = []
        for cell in data:
            distances.append(calculate_distance(vector, cell))
        dists = np.array(distances)
        ordered = zip(dists, data)

        ordered.sort(key=lambda tup: tup[0])
        # print(vector, ordered[0:size])
        ordered_data = [x for y, x in ordered]
        #single_neighbour = [0] * len(data[0])
        return ordered_data[0:size]


def calculate_distance(vector, track):

    """Simple L2 distance between two vectors (using values 2,3,4 for XYZ - not sure why)
    """
    
    dist = (size_x * (vector[2] - track[2]))**2 + \
        (size_y * (vector[3] - track[3]))**2  + \
         (size_z * (vector[4] - track[4]))**2
    dist = sqrt(dist)
    return dist


def test_empty_vector():
    assert generate_neighbourhood([], data, 1) == []


def test_empty_data():
    assert generate_neighbourhood(vector, [], 1) == []


def test_size():
    assert len(generate_neighbourhood(vector, data, 12)) == 12


def test_length():
    assert len(generate_neighbourhood(vector, data, 5)[0]) == len(data[0])


def test_distance_x():
    assert calculate_distance(np.array([10.0, 10.0, 1.0, 0.0, 0.0]),
                              np.array([8.0, 7.0, 0.0, 0.0, 0.0])) == size_x


def test_distance_y():
    assert calculate_distance(np.array([10.0, 10.0, 0.0, 1.0, 0.0]),
                              np.array([8.0, 7.0, 0.0, 0.0, 0.0])) == size_y


def test_distance_z():
    assert calculate_distance(np.array([10.0, 10.0, 0.0, 0.0, 1.0]),
                              np.array([8.0, 7.0, 0.0, 0.0, 0.0])) == size_z


def test_all_distances():
    assert calculate_distance(np.array([10.0, 10.0, -2.0, -0.5, 0.0]),
                              np.array([8.0, 7.0, 0.0, 1.0, 3.0])) - 7.21829 < 0.001


def test_use_mock():
    assert len(generate_neighbourhood(vector, data_mock, 1)[0]) == len(data[0])


def test_size_too_big():
    assert (generate_neighbourhood(vector, data_mock, 5) == data_mock).all()


def test_size_mock_single():
    assert (generate_neighbourhood(vector, data_mock, 1) == data_mock[1]).all()


print(generate_neighbourhood(vector, data, 3))
