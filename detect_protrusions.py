#@ File    (label = "Input file", style = "file") srcFile
#@ Integer (label = "Erosions", value = 3) erosions
#@ Integer (label = "Minimum protrusion size", value = 10) min_size

from ij import IJ
from ij.plugin import ImageCalculator
from ij.measure import ResultsTable
import os
from ij import WindowManager

'''    setPasteMode("Subtract");
     run("Set Slice...", "slice="+nSlices);
     run("Select All");
     for(i=1; i<nSlices; i++) {
         run("Previous Slice [<]");
         run("Copy");
         run("Next Slice [>]");
         run("Paste");
         run("Previous Slice [<]");
     }

     '''

IJ.run("Bio-Formats Importer", "open=" + str(srcFile) + " color_mode=Default view=Hyperstack stack_order=XYCZT")
image = IJ.getImage()
proc = image.getStack()
image_orig = image.createImagePlus()
proc2 = proc.duplicate()
image_orig.setStack("copy", proc2)
image_orig.show()
directory = os.path.dirname(str(srcFile))
#directory = image.getFileInfo()
print(directory)

#IJ.run(image, "Duplicate...", "duplicate")

#image_orig = IJ.getImage()
#IJ.run(image, "Convert to Mask", "method=Default background=Default calculate black");
for i in range(erosions):
	IJ.run(image, "Erode", "stack")

for i in range(erosions):
	IJ.run(image, "Dilate", "stack")

calc = ImageCalculator()
print(image, image_orig)
result = calc.run("Subtract create stack", image_orig, image)
#IJ.run(result, "Invert", "stack")
result.show()

image.changes = False
image.close()
image_orig.close()

IJ.run("Set Scale...", "distance=0 known=0 pixel=1 unit=pixel");
IJ.run(result,"Analyze Particles...", "size="+str(min_size)+"-Infinity show=Masks display clear add stack")
#result.close()

rt = ResultsTable.getResultsTable()
print("saving to "+str(directory)+"/protrusions.csv")
rt.saveAs(str(directory)+"/protrusions.csv")

image = IJ.getImage()
#image.close()
