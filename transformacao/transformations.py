import math
import cv2 as cv
import sys
import maior_intencidade

def log_proces():
    
    img = cv.imread(cv.samples.findFile("imagem-preto-branco.jpg"), 2)
    if img is None:
        sys.exit("Could not read the image.")
    
    #constante = int(255/(math.log10(1 + maior_intencidade.get_max_intensity(img))))
    constante = 50  #aqui é a constante

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            p = int(constante*(math.log(img[x,y] + 1)))
            if p > 255:
                img[x,y] = 255
            else:
                img[x,y] = p
    
    cv.imshow("Display window", img)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("imagem-preto-branco-transormada.png", img)


def exponential():
    
    img = cv.imread(cv.samples.findFile("image-teste.jpg"), 2)
    if img is None:
        sys.exit("Could not read the image.")

    constante = 1
    exponente = 1

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            p = constante*(int(math.pow(img[x,y],exponente)) + 1)
            if p > 255:
                img[x,y] = 255
            else:
                img[x,y] = p

    cv.imshow("Display window", img)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("image-teste-expo.png", img)

def inversa():
    img = cv.imread(cv.samples.findFile("imagem-preto-branco.jpg"), 2)
    if img is None:
        sys.exit("Could not read the image.")
    
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            img[x,y] = 255 - img[x,y]

    cv.imshow("Display window", img)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("image-teste-expo.png", img)
    