# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 15:58:53 2018

@author: erick
"""


def neighbors(a, radius, rowNumber, columnNumber):
    """Returns a list of neighbours on a radius-sized square around
    rowNumber and columnNumber on the matrix a.

    Parameters:
    a (two-dimensional array): matrix where we search for neighbours
    radius (int): half-size of the square inside which we'll search
    rowNumber, columnNumber (ints): coordinates around which we search

    Returns:
    list:List of neighbour values

   """

    return [[a[i][j] if i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) else 0
             for j in range(columnNumber - radius, columnNumber + radius)]
            for i in range(rowNumber - radius, rowNumber + radius)]


def normalize_l2(v):

    """simple wrapper for LO2 normalisation
    
    """

    import numpy as np
    norm = np.linalg.norm(v, ord=2)
    if norm == 0:
        return v
    return v / norm


def collapse_z(points, radius):

    """Generates an array of centroids from clusters of similar points

    Parameters:
    points (two-dimensional array): Array of 4D points (XYZ + value, I think?)
    radius (float?): maximum distance between points in a cluster

    Returns:
    list:List of neighbour values


    """

    import numpy as np
    new_points = []
    count = 0
    while count < len(points):
        point = points[count]
        cluster = [point]
        test_points = points[:]
        test_points.remove(point)

        for test_point in test_points:
            if (abs(point[0] - test_point[0]) < radius and
                abs(point[1] - test_point[1]) < radius and
                abs(point[2] - test_point[2]) < radius / 2.25 and
                    point[3] == test_point[3]):
                cluster.append(test_point)
        centroid = np.mean(np.array(cluster), axis=0)
        centroid = centroid.round().astype(int)
        new_points.append(centroid)
        for removal in cluster:
            #            print("removing?",removal)
            points.remove(removal)
#        print(cluster,centroid)
#        print("points now: ", points)
#    print(new_points)
    return new_points


def generate_curvature(filename, neighbours, threshold):

    """Generates a list of points with curvature above a certain threshold

    Parameters:
    filename (string): Path to file from where we'll detect curvatures
    neighbours (int): neighbourhood size for curvature calculation
    threshold (float): curvature threshold for detecting "points of interest"

    Returns:
    interest_points (list): List of neighbour values


    """
    from calculate_curvature import calculate_curvature
    from get_metadata import get_metadata
    from read_plane import read_plane
    import matplotlib.pyplot as plt
    import numpy as np

    np.set_printoptions(threshold='nan')

    filename_split = filename.split(".")
#    print(filename_split[-2:])
    filename_area = '.'.join(
        filename_split[:-2]) + '_areas' + '.' + '.'.join(filename_split[-2:])
#    print(filename_area)

    H, W, Z, T, C = get_metadata(filename)

    total_images = Z * T * C

    vec_x = []
    vec_y = []
    vec_comp1 = []
    vec_comp2 = []

    interest_points = []
    for count in range(total_images):
        print(count)
        neigh_size = neighbours

        plane, curr_z, curr_c, curr_t = read_plane(filename, count)
        area, gar1, gar2, gar3 = read_plane(filename_area, count)
        plane = plane.astype(float)
        it = np.nditer(plane, flags=['multi_index'], op_flags=['readwrite'])
        while not it.finished:
            #            print(it.value)
            if (it.value > 0):
                x, y = it.multi_index
#                if (y == 0):
#                    print ("%d <%s>" % (it.value, it.multi_index))
                neigh = neighbors(plane, neigh_size, x, y)
                curv, centre = calculate_curvature(neigh)
                np_centre = np.array(centre)
                normal = normalize_l2(np_centre)
                move = neigh_size * normal
                if (curv > 0.0):
                    vec_x.append(x)
                    vec_y.append(y)
                    vec_comp1.append(move[0])
                    vec_comp2.append(move[1])

                move = np.round(move).astype(int)
#                print(move)
                if (x + move[0] < 0 or x + move[0] >= len(plane) or
                    y + move[1] < 0 or y + move[1] >= len(plane[0]) or
                        area[x + move[0]][y + move[1]] == 0):
                    plane[x][y] = 0.01
                else:
                    if curv > threshold:
                        plane[x][y] = curv

                    else:
                        plane[x][y] = 0.01

                # calculate unit vector from x,y to centre, move a few pixels (neigh_size?) to that direction, check if it's in area/inbounds
    #            plane[x][y] = curv

#                if (curv>0.2):
#                    print(x, y, plane[x][y], curv, move)

    #        print(x,y)
            it.iternext()
#        print(neighbors(plane, neigh_size, 274,485))

    # detect points of high curvature with the correct direction
        neigh_size = neighbours
        it = np.nditer(plane, flags=['multi_index'], op_flags=['readwrite'])
#        fig = plt.figure()
        while not it.finished:
            #            print(it.value,it.multi_index)
            if (it.value > 0.02):
                x, y = it.multi_index
#                print ("%d <%s>" % (it.value, it.multi_index))
                neigh = neighbors(plane, neigh_size, x, y)
                neigh = np.array(neigh)
#                print(neigh)
                neigh[neigh_size][neigh_size] = 0.01
                if (plane[x][y] <= neigh.max()):
                    plane[x][y] = 0.01
                else:
                    interest_points.append([x, y, curr_z, curr_t])
            it.iternext()
#        fig.clf()
#        plt.imshow(plane, cmap='hot_r')
# plt.quiver(vec_y,vec_x,vec_comp1,vec_comp2,linewidth=0.001,width=0.001)
#
#        plt.savefig('/home/erick/Nextcloud/CMCB/Michael_protrusions/test.tiff', dpi=300)
#    #    plt.colorbar()
#        plt.show()
#    print(len(interest_points))
    # print(interest_points)
    return interest_points


if __name__ == "__main__":
    filename = '/home/erick/Nextcloud/CMCB/Michael_protrusions/smallstack.ome.tiff'
    radius = 5.0
    prot = generate_curvature(filename, 5, 0.4)
    filtered_prot = collapse_z(prot, radius)
    print(filtered_prot)
#    print(len(filtered_prot))
