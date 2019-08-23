#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://www.scipy.org/Cookbook/Least_Squares_Circle
"""


# Coordinates of the 2D points


def calculate_curvature(mat):

    """Fits a circle to the nonzero points of a matrix
    From http://www.scipy.org/Cookbook/Least_Squares_Circle
    Returns the curvature of the circle (1/R) and the XY coordinates of the centre
    
    """

    import numpy as np
    from scipy.optimize import leastsq

    size = np.size(mat, 0)
    # print(size)
    # print(np.subtract(np.nonzero(mat),size//2))
    x = np.subtract(np.nonzero(mat), size // 2)[1]
    y = np.subtract(np.subtract(size - 1, np.nonzero(mat)[0]), size // 2)
    # print(test1)
    # print(test2)
    #
    #points = [[0,0], [1,0], [2,0], [3,0], [3,1], [4,1], [5,1], [0,-1], [-1,-1], [-2,-1], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-3, 1], [-4, 1]]
    #
    #
    #x = np.array([item[0] for item in points])
    #y = np.array([item[1] for item in points])
    # print(x)
    # print(y)
    basename = 'circle'
    # coordinates of the barycenter
    x_m = np.mean(x)
    y_m = np.mean(y)

    # calculation of the reduced coordinates
    u = x - x_m
    v = y - y_m

    def calc_R(xc, yc):
        import numpy as np
        """ calculate the distance of each 2D points from the center c=(xc, yc) """
        return np.sqrt((x - xc)**2 + (y - yc)**2)

    #@countcalls
    def f_2b(c):
        """ calculate the algebraic distance between the 2D points and the mean circle centered at c=(xc, yc) """
        Ri = calc_R(*c)
        return Ri - Ri.mean()

    #@countcalls
    def Df_2b(c):
        import numpy as np
        """ Jacobian of f_2b
        The axis corresponding to derivatives must be coherent with the col_deriv option of leastsq"""
        xc, yc = c
        df2b_dc = np.empty((len(c), x.size))

        Ri = calc_R(xc, yc)
        df2b_dc[0] = (xc - x) / Ri                   # dR/dxc
        df2b_dc[1] = (yc - y) / Ri                   # dR/dyc
        df2b_dc = df2b_dc - df2b_dc.mean(axis=1)[:, np.newaxis]

        return df2b_dc

    center_estimate = x_m, y_m
    center_2b, ier = leastsq(f_2b, center_estimate, Dfun=Df_2b, col_deriv=True)

    xc_2b, yc_2b = center_2b
    Ri_2b = calc_R(xc_2b, yc_2b)
    R_2b = Ri_2b.mean()
#    print(xc_2b, yc_2b, Ri_2b)
    return 1 / R_2b, (xc_2b, yc_2b)
#residu_2b    = sum((Ri_2b - R_2b)**2)
#residu2_2b   = sum((Ri_2b**2-R_2b**2)**2)
#ncalls_2b    = f_2b.ncalls


if __name__ == "__main__":

    mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
           [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
           [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], ]
# Summary
    print(calculate_curvature(mat))


# plotting functions
