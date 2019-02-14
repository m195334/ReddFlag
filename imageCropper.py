import cv2
import numpy as np
import os

directory = "imageFiles"
fileIndex = 1

for filename in os.listdir(directory):
    if filename.endswith(".png"):
        try:
            # load image
            img = cv2.imread(filename)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale
            # threshold to get just the signature (INVERTED)
            retval, thresh_gray = cv2.threshold(gray, thresh=150, maxval=255, \
                                               type=cv2.THRESH_BINARY_INV)

            contours, hierarchy = cv2.findContours(thresh_gray,cv2.RETR_LIST, \
                                               cv2.CHAIN_APPROX_SIMPLE)

            # Find object with the biggest bounding box
            mx = (0,0,0,0)      # biggest bounding box so far
            mx_area = 0
            for cont in contours:
                x,y,w,h = cv2.boundingRect(cont)
                area = w*h
                if area > mx_area:
                    mx = x,y,w,h
                    mx_area = area
            x,y,w,h = mx

            # Output to files
            roi=img[y:y+h,x:x+w]
            cv2.imwrite('Image_' + str(fileIndex) + '_Cropped.png', roi)

            cv2.rectangle(img,(x,y),(x+w,y+h),(200,0,0),2)
            cv2.imwrite('Image_' + str(fileIndex) + '_Original.png', img)

            fileIndex = fileIndex + 1
        except:
            print("Error reading: " + filename)
