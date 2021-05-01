import cv2
import numpy as np
path = r'C:\Users\CHANDU\OneDrive\Desktop\opencv basics\car1.jfif'
jiraiya = r'C:\Users\CHANDU\OneDrive\Desktop\opencv basics\wallpapersden.com_jiraiya-naruto_3840x2160.jpg'
akatsuki = r'C:\Users\CHANDU\OneDrive\Desktop\opencv basics\733409.png'

image = cv2.imread(path)
image1 = cv2.imread(jiraiya)
image2 = cv2.imread(akatsuki)
resize1 = cv2.resize(image2, (800, 500))
resize = cv2.resize(image1, (1000, 500))
imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def func(a):
    pass

# after checking manually
# i set the minimum values to those acquired to get mask right after running
# we dont have to adjust the trackbars again
# these values are different for different images

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars', 640, 240)
cv2.createTrackbar('Hue min', 'Trackbars', 0, 179, func)
cv2.createTrackbar('Hue max', 'Trackbars', 179, 179, func)
cv2.createTrackbar('Sat min', 'Trackbars', 17, 255, func)
cv2.createTrackbar('Sat max', 'Trackbars', 207, 255, func)
cv2.createTrackbar('Val min', 'Trackbars', 162, 255, func)
cv2.createTrackbar('Val max', 'Trackbars', 255, 255, func)

while True:
    h_min = cv2.getTrackbarPos('Hue min', 'Trackbars')
    h_max = cv2.getTrackbarPos('Hue max', 'Trackbars')
    s_min = cv2.getTrackbarPos('Sat min', 'Trackbars')
    s_max = cv2.getTrackbarPos('Sat max', 'Trackbars')
    v_min = cv2.getTrackbarPos('Val min', 'Trackbars')
    v_max = cv2.getTrackbarPos('Val max', 'Trackbars')
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(image, lower, upper)

    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow('HSV', imgHSV)
    cv2.imshow('mask', mask)
    cv2.imshow('color', result)

    cv2.waitKey(1)
