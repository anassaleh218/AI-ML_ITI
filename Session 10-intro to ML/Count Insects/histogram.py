import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the image
image = cv2.imread('2.jpg')

# 2. Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



# Alternatively, you can use adaptive thresholding for more complex images
binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# 4. Apply morphological operations to remove noise (optional)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
processed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# 5. Find contours
contours, _ = cv2.findContours(processed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 6. Count the number of objects
num_objects = len(contours)
print(f'Number of objects: {num_objects}')

# 7. Draw contours on the original image (for visualization)
output_image = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)

# 8. Show the image with contours
cv2.imshow('Objects Detected', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 9. Plot the histogram of pixel intensities (Optional)
plt.hist(gray_image.ravel(), bins=256, range=[0, 256])
plt.title('Histogram of Pixel Intensities')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
