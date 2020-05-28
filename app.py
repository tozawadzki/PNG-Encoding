import Data
import zlib
import crypting
import keys
import rabinMiller

IDAT = '49444154'
IEND = '49454e44'

filename = '3x2.png'
publicKey, privateKey = keys.generateKey(1024)

def encrypt_compressed(file,public):
    _, compress, decompress, _, _ = Data.getIDAT(file)
    encrypt_compress = []
    compress= compress.hex()
    k=0
    if len(compress)%8 != 0:
        for add in range(len(compress)%8):
            compress+='0'
    while k < len(compress):
        if k+256<len(compress):
            block = compress[k:k+256]
        else:
            block = compress[k:len(compress)]
        print(int(block,16))
        encrypy_block=crypting.encrypting(int(block,16),public)
        encrypt_compress.append(encrypy_block)
        k+=256
    print(encrypt_compress)
    print(crypting.decrypting(encrypt_compress[0],privateKey))


def encrypt_decompressed(filename,public):
    _, comp, decompress, _, _ = Data.getIDAT(filename)
    encrypt_decompress = []
    size = len(decompress)
    decompress = decompress.hex()
    k = 0
    if len(decompress) % 8 != 0:
        for add in range(len(decompress) % 8):
            decompress += '0'
    while k < len(decompress):
        if k + 256 < len(decompress):
            block = decompress[k:k + 256]
        else:
            block = decompress[k:len(decompress)]
        print(int(block, 16))
        encrypy_block = crypting.encrypting(int(block, 16), public)
        encrypt_decompress.append(encrypy_block)
        k += 256
    print(encrypt_decompress)
    print(crypting.decrypting(encrypt_decompress[0], privateKey))

def decrypt_compressed(filename,private):
    _,compress,decompress,_,_ = Data.getIDAT(filename)
    decrypt_compress = []
    for j in range(len(compress)):
        decrypt_compress.append(crypting.decrypting(compress[j],private))
   # print(decrypt_compress)
def decrypt_decompressed(filename,private):
    _, comp, decompress, _, _ = Data.getIDAT(filename)
    decrypt_dec = []
    for j in range(len(decompress)):
        decrypt_dec.append(crypting.decrypting(decompress[j], private))
   # print(decrypt_dec)

def savePNG(OGfile,newfile):
    file = open(OGfile, 'rb')
    fileInHex = file.read().hex()
    posIDAT = fileInHex.find(IDAT)
    posIEND = fileInHex.find(IEND)
    text_file = open(newfile, 'wb')
    n = text_file.write(fileInHex[:(posIDAT + 8)].encode('utf-8'))
   # n=text_file.write(encrypt_decompressed(OGfile,publicKey,privateKey))
    n = text_file.write(fileInHex[posIEND:].encode('utf-8'))
    text_file.close()
    print("Hex version of this file has been saved to given file")
    file.close()
    text_file.close()

encrypt_compressed(filename,publicKey)
encrypt_decompressed(filename,publicKey)

#savePNG('b3x3.png','test.png')


