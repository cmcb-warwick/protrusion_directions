#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:50:04 2018

@author: erick
"""


def read_cells(filename):

    """
    Reads a csv with cell information and calculate pixel data from XYZ positions


    Parameters:
    filename (string): path to csv file with cell info

    Returns:
    frame (pd.Dataframe): Pandas Dataframe with data from CSV plus calculated pixel data



    """

    import pandas as pd

    min_x = -1.77
    min_y = 174.0
    min_z = -183.0

    size_x = 0.972
    size_y = 3.69
    size_z = 0.976

    frame = pd.read_csv(filename, skiprows=3)
    # frame = pd.read_csv(filename)

#    print("X range:",min(frame['Position X']), max(frame['Position X']), "dynamic range:", max(frame['Position X'])-min(frame['Position X']))
#    print("Y range:",min(frame['Position Y']), max(frame['Position Y']), "dynamic range:", max(frame['Position Y'])-min(frame['Position Y']))
#    print("Z range:",min(frame['Position Z']), max(frame['Position Z']), "dynamic range:", max(frame['Position Z'])-min(frame['Position Z']))
#
    # will need to check IMARIS for correspondence between exported um files and pixel values
    # X and Z on csv files are my X and Y on resliced images

    frame["Pixel X"] = (frame['Position X'] - min_x) / size_x
    frame["Pixel X"] = frame["Pixel X"].round().astype(int)

    frame["Pixel Y"] = (frame['Position Z'] - min_z) / size_z
    frame["Pixel Y"] = frame["Pixel Y"].round().astype(int)

    frame["Pixel Z"] = (frame['Position Y'] - min_y) / size_y
    frame["Pixel Z"] = frame["Pixel Z"].round().astype(int)

    print("X pixel range:", min(frame["Pixel X"]), max(
        frame["Pixel X"]), "dynamic range:", max(frame["Pixel X"]) - min(frame["Pixel X"]))
    print("Y pixel range:", min(frame["Pixel Y"]), max(
        frame["Pixel Y"]), "dynamic range:", max(frame["Pixel Y"]) - min(frame["Pixel Y"]))
    print("Z pixel range:", min(frame["Pixel Z"]), max(
        frame["Pixel Z"]), "dynamic range:", max(frame["Pixel Z"]) - min(frame["Pixel Z"]))
#    print(frame)
    frame.to_csv("frame.csv")
    return frame


if __name__ == "__main__":

    filename = 'greencells_stats/greencells_Position.csv'

    data = read_cells(filename)
