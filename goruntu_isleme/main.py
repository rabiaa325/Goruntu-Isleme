import cv2
import numpy as np

gul=cv2.imread("gul.jpg",0)

dizi=np.zeros(256)
height, width= gul.shape

for i in range(height):
    for j in range(width):
        piksel=gul[i][j]
        dizi[piksel]=dizi[piksel]+1

for histogramIndeks in range(256):
    print(dizi[histogramIndeks])

cv2.imshow("gul", gul)
cv2.waitKey()




