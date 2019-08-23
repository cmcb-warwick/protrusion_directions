#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:50:04 2018

@author: erick
"""


def read_pink_cells(filename_mean, filename_start):


    """
    Reads csv files with the mean cell position and the initial cell position and calculate pixel data from XYZ positions


    Parameters:
    filename_mean (string): path to csv file with cell mean position info
    filename_start (string): path to csv file with initial cell position info

    Returns:
    vectors (2D array): structure containing XY direction of tracks and XYZ mean pixels



    """

    import pandas as pd
    import numpy as np

    min_x = -84.0
    min_y = 116.0
    min_z = -230.0

    size_x = 0.999
    size_y = 2.26
    size_z = 0.976

    frame_mean = pd.read_csv(filename_mean, skiprows=3)
    frame_start = pd.read_csv(filename_start, skiprows=3)

    # will need to check IMARIS for correspondence between exported um files and pixel values
    # X and Z on csv files are my X and Y on resliced images

    frame_mean["Pixel X Mean"] = (
        frame_mean['Track Position X Mean'] - min_x) / size_x
    frame_mean["Pixel X Mean"] = frame_mean["Pixel X Mean"].round().astype(int)

    frame_mean["Pixel Y Mean"] = (
        frame_mean['Track Position Z Mean'] - min_z) / size_z
    frame_mean["Pixel Y Mean"] = frame_mean["Pixel Y Mean"].round().astype(int)

    frame_mean["Pixel Z Mean"] = (
        frame_mean['Track Position Y Mean'] - min_y) / size_y
    frame_mean["Pixel Z Mean"] = frame_mean["Pixel Z Mean"].round().astype(int)

    frame_mean["X direction"] = frame_mean['Track Position X Mean'] - \
        frame_start['Track Position X Start']
    frame_mean["Y direction"] = frame_mean['Track Position Z Mean'] - \
        frame_start['Track Position Z Start']

    list1 = np.array(frame_mean["X direction"].values.tolist())
    list2 = np.array(frame_mean["Y direction"].values.tolist())
    list3 = np.array(frame_mean["Pixel X Mean"].values.tolist())
    list4 = np.array(frame_mean["Pixel Y Mean"].values.tolist())
    list5 = np.array(frame_mean["Pixel Z Mean"].values.tolist())
    # print(frame_mean)

    vectors = np.column_stack((list1, list2, list3, list4, list5))
    # print(vectors)
    # print(frame_mean["X direction"])
    # print(frame_mean)
    frame_mean.to_csv("frame_mean.csv")
    return vectors


if __name__ == "__main__":

    from visualise_results import generate_histogram

    filename_mean = 'pinkcells_stats/pinkcells_Track_Position.csv'
    filename_start = 'pinkcells_stats/pinkcells_Track_Position_Start.csv'

    data = read_pink_cells(filename_mean, filename_start)
    generate_histogram(data)
