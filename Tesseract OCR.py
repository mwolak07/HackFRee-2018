from PIL import Image
from pytesseract import image_to_string
import numpy as np
from matplotlib import pyplot as plt
import cv2

image = cv2.imread('images/Tesseract-Test.png', flags=cv2.IMREAD_GRAYSCALE)
image = np.array(image)

plt.imshow(image, cmap='gray')
plt.show()

text = image_to_string(Image.fromarray(image))

print("Text: " + text)
