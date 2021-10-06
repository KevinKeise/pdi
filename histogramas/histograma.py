import numpy
from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread('imagem-preto-branco.jpg', 0)
plt.hist(img.ravel(),256,[0,256]); 
plt.show()