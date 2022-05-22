import os
from imageFetch import imageDownload, imageResize
from imageProcessing import imageFiltering, imageProcess, imageCoords

imageDir = './images'
resizedImages = './resizedImages'
filteredDir = './filteredImages'

if not os.path.exists(imageDir) and not os.path.exists(filteredDir):
    os.makedirs(imageDir)
    os.makedirs(filteredDir)

if not os.path.exists(resizedImages):
    os.mkdir(resizedImages)

#imageDownload('https://valkyrie-backend-dev-images-bucket.s3.amazonaws.com/DJI_0002.JPG', 'testImage3')
imageResize()
imageFiltering()
imageProcess(imageCoords())
