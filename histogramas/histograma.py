import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread('menina.jpg', 0)
plt.hist(img.ravel(),256,[0,256]); 
plt.show()

# create a CLAHE object (Arguments are optional). 
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv.imwrite('menina-equalizado.jpg',cl1)
plt.hist(cl1.ravel(),256,[0,256]);
plt.show()

