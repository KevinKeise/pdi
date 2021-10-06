import math
import cv2 as cv
import sys
import maior_intencidade

def transformacao_logaritmica():
    
    try:
        constante = float(input("Informe o valor da constante: "))
    except:
        return 0    

    img = cv.imread(cv.samples.findFile("imagem-teste1.jpg"), 2)
    if img is None:
        sys.exit("Could not read the image.")
    
    #constante = int(255/(math.log10(1 + maior_intencidade.get_max_intensity(img))))

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
        cv.imwrite("imagem-teste-logaritmica.png", img)

    return 1


def transformacao_exponential():
    
    img = cv.imread(cv.samples.findFile("image-teste1.jpg"), 2)
    if img is None:
        sys.exit("Could not read the image.")

    try:
        constante = int(input("Informe o valor da constante: "))
        exponente = float(input("Informe o valor do expoente: "))
    except:
        return 0   

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
        cv.imwrite("image-teste-exponecial.png", img)
    
    return 1

def transformacao_inversa():
    img = cv.imread(cv.samples.findFile("imagem-teste1.jpg"), 2)
    if img is None:
        sys.exit("Could not read the image.")
    
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            img[x,y] = 255 - img[x,y]

    cv.imshow("Display window", img)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("image-teste-inversa.png", img)
    