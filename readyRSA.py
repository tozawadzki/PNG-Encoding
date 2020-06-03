#ch9_encrypt_blob.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64
#ch9_generate_keys.py
from Crypto.PublicKey import RSA

#Generate a public/ private key pair using 4096 bits key length (512 bytes)
new_key = RSA.generate(1024, e=65537)

#The private key in PEM format
private_key = new_key.exportKey("PEM")

#The public key in PEM Format
public_key = new_key.publickey().exportKey("PEM")

print (private_key)
fd = open("private_key.pem", "wb")
fd.write(private_key)
fd.close()

print (public_key)
fd = open("public_key.pem", "wb")
fd.write(public_key)
fd.close()
#Our Encryption Function
def encrypt_blob(blob, public_key):
    #Import the Public Key and use for encryption using PKCS1_OAEP
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    #compress the data first
    blob = zlib.compress(blob)

    #In determining the chunk size, determine the private key length used in bytes
    #and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted
    #in chunks
    chunk_size = 470
    offset = 0
    end_loop = False
    encrypted =  ""

    while not end_loop:
        #The chunk
        chunk = blob[offset:offset + chunk_size]

        #If the data chunk is less then the chunk size, then we need to add
        #padding with " ". This indicates the we reached the end of the file
        #so we end loop here
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += " " * (chunk_size - len(chunk))

        #Append the encrypted chunk to the overall encrypted file
        encrypted += rsa_key.encrypt(chunk)

        #Increase the offset by chunk size
        offset += chunk_size

    #Base 64 encode the encrypted file
    return base64.b64encode(encrypted)

#Use the public key for encryption
fd = open("public_key.pem", "rb")
public_key = fd.read()
fd.close()

#Our candidate file to be encrypted
fd = open("b3x3.png", "rb")
unencrypted_blob = fd.read()
fd.close()

encrypted_blob = encrypt_blob(unencrypted_blob, public_key)

#Write the encrypted contents to a file
fd = open("encrypted_img.png", "wb")
fd.write(encrypted_blob)
fd.close()