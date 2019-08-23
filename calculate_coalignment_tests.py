import numpy as np

from calculate_coalignment import calculate_coalignment, normalize
from generate_neighbourhood import generate_neighbourhood
from read_pink_cells import read_pink_cells



vector = np.array([9, 10, 353, 484, 22, 1])

filename_mean = 'pinkcells_stats/pinkcells_Track_Position.csv'
filename_start = 'pinkcells_stats/pinkcells_Track_Position_Start.csv'

data = read_pink_cells(filename_mean, filename_start)


def test_empty_vector():
    neigh = generate_neighbourhood(vector, data, 3)
    assert calculate_coalignment([], neigh) == []


def test_empty_neigh():
    assert calculate_coalignment(vector, []) == []


def test_size():
    neigh = generate_neighbourhood(vector, data, 3)
    assert len(calculate_coalignment(vector, neigh)) == len(neigh)


def test_product_zero():
    assert calculate_coalignment(
        vector, np.array([[0, 0, 1, 0, 0]])) == [0]


def test_product_x():
    assert calculate_coalignment(
        vector, np.array([[1, 0, 0, 0, 0]])) == normalize(vector[0:2])[0]


def test_product_y():
    assert calculate_coalignment(
        vector, np.array([[0, 1, 0, 0, 0]])) == normalize(vector[0:2])[1]


def test_product_multiple_pos():
    assert abs(calculate_coalignment(
        vector, np.array([[9, 10, 0, 0, 0]]))[0] - 1) < 0.0001


def test_product_multiple_neg():
    assert abs(calculate_coalignment(
        vector, np.array([[-9, -10, 0, 0, 0]]))[0] + 1) < 0.0001


def test_norm_zero():
    assert normalize([0, 0]) == [0, 0]


def test_norm_x():
    assert (normalize([1000, 0]) == [1, 0]).all()


def test_norm_y():
    assert (normalize([0, 10000]) == [0, 1]).all()


def test_norm_all():
    assert normalize([1, 1])[0] == normalize([1, 1])[1]


def test_norm_val():
    assert abs(np.linalg.norm(normalize([1, 1])) - 1) < 0.00001
