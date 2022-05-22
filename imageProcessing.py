import os
import cv2
import numpy as np
import exif
from PIL import Image

originalImages = './images'
resizedImages = './resizedImages'
filteredImages = './filteredImages'

def imageFiltering():
    for image in os.listdir(resizedImages):
        if image.endswith(".jpg"):
            imageToFilter = cv2.imread('./resizedImages/{}'.format(image))

            filteredImage = cv2.cvtColor(imageToFilter, cv2.COLOR_BGR2HSV)
            filteredPath = './filteredImages/filtered-{}'.format(image)

            cv2.imwrite(filteredPath, filteredImage)

def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == "S" or ref == "W":
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def imageCoords():
    for image in os.listdir(originalImages):
        with open('./images/{}'.format(image), 'rb') as src:
            images = exif.Image(src)
        if images.has_exif:
            try:
                images.gps_longitude
                coords = (decimal_coords(images.gps_latitude,
                                         images.gps_latitude_ref),
                          decimal_coords(images.gps_longitude,
                                         images.gps_longitude_ref))
            except AttributeError:
                print('No Coordinates')
        else:
            print('No Atributes')

        return coords



def imageProcess(coords):
    greenColor = 0
    total = 0

    for image in os.listdir(filteredImages):
        if image.endswith(".jpg"):
            readImage = Image.open('./filteredImages/{}'.format(image))
            numpyData = np.asarray(readImage)

            for line in numpyData:
                for column in line:
                    Red = column[0]
                    Green = column[1]
                    Blue = column[2]
                    if Green > Red and Green > Blue:
                        greenColor += 1
                    total += 1

            greenPercetage = greenColor / total

            imageData = {
                "id": image,
                "greenQuantity": greenPercetage,
                "latitude": coords[0],
                "longitude": coords[1]
            }

        return print(imageData)