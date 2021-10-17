import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img3 = cv.imread("flor.jpg") # somente imagens coloridas



color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img3],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

img_blue = img3[:,:,0] # obtem a insensidade do canal azul
img_green = img3[:,:,1] # ibtem a intensidade do canal verde
img_red = img3[:,:,2]   # obtem a intensidade do canal vermelho

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img3[:,:,0] = clahe.apply(img_blue) # normaliza canal azul
img3[:,:,1] = clahe.apply(img_green) # normaliza canal verde
img3[:,:,2] = clahe.apply(img_red)  # normaliza canal vermelho

for i,col in enumerate(color):
    histr = cv.calcHist([img3],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

cv.imwrite('imagem-colorida-equalizada.jpg',img3)



