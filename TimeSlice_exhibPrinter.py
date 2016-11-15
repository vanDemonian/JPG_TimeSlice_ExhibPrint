#!/usr/local/Cellar/python
"""
	Martin Walch : 06 May 2016.

	This program will take 294 jpeg images and combine them into a single
	hig-definition file fro exhibition printing.

	It is specifically designed to work with files from Nikon D800 
	@ 7360 x 4912 pixels.

	The output  = 7350 x  4912

"""



from __future__ import generators
import glob
from PIL import Image
from PIL import ImageStat
from PIL import ImageChops
from PIL.ExifTags import TAGS, GPSTAGS
import string, sys, traceback, datetime, time, calendar
import EXIF, os, shutil
import dirwalk
from PIL import *
import numpy as np
from SlicePrintObject import *


#_______________________________________________________________________________________________________
ScreenWidth = 7360
ScreenHeight = 4912

SliceWidth = sW = 25


quality = 100
fileExt = '.jpg'

inputDir = '/Users/pyDev/Documents/JPG_TIMESLICERY/JPG_TimeSlice_ExhibPrint/input/D800_hunter_17'
#inputDir = '/Users/marty/Documents/DTLA_Programming/JPG_REFINERY/JPG_PIXEL_TEST/input'
outputDir = '/Users/pyDev/Documents/JPG_TIMESLICERY/JPG_TimeSlice_ExhibPrint/output'
print
print "_________________________________________________________________________________________________________"
print
print "TimeSLice Exhibiton Printer "
print
print "Input directory  = ", inputDir
print "Output directory = ", outputDir
print
print "File extension = ", fileExt
print "Quality = ", quality
print


namePaths = []					# a list of the full paths to each file
SlicePrintObjectList = SOL = []		# list of all input files(jpegs) as instances of class SlicePrintObject


slicePix=[]
imgSlice=[]




#_______________________________________________________________________________________________________

def renderA(SlicePrintObject):


	sliceWidth = 25


	AA=[]
	AAx1 = 0
	AAx2 = sliceWidth
	for i in range(294):
		aa = [AAx1,AAx2]
		AA.append(aa)
		AAx1 = AAx2
		AAx2 += sliceWidth

	print "AA "
	print AA
	print

	zz=0


	#-----------------------------------------------------------------------------------------------------
	#  FRAME A

	img2 = Image.new('RGB', (ScreenWidth, ScreenHeight))
	arrayGround1 = np.array(img2)
	xx = len(AA)-1

	img4 = Image.new('RGB', (ScreenWidth, ScreenHeight))
	arrayGround2 = np.array(img4)

	

	while xx >= 0:

		ax1 = AA[xx][0]
		ax2 = AA[xx][1]

		print ax2
		print ax1
		
		img1 = Image.open(SOL[xx].namePath)
		arrayImg = np.array(img1)

		slicePix1 = arrayImg[0:, ax1:ax2]



		arrayGround1[0:, ax1:ax2] = slicePix1


		xx-=1

	outNum1 = 0


	outpathName = outputDir  + '/' +  'Still_Slice_HunterNth_Tues_17_May_2016' + str(outNum1).rjust(6).replace(' ','0') + '.jpg'
	img2 = Image.fromarray(arrayGround1)
	img2.save(outpathName, 'jpeg', quality=quality)




#____1____________________________________________________________________________________________________
#	 walk the directory and make a list that contains the name and dir path for every jpeg file

for root, dirs, files in os.walk(inputDir):
	for name in files:
		if name.endswith(fileExt):
			namePaths.append(os.path.join(root,name))

xP = len(namePaths)
print "total number of jpegs to be input = ", xP
print




#_____2___________________________________________________________________________________________________
#	iterate over the list of all namePaths - creating a SliceObject for every element
#	and a SOL SLiceObjectList that contains them all

z = 0
for name in namePaths:
	SO = SlicePrintObject(name, ScreenWidth, ScreenHeight, sW)
	SOL.append(SO)
	
	print SOL[z].namePath
	z+= 1

SOL_total = len(SOL)


print
print "SOL_total : ", SOL_total
print
print

#______3__________________________________________________________________________________________________

print " ABOUT TO RENDER "
print

renderA(SOL)



print 
print "*__________________*___________________*_____________________* "
print


print 'all done'
print















