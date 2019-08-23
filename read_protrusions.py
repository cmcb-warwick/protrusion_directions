import pandas as pd
import numpy as np


def read_protrusions(filename):

"""
Creates a list-of-lists with XYZ info read from the filename provided
"""
    frame = get_frame(filename)
    data = []
    for i in range(len(frame['X'])):
        data.append([int(frame['X'][i]),
                     int(frame['Y'][i]), 1,
                     int(frame['Slice'][i])])

    return data


def get_frame(filename):
"""
Simple read_csv wrapper
"""
    f = pd.read_csv(filename)
    return f


def test_read_columns():
    filename = "protrusions.csv"
    # print(list(read_protrusions(filename)))
    assert len(list(get_frame(filename))) == 9


def test_read_data():
    filename = "protrusions.csv"
    # print(type(read_protrusions(frame)[0]))
    assert type(read_protrusions(filename)) == list


def test_type_data():
    filename = "protrusions.csv"
    assert type(read_protrusions(filename)[0][0]) == int


def test_size_data():
    filename = "protrusions.csv"
    assert len(read_protrusions(filename)[0]) == 4


def test_Z_range():
    filename = "protrusions.csv"
    data = read_protrusions(filename)
    for i in range(len(data)):
        assert data[i][2] == 1


def test_T_range():
    filename = "protrusions.csv"
    data = read_protrusions(filename)
    for i in range(len(data)):
        assert data[i][3] > 0 and data[i][3] < 75


if __name__ == "__main__":
    test_read_data()
