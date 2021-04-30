import cv2
import numpy as np

img = np.ones((512, 512, 3))
cv2.line(img, (0, 0), (128, 256), (0, 0, 25), thickness=2)
cv2.rectangle(img, (128, 128), (256, 256), (0, 255, 0), thickness=2)
cv2.circle(img, (256, 256), 64, (0, 0, 255), thickness=2)
cv2.putText(img, ' OpenCV ', (128, 384), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=2, color=(102, 234, 0), thickness=2)
cv2.imshow('ones', img)
cv2.waitKey(0)