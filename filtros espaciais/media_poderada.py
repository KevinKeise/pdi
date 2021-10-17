import cv2 as cv
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])
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
        media_pod = int(np.average(arr, weights=np.array([1,2,1,2,3,2,1,2,1])))
        img2[x,y] = media_pod

cv.imwrite("imagem-media-poderada.png", img2)