#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 16:19:53 2018

@author: erick
"""


def generate_histogram(vectors):
    import numpy as np
    import matplotlib.pyplot as plt
    import math

    N = 20
    bottom = 0
    max_height = 30

    theta = np.linspace(-1.0001 * np.pi,  1.0001 * np.pi, N, endpoint=True)
    # print(theta)
    radii = np.zeros(N)
    for vector in vectors:
        this_theta = math.atan2(-vector[1],vector[0])
        # print(this_theta)
        radii[np.digitize(this_theta, theta)] += 1
        # print(np.digitize(this_theta, theta))

    width = (2*np.pi) / N

    ax = plt.subplot(111, polar=True)
    bars = ax.bar(theta, radii, width=width, bottom=bottom)
    plt.show()


def visualise_results(filename, cells, vectors):
    from get_metadata import get_metadata
    from read_plane import read_plane
    import matplotlib.pyplot as plt

    H, W, Z, T, C = get_metadata(filename)
#    output_file = "test.ome.tiff"
    total_images = Z * T * C

    for count in range(total_images):
        plane, curr_z, curr_c, curr_t = read_plane(filename, count)
        # print(curr_z, curr_t)
#        if (curr_z == 44):
        fig = plt.figure()
        fig.clf()
        ax = fig.add_subplot(111)
        ax.imshow(plane, cmap='jet')
        plt.axis('off')
#        fig.axes.get_xaxis().set_visible(False)
#        fig.axes.get_yaxis().set_visible(False)
#        ax.axes.get_xaxis().set_visible(False)
#        ax.axes.get_yaxis().set_visible(False)
        ax.set_frame_on(False)
#        plt.arrow(100,100,100,100,color='white', head_width = 10, head_length = 10)
        # find vectors on this Z/T/C coord
        for vector in vectors:
            # print(vector)
            # print(curr_z, curr_t)
            # if (vector[5] -1 == curr_z and vector[4]  - 1 == curr_t:):
            if vector[5] - 1 == curr_z:
                #                if (curr_z == 44):
                # plot plane and vectors
                plt.arrow(vector[2], vector[3], vector[0], vector[1],
                          color='white', head_width=3, head_length=3)

                # print(vector)

        plt.savefig("figures/frame_" + str(count) + ".tif",
                    bbox_inches='tight', pad_inches=0)
        plt.close(fig)
#        pixels = fig2data(fig)

        # convert plot to pixels

        # write pixels to TIFF
#        write_plane(output_file, count, pixels)
    generate_histogram(vectors)
    return


if __name__ == "__main__":

    import numpy as np

    samples = 1000000
    vectors = []
    for i in range(samples):
        vectors.append( -1 + 2* np.random.rand(2))
    # print(vectors)
    generate_histogram(vectors)