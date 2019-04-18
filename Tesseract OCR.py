from PIL import Image
from pytesseract import image_to_string
import numpy as np
from matplotlib import pyplot as plt
import cv2

# Image read from file system and converted to numpy array
image = cv2.imread('images/Tesseract-Test.png', flags=cv2.IMREAD_GRAYSCALE)
image = np.array(image)

# Displaying the original image
plt.imshow(image, cmap='gray')
plt.title("Original")
plt.show()

# Filtering the image with openCV medianBlur function with 5x5 window to minimize noise
image = cv2.medianBlur(image, 3)

# Displaying filtered image
plt.imshow(image, cmap='gray')
plt.title("Filtered")
plt.show()

# Using tesseract OCR to extract text from the image
text = image_to_string(Image.fromarray(image))

# Showing the extracted text
print("Text: \n" + text)
