
# Function that calculates x^m modulo n using O(log(m)) operations
def power(x, m, n):

    a = 1
    while m > 0:
        if m % 2 == 1:
            a = (a * x) % n
        x = (x * x) % n
        m //= 2
    return a

def encryptRSA (publicKey,tmpNumber):
    tmp=power(tmpNumber,publicKey[0],publicKey[1])
    return tmp

def decryptRSA (privateKey,tmpNumber):
    tmp=power(tmpNumber,privateKey[0],privateKey[1])
    return tmp
