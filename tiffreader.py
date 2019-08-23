# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 17:21:10 2018

@author: Erick Martins Ratamero
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
import ome_files

reader = ome_files.OMETIFFReader()
reader.set_id('/home/erick/Nextcloud/CMCB/Michael_protrusions/smallstack.ome.tiff')

# calculate number of planes
no_planes = reader.get_image_count()
print(no_planes)
z = reader.get_size_z()
print(z)
# for each plane:
for plane in range(no_planes):
    pixels = reader.open_bytes_simple(plane)

    # for each non-zero pixel:
        # get neighbourhood (adjust for borders)
        # fit circle to neighbourhood 
        # replace pixel with value based on circle radius


# write new ome tiff with new values

#plt.imshow(pixels, cmap="gray")

reader.close()