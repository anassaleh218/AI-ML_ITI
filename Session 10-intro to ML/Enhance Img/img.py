import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow

image_path = '3.jpg'
image = cv2.imread(image_path)
print("Image shape:", image.shape)

def ResizeImg():
    image = cv2.imread(image_path)
    target_size = (224, 224)
    resized_image = cv2.resize(image, target_size)
    cv2.imshow('Image', image)  
    cv2.waitKey(0) 
    cv2.imshow('Resized Image', resized_image)  
    cv2.waitKey(0)  # Wait for a key press to close the display window
    cv2.destroyAllWindows()  # Close all display windows
ResizeImg()

# Normalization:
# Transfer Learning: using Pretrained model
# compare between images
# Data Consistency
# generating new images using generative models, normalization can impact the final output's quality and style.

def min_max_scaling(image): #[0 - 1]
    max_value = image.max()
    min_value = image.min()
    normalized_image = (image - min_value) / (max_value - min_value)
    return normalized_image

def standardize(image): #M=0 Std=1
    mean = image.mean()
    std = image.std()
    standardized_image = (image - mean) / std
    return standardized_image

def DisplayNormalization():

    image_array = np.array(image)

    normalized_image = min_max_scaling(image_array)
    standardized_image = standardize(image_array)

    # Plot original, normalized, and standardized images
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(image)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(normalized_image)
    plt.title('Normalized Image')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(standardized_image)
    plt.title('Standardized Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    # plt.subplot(1, 3, 1)
    # plt.hist(image_array.flatten(), bins=256, color='blue', alpha=0.7)
    # plt.title('Original Image')
    # plt.xlabel('Pixel Value')
    # plt.ylabel('Frequency')

    # plt.subplot(1, 3, 2)
    # plt.hist(normalized_image.flatten(), bins=256, color='green', alpha=0.7)
    # plt.title('Normalized Image')
    # plt.xlabel('Normalized Pixel Value')
    # plt.ylabel('Frequency')

    # plt.subplot(1, 3, 3)
    # plt.hist(standardized_image.flatten(), bins=256, color='red', alpha=0.7)
    # plt.title('Standardized Image')
    # plt.xlabel('Standardized Pixel Value')
    # plt.ylabel('Frequency')

    # plt.tight_layout()
    # plt.show()
DisplayNormalization()

#Data Augmentation:
# Apply data augmentation techniques to increase the diversity of your training data 
# and improve model generalization. Techniques include rotation, flipping, zooming, and shifting.
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
def generateDAugmentationByTensorflow():

    # Create an ImageDataGenerator instance with augmentation options {Balancing data, varient data}
    datagen = ImageDataGenerator(
        rotation_range=20,  
        width_shift_range=0.2,  
        height_shift_range=0.2,  
        shear_range=0.2,
        zoom_range=0.2,  
        horizontal_flip=True,  
        fill_mode='nearest'  
    )

    img = image.load_img(image_path, target_size=(224, 224))

    x = image.img_to_array(img) # to convert to numpy
    x = x.reshape((1,) + x.shape)  # Reshape to (1, height, width, channels)
    num_augmented_images = 9
    fig, axs = plt.subplots(3, 3, figsize=(10, 10))
    for i, augmented_img in enumerate(datagen.flow(x, batch_size=1)):
        ax = axs[i // 3, i % 3]
        ax.imshow(augmented_img[0].astype(int))
        ax.axis('off')
        if i == num_augmented_images - 1:
            break

    plt.tight_layout()
    plt.show() 
# generateDAugmentationByTensorflow()   
 
import imageio # install imageio
import imgaug as ia #install imgaug
import imgaug.augmenters as iaa
input_img = imageio.v2.imread('3.jpg')
def GenerateAugmentaionByyImago():
        
    # #Horizontal Flip
    # hflip= iaa.Fliplr()
    # input_hf= hflip.augment_image(input_img)
    # plt.subplot(121),plt.imshow(input_img,cmap=plt.cm.gray),plt.title('Original Noisy Image')
    # plt.subplot(122),plt.imshow(input_hf,cmap=plt.cm.gray),plt.title('horizontal flip Noisy Image')
    # plt.show()

    # #Vertical Flip
    # vflip= iaa.Flipud()
    # input_vf= vflip.augment_image(input_img)
    # plt.subplot(121),plt.imshow(input_img,cmap=plt.cm.gray),plt.title('Original Noisy Image')
    # plt.subplot(122),plt.imshow(input_vf,cmap=plt.cm.gray),plt.title('Vertical flip Noisy Image')
    # plt.show()

    # # rotation
    # rot1 = iaa.Affine(rotate=(-80,50))
    # input_rot1 = rot1.augment_image(input_img)
    # plt.subplot(121),plt.imshow(input_img,cmap=plt.cm.gray),plt.title('Original Noise Image')
    # plt.subplot(122),plt.imshow(input_rot1,cmap=plt.cm.gray),plt.title('Rotation Noise Image')
    # plt.show()

    # crop1 = iaa.Crop(percent=(0.3)) 
    # input_crop1 = crop1.augment_image(input_img)
    # plt.subplot(121),plt.imshow(input_img,cmap=plt.cm.gray),plt.title('Original Noise Image')
    # plt.subplot(122),plt.imshow(input_crop1,cmap=plt.cm.gray),plt.title('Crop  Noise Image')
    # plt.show()


    # noise=iaa.AdditiveGaussianNoise(10,40)
    # input_noise=noise.augment_image(input_img)
    # plt.subplot(121),plt.imshow(input_img,cmap=plt.cm.gray),plt.title('Original Noise Image')
    # plt.subplot(122),plt.imshow(input_noise,cmap=plt.cm.gray),plt.title('Noise Image')
    # plt.show()
    # # 
    # shear = iaa.Affine(shear=(-40,40))
    # input_shear=shear.augment_image(input_img)
    # plt.subplot(121),plt.imshow(input_img,cmap=plt.cm.gray),plt.title('Original Noise Image')
    # plt.subplot(122),plt.imshow(input_shear,cmap=plt.cm.gray),plt.title('Shearing Image')
    # plt.show()

    contrast=iaa.GammaContrast((0.5, 2.0))
    # makes dark parts of the image darker and bright parts brighter,
    # It works well for improving details in images, like making objects stand out more.
    contrast_sig = iaa.SigmoidContrast(gain=(5, 10), cutoff=(0.4, 0.6))
    # smoothly transforms the brightness levels, creating a smoother transition between dark and light areas.
    # It can help avoid harsh contrasts and improve the overall balance of brightness in the image.
    contrast_lin = iaa.LinearContrast((0.6, 0.4))
    # changes the brightness levels in a simple linear manner, which can subtly enhance or decrease contrast.
    # It's useful for making slight contrast adjustments without introducing extreme changes.
    input_contrast = contrast.augment_image(input_img)
    sigmoid_contrast = contrast_sig.augment_image(input_img)
    linear_contrast = contrast_lin.augment_image(input_img)
    plt.subplot(141),plt.imshow(input_img,cmap=plt.cm.gray),plt.title('Original Noise Image')
    plt.subplot(142),plt.imshow(input_contrast,cmap=plt.cm.gray),plt.title('Gamma_contrast Image')
    plt.subplot(143),plt.imshow(sigmoid_contrast,cmap=plt.cm.gray),plt.title('sigmoid_contrast Image')
    plt.subplot(144),plt.imshow(linear_contrast,cmap=plt.cm.gray),plt.title('linear_contrast Image')
    plt.tight_layout()
    plt.show()

    # elastic = iaa.ElasticTransformation(alpha=60.0, sigma=4.0)
    # polar = iaa.WithPolarWarping(iaa.CropAndPad(percent=(-0.2, 0.7)))
    # jigsaw = iaa.Jigsaw(nb_rows=20, nb_cols=15, max_steps=(3, 7))
    # input_elastic = elastic.augment_image(input_img)
    # input_polar = polar.augment_image(input_img)
    # input_jigsaw = jigsaw.augment_image(input_img)
    # plt.subplot(141),plt.imshow(input_img,cmap=plt.cm.gray),plt.title('Original Noise Image')
    # plt.subplot(142),plt.imshow(input_elastic,cmap=plt.cm.gray),plt.title('elastic Image')
    # plt.subplot(143),plt.imshow(input_polar,cmap=plt.cm.gray),plt.title('polar Image')
    # plt.subplot(144),plt.imshow(input_jigsaw,cmap=plt.cm.gray),plt.title('jigsaw Image')
    # plt.show()
GenerateAugmentaionByyImago()

def RemoveNoise():

    color_image = cv2.imread('3.jpg')
    # color_image1=cv2.imread('CommonStepsML/NoiseImageSaltandPaper.png')
    gray_img = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    # gray_img1=cv2.cvtColor(color_image1, cv2.COLOR_BGR2GRAY)
    sliding_window_size_x = 3
    sliding_window_size_y = 3
    mean_filter_kernel = np.ones((sliding_window_size_x,sliding_window_size_y),np.float32)/(sliding_window_size_x*sliding_window_size_y)

    filtered_imageMean = cv2.filter2D(gray_img,-1,mean_filter_kernel) #Depth of the output image [ -1 will give the output image depth as same as the input image]
    filtered_imageMedian=cv2.medianBlur(gray_img,3)
    # #1 0 1; 0 10 1; 9 5 7
    #  #0 0 1 1 1 5 7 9 10 
    
    # filtered_imageMean1=cv2.filter2D(gray_img1, -1,mean_filter_kernel)
    # filtered_imageMedian1=cv2.medianBlur(gray_img1,3)

    plt.subplot(231),plt.imshow(gray_img,cmap=plt.cm.gray),plt.title('Original Noise Image')
    # plt.xticks([]), plt.yticks([])
    # Mean filtered Image
    plt.subplot(232),plt.imshow(filtered_imageMean,cmap=plt.cm.gray),plt.title('Filtered Image with mean filter')
    plt.subplot(233),plt.imshow(filtered_imageMedian,cmap=plt.cm.gray),plt.title('Filtered Image with median filter')

    # Median filtered Image 
    # plt.subplot(234),plt.imshow(gray_img1,cmap=plt.cm.gray),plt.title('Original Paper&Salt Noise')
    # plt.subplot(235),plt.imshow(filtered_imageMean1,cmap=plt.cm.gray),plt.title('Filtered Image with mean filter')
    # plt.subplot(236),plt.imshow(filtered_imageMedian1,cmap=plt.cm.gray),plt.title('Filtered Image with median filter')
    plt.xticks([]), plt.yticks([])
    plt.show()
RemoveNoise()