# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 17:21:10 2018

@author: erick
"""

#%matplotlib inline
def get_metadata(filename):

    """
    Simple wrapper for retrieving the 5D dimensions of an image from omefiles
    """
    import ome_files
    
    reader = ome_files.OMETIFFReader()
    reader.set_id(filename)
    H, W, Z, T, C = reader.get_size_y(), reader.get_size_x(), reader.get_size_z(), reader.get_size_t(), reader.get_size_c()
    reader.close()
    return H, W, Z, T, C



if __name__ == "__main__":
    
    filename = '/home/erick/Nextcloud/CMCB/Michael_protrusions/outlines.ome.tiff'
    print(get_metadata(filename))