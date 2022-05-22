import urllib.request
import os
import cv2

imageDataset = './images'
resizedImages = './resizedImages'

def imageDownload(url, imageName):
    urllib.request.urlretrieve(url, 'images/{}.jpg'.format(imageName))

def imageResize():
    for image in os.listdir(imageDataset):
        if image.endswith(".jpg"):
            imageToResize = cv2.imread('./images/{}'.format(image))
            imageResized = cv2.resize(imageToResize, dsize=(1600, 1200), interpolation=cv2.INTER_CUBIC)

            resizedPath = './resizedImages/resized-{}'.format(image)
            cv2.imwrite(resizedPath, imageResized)
