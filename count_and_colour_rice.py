#import necessary dependencies
import os, numpy as np
import matplotlib
from matplotlib import pyplot as plt
from skimage import io, color, filters, morphology, measure, segmentation, feature, img_as_ubyte
from scipy import ndimage as ndi

def show(im, title="", cmap='gray'):
    plt.figure(figsize=(6,6))
    plt.imshow(im, cmap=cmap)
    plt.title(title)
    plt.axis('off')

IMG_IN = "figs/rice.png"
IMG_OUT = "figs/rice_coloured_img.png"

#The purpose of this command is to check the original picture, To load & view
#Use io  for this purpose
img= io.imread(IMG_IN)
show(img, "original")

#I am calling the image and making a gray scale + a light blur
gray = img if img.ndim == 2 else color.rgb2gray(img)
blur = filters.gaussian(gray, sigma=1.0)   #
show(blur, "gray + blur")

#Threshold to clean mask, Clear difference between rice and others
otsu_threshold= filters.threshold_otsu(blur)
binary = (blur > (otsu_threshold - 0.02)) #I introduced this to fill in holes better

#This step will remove dust and fill in the holes inside grains
binary = morphology.remove_small_objects(binary, min_size=30)
binary = morphology.remove_small_holes(binary, area_threshold=80) #to fill in the holes inside grains

#improved step to refurbish the smallest of gaps on the grain edges
binary = morphology.binary_closing(binary, morphology.disk(1))
show(binary, "binary mask")

#Use a distance map, make a bigger window, use seeds to split the touching grains, this marks one point per grain so watershed can split touching grains
dist = ndi.distance_transform_edt(binary) #dist map

#I am deleting indices argument as this version of python was not accepting it.
coords = feature.peak_local_max(
    dist,
    min_distance=8,
    labels=binary)

#Now I am changing the coordinates into booleans seed map
seeds = np.zeros_like(dist, dtype=bool)#this will keep seeds only on rice
seeds[tuple(coords.T)] = True
markers = measure.label(seeds)  #this will turn the seeds into ids
show(dist, "distance map")

#Using watershed I am removing any small leftovers, I will also remove any small blobs. It will help me from aviding errors before I begin the count
labels= segmentation.watershed(-dist, markers, mask=binary)

#By looking at the image it is pretty obvious that the grains are much bigger than 80 pixel
min_size_pixels = 60 #Small tweak from 80 to 60 to improve grain coloring
labels = morphology.remove_small_objects(labels, min_size=min_size_pixels)

#Now i will relabel and count again
labels = measure.label(labels > 0)
count = labels.max()
print("grains counted:", count)

count

#Color Save, with every ricecorn a different 'unique color'
# Now i am making a colour representation for each grain, as that is what the task asks
n = int(labels.max())
h = np.linspace(0, 1, n, endpoint=False)
hsv = np.stack ([h, np.ones(n), np.ones(n)], axis=1)
colors = color.hsv2rgb(hsv) # originally some ricecorn grains were of the same color so now I am introducing a robust code to keep each colored grain unique
coloured = color.label2rgb(
    labels,
    image=img,
    colors=colors, #this step confirms that each grain is a unique color
    bg_label=0,
    kind='overlay',
    alpha=0.9
) #label12rgb is from sckikit-image, I am using it to run labeled grains into colors

#Use io to save it
IMG_OUT = "figs/rice_coloured.png"
io.imsave(IMG_OUT, img_as_ubyte(coloured))

#Show and print the count
show(coloured, f"saved: {IMG_OUT}")
print("final grains counted:" , count)
