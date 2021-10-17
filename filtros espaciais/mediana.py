import cv2 as cv
import numpy as np

arr = np.array([1,2,11,4,5,6,45,90,9])
img = cv.imread("crianca.jpg",0)
img2 = img
#img.shape[0]-1
for x in range(1,img.shape[0]-1):
    for y in range(1,img.shape[1]-1):
        arr[0] = img[x-1,y-1]
        arr[1] = img[x-1,y]
        arr[2] = img[x-1,y+1]
        arr[3] = img[x,y-1]
        arr[4] = img[x,y]
        arr[5] = img[x,y+1]
        arr[6] = img[x+1,y-1]
        arr[7] = img[x+1,y]
        arr[8] = img[x+1,y+1]
        arr_ordenado = np.sort(arr)
        mediana = arr_ordenado[4]
        img2[x,y] = mediana

cv.imwrite("imagem-mediana.png", img2)
