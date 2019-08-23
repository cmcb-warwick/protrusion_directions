# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 17:21:10 2018

@author: erick
"""

#%matplotlib inline
def read_plane(filename, plane):
"""
Simple wrapper for ome_files reader, choosing the correct ZCT coords from the plane value
"""
    import ome_files
    
    reader = ome_files.OMETIFFReader()
    reader.set_id(filename)
    pixels = reader.open_array(plane)
    Z, C, T = reader.get_zct_coords(plane)
    
    reader.close()
    return pixels, Z, C, T
