import numpy as np
from generate_neighbourhood import generate_neighbourhood
from read_pink_cells import read_pink_cells

vector = np.array([9, 10, 353, 484, 22, 1])

filename_mean = 'pinkcells_stats/pinkcells_Track_Position.csv'
filename_start = 'pinkcells_stats/pinkcells_Track_Position_Start.csv'

data = read_pink_cells(filename_mean, filename_start)


def normalize(v):
    """simple wrapper for L1 normalisation
    
    """
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def calculate_coalignment(vector, neigh):

    """Calculates coalignment between a given protrusion vector and its closest neighbours (I think).
    It averages the neighbourhood and then uses a dot product to calculate the coalignment.
    
    """

    if (vector == [] or neigh == []):
        return []
    total_direction = [0, 0]
    for current in neigh:

        total_direction += current[0:2]
    total_direction = normalize(total_direction[0:2])
    print("total direction: " + ','.join(map(str, total_direction)))
    norm_tot = normalize(total_direction)
    print("normalized total direction: " + ','.join(map(str, norm_tot)))

    coaligns = []
    vec_norm = normalize(vector[0:2])
    
    angle = np.arccos(np.dot(vec_norm, norm_tot))
    coaligns.append(np.dot(vec_norm, norm_tot))

    return coaligns, angle


neigh = generate_neighbourhood(vector, data, 3)
print(neigh)
print(calculate_coalignment(vector, neigh))
