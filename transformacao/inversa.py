import cv2 as cv

img = cv.imread(cv.samples.findFile("imagem.jpg"), 2)
    
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        img[x,y] = 255 - img[x,y]  # função inversa

cv.imwrite("imagem-inversa.png", img)