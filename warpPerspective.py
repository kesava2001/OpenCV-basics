import cv2
import numpy as np

image = r'C:\Users\CHANDU\OneDrive\Desktop\opencv basics\cards1.jfif'
src = cv2.imread(image)
width, height = 250, 350
#i got all these coordinates from opening the image in paint
points1 = np.float32([[165, 47], [230, 31], [216, 120], [285, 100]])
points2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(points1, points2)

finalImg = cv2.warpPerspective(src, matrix, (width, height))

cv2.imshow('kings', finalImg)
cv2.waitKey(0)

#using this function we can create a document scanner application