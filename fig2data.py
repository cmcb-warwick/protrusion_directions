#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:15:59 2018

@author: erick
"""


 
def fig2data ( fig ):
    import numpy
    """
    @brief Convert a Matplotlib figure to a 3D numpy array with RGB channels and return it
    @param fig a matplotlib figure
    @return a numpy array of R values (we only need those for our images)
    """
    # draw the renderer
    fig.canvas.draw ( )
 
    # Get the RGBA buffer from the figure
    w,h = fig.canvas.get_width_height()
    buf = numpy.fromstring ( fig.canvas.tostring_rgb(), dtype=numpy.uint8 )
    buf.shape = ( w, h,3)
 
    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
#    buf = numpy.roll ( buf, 3, axis = 2 )
    return buf[:,:,0]


if __name__ == "__main__":

    import matplotlib.pyplot as plt
    import numpy
     
    # Generate a figure with matplotlib</font>
    figure =plt.figure(  )
    plot   = figure.add_subplot ( 111 )
     
    # draw a cardinal sine plot
    x = numpy.arange ( 0, 300, 0.1 )
    y = numpy.sin ( x ) / x
    
    plot.plot ( x, y )
    plt.axis('off')
    
    test = fig2data(figure)
    
    print(test.shape)
    #print(numpy.argmin(test, axis=1))