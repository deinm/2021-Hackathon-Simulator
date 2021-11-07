import numpy as np
import cv2

map = np.loadtxt("map1.txt", delimiter = " ")

print(map.shape)
cv2.imshow("window",map)
cv2.waitKey(0)