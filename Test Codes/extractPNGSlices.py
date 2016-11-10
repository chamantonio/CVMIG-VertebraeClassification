### get xy, xz, yz slices from a .mhd file (3D CT-Scan)
### this code gets the WHOLE slice, and iteratively per plane
### eventually, code should get small patches of about 25x25 planes per voxel


import SimpleITK as sitk
import numpy as np
from scipy.misc import imsave
import os, sys

file_dir = os.path.expanduser('~') + "/downloads/xVertSeg.v1/Data1/images/"
savefile_dir = os.path.expanduser('~') + "/desktop/ACADS 1617A/CS 198/PNG Slices v1/"

for data_num in range(1,2):
	
	# create folder for image
	new_dir = savefile_dir + str(data_num)
	if not os.path.exists(new_dir):
		os.mkdir(new_dir)

	# set file name
	if data_num < 10:
		file_name = file_dir + "image00" + str(data_num) + ".mhd"
	else:
		file_name = file_dir + "image0" + str(data_num) + ".mhd"
	
	# load the .mhd file using SimpleITK
	image_sitk = sitk.ReadImage(file_name)
	# get dimensions of the image
	image_dimensions = image_sitk.GetSize()

	# get x slices, step size 10
	if not os.path.exists(new_dir+"/x/"):
		os.mkdir(new_dir+"/x/")
	for i in range(0, image_dimensions[0], 10):
		slice_sitk = image_sitk[i,:,:] # get a single slice (2D)
		slice_numpy = sitk.GetArrayFromImage(slice_sitk) # convert sitk image into 2D numpy array
		imsave(new_dir + "/x/" + str(data_num) + "-x-" + str(i) + ".png", slice_numpy) # save 2D numpy array as png using SciPy

	# get z slices, step size 10
	if not os.path.exists(new_dir+"/y/"):
		os.mkdir(new_dir+"/y/")
	for i in range(0, image_dimensions[1], 10):
		slice_sitk = image_sitk[:,i,:] # get a single slice (2D)
		slice_numpy = sitk.GetArrayFromImage(slice_sitk) # convert sitk image into 2D numpy array
		imsave(new_dir + "/y/" + str(data_num) + "-y-" + str(i) + ".png", slice_numpy) # save 2D numpy array as png using SciPy

	# get z slices, step size 10
	if not os.path.exists(new_dir+"/z/"):
		os.mkdir(new_dir+"/z/")
	for i in range(0, image_dimensions[2], 10):
		slice_sitk = image_sitk[:,:,i] # get a single slice (2D)
		slice_numpy = sitk.GetArrayFromImage(slice_sitk) # convert sitk image into 2D numpy array
		imsave(new_dir + "/z/" + str(data_num) + "-z-" + str(i) + ".png", slice_numpy) # save 2D numpy array as png using SciPy

