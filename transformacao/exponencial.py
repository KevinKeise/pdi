import math
import cv2 as cv

img = cv.imread(cv.samples.findFile("imagem.jpg"), 2)
# somente alterar a contante e o expoente
constante = 1           # constante
expoente = 1.12         # expoente

# percorre a imagem
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        p = constante*(int(math.pow(img[x,y],expoente)) + 1) # função exponecial
        if p > 255:
            img[x,y] = 255
        else:
            img[x,y] = p

cv.imwrite("image-exponecial.png", img)