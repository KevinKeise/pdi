import cv2 as cv
import numpy as np
import sys

img3 = cv.imread("flor.jpg")

if img3 is None:
    sys.exit("Could not read the image.")

img_blue = img3[:,:,0] # obtem a insensidade do canal azul
img_green = img3[:,:,1] # ibtem a intensidade do canal verde
img_red = img3[:,:,2]   # obtem a intensidade do canal vermelho

cv.imwrite("imagem-blue.png", img_blue) # salva imagem do canal azul
cv.imwrite("imagem-green.png", img_green)   # salva imagem do canal verde
cv.imwrite("imagem-red.png", img_red)   # salva imagem do canal vermelho


img_hsv3 = cv.cvtColor(img3,  cv.COLOR_BGR2HLS_FULL) # transforma a imagem para HSI

img_hsv_h = img_hsv3[:,:,0] # obtem a matiz
img_hsv_i = img_hsv3[:,:,1] # obtem a intensidade (imagem em preto e branco)
img_hsv_s = img_hsv3[:,:,2] # obtem a saturação   

cv.imwrite("imagem-hsv.png", img_hsv3)
cv.imwrite("imagem-hsv-matiz.png", img_hsv_h)
cv.imwrite("imagem-hsv-saturacao.png", img_hsv_s)
cv.imwrite("imagem-hsv-intensidade.png", img_hsv_i)

# aumenta o valor da saturação em mais 50
for x in range(img3.shape[0]):
        for y in range(img3.shape[1]):
            n = img_hsv3[x,y,2] + 30
            if n > 255:
                img_hsv3[x,y,2] = 255
            else:
                img_hsv3[x,y,2] = n

ig = img_hsv3[:,:,2]
cv.imwrite("imagem-saturacao-mod.png", ig)
img_hsv4 = cv.cvtColor(img_hsv3,  cv.COLOR_HLS2BGR_FULL)
cv.imwrite("imagem-mod.png", img_hsv4)





