# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 17:31:29 2018

@author: Atheer
"""


import cv2
# to load the required haarcascade_frontalface_default.xml classifiers
face_cascade = cv2.CascadeClassifier('C:\\Users\\Atheer\\ana\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')

# The first image
img = cv2.imread('people.jpg')

# to load the input image in grayscale mode in order to apply the Haar features
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# to find the faces by reducing the image size to fit the features size
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# to drow a rectangle on the detected faces, "i" is used to count the number of rectangles
i =0
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    i=i+1

# to show the image after applying Haar featurs on it    
cv2.imshow("There are {} faces in the image".format(i),img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# The second image
img = cv2.imread('people1.jpg')

# to load the input image in grayscale mode in order to apply the Haar features
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# to find the faces by reducing the image size to fit the features size
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# to drow a rectangle on the detected faces, "i" is used to count the number of rectangles
i =0
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    i=i+1

# to show the image after applying Haar featurs on it        
cv2.imshow("There are {} faces in the image".format(i),img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# The third image
img = cv2.imread('people3.jpg')

# to load the input image in grayscale mode in order to apply the Haar features
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# to find the faces by reducing the image size to fit the features size
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# to drow a rectangle on the detected faces, "i" is used to count the number of rectangles
i =0
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    i=i+1
 
# to show the image after applying Haar featurs on it        
cv2.imshow("There are {} faces in the image".format(i),img)
cv2.waitKey(0)
cv2.destroyAllWindows()