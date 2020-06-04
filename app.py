import Data
import zlib
import crypting
import keys
import rabinMiller
import fileOperations

IDAT = '49444154'
IEND = '49454e44'

filename = '3x2.png'
publicKey, privateKey = keys.generateKey(1024)

def test_en(file, public, private):
    _, compress, decompress, _, _ = Data.getIDAT(file)
    en = []
    de = []
    asrt = []
    k=0
    block_size = 256
    compress = bytearray(compress)
    nozeroes = compress
    zeroes = bytearray()
    for times in range((len(compress)%block_size)):
        zeroes.append(0)
    compress = zeroes+compress
    while k < len(compress):
        if k==0:
            block = compress[k:block_size]
            foo = nozeroes[k:block_size]
        elif k+block_size<len(compress):
            block = compress[k:k+block_size-1]
            foo = nozeroes[k:k+block_size-1]
            print(len(block))
        else:
            block = compress[k:len(compress)]
            foo= nozeroes[k:len(nozeroes)-1]
        asrt.append(block)
        de.append(foo)
        encryp = crypting.encrypting(int.from_bytes(block, byteorder='big'),public)
        foo = (encryp.to_bytes((encryp.bit_length() // 8) + 1, byteorder='big')).hex()
        en.append(bytes.fromhex(foo))
        k+=block_size
    return b''.join(en), en, asrt, de

def test_dec(file, public, private):
    encoded, idat, asrt, nozero = test_en(file,public,private)
    _, compress, decompress, _, _ = Data.getIDAT(file)
    final = 0
    decrypt = []
    idatt = []
    k = 0
    block_size = 256
    print(len(encoded)//block_size)
    for block in idat:
        decryp = crypting.decrypting(int.from_bytes(block, byteorder='big'),private)
        foo = (decryp.to_bytes((decryp.bit_length() // 8) + 1, byteorder='big')).hex()
        decrypt.append(bytes.fromhex(foo))
    final = b''.join(decrypt)
    final = bytearray(final)
    k=0
    while k < len(final):
        if k + block_size < len(compress):
            block = compress[k:k + block_size]
            foo = final[k:k + block_size]
            print(len(block))
        else:
            block = compress[k:len(compress)]
            foo = final[k:len(final)]
        k+=block_size
        idatt.append(foo)
    print(compress==final)
    return final
'''
def test_en_dec(file, public, private):
    _, compress, decompress, _, _ = Data.getIDAT(file)
    en = []
    de = []
    asrt = []
    k=0
    block_size = 256
    decompress = bytearray(decompress)
    nozeroes = compress
    zeroes = bytearray()
    for times in range((len(decompress)%block_size)):
        zeroes.append(0)
    compress = zeroes+decompress
    while k < len(decompress):
        if k+block_size<len(decompress):
            block = decompress[k:k+block_size]
            foo = nozeroes[k:k+block_size]
            print(len(block))
        else:
            block = decompress[k:len(decompress)]
            foo= nozeroes[k:len(nozeroes)]
        asrt.append(block)
        de.append(foo)
        encryp = crypting.encrypting(int.from_bytes(block, byteorder='big'),public)
        foo = (encryp.to_bytes((encryp.bit_length() // 8) + 1, byteorder='big')).hex()
        en.append(bytes.fromhex(foo))
        k+=block_size
    return b''.join(en), en, asrt, de

def test_dec_dec(file, public, private):
    encoded, idat, asrt, nozero = test_en_dec(file,public,private)
    _, compress, decompress, _, _ = Data.getIDAT(file)
    final = 0
    decrypt = []
    idatt = []
    k = 0
    block_size = 256
    print(len(encoded)//block_size)
    for block in idat:
        decryp = crypting.decrypting(int.from_bytes(block, byteorder='big'),private)
        foo = (decryp.to_bytes((decryp.bit_length() // 8) + 1, byteorder='big')).hex()
        decrypt.append(bytes.fromhex(foo))
    final = b''.join(decrypt)
    final = bytearray(final)
    print(decompress==final)
    return final
'''
def savePNG_decompress(OGfile,newfile):
    file = open(OGfile, 'rb')
    fileInHex = file.read().hex()
    posIDAT = fileInHex.find(IDAT)
    posIEND = fileInHex.find(IEND)
    text_file = open(newfile, 'wb')
    #print(fileInHex[:(posIDAT + 8)].encode('utf-8'))  wrong way
    #print(bytes.fromhex(fileInHex[:(posIDAT + 8)]))   corect way
    n = text_file.write(bytes.fromhex(fileInHex[:(posIDAT + 8)]))
    idata = test_dec(OGfile,publicKey,privateKey)
    #print(idata)
    n=text_file.write(idata)
    #n = text_file.write(bytes.fromhex(fileInHex[posIEND:]))
    text_file.close()
    print("Hex version of this file has been saved to given file")
    file.close()
    text_file.close()


#test('3x2.png',publicKey,privateKey)
test_dec('150x150.png',publicKey,privateKey)
#test_dec_dec('b3x3.png',publicKey,privateKey)
#encrypt_compressed(filename,publicKey)
#encrypt_decompressed(filename,publicKey)
#fileOperations.displayImage('test.png')
#savePNG_decompress('80x80.png','test.png')


