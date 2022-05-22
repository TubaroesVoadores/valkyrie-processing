import os
from imageFetch import imageDownload, imageResize
from imageProcessing import imageFiltering

imageDir = './images'
resizedImages = './resizedImages'
filteredDir = './filteredImages'

if not os.path.exists(imageDir) and not os.path.exists(filteredDir):
    os.makedirs(imageDir)
    os.makedirs(filteredDir)

if not os.path.exists(resizedImages):
    os.mkdir(resizedImages)

imageDownload('https://tm.ibxk.com.br/2022/02/21/21085301870048.jpg?ims=1200x675', 'testImage2')
imageResize()
imageFiltering()