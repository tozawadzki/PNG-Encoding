import io
from PIL import Image
import cv2

def isPng(filename):
    fileInHex = getFileInHex(filename)
    # check whether IDAT chunk exists
    if fileInHex[0:16] != "89504e470d0a1a0a":
        return False
    else:
        return True

def getFileInHex(filename):
    with open('images/{}'.format(filename), 'rb') as f:
        fileInHex = f.read.hex()
        return fileInHex

def openImage(filename):
    return Image.open(filename)

def showImage(image):
    image.show()

def displayImage(filename):
    img = cv2.imread(filename)
    cv2.imshow('PNG Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

