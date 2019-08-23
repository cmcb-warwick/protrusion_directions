# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 17:21:10 2018

@author: erick
"""

#%matplotlib inline
def write_plane(filename, plane, pixels):
    import ome_files
    
    writer = ome_files.OMETIFFWriter()
    writer.set_id(filename)
    writer.save_bytes_simple(plane, pixels)
    
   
    
    writer.close()
    