import os
import cv2

resizedImages = './resizedImages'

def imageFiltering():
    for image in os.listdir(resizedImages):
        if image.endswith(".jpg"):
            imageToFilter = cv2.imread('./resizedImages/{}'.format(image))

            filteredImage = cv2.cvtColor(imageToFilter, cv2.COLOR_BGR2HSV)
            filteredPath = './filteredImages/{}'.format(image)

            cv2.imwrite(filteredPath, filteredImage)