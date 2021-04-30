import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)
jiraiya = r'C:\Users\CHANDU\OneDrive\Desktop\opencv basics\wallpapersden.com_jiraiya-naruto_3840x2160.jpg'

image1 = cv2.imread(jiraiya)
resized = cv2.resize(image1, (500, 300))
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)
canny = cv2.Canny(gray, 150, 200)
dilate = cv2.dilate(canny, kernel, iterations=1)
erode = cv2.erode(dilate, kernel, iterations=1)
cv2.imshow('resized', resized)
cv2.imshow('gray', gray)
cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
cv2.waitKey(0)