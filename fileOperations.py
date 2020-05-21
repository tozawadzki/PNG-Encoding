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
