import math
import cv2 as cv
import maior_intencidade

img = cv.imread(cv.samples.findFile("imagem.jpg"), 0)
    
constante = int(255/(math.log10(1 + maior_intencidade.get_max_intensity(img)))) # Constante calculada automaticamente
#constante = 30

for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        p = constante*(int(math.log(img[x,y] + 1,10))) # funçao logaritmica
        if p > 255:
            img[x,y] = 255
        else:
            img[x,y] = p
    
cv.imwrite("imagem-logaritmica.png", img)