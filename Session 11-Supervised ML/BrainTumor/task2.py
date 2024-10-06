# Given the Tumar Dataset,
# Make a comparison between KNN, Decision tree, and Naïve Bayes  in Accuracy (80,20),
# K fold cross validation(k=10), Confusion Matrix, and F1 score, Precision, and recall,
# Don’t forget to extract features of Image before use it


#1- Feature Extraction Image
# python -m pip install msvc-runtime  there exist error in skinmage library in mininmum threshold method

# Edge Features
#importing the required libraries
# import numpy as np
# from skimage.io import imread, imshow
# from skimage.filters import prewitt_h,prewitt_v
# import matplotlib.pyplot as plt
# import cv2

# # #reading the image 
# image = imread('CommonStepsML/mkf97.jpg',as_gray=True)

# # #calculating horizontal edges using prewitt kernel
# edges_prewitt_horizontal = prewitt_h(image)
# # #calculating vertical edges using prewitt kernel
# edges_prewitt_vertical = prewitt_v(image)
# plt.imshow(edges_prewitt_horizontal, cmap='gray')
# plt.show()
       
       
##################### Histogram ###################################3
    # #important library to show the image 
# # from operator import truediv
# import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
# # # #importing numpy to work with large set of data.
# import numpy as np
# #image read function
# img=mpimg.imread('Techniques of ML/mydecisiontree.png')
# # #image sclicing into 2D.  onepixel=(0,0,[255,255,255]) //3channels R(0-255)G ()B ()
# x=img[:,:,0]
# # # x co-ordinate denotation. 
# plt.xlabel("Value")
# # # y co-ordinate denotation.
# plt.ylabel("pixels Frequency")
# # # title of an image .
# plt.title("Original Image")
# # # imshow function with comperision of gray level value.
# plt.imshow(x,cmap="gray")
# # #plot the image on a plane.
# plt.show()

# plt.title("HIstogramm for given Image'  ")
# plt.xlabel("Value")
# plt.ylabel("pixels Frequency")
# #hist function is used to plot the histogram of an image.
# plt.hist(x) ###################################
# plt.show()

######Segmentation#####
# import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
# import numpy as np
# import cv2
# from skimage.filters import threshold_minimum
# color_image = cv2.imread('CommonStepsML/Coin.jpg')
# image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# thresh_min = threshold_minimum(image)
# binary_min = image > thresh_min

# fig, ax = plt.subplots(2, 2, figsize=(10, 10))

# ax[0, 0].imshow(image, cmap=plt.cm.gray)
# ax[0, 0].set_title('Original')

# ax[0, 1].hist(image.ravel(), bins=256) #numpy.ravel() == numpy.reshape(-1)

# ax[0, 1].set_title('Histogram')

# ax[1, 0].imshow(binary_min, cmap=plt.cm.gray)
# ax[1, 0].set_title('Thresholded (min)')

# ax[1, 1].hist(image.ravel(), bins=256)
# ax[1, 1].axvline(thresh_min, color='r')

# # ax[1, 1].hist(binary_min, bins=256)
# # ax[1, 1].set_title('Histogram')

# for a in ax[:, 0]:
#     a.axis('off')
# plt.show()

################################
# ###########################
import matplotlib.pyplot as plt
import cv2
from skimage import data
from skimage.filters import try_all_threshold

color_image = cv2.imread('CommonStepsML/WithIllumination.png')
# color_image = cv2.imread('CommonStepsML/Coin.jpg')
image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

fig, ax = try_all_threshold(image, figsize=(10, 8), verbose=True)
plt.show()