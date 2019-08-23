#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 11:12:56 2018

@author: erick
"""


def normalize_l2(v):
    """simple wrapper for L2 normalisation
    
    """
    import numpy as np
    norm = np.linalg.norm(v, ord=2)
    if norm == 0:
        norm = np.finfo(v.dtype).eps
    return v / norm


def protrusion_vectors(stack, cells, filename_diff):
    """Returns a list of vectors from detected cells/nuclei to
    points of interest/protrusions

    Parameters:
    stack (list): list of detected protrusions/points of interest
    cells (pd.Dataframe): Pandas dataframe with information about the cells/nuclei
    filename_diff (?): not being used?

    Returns:
    vectors (list of np.arrays): np.arrays with vectors from cell nuclei/centroids to protrusions/points of interest

   """


    import numpy as np
    from check_difference import check_difference
    vectors = []
    size_x = 0.999
    size_z = 2.26
    size_y = 0.976
    for prot in stack:

        # check_diff = check_difference(prot, filename_diff)
        check_diff = True
        print(prot, check_diff)
        if not check_diff:
            continue
        # print(prot)
        rel_cells = cells[cells["Time"] == prot[3]].copy()
        # rel_cells = rel_cells[rel_cells["Pixel Z"] < 45].copy()


        rel_cells["Dist_sq"] = (size_x * (rel_cells["Pixel X"] - prot[0]))**2 + \
                               (size_y * (rel_cells["Pixel Y"] - prot[1]))**2 # + \
                               # (size_z * (rel_cells["Pixel Z"] - prot[2]))**2
        rel_cells.to_csv(
            "relcells/" + str(prot[0]) + str(prot[1]) + "_frame.csv")
        if (not rel_cells.empty):
            minimum = rel_cells.loc[rel_cells["Dist_sq"].idxmin()]
            # print(minimum)
            vec = np.array([prot[0] - minimum["Pixel X"],
                            prot[1] - minimum["Pixel Y"]])
            # print(prot[1], prot[0], vec)
            vec_norm = np.linalg.norm(vec, ord=2)
#            vec = normalize_l2(vec)
            # print(vec_norm)
            if(vec_norm < 30.0):
                vectors.append(np.array([vec[0], vec[1],
                                         minimum["Pixel X"], minimum["Pixel Y"], minimum["Pixel Z"], minimum["Time"]]))
            # print(vectors[-1])
        else:
            minimum = []
            continue
    # print(vectors)

    return vectors


if __name__ == "__main__":

    from generate_curvature import generate_curvature, collapse_z
    from read_cells import read_cells
    from read_pink_cells import read_pink_cells
    from visualise_results import visualise_results
    from visualise_angles import visualise_angles
    from generate_neighbourhood import generate_neighbourhood
    from calculate_coalignment import calculate_coalignment
    from read_protrusions import read_protrusions
    import numpy as np
    import matplotlib.pyplot as plt
    filename = '/home/erick/Nextcloud/CMCB/Michael_protrusions/TP_wt_lat/20140521/channel1_reslice_MIP_areas.ome.tif'
    filename_diff = '/home/erick/Nextcloud/CMCB/Michael_protrusions/TP_wt_lat/20140521/channel1_reslice_MIP_areas_diff.ome.tif'
    radius = 5
    #prot = generate_curvature(filename, radius, 0.3)
    filename_prot = '/home/erick/Nextcloud/CMCB/Michael_protrusions/TP_wt_lat/20140521/protrusions.csv'
    prot = read_protrusions(filename_prot)
    # print(prot)
#    stack = collapse_z(prot, radius)
    filename_cells = '/home/erick/Nextcloud/CMCB/Michael_protrusions/TP_wt_lat/20140521/20140521_cellCollective_Position.csv'
#    print(stack)
    cells = read_cells(filename_cells)
#    protrusion_vectors(stack, cells)
#    vectors = protrusion_vectors(stack, cells)
    vectors = protrusion_vectors(prot, cells, filename_diff)

    vecs = open("/home/erick/Nextcloud/CMCB/Michael_protrusions/TP_wt_lat/20140521/vectors.csv", "w")
    for vector in vectors:
        #x, y = vector[0], vector[1]
        print(vector)
        vecs.write(','.join(map(str, vector)) + "\n")
        # vecs.write("test")
    vecs.close()

    filename_mean = '/home/erick/Nextcloud/CMCB/Michael_protrusions/TP_wt_lat/20140521/20140521_spots_Track_Position.csv'
    filename_start = '/home/erick/Nextcloud/CMCB/Michael_protrusions/TP_wt_lat/20140521/20140521_spots_Track_Position_Start.csv'
    size_neigh = 7
    data = read_pink_cells(filename_mean, filename_start)
    coaligns = []
    all_angles = []
    f = open('/home/erick/Nextcloud/CMCB/Michael_protrusions/TP_wt_lat/20140521/angles.csv', 'w')
    f.write('vec_x,vec_y,pos_x,pos_y,pos_z,timepoint,angle(rad),coalignment\n')
    for vector in vectors:
        print(vector)
        neigh = generate_neighbourhood(vector, data, size_neigh)
        print(neigh)
        product, angles = calculate_coalignment(vector, neigh)
        print(product)
        f.write(','.join(map(str,vector)) + ',' + str(angles) + ',' + str(product[0]) + '\n')
        coaligns.append(product)
        all_angles.append(angles)
    f.close()
#    print(vectors)
    print("MEAN COALIGNMENT: ", str(np.mean(coaligns)))
    print("MEDIAN COALIGNMENT: ", str(np.median(coaligns)))
    # tuples = [(coaligns.index(x), num) for x in coaligns for num in x]
    # x, y = zip(*tuples)
    # avg = np.mean(y)

    # plt.scatter(x, y)
    # xmin, xmax = plt.xlim()
    # print(avg)
    # plt.hlines(avg,xmin, xmax)
    # plt.show()
    visualise_angles(all_angles)
    visualise_results(filename, cells, vectors)
    # print(vectors)
